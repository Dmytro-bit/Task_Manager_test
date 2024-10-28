# Task Manager

### Project setup

1. start web and DB containers

```bash
   docker compose up --build
```

2. Parse CSV files

```bash
docker exec web python manage.py import_csv
```

3. Import Postman waypoints from Main.postman_collection.json