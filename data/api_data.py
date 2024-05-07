import pytest


# 登入帳號
@pytest.fixture
def login_account_json(user):
    login_account_data = {
        "account": user.account,
        "password": user.password,
        "deviceID": user.device_id,
        "deviceModel": user.device_model,
        "os": user.os,
        "isAutoLogin": user.is_auto_login,
    }
    return login_account_data


# 註冊帳號
@pytest.fixture
def registry_account_json(user):
    registry_account_data = {
        "account": user.account,
        "password": user.password,
        "deviceID": user.device_id,
        "deviceModel": user.device_model,
        "os": user.os,
    }
    return registry_account_data


# 確認帳號
@pytest.fixture
def check_account_json(user):
    check_account_data = {"account": user.account}
    return check_account_data


# 快速登入
@pytest.fixture
def login_access_json(user, token):
    login_access_data = {
        "accessToken": token,
        "deviceID": user.device_id,
        "deviceModel": user.device_model,
        "os": user.os,
        "isAutoLogin": user.is_auto_login,
    }
    return login_access_data


# 立即登入
@pytest.fixture
def login_anonymously_json(user, token):
    login_anonymously_data = {
        "token": token,
        "deviceID": user.device_id,
        "deviceModel": user.device_model,
        "os": user.os,
    }
    return login_anonymously_data


# 註冊立即登入
@pytest.fixture
def registry_anonymously_json(user):
    registry_anonymously_data = {
        "deviceID": user.device_id,
        "deviceModel": user.device_model,
        "os": user.os,
    }
    return registry_anonymously_data


# 登入google
@pytest.fixture
def login_google_json(user, token):
    login_google_data = {
        "token": token,
        "deviceID": user.device_id,
        "deviceModel": user.device_model,
        "os": user.os,
    }
    return login_google_data


# 登入fb
@pytest.fixture
def login_fb_json(user, token):
    login_google_data = {
        "token": token,
        "deviceID": user.device_id,
        "deviceModel": user.device_model,
        "os": user.os,
    }
    return login_google_data


# 登入apple
@pytest.fixture
def login_apple_json(user, token):
    login_apple_data = {
        "token": token,
        "deviceID": user.device_id,
        "deviceModel": user.device_model,
        "os": user.os,
    }
    return login_apple_data


# 登入line
@pytest.fixture
def login_line_json(user, token):
    login_line_data = {
        "token": token,
        "deviceID": user.device_id,
        "deviceModel": user.device_model,
        "os": user.os,
    }
    return login_line_data


# 忘記密碼
@pytest.fixture
def forget_password_json(user, sms_code):
    forget_password_data = {
        "account": user.account,
        "smsCode": sms_code,
        "phone": user.phone,
        "countryCode": user.country_code,
    }
    return forget_password_data


# 忘記密碼 -> 更換密碼
@pytest.fixture
def change_forget_json(user, token):
    change_forget_data = {
        "token": token,
        "password": user.new_password,
    }
    return change_forget_data


# 發送簡訊驗證碼-忘記密碼
@pytest.fixture
def send_forget_sms_code_json(user):
    send_forget_sms_data = {
        "account": user.account,
        "phone": user.phone,
        "countryCode": user.country_code,
    }
    return send_forget_sms_data


# 發送簡訊驗證碼-忘記密碼
@pytest.fixture
def send_email_code_json(user):
    send_forget_sms_data = {"email": user.email}
    print(send_forget_sms_data)
    return send_forget_sms_data
