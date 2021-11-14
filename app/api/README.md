# cpytter

## Prerequisites

Make preparations for deploy to Google Cloud Platform

## Project setup

`python -m venv .venv`  
`pip install -r requirements.txt`

### Compiles and hot-reloads for development

Place cloud_sql_proxy.exe file to this repository's parent path.  
`../../../cloud_sql_proxy -instances=[project nmae]:[Cluod SQL instance]:5432`  
`python manage.py runserver`

### Migrations

`python manage.py makemigrations`  
`python manage.py migrate`

### Dependencies update

`pip freeze > requirements.txt`

### Deply to GCP

`gcloud app deploy --project=[project id]`

### Output API Document HTML

Need to install Node.js, redoc-cli  
`npm install -g redoc-cli`

Output  
`redoc-cli bundle .\schema.yml -o ..\..\docs\api\api_doc.html`
