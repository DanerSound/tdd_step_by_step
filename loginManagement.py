
def validate_user_data(user_data):
    required_fields = ["username", "password", "email", "registration_date"]
    
    for field in required_fields:
        if field not in user_data:
            raise ValueError(f"Missing required field: {field}")
    
    if len(user_data["password"]) < 8:
        raise ValueError("Password must be at least 8 characters long")
    
    if "@" not in user_data["email"]:
        raise ValueError("Invalid email address")
    
    try:
        year, month, day = map(int, user_data["registration_date"].split("-"))
    except ValueError:
        raise ValueError("Invalid registration date format. Expected YYYY-MM-DD")
    
    return True