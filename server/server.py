from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def hello_world():
    if request.method == 'POST':
        return jsonify(id=6, en='Charizard', de='Glurak')
    else:
        return 'Server running!'

if __name__ == '__main__':
    app.run(debug=True)