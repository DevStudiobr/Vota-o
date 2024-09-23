from flask import Flask, render_template, request, redirect, url_for, jsonify
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///votes.db'
db = SQLAlchemy(app)

class Poll(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    question = db.Column(db.String(200), nullable=False)
    options = db.Column(db.String(500), nullable=False)
    votes = db.Column(db.String(500), nullable=False, default='')

@app.route('/')
def index():
    polls = Poll.query.all()
    return render_template('index.html', polls=polls)

@app.route('/create_poll', methods=['POST'])
def create_poll():
    question = request.form['question']
    options = request.form['options'].split(',')
    poll = Poll(question=question, options=','.join(options))
    db.session.add(poll)
    db.session.commit()
    return redirect(url_for('index'))

@app.route('/vote/<int:poll_id>', methods=['POST'])
def vote(poll_id):
    poll = Poll.query.get_or_404(poll_id)
    votes = poll.votes.split(',') if poll.votes else []
    option = request.form['option']
    if option in votes:
        votes.remove(option)
    else:
        votes.append(option)
    poll.votes = ','.join(votes)
    db.session.commit()
    return redirect(url_for('index'))

if __name__ == '__main__':
    db.create_all()
    app.run(debug=True)
