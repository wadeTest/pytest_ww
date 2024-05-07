import sys

sys.path.extend(["d:\\pytest_ww"])
from data.api_url import ApiPath, Env
from utils.base_request import HTTPRequest


class Api:
    # 設定環境
    def __init__(self, env: str):
        if env.lower() == "dev":
            self.url = Env.dev
        else:
            self.url = Env.qa

    # 註冊帳號
    def registry_account(self, registry_account):
        res = HTTPRequest(self.url).post(
            ApiPath.register_account, json=registry_account
        )
        return res

    # 確認帳號
    def check_account(self, check_account_json):
        res = HTTPRequest(self.url).post(
            ApiPath.register_account, json=check_account_json
        )
        return res

    # 登入帳號
    def login_account(self, login_account_json):
        res = HTTPRequest(self.url).post(
            ApiPath.register_account, json=login_account_json
        )
        return res

    # 快速登入
    def login_access_token(self, login_access_json):
        res = HTTPRequest(self.url).post(
            ApiPath.register_account, json=login_access_json
        )
        return res

    # 立即登入
    def login_anonymously(self, login_anonymously_json):
        res = HTTPRequest(self.url).post(
            ApiPath.register_account, json=login_anonymously_json
        )
        return res

    # 註冊立即登入
    def registry_anonymously(self, registry_anonymously_json):
        res = HTTPRequest(self.url).post(
            ApiPath.register_account, json=registry_anonymously_json
        )
        return res

    # 登入google
    def login_google(self, login_google_json):
        res = HTTPRequest(self.url).post(
            ApiPath.register_account, json=login_google_json
        )
        return res

    # 登入fb
    def login_fb(self, login_fb_json):
        res = HTTPRequest(self.url).post(ApiPath.register_account, json=login_fb_json)
        return res

    # 登入apple
    def login_apple(self, login_apple_json):
        res = HTTPRequest(self.url).post(
            ApiPath.register_account, json=login_apple_json
        )
        return res

    # 登入line
    def login_line(self, login_line_json):
        res = HTTPRequest(self.url).post(ApiPath.register_account, json=login_line_json)
        return res

    # 取得Client設定
    def get_client_config(self):
        res = HTTPRequest(self.url).post(ApiPath.get_client_config)
        return res

    # 忘記密碼
    def forget_password(self, forget_password_json):
        res = HTTPRequest(self.url).post(ApiPath.forget, json=forget_password_json)
        return res

    # 忘記密碼 -> 更換密碼
    def change_forget(self, change_forget_json):
        res = HTTPRequest(self.url).post(ApiPath.change_forget, json=change_forget_json)
        return res

    # 發送簡訊驗證碼-忘記密碼
    def send_forget_sms_code(self, forget_password_sms_json):
        res = HTTPRequest(self.url).post(
            ApiPath.send_forget_password_sms_code, json=forget_password_sms_json
        )
        return res

    # 發送簡訊驗證碼-忘記密碼
    def send_email_code(self, send_email_code_json):
        res = HTTPRequest(self.url).post(
            ApiPath.send_email_code, json=send_email_code_json
        )
        return res


# test = Api("dev")
# test_data = TestData(
#     "wade1",
#     "aa123456",
#     "postman",
#     "postman",
#     "windows",
#     "aa1234567",
#     "lu_wade@way-win.com",
# )
# result = test.send_email_code(test_data.send_email_code_json())
# print(result.text)
