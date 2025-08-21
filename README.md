# Weather App

A Python CLI app that fetches weather data from OpenWeatherMap API and stores it in PostgreSQL.

## Setup

1. Install dependencies:
   ```bash
   pip install psycopg2 requests python-dotenv
   ```

2. Create `config.py` with your PostgreSQL credentials:
   ```python
   hostname = "your_host"
   username = "your_username"
   database = "your_database"
   pwd = "your_password"
   ```

3. Create `.env` file with your OpenWeatherMap API key:
   ```
   api_key=your_api_key_here
   ```

4. Add to `.gitignore`:
   ```
   .env
   config.py
   ```

## Usage

```bash
python weather_api.py
```

**Menu Options:**
1. Get weather report for a city
2. View stored weather data
3. Exit

## Features

- Fetches real-time weather data
- Stores data in PostgreSQL (city, country, temperature, description)
- View historical weather reports
- Auto-creates database table

## Requirements

- Python 3.x
- PostgreSQL
- OpenWeatherMap API key
