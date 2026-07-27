from pydantic_settings import BaseSettings, SettingsConfigDict

class db_config(BaseSettings):
    db_url: str | None

    model_config = SettingsConfigDict(
      env_file= '.env'
    )

db = db_config()
