import flask
from flask import request, jsonify

app = flask.Flask(__name__)
app.config["DEBUG"] = True


@app.route('/student/', methods=['GET'])
def home():
    return jsonify({'Student Name':'Prakhar Shrivas',
                    'Enrollment':'EN19CS304011' , 
                    'assignment': 'numpy.txt' , 
                    'plagiarism percent' : '87'})
app.run()