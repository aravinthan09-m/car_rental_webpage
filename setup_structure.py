import os

# Folders to create
folders = [
    "static/css",
    "static/images",
    "templates"
]

# Files to create with default content
files = {
    "app.py": "",
    "config.py": "",
    "requirements.txt": "flask\nmysql-connector-python\n",
    "static/css/style.css": "/* Your CSS goes here */",
    "templates/index.html": "<h1>Welcome to Car Rental</h1>",
    "templates/login.html": "<h1>Login Page</h1>"
}

# Create folders
for folder in folders:
    os.makedirs(folder, exist_ok=True)

# Create files
for path, content in files.items():
    with open(path, "w") as file:
        file.write(content)

print("Project structure created successfully!")
