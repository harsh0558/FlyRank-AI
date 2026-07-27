from pydantic_settings import BaseSettings, SettingsConfigDict

class configDB(BaseSettings):
    Postgres_URL: str

    model_config = SettingsConfigDict(
        env_file=".env",
        extra="ignore"
    )

db_config = configDB()

