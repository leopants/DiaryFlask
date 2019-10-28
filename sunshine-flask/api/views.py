from flask import Blueprint, jsonify, request
from . import db
from .models import Entry

main = Blueprint('main', __name__)


@main.route('/add_entry', methods=['POST'])
def add_entry():
    entry_data = request.get_json()

    new_entry = Entry(body=entry_data['body'], tag=entry_data['tag'], date=entry_data['date'])  # noqa

    db.session.add(new_entry)
    db.session.commit()

    return 'Done', 201


@main.route('/entries')
def entries():
    entry_list = Entry.query.all()
    entries = []

    for entry in entry_list:
        entries.append({'body': entry.body, 'tag': entry.tag, 'date': entry.date}) # noqa

    return jsonify({'entries': entries})
