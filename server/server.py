import os
from flask import Flask, abort, request, jsonify
from flask_cors import CORS
from flask_ngrok import run_with_ngrok
from werkzeug.utils import secure_filename

from classifier import Classifier

app = Flask(__name__)
CORS(app)
run_with_ngrok(app)
app.config['UPLOAD_FOLDER'] = './uploads'

classifier = Classifier()

@app.route('/', methods=['GET', 'POST'])
def hello_world():
    if request.method == 'POST':
        file = request.files['file']
        if file and file.filename:
            filename = secure_filename(file.filename)
            filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
            
            if not os.path.exists(app.config['UPLOAD_FOLDER']):
                os.makedirs(app.config['UPLOAD_FOLDER'])
            
            file.save(filepath)
            
            pokemon_id, pokemon_en, pokemon_de = classifier.classify(filepath)
            print('CLASSIFIED:', pokemon_en)
            return jsonify(id=pokemon_id, en=pokemon_en, de=pokemon_de)
        else:
            abort(400)
    else:
        return 'Server running!'

if __name__ == '__main__':
    app.run()
