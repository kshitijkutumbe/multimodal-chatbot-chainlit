# app/config.py
from dataclasses import dataclass
import os

os.environ['OPENAI_API_KEY'] = ''


@dataclass
class Config:
    OPENAI_API_KEY: str = os.getenv('OPENAI_API_KEY')
