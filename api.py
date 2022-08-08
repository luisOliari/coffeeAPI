import numpy as np
from flask import Flask, request, render_template
import pickle


app = Flask(__name__)
model = pickle.load(open('titanic_model.pickle', 'rb'))

@app.route('/')
def index():
    return render_template('./index.html')


# from flask import Flask
# from flask import jsonify

# def create_app(enviroment):
#     app = Flask(__name__)
#     return app

# app = create_app()

# app.route('/api/v1/users', methods=['GET'])
# def get_users():
#     response = {'message': 'success'}
#     return jsonify(response)
# app.route('/api/v1/users', methods=['GET'])
# def get_users():
#     response = {'message': 'success'}
#     return jsonify(response)