import os
import subprocess

# === Eingaben ===
project_name = input("What's your project name?: ").strip()
git_input = input("Do you want to initialize a git repository? (y/n) (default: y): ").lower().strip()
lib = input("Wich librarys do you want to install?: ")

os.mkdir(project_name)
os.chdir(project_name)

# === Git vorbereiten ===
git = (git_input == '' or git_input == 'y')
if git:
    subprocess.run(["git", "init"])
    with open(".gitignore", "w") as f:
        f.write("""/a
/test
""")

# === Virtuelle Umgebung ===
subprocess.run(["python", "-m", "venv", ".env"])

# Pfad zur Python-Exe in der venv
venv_python = ".env\\Scripts\\python.exe" if os.name == "nt" else ".env/bin/python"

# === Pakete installieren ===
subprocess.run([venv_python, "-m", "pip", "install", "--upgrade", "pip"])
if not lib == "":
    subprocess.run([venv_python, "-m", "pip", "install", *lib.split()])
if git:
    subprocess.run(["git", "add", "."])
    subprocess.run(["git", "commit", "-m", "start Python project"])
