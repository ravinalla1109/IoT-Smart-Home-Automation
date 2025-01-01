from flask import Flask, render_template
import sqlite3

app = Flask(__name__)

@app.route('/')
def dashboard():
    conn = sqlite3.connect('backend/devices.db')
    c = conn.cursor()
    c.execute("SELECT device, state FROM devices")
    devices = c.fetchall()
    conn.close()
    return render_template('dashboard.html', devices=devices)

if __name__ == '__main__':
    app.run(debug=True)
