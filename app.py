from flask import Flask, jsonify, request
import sqlite3

app = Flask(__name__)
db_file = "APIdata.db"

def create_connection(db_file):
    conn = None
    try:
        conn = sqlite3.connect(db_file)
    except sqlite3.Error as e:
        print(e)
    return conn

@app.route('/', methods=['GET', 'POST'])
def api_app():
    if request.method == 'GET':
        # data = {
        #     "message": "Hello"
        # }
        db= create_connection(db_file)
        cursor = db.cursor()
        data1 = cursor.execute("SELECT * FROM api")
        db.commit()
        #cursor.close()
        #db.close()
        return data1
        
        return jsonify(data)
    elif request.method == 'POST':
        data = request.json  # Assuming the data is sent in JSON format
        
        # Check if data contains the expected key
        if not data or 'key' not in data:
            return jsonify(status="error", message="Missing 'key' in request data"), 400
        
        try:
            db = create_connection(db_file)
            cursor = db.cursor()
            cursor.execute("INSERT INTO api (data) VALUES (?)", (data['key'],))
            db.commit()
            #cursor.close()
            #db.close()
            return jsonify({'Message': 'Done'})
        except sqlite3.Error as e:
            return jsonify(status="error", message=str(e)), 500
    else:
        return jsonify({'Message': 'error'})

if __name__ == '__main__':
    app.run(debug=True)
