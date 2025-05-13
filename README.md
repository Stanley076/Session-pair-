# Stany Tech Secure Upload System

![Stany Tech Logo](https://files.catbox.moe/rmxujw.jpeg)

A secure file upload system with military-grade session ID generation.

## Features
- Modern UI with gradient background
- Secure session ID generation
- File upload handling
- Responsive design
- Heroicon-based interface

## Deployment to Heroku

1. Clone the repository
2. Create a new Heroku app
3. Set up Heroku CLI
4. Deploy using Git:

```bash
git push heroku master
```

5. Add required buildpacks:
```bash
heroku buildpacks:add heroku/python
```

## Requirements
- Python 3.9+
- Flask
- Gunicorn

## Running Locally

```bash
pip install -r requirements.txt
python app.py
```

## Environment Variables
Create `.env` file:
```
FLASK_APP=app.py
FLASK_ENV=development
SECRET_KEY=your_secret_key_here
```

## Project Structure
```
/stany-tech
├── app.py
├── requirements.txt
├── Procfile
├── README.md
└── /templates
    ├── index.html
    └── result.html
```

[![Deploy to Heroku](https://www.herokucdn.com/deploy/button.svg)](https://heroku.com/deploy)
