from flask import Flask,jsonify, request

app = Flask(__name__)

@app.route('/')
def api():
    if request.method == 'GET':
        data={
            "message": "Hello"
        }
    
        return data
    if request.method =='POST':
        data = request.data
        return jsonify(data=data)

if __name__ == '__main__':
    app.run()
