import sqlite3
import random

# יצירת חיבור למסד נתונים
conn = sqlite3.connect('smart_home.db')
c = conn.cursor()

# יצירת טבלאות לטמפרטורה ותאורה
c.execute("""CREATE TABLE IF NOT EXISTS temperature (
              room_id INTEGER PRIMARY KEY,
              current_temp REAL
              )""")

c.execute("""CREATE TABLE IF NOT EXISTS lighting (
              room_id INTEGER PRIMARY KEY,
              is_on TEXT
              )""")

conn.commit()

# פונקציה להוספת טמפרטורה לחדר
def insert_temperature(room_id, current_temp):
    with conn:
        c.execute("INSERT INTO temperature (room_id, current_temp) VALUES (:room_id, :current_temp)",
                  {'room_id': room_id, 'current_temp': current_temp})

# פונקציה לעדכון טמפרטורה של חדר
def update_temperature(room_id, current_temp):
    with conn:
        c.execute("""UPDATE temperature SET current_temp = :current_temp WHERE room_id = :room_id""",
                  {'room_id': room_id, 'current_temp': current_temp})

# פונקציה לקבלת טמפרטורה לפי מספר חדר
def get_temperature(room_id):
    c.execute("SELECT * FROM temperature WHERE room_id = :room_id", {'room_id': room_id})
    return c.fetchone()

# פונקציה להוספת תאורה לחדר
def insert_lighting(room_id, is_on):
    with conn:
        c.execute("INSERT INTO lighting (room_id, is_on) VALUES (:room_id, :is_on)",
                  {'room_id': room_id, 'is_on': is_on})

# פונקציה לעדכון מצב התאורה של חדר
def update_lighting(room_id, is_on):
    with conn:
        c.execute("""UPDATE lighting SET is_on = :is_on WHERE room_id = :room_id""",
                  {'room_id': room_id, 'is_on': is_on})

# פונקציה לקבלת מצב התאורה לפי מספר חדר
def get_lighting(room_id):
    c.execute("SELECT * FROM lighting WHERE room_id = :room_id", {'room_id': room_id})
    return c.fetchone()

# יצירת טמפרטורות ותאורה אקראיות לחדרים
for x in range(1, 21):
    insert_temperature(x, random.uniform(18.0, 30.0))  # טמפרטורה אקראית בין 18 ל-30
    insert_lighting(x, random.choice(['on', 'off']))  # מצב תאורה אקראי

# דוגמאות לשימוש בפונקציות
print(get_temperature(1))  # הדפסת טמפרטורה של חדר מספר 1
print(get_lighting(1))     # הדפסת מצב תאורה של חדר מספר 1

# סגירת החיבור למסד הנתונים
conn.close()
