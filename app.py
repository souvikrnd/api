from flask import Flask,jsonify
import sqlite3

app = Flask(__name__)
db_file ="APIdata.db"

@app.route('/')
def api():
    if request.method == 'GET':
        data={
            "message": "Hello"
        }
    
        return data
    if request.method =='POST':
        data = request.data
        
        db = create_connection(db_file)
        cursor = db.cursor()
        cursor.execute("INSERT INTO api(data) values(?)",(data['key'],))
        db.commit()
        cursor.close()
        db.close()
        
        
        return jsonify(data=data)

if __name__ == '__main__':
    app.run()
