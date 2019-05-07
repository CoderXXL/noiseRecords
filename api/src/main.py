# coding=utf-8

from flask import Flask, jsonify, request

from .entities.entity import Session, engine, Base
from .entities.exam import Exam, ExamSchema

app = Flask(__name__)

Base.metadata.create_all(engine)


@app.route('/exams')
def get_exams():
    session = Session()
    exam_objects = session.query(Exam).all()

    schema = ExamSchema(many=True)
    exams = schema.dump(exam_objects)

    session.close()
    return jsonify(exams.data)


@app.route('/exams', methods=['POST'])
def add_exam():
    posted_exam = ExamSchema(only=('title', 'description'))\
        .load(request.get_json())

    exam = Exam(**posted_exam.data, created_by="HTTP post request")

    session = Session()
    session.add(exam)
    session.commit()

    new_exam = ExamSchema().dump(exam).data
    session.close()
    return jsonify(new_exam), 201
