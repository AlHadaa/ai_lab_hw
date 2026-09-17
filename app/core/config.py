"""Application configuration settings."""

import os
from dataclasses import dataclass


@dataclass(frozen=True)
class AppConfig:
    """Application configuration container."""

    APP_NAME: str = "SmartText AI & Vibe Studio"
    APP_VERSION: str = "1.0.0"
    DEBUG: bool = os.getenv("FLASK_DEBUG", "True").lower() in ("true", "1", "t")
    HOST: str = os.getenv("HOST", "127.0.0.1")
    PORT: int = int(os.getenv("PORT", 5000))
    SECRET_KEY: str = os.getenv("SECRET_KEY", "dev-secret-key-change-in-production")


config = AppConfig()
