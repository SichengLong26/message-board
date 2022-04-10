from flask import render_template, flash, url_for
from werkzeug.utils import redirect

from messageboard import app, db
from messageboard.forms import HelloForm
from messageboard.models import Message


@app.route('/', methods=['GET','POST'])
def index():
    form = HelloForm()
    if form.validate_on_submit():
        name = form.name.data
        body = form.body.data
        message = Message(name=name, body=body)
        db.session.add(message)
        db.session.commit()
        flash('Your messages have been submitted successfully!')
        return redirect(url_for('index'))
        
    messages = Message.query.order_by(Message.timestamp.desc()).all()
    return render_template('index.html', form=form, messages=messages)