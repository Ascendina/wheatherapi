CREATE TABLE IF NOT EXISTS requested_ID_weather (
    request_id TEXT PRIMARY KEY,
    user_id TEXT, 
    total_cities INTEGER
);

CREATE TABLE IF NOT EXISTS weather_data (
    request_id TEXT,
    user_id TEXT,
    datetime TEXT,
    city_id INTEGER,
    temperature REAL,
    humidity INTEGER,
    FOREIGN Key (request_id) REFERENCES requested_ID_weather (request_id) 
);

