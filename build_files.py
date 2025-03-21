import os
import subprocess

# Install dependencies
subprocess.run(["pip", "install", "-r", "requirements.txt"], check=True)
# Collect static files
subprocess.run(["python", "manage.py", "collectstatic", "--noinput"], check=True)