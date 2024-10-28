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

## API endpoints 
| **Section** | **Endpoint Name**       | **Method** | **Endpoint Path**                       | **Body (JSON)**                                                                                                 |
|-------------|--------------------------|------------|-----------------------------------------|------------------------------------------------------------------------------------------------------------------|
| Projects    | All projects             | GET        | `{{url}}api/projects/`                  | None                                                                                                             |
| Projects    | Add user to project      | POST       | `{{url}}api/projects/<pr_id>/add-user/` | `{ "email": "davidwilson@example.com" }`                                                                        |
| Tasks       | Get tasks by project     | GET        | `{{url}}api/tasks/by-project/`          | `{ "project_id": 1, "email": "davidwilson@example.com" }`                                                       |
| Users       | Create user              | POST       | `{{url}}api/users/`                     | `{ "name": "Micle", "email": "michaeljohnson2@example.com", "password": "password123" }`                        |
| Users       | Delete user              | DELETE     | `{{url}}api/users/1/`                   | `{ "password": "password123" }`                                                                                 |
| Users       | Edit user                | PATCH      | `{{url}}api/users/3/`                   | `{ "name": "New Name" }`                                                                                        |
| Users       | Get user                 | GET        | `{{url}}api/users/2/`                   | None                                                                                                             |
