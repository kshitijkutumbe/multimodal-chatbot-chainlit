# template.py
import os

dirs = [
    "app"
]

files = [
    "app/__init__.py",
    "app/main.py",
    "app/api.py",
    "app/utils.py",
    "app/config.py",
    "app/logger.py",
    "Dockerfile",
    "requirements.txt"
]

for dir in dirs:
    os.makedirs(dir, exist_ok=True)

for file_path in files:
    with open(file_path, "w") as f:
        pass

print("Project structure created successfully.")
