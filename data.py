BASE_URL = 'https://stellarburgers.nomoreparties.site'
API_ENDPOINTS = {
    "create_order": f"{BASE_URL}/api/orders",
    "create_user": f"{BASE_URL}/api/auth/register",
    "login": f"{BASE_URL}/api/auth/login",
    "changing_user_data": f"{BASE_URL}/api/auth/user",
    "receiving_orders": f"{BASE_URL}/api/orders"
}
ingredient1 = "61c0c5a71d1f82001bdaaa6c"
ingredient2 = "61c0c5a71d1f82001bdaaa70"
EXISTED_PAYLOAD = {
    "email": "alex25@mail.com",
    "password": "13b4Bo9T",
    "name": "Alex"
}
AUTH_ERROR_RESPONSE = {
            "success": False,
            "message": "You should be authorised"
        }
EMAIL_ERROR_RESPONSE = {
            "success": False,
            "message": "User with such email already exists"
        }
INGR_ID_ERROR_RESPONSE = {
            "success": False,
            "message": "Ingredient ids must be provided"
        }
EXIST_USER_ERROR_RESPONSE = {
            "success": False,
            "message": "User already exists"
        }
LOGIN_ERROR_RESPONSE = {
            "success": False,
            "message": "email or password are incorrect"
        }