from celery import Celery
from celery.utils.log import get_task_logger
import requests
from datetime import datetime
from DB import get_db
import logging
from celery.contrib import rdb

app = Celery('tasks', broker='redis://localhost:6379/0')



# Configurar o logging
logger = logging.getLogger('celery_app')
logger.setLevel(logging.DEBUG)

# Criar um handler para o console
console_handler = logging.StreamHandler()
console_handler.setLevel(logging.DEBUG)

# Criar um formatter e adicionar ao handler
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
console_handler.setFormatter(formatter)

# Adicionar o handler ao logger
logger.addHandler(console_handler)

# Configurar o logging do Celery para usar o mesmo logger
app.conf.update(
    worker_hijack_root_logger=False,
    worker_log_format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    worker_task_log_format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
)

API_KEY = "fe51ec7a7dc746a81cfb09743ebaab46"
BASE_URL = 'http://api.openweathermap.org/data/2.5/weather'

@app.task
def collect_weather(request_id, user_id, city_ids, all_cities):
    db = get_db()

    for city_id in city_ids: 
        # Coletar dados do OpenWeather
        params = {
            'id': city_id,
            'appid': API_KEY,
            'units': 'metric'
        }
        response = requests.get(BASE_URL, params=params)

        #if response.status_code != 200:
        #    continue

        weather_data = response.json()
        temperature = weather_data['main']['temp']
        humidity = weather_data['main']['humidity']

        logger.debug('request_id %s', request_id)

        # Armazenar no banco de dados
        db.execute('PRAGMA foreign_keys = ON;')

        logger.debug("Value Receveid Request_ID BD---------------------")
        logger.debug('request_id %s', request_id)

        dateTime = datetime.now().isoformat()
        total_cities = all_cities

        db.execute ('''
            INSERT INTO requested_ID_weather(request_id, user_id, total_cities) 
                    VALUES (?,?,?) ON CONFLICT(request_id) DO NOTHING
        ''', (request_id, user_id, total_cities))
        db.commit()


        db.execute('''
            INSERT INTO weather_data (user_id, datetime, city_id, temperature, humidity)
            VALUES (?, ?, ?, ?, ?)
        ''', (user_id, dateTime, city_id, temperature, humidity))
        db.commit()

        db.execute ('''
            UPDATE weather_data SET request_id = ? WHERE user_id = ? AND datetime = ?
        ''', (request_id, user_id, dateTime))
        db.commit()        
    db.close()

    logger.debug("END ------------------------------- BD")