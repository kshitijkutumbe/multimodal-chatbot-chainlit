# app/config.py
from dataclasses import dataclass
import os

@dataclass
class Config:
    OPENAI_API_KEY: str = os.getenv('OPENAI_API_KEY')
