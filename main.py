from flask import Flask
from flask_restful import Api, Resource, reqparse


from resistor_pick import pick, RESISTORS
from db_ops import db


app = Flask('ResistorPicker')
api = Api(app)
 #Need to implement a way to check if there is a db in root so we can setup from main




class Resistor(Resource):
    def get(self, target_resistance):
        dev_db = db()
        data = pick(target_resistance, dev_db.get_lab_res())
        return data


api.add_resource(Resistor, '/api/v1/resistor/<int:target_resistance>')


if __name__ == '__main__':
    app.run(port=4848, debug=True, host='0.0.0.0')