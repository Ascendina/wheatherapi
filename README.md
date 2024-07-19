# Wheather API ✨ 
A distributed system to obtain weather data from the free weather API using Python (Flask, Celery, and Redis).
😎

## Project - How it works  🙋‍♂️
This project utilizes the following Python frameworks: Flask, Celery, and Redis. The diagram below explains how these software components communicate with each other and what roles they play within the system.

<div align="center">
  <img src="https://github.com/Ascendina/wheatherapi/blob/main/diagrama_flask_celery_redis.png" alt="ProjectDiagram" style="width:50%;"/>
</div>

The client (user) makes a request, and Flask, a web framework, handles the HTTP requests, routing, and responses to the user. After that, Redis functions as a memory storage and message broker for Celery. Finally, Celery manages asynchronous task processing (fetching weather values from the free weather API and returning the processing percentage).

Beyond these frameworks, unittest and coverage (Python) were used to implement automated testing.

## How to Run 🚀

To run the project, follow this steps:

### Run Docker
```
docker run -d -p 6379:6379 redis
```

### Run Celery
```
celery -A tasks worker --loglevel=info
```


### Run Services
```
python .\services.py
```

If you'd like, you can see the project in action with some examples. Below are two examples (POST and GET). To run these examples, open a new terminal in the same directory as the project and enter the commands. For the GET example, you will need to replace the request_id value (the example uses 6861a88e-4bd8-4ee6-a904-b16d88a08716).

### Examples

#### POST
```
$headers = @{
>>     "Content-Type" = "application/json"
>> }
>>
>> $body = @{
>>     user_id = "user123"
>>     city_ids = @(3480822)
>> } | ConvertTo-Json
>> 
>> Invoke-RestMethod -Uri "http://127.0.0.1:5000/weather" -Method POST -Headers $headers -Body $body
```

#### GET
```
Invoke-RestMethod -Uri "http://127.0.0.1:5000/weather/6861a88e-4bd8-4ee6-a904-b16d88a08716" -Method GET 
```

## How to Test🚀

To test the project, follow this steps:

#### Run test
```
python -m unittest test_tasks
```

#### Verify Coverage
```
coverage run -m unittest test_tasks
```

```
coverage report
coverage html
```

