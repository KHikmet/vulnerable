# vulnerable_app.py

import subprocess
import os

# Hardcoded secret (Snyk və Semgrep bunu tapacaq)
API_KEY = "123456"

# Command injection zəifliyi (Semgrep və Bandit bunu aşkar edəcək)
def run_command(cmd):
    subprocess.call(cmd, shell=True)

user_input = input("Enter a command: ")
run_command(user_input)

# Secret fayl oxunur (Semgrep bunu təhlil edəcək)
with open(".env", "r") as f:
    env_data = f.read()
    print(env_data)
