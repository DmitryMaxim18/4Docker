import pytest
from regular.pages import login_page


class TestLogin:
    @pytest.fixture
    def login(self, driver):
        return login_page.LoginPage(driver)

    # @pytest.mark.shallow
    # def test_valid_credentials_1(self, login):
    #     login.with_("tomsmith", "SuperSecretPassword!")
    #     assert login.success_message_present()

    @pytest.mark.shallow
    def test_example(self):
        assert 1 == 1

    @pytest.mark.parametrize("name, passw", [("tomsmith", "SuperSecretPassword!"), ("tomsmith", "SuperSecretPassword!!")])
    def test_valid_credentials_2(self, login, name, passw):
        login.with_(name, passw)
        assert login.success_message_present()

    @pytest.mark.deep
    def test_invalid_credentials(self, login):
        login.with_("tomsmith", "bad_password")
        assert login.failure_message_present()
