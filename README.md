# Task Manager API

## Requirements

- **Python 3+**
- **PostgreSQL**
- **Docker** + **Docker compose**

## Tech Stack

- **Backend Framework**: Django
- **API Framework**: Django REST Framework
- **Database**: PostgreSQL



## Project setup

1. Clone git Repository

```bash
git clone https://github.com/Dmytro-bit/Task_Manager_test
cd Task_Manager_test
```

2. copy example.env with name .env


3. start web and DB containers

```bash
   docker compose up --build
```

4. Parse CSV files

```bash
docker exec web python manage.py import_csv
```

5. Import Postman endpoints from Main.postman_collection.json
6. Set {{url}} variable 