# Copyright 2018 Cleuton Sampaio

# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at

#     http://www.apache.org/licenses/LICENSE-2.0

# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import os, sys
from flask import Flask, request, redirect, url_for, abort,  json
from werkzeug.utils import secure_filename
import Foto

UPLOAD_FOLDER = 'serverutil/uploads/unknown'
ALLOWED_EXTENSIONS = set(['jpg'])

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/', methods=['POST'])
def upload_file():
    if 'file' not in request.files:
        print('No file part!', file=sys.stderr)
        return 'No File Part', 422
    file = request.files['file']
    if file.filename == '':
        print('No selected file!', file=sys.stderr)
        return 'No selected file', 400
    if file and allowed_file(file.filename):
        filename = secure_filename(file.filename)
        file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
        retorno = Foto.process()
        print('Retorno do processamento: ', retorno)
        status=200
        if not retorno:
            status=404
        response = app.response_class(
            response=json.dumps({'status':'OK'}),
            status=status,
            mimetype='application/json'
        )        
        return response
if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8088, debug=True)