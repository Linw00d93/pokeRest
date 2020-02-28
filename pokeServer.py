#!/usr/bin/python3
from flask import Flask, request, jsonify
from flask_restful import Resource, Api
from sqlalchemy import create_engine
from json import dumps
import os
db_connect = create_engine('sqlite:///thePokedex.db')
app = Flask(__name__)
api = Api(app)


###############################################################################
#pikachu
#ash pokemon find ouut how to not return null values
###############################################################################



class Pokedex(Resource):
    def get(self):
        conn = db_connect.connect()
        query = conn.execute("select pokedex_number, name, japanese_name, generation from pokedex1 where name is not null order by name")
        return {'pokedex': [dict(zip(tuple (query.keys()) ,i)) for i in query.cursor]}
        return jsonify(result)
        conn.close()


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
        conn.close()

class Number(Resource):
    def get(self, pokedex_number):
        conn = db_connect.connect()
        query = conn.execute("select * from pokedex1 where pokedex_number =%d order by name"  %int(pokedex_number))
        result = {'data': [dict(zip(tuple (query.keys()) ,i)) for i in query.cursor]}
        return jsonify(result)
        conn.close()


class Name(Resource):
    def get(self,name):
        conn = db_connect.connect()
        name.capitalize()
        query = conn.execute("select * from pokedex1 where name like '%s' order by name" %str(name))
        result = {'data': [dict(zip(tuple (query.keys()) ,i)) for i in query.cursor]}
        return jsonify(result)
        conn.close()

class Strongest(Resource):
    def get(self):
        conn = db_connect.connect()
        query = conn.execute(" select name, attack, pokedex_number, classfication, type1, type2 from pokedex1 order by attack desc limit 10 ")
        result = {'data': [dict(zip(tuple (query.keys()) ,i)) for i in query.cursor]}
        return jsonify(result)
        conn.close()

class Fastest(Resource):
    def get(self):
        conn = db_connect.connect()
        query = conn.execute(" select name, speed, pokedex_number, classfication, type1, type2 from pokedex1 order by speed desc limit 10 ")
        result = {'data': [dict(zip(tuple (query.keys()) ,i)) for i in query.cursor]}
        return jsonify(result)
        conn.close()

class Heaviest(Resource):
    def get(self):
        conn = db_connect.connect()
        query = conn.execute(" select name, weight, pokedex_number, classfication, type1, type2 from pokedex1 order by weight desc limit 10 ")
        result = {'data': [dict(zip(tuple (query.keys()) ,i)) for i in query.cursor]}
        return jsonify(result)
        conn.close()

class Lightest(Resource):
    def get(self):
        conn = db_connect.connect()
        query = conn.execute(" select name, weight, pokedex_number, classfication, type1, type2 from pokedex1 where weight is not null order by weight asc limit 10  ")
        result = {'data': [dict(zip(tuple (query.keys()) ,i)) for i in query.cursor]}
        return jsonify(result)
        conn.close()

class MostHP(Resource):
    def get(self):
        conn = db_connect.connect()
        query = conn.execute(" select name, hp, pokedex_number, classfication, type1, type2 from pokedex1 order by hp desc limit 10 ")
        result = {'data': [dict(zip(tuple (query.keys()) ,i)) for i in query.cursor]}
        return jsonify(result)
        conn.close()

class Tallest(Resource):
    def get(self):
        conn = db_connect.connect()
        query = conn.execute(" select name, height, pokedex_number, classfication, type1, type2 from pokedex1 where height is not null order by height desc limit 10 ")
        result = {'data': [dict(zip(tuple (query.keys()) ,i)) for i in query.cursor]}
        return jsonify(result)
        conn.close()

class Type(Resource):
    def get(self, type):
        conn = db_connect.connect()
        query = conn.execute("select * from pokedex1 where type1 ='%s' order by name"  %str(type))
        result = {'data': [dict(zip(tuple (query.keys()) ,i)) for i in query.cursor]}
        return jsonify(result)
        conn.close()


class Legend(Resource):
    def get(self):
        conn = db_connect.connect()
        query = conn.execute(" select * from pokedex1 where is_legendary= 1")
        result = {'data': [dict(zip(tuple (query.keys()) ,i)) for i in query.cursor]}
        return jsonify(result)
        conn.close()


api.add_resource(Pokedex, '/pokedex')
api.add_resource(Number, '/pokedex/pokeNumber/<pokedex_number>')
api.add_resource(Type, '/pokedex/type/<type>')
api.add_resource(Name, '/pokedex/name/<name>')
api.add_resource(Legend, '/pokedex/legendary/')
api.add_resource(Strongest, '/pokedex/strongest/')
api.add_resource(MostHP, '/pokedex/MostHP/')
api.add_resource(Lightest, '/pokedex/lightest/')
api.add_resource(Heaviest, '/pokedex/heaviest/')
api.add_resource(Fastest, '/pokedex/fastest/')
api.add_resource(Tallest, '/pokedex/tallest/')
if __name__ == '__main__':
	app.run(host = '0.0.0.0' , port= 1993, debug = False )
