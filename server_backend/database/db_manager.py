import sqlite3
import pandas as pd
from datetime import datetime
import os

# Put the database file in the server_backend root
DB_PATH = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "sensor_data.db")

def init_db():
    """Creates the table for machine telemetry if it doesn't exist."""
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS machine_telemetry (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            timestamp DATETIME DEFAULT CURRENT_TIMESTAMP,
            device_id TEXT,
            sound INTEGER,
            rpm_pulse INTEGER
        )
    ''')
    conn.commit()
    conn.close()
    print("Database initialized successfully.")

def insert_reading(device_id, sound, rpm_pulse):
    """Inserts a single sensor reading into the database."""
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute('''
        INSERT INTO machine_telemetry (device_id, sound, rpm_pulse)
        VALUES (?, ?, ?)
    ''', (device_id, sound, rpm_pulse))
    conn.commit()
    conn.close()

def get_training_data():
    """Extracts data into a Pandas DataFrame for the ML pipeline."""
    conn = sqlite3.connect(DB_PATH)
    query = "SELECT timestamp, sound, rpm_pulse FROM machine_telemetry"
    df = pd.read_sql_query(query, conn)
    conn.close()
    return df

# Run initialization when the script is imported
init_db()