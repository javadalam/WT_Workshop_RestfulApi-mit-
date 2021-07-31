from flask import Flask
from flask_restful import Resource, Api 
 
app = Flask(__name__)
api = Api(app)

class People(Resource):
    def get(self, Name, Age , Mail , Gender):
        return{"name" : Name , "age" : Age , "mail" : Mail , "gender" : Gender}

api.add_resource(People,"/people/<string:Name>/<int:Age>/<string:Mail>/<string:Gender>")

if __name__ == "__main__":
    app.run(debug=True)