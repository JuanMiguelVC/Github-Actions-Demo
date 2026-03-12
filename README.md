# Github Actions Demo
🔐 Password Generator: CI/CD with GitHub Actions & Docker
This project is a practical demonstration of a modern DevOps workflow. It features a secure password generator written in Python, fully automated through a CI/CD pipeline that handles testing, linting, and deployment to Docker Hub <br>
Inspired by the following TechWorld with Nana tutorial: https://www.youtube.com/watch?v=R8_veQiYBjI

## 🚀 Key Features
Language: Developed in Python 3.13 (latest stable version). <br>
CI/CD Pipeline: Fully automated workflow using GitHub Actions. <br>
Quality Assurance: Automated Linting and Unit Testing (Pytest) on every push. <br>
Containerization: Automated Docker image build and push to Docker Hub. <br>
Versatility: Interactive terminal interface to customize password length, quantity, and special characters. <br>

## 🛠️ How It Works
Interactive Script
The script allows users to configure the password generation directly from the terminal. <br>
![Options to configure on the terminal](./assets/password-generator-options.png)
Sample Output: <br>
![Passwords generated](./assets/passwords-generated.png)

## 🏃 Run the Project
Option 1: Run with Docker (Recommended)
You don't need Python installed! Just run the image directly from Docker Hub: <br>
```bash
docker run -it juanmiguelvime/password-generator-python:latest
```
Option 2: Run Locally
Clone the repository.<br>
Ensure you have Python 3.13 installed.<br>
Run:
```bash
python3 password_generator.py
```

Also you can run the script using PyCharm or Visual Studio Code
### Run with PyCharm
1. Open the project folder in PyCharm.
2. Right-click `password_generator.py` and select **Run 'password_generator'**.

### Run with Visual Studio Code
1. Open the project folder
2. Locate password_generator.py
3. Right-click the file and choose Run Python File in Terminal

## 🤖 CI/CD Pipeline (GitHub Actions)
The workflow is defined in .github/workflows/ and triggers on every push to the main branch. It follows these stages:
Environment Setup: Spins up an Ubuntu runner with Python 3.13. <br>
Linting: Checks code quality and standards. <br>
Testing: Executes unit tests to ensure script reliability. <br>
Docker Build & Push: Builds the Docker image using the Dockerfile. <br>
Pushes the image to Docker Hub with the latest tag. <br>

## ⚙️ Technologies Used
CI/CD: GitHub Actions (v4+ actions). <br>
Containerization: Docker & Docker Hub. <br>
Language: Python 3.13. <br>
Testing: Pytest / Unittest. <br>

