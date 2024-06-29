# app/server.py
from flask import Flask, render_template
from database import create_table, insert_records, fetch_records

app = Flask(__name__)

# Database initialization
create_table()  # Create a table on server startup (for demo purposes)

@app.route('/')
def index():
    # Fetch records from the database
    records = fetch_records()
    return render_template('index.html', records=records)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
