# HNG Backend Stage Two Task

## Setup

This django app was developed with python 3.10.5. 
It is an API that supports CRUD operations on a Person Object with a 'name' field.

From the root directory run the command in the terminal to install dependencies:
```sh
pip install -r requirements.txt
```
Start the server:
```sh
python manage.py runserver
```

## Using the API
The API provides four endpoints for interacting with the Person Object.

Create endpoint using POST request:
```sh
localhost:8000/api
```
Read endpoint using GET request:
```sh
localhost:8000/api/user_id
```
Update endpoint using PATCH request
```sh
localhost:8000/api/user_id
```
Delete endpoint using DELETE request
```sh
localhost:8000/api/user_id
```
## Testing
Use the postman collection provided.