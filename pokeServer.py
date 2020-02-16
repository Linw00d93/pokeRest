#!/usr/bin/python3
from flask import Flask, request, jsonify
from flask_restful import Resource, Api
from sqlalchemy import create_engine
from json import dumps
import os
db_connect = create_engine('sqlite:///thePokedex.db')
app = Flask(__name__)
api = Api(app)


class Pokedex(Resource):
    def get(self):
        conn = db_connect.connect() # connect to database
        query = conn.execute("select * from pokedex") # This line performs query and returns json result
        return {'pokedex': [i[0] for i in query.cursor.fetchall()]} # Fetches first column that is Employee ID

    def post(self):
        conn = db_connect.connect()
        print(request.json)
        pokedex_number = request.json['pokedex_number']
        name = request.json['name']
        japanese_name = request.json['japanese_name']
        classfication = request.json['classfication']
        height_m = request.json['height_m']
        weight_kg = request.json['weight_kg']
        hp = request.json['hp']
        attack = request.json['attack']
        defense = request.json['defense']
        sp_attack = request.json['sp_attack']
        sp_defense = request.json['sp_defense']
        speed = request.json['speed']
        type1 = request.json['type1']
        type2 = request.json['type2']
        generation = request.json['generation']
        is_legendary = request.json['is_legendary']
        query = conn.execute("insert into pokemon values(null, '{0}','{1}','{2}','{3}', \
                             '{4}','{5}','{6}','{7}','{8}','{9}','{10}','{11}','{12}', \
                             '{13}', ''{14}', '{15}')".format(pokedex_number,name,japanese_name,
                             classfication, height_m, weight_kg, hp, attack, defense, sp_attack,
                             sp_defense, speed, type1, type2, generation, is_legendary))
        return {'status':'success'}

api.add_resource(Pokedex, '/pokedex') # Route_1

if __name__ == '__main__':
	app.run(host = '0.0.0.0' , port= 1993, debug = False )
