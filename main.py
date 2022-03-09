from flask import Flask
from flask_restful import Api, Resource, reqparse


from resistor_pick import pick, RESISTORS


app = Flask('ResistorPicker')
api = Api(app)


class Resistor(Resource):
    def get(self, target_resistance):
        data = pick(target_resistance, RESISTORS)
        return data


api.add_resource(Resistor, '/api/v1/resistor/<int:target_resistance>')


if __name__ == '__main__':
    app.run(debug=True)