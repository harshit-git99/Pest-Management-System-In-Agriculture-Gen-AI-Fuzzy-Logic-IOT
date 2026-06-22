from pathlib import Path
import sqlite3, json
from datetime import datetime, timedelta
from werkzeug.security import generate_password_hash

BASE=Path(__file__).resolve().parents[1]
DB=BASE/'instance'/'agropest.db'
DB.parent.mkdir(exist_ok=True)
conn=sqlite3.connect(DB)
cur=conn.cursor()
cur.executescript('''
CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY AUTOINCREMENT,name TEXT NOT NULL,email TEXT UNIQUE NOT NULL,password_hash TEXT NOT NULL,role TEXT NOT NULL,farm_name TEXT,location TEXT,created_at TEXT NOT NULL);
CREATE TABLE IF NOT EXISTS detections (id INTEGER PRIMARY KEY AUTOINCREMENT,user_id INTEGER NOT NULL,crop_type TEXT NOT NULL,field_name TEXT,image_path TEXT,pest TEXT NOT NULL,confidence REAL NOT NULL,severity REAL NOT NULL,temperature REAL NOT NULL,humidity REAL NOT NULL,risk TEXT NOT NULL,risk_score REAL NOT NULL,advice_json TEXT NOT NULL,notes TEXT,status TEXT DEFAULT 'Open',created_at TEXT NOT NULL);
CREATE TABLE IF NOT EXISTS feedback (id INTEGER PRIMARY KEY AUTOINCREMENT,detection_id INTEGER NOT NULL,user_id INTEGER NOT NULL,rating INTEGER NOT NULL,outcome TEXT NOT NULL,comment TEXT,created_at TEXT NOT NULL);
CREATE TABLE IF NOT EXISTS sensor_logs (id INTEGER PRIMARY KEY AUTOINCREMENT,user_id INTEGER NOT NULL,field_name TEXT NOT NULL,temperature REAL NOT NULL,humidity REAL NOT NULL,soil_moisture REAL NOT NULL,pest_count INTEGER NOT NULL,created_at TEXT NOT NULL);
''')
