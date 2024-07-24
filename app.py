from flask import Flask, render_template, request
import sqlite3

app = Flask(__name__)

@app.route('/')
def home():
    conn = sqlite3.connect('healthcare.db')
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM vitals')
    data = cursor.fetchall()
    conn.close()
    return render_template('index.html', data=data)

@app.route('/add', methods=['POST'])
def add_vital():
    heart_rate = request.form['heart_rate']
    blood_pressure = request.form['blood_pressure']
    temperature = request.form['temperature']
    conn = sqlite3.connect('healthcare.db')
    cursor = conn.cursor()
    cursor.execute('INSERT INTO vitals (heart_rate, blood_pressure, temperature) VALUES (?, ?, ?)', (heart_rate, blood_pressure, temperature))
    conn.commit()
    conn.close()
    return 'Data added'

if __name__ == '__main__':
    app.run(debug=True)
