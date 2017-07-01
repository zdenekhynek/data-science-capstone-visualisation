from flask import Flask, render_template
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)

@app.route('/')
def hello_world():
    return 'Hello, World!'

@app.route('/viz/')
def viz(name=None):
    return render_template('viz.html', name=name)


class Clusters(Resource):
    def get(self):
        return {'clusters': '123'}

api.add_resource(Clusters, '/api/clusters')
