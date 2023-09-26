from flask import Flask, Response, blueprints
from src.api.api import api




app = Flask(__name__)

# register blueprint
app.register_blueprint(api)


@app.route('/')
def first_entrada():
    return Response('Hello World!', status=200)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)

