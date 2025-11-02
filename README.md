# Python Project Starter

This script automatically creates a new Python project structure, sets up a virtual environment, and optionally installs libraries. It can also initialize a Git repository if desired.

## 🧩 Features

- Creates a new project directory  
- Generates a `main.py` file  
- Optionally initializes a Git repository  
- Creates a `.gitignore` file  
- Sets up a virtual environment (`.env`)  
- Upgrades `pip`  
- Installs specified Python libraries  

## ⚙️ Requirements

- **Python 3.x** installed  
- **Git** (optional, if you want to use Git)

## 🚀 Usage

1. ### Run the script:
 ```bash
   python create_project.py

```
2. ### Follow the prompts:
```bash
What's your project name?: my_project
Do you want to initialize a git repository? (y/n) (default: y): y
Wich librarys do you want to install?:
```

3. ### The script will automatically:

- Create the project folder my_project

- Generate a main.py file

- Initialize Git (if selected)

- Create a virtual environment (.env)

- Install requests and flask

- Make the first Git commit (if enabled)

## 📁 Example Project Structure

```bash
my_project/
├── .env/
├── .git/
├── .gitignore
└── main.py
```

## 🧠 Notes

- Git initialization is enabled by default when you just press Enter.

- Leave the library input blank if you don’t want to install any packages.

- On Windows, the virtual environment uses .env\Scripts\python.exe;
on Linux or macOS, it uses .env/bin/python.
