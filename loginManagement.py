from datetime import datetime

def validate_user_data(user_data):
    if not isinstance(user_data, dict):
        raise TypeError("user_data must be a dictionary")

    required_fields = ["username", "password", "email", "registration_date"]

    missing_keys = required_fields - user_data.keys()
    if missing_keys:
        raise KeyError(f"missing keys:{missing_keys}")

    for field in required_fields:
        if field not in user_data:
            raise ValueError(f"Missing required field: {field}")

    if not user_data["username"].strip():
        raise ValueError("Username non valido")
    
    if len(user_data["password"]) < 8:
        raise ValueError("Password must be at least 8 characters long")
    
    if "@" not in user_data["email"]:
        raise ValueError("Invalid email address")

    try:
        year, month, day = map(int, user_data["registration_date"].split("-"))
    except ValueError:
        raise ValueError("Invalid registration date format. Expected YYYY-MM-DD")

    try:
        datetime.strptime(user_data["registration_date"], "%Y-%m-%d")
    except ValueError:
        raise ValueError("Invalid date format or non-existent date")
    
    return True