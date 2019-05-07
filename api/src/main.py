# coding=utf-8

from flask import Flask, jsonify, request

from .entities.entity import Session, engine, Base
from .entities.user import User, UserSchema
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

Base.metadata.create_all(engine)


@app.route('/users')
def get_users():
    session = Session()
    user_objects = session.query(User).all()

    schema = UserSchema(many=True)
    users = schema.dump(user_objects)

    session.close()
    return jsonify(users.data)


@app.route('/users', methods=['POST'])
def add_user():
    posted_user = UserSchema(only=('name', 'description'))\
        .load(request.get_json())

    user = User(**posted_user.data, created_by="HTTP post request")

    session = Session()
    session.add(user)
    session.commit()

    new_user = UserSchema().dump(user).data
    session.close()
    return jsonify(new_user), 201
