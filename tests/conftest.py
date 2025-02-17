import pytest
from data import EXISTED_PAYLOAD
from methods.create_user_methods import CreateUser
from methods.login_user_methods import LoginUser
from methods.changing_user_data_methods import UserProfile
from methods.creating_order_methods import CreatingOrder
from methods.get_order_methods import Order

@pytest.fixture(scope="function")
def user_fixture(user_methods):
    """Создание тестового пользователя перед тестом и удаление после теста."""
    payload = user_methods.generate_user_data()
    user = user_methods.create_user(payload)
    token = user.json().get("accessToken")
    yield payload, token  # Передаем данные пользователя и токен в тест
    user_methods.delete_user(token)

@pytest.fixture(scope="function")
def user_methods():
    """Фикстура для работы с созданием пользователей."""
    return CreateUser()


@pytest.fixture(scope="function")
def login_user():
    """Фикстура для работы с логином пользователей."""
    return LoginUser()


@pytest.fixture(scope="function")
def profile_methods():
    """Фикстура для работы с профилем пользователей."""
    return UserProfile()

@pytest.fixture(scope="function")
def order_methods():
    """Фикстура для работы с заказами."""
    return CreatingOrder()

@pytest.fixture(scope="function")
def get_order_methods():
    """Фикстура для получения заказов."""
    return Order()

@pytest.fixture(scope="module")
def existing_user_fixture():
    """Получение токена для уже существующего пользователя."""
    login_user = LoginUser()
    token = login_user.get_token(EXISTED_PAYLOAD["email"], EXISTED_PAYLOAD["password"])
    return token
