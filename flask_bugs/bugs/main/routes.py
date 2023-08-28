from flask import Flask, url_for, render_template, Blueprint, flash
from bugs import col
main = Blueprint('main', __name__)


@main.route('/')
@main.route('/home')
def home():
    bug_tickets = col.find()
    return render_template('index.html', title='Index page', bug_tickets=bug_tickets)
