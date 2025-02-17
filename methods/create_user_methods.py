import string
import random
import requests
import allure
from data import API_ENDPOINTS


class CreateUser:

    @allure.step("Генерация случайной строки")
    def generate_random_string(self, length):
        letters = string.ascii_lowercase
        return ''.join(random.choice(letters) for _ in range(length))

    @allure.step("Генерация данных пользователя")
    def generate_user_data(self):
        email = f'{self.generate_random_string(8)}@mail.com'
        password = self.generate_random_string(8)
        name = self.generate_random_string(8)

        payload = {
            "email": email,
            "password": password,
            "name": name
        }
        return payload

    @allure.step("Создание пользователя")
    def create_user(self, payload=None):
        if payload is None:
            payload = self.generate_user_data()

        response = requests.post(API_ENDPOINTS["create_user"], json=payload)
        return response

    def delete_user(self, token):

        response = requests.delete(API_ENDPOINTS["delete_user"], headers={'Authorization': token})
        return response