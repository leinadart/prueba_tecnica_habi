from app.application.config import Settings


class TestConfig:
    def test_settings_default_values(self):
        settings = Settings()

        assert settings.host == ""
        assert settings.user == ""
        assert settings.password == ""
        assert settings.database == ""
        assert settings.port == ""