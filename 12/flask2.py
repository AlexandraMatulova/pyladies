from flask import Flask, abort
from flask import url_for
import json

app = Flask(__name__)
app.config['DEBUG'] = True


@app.route('/')
def index():    
    return '''Ukazka celedi rostlin: pro zobrazeni zastupcu 
        zadej do url adresy lomitko a jednu z nasledujicich celedi: 
        amarylkovite, aralkovite, brukvovite, hluchavkovite, koprivovite'''

@app.route('/<celedi>')
def celedi(celedi):
    with open('flask.txt') as file_:
        celedi_dict = json.loads(file_.read())
    if celedi not in celedi_dict:
        abort(404)
    return ','.join(celedi_dict[celedi])

if __name__ == "__main__":
    app.run(host='127.0.0.1', port=5001)