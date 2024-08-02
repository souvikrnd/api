from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def api():
    if request.method == 'GET':
        data = {
            "message": "Hello"
        }
        return jsonify(data)
    elif request.method == 'POST':
        data = request.json  # Assuming the data is sent in JSON format
        return jsonify(data=data)

if __name__ == '__main__':
    app.run(debug=True)
