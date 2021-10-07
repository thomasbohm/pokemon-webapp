import os
from flask import Flask, abort, request, jsonify
from flask_cors import cross_origin
from werkzeug.utils import secure_filename

from classifier import Classifier

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = './uploads'

classifier = Classifier()

@app.route('/', methods=['GET', 'POST'])
@cross_origin(origins=['http://localhost:3000'])
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
            return jsonify(id=pokemon_id, en=pokemon_en, de=pokemon_de)
        else:
            abort(400)
    else:
        return 'Server running!'

if __name__ == '__main__':
    app.run(debug=True)