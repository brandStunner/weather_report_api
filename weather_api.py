from dotenv import load_dotenv
import psycopg2
from config import hostname, username, database,pwd
import requests
import os
load_dotenv()

api_keys = os.getenv("api_key")

weather_api_url = "https://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={api_keys}"



def get_weather_report(cursor, connection, city_name):
    response = requests.get(weather_api_url.format(city_name = city_name, api_keys = api_keys))
    if response.status_code == 200:
        data = response.json()
        print(data)
    # parameters to store
        city = data['name']
        country = data['sys']['country']
        temperature = data['main']['temp']   
        weather_description = data['weather'][0]['description'] 
        humidity = data['main']['humidity']

    # store in database
        cursor.execute("INSERT INTO weather_report(city, country, temperature, weather_description) VALUES (%s,%s,%s,%s)", (city, country, temperature, weather_description))
        connection.commit()
        

    else:
        print("Error fetching data:", response.status_code)

def view_weather_data(cursor, connection):
    cursor.execute("SELECT * FROM weather_report")
    rows = cursor.fetchall()
    for row in rows:
        print(row)

def create_table(cursor,connection):
    create_table = f'''
        CREATE TABLE IF NOT EXISTS weather_report(
        id SERIAL PRIMARY KEY,
        city VARCHAR(100),
        country VARCHAR(60),
        temperature DECIMAL,
        weather_description VARCHAR(100),
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP   
    )
        '''
    cursor.execute(create_table)
    connection.commit()
    # cursor.close()

    print("Table created successfully.")

def weather_app():
    
    while True:
       
        try:
            connection = psycopg2.connect(
            host = hostname,
            user = username,
            dbname = database,
            password = pwd,
            port = 5432
        )
            cursor = connection.cursor()
        except Exception as e:
            print("Error connecting to the database:", e) 
            return
        create_table(cursor,connection)
        print("1. Get weather report")
        print("2. View weather report")
        print("3. Exit")
        choice = input("Enter your option: ")

        if choice == "1":
            city_name = input("Enter city of interest: ")
            get_weather_report(cursor, connection, city_name)
        elif choice == "2":
            view_weather_data(cursor,connection)
        elif choice == "3":
            cursor.close()
            connection.close()
            break
        else:
            print("Invalid choice, try again")

if __name__ == "__main__":
    weather_app()

