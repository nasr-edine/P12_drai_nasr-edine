# Develop a secure back-end architecture using Django ORM

## Rights for each models

![rights for each models](https://github.com/nasr-edine/P12_drai_nasr-edine/blob/develop/database_diagram/rights%20of%20each%20models.png?raw=true)

## Entity Relationship Diagram (ERD)

![Entity Relationship Diagram (ERD)](https://github.com/nasr-edine/P12_drai_nasr-edine/blob/develop/database_diagram/entity_relationship_diagram.jpg?raw=true)

## Installation

clone repository locally

```bash
git clone https://github.com/nasr-edine/P12_drai_nasr-edine.git
```

Move to the P12_drai_nasr-edine root folder then backend folder with:

```bash
cd P12_drai_nasr-edine/backend/
```

Create a virtual environment in root folder of project

```bash
python3 -m venv env
```

Activate virtual environment

```bash
source ./env/bin/activate
```

Install dependencies

```bash
pip install -r requirements.txt
```

Create a database and configure parameters in django settings file

```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'your_database_name',
        'USER':  'your_server_database_username',
        'PASSWORD': 'your_password',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}
```

Make Migration for 3 apps in the order below:

```bash
django mm staff
django mm customer
django mm contract
```

Migrate

```bash
django m
```

Create a super user in command line:

```bash
django csu
```

Run python script "add_permissions.py" to set groups and permissions

```bash
django s < add_groups_permissions.py
```

## Usage

Run the Django Server:

```bash
django r
```

## Access to API documentation:

[https://documenter.getpostman.com/view/5359695/UUxxfTGb](https://documenter.getpostman.com/view/5359695/UUxxfTGb)

## Using django admin

Open your browser and enter the URL below and login as superuser:
[http://localhost:8000/adminzone/](http://localhost:8000/adminzone/)
