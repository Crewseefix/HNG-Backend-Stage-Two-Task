# API Documentation
This API supports Basic CRUD operations on a Person Object.
## Getting Started
- This API has four endpoints, each for Creating, Reading, Updating and Deleting a Person.
- The API accepts requests and returns responses in JSON format.
## Person
The `/api` and `/api/{user_id}` paths lets you manage information about the person.
- The Person object has four fields: `'name'`, `'sex'`, `'religion'` and `'country'`.
- The `'name'` field is required and must be supplied.
- The `'sex'` and `'religion'` field are optional and may be omitted.
- The `'country'` field is optional and defaults to 'Nigeria'.
## GET (READ ENDPOINT)
Reads person with the given user_id.
### Request URL
```sh
https://crewseefix.pythonanywhere.com/api/{user_id}
```
### Example
### URL
```sh
https://crewseefix.pythonanywhere.com/api/1
```
### Response
```sh
{
    'name': 'mark Eessien',
    'sex': 'male',
    'religion': 'christian',
    'country': 'Nigeria'
}
```
### Error Response
```sh
{
    'detail': '...'
}
```
## POST (CREATE ENDPOINT)
Creates person with the given JSON request body.
### Request URL
```sh
https://crewseefix.pythonanywhere.com/api
```
### Example
### Request Body
```sh
{
    'name': 'mark Eessien',
    'sex': 'male' or 'female',
    'religion': 'christian' or 'muslim' or 'other',
    'country': 'Nigeria' or any other real country
}
```
### Response
```sh
{
    'name': 'mark Eessien',
    'sex': 'male',
    'religion': 'christian',
    'country': 'Nigeria'
}
```
### Error Response
```sh
{
    'detail': '...'
}
```
## PATCH (UPDATE ENDPOINT)
Updates person with the given JSON request body.
### Request URL
```sh
https://crewseefix.pythonanywhere.com/api/{user_id}
```
### Example
### URL
```sh
https://crewseefix.pythonanywhere.com/api/1
```
### Request Body
```sh
{
    'name': 'mark Eessien',
    'sex': 'male' or 'female',
    'religion': 'christian' or 'muslim' or 'other',
    'country': 'Nigeria' or any other real country
}
```
### Response
```sh
{
    'name': 'mark Eessien',
    'sex': 'male',
    'religion': 'christian',
    'country': 'Nigeria'
}
```
### Error Response
```sh
{
    'detail': '...'
}
```
## DELETE (DELETE ENDPOINT)
Deletes person with the given user_id.
### Request URL 
```sh
https://crewseefix.pythonanywhere.com/api/{user_id}
```
### Example
### URL
```sh
https://crewseefix.pythonanywhere.com/api/1
```
### Response
```sh
{
    'detail': '...deleted sucessfully'
}
```
### Error Response
```sh
{
    'detail': '...'
}
```