from faker import Faker

faker  = Faker() # вспомогательная функция, генерирует рандомные данные

def generate_registration_data():
    email = faker.email()
    password = faker.password(Length=6, digits=True) # опционально special_chars=True, upper_case=True, lower_case=True
    return email, password