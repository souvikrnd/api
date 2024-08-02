from flask import Flask,jsonify, request
import sqlite3

app = Flask(__name__)
db_file ="APIdata.db"

@app.route('/')
def api_app():
    if request.method == 'GET':
        data={
            "message": "Hello"
        }
    
        return data
    elif request.method =='POST':
        data = request.data
        db = create_connection(db_file)
        cursor = db.cursor()
        cursor.execute("INSERT INTO api(data) values(?)",(data['key'],))
        db.commit()
        cursor.close()
        db.close()
        return jsonify({'Message': 'Done'})
            
        
if __name__ == '__main__':
    app.run(debug=True)
