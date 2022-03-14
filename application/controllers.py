#from re import S
from flask import Blueprint, render_template, request, flash
from flask_login import login_user, logout_user, current_user
from flask_login.utils import login_required
from werkzeug.utils import redirect
from application.models import User, Deck , Card

from application.db_init import db
import requests
from datetime import datetime

views= Blueprint("views", __name__)



#________________________landing page/home page_____________________--
@views.route('/', methods=['GET'])
def home_page():
    return render_template('home_page_.html')


#________________________________login page_____________________________
@views.route('/login', methods = ['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form.get("user_name")
        password = request.form.get("password")

        user = User.query.filter_by(username=username).first()
        if user:
            if user.password==password:
                login_user(user, remember=True)
                return redirect('/dashboard')
            else:
                flash('Pls trpe the right passowrd.', category='error')
        else:
            flash('No user, with that user name', category='error')

    return render_template('login_.html')



#____________________________ link for sign-up / register_____________________________
@views.route('/register', methods = ['GET', 'POST'])
def register():
    return render_template('register_.html')


#_________________________dashboard______________________--
@views.route('/dashboard', methods = ['GET', 'POST'])
@login_required
def dashboard():
    deck_info= requests.get(f'http://127.0.0.1:5000/api/deck/{current_user.username}')    
    return render_template('dashboard_.html', decks=deck_info.json(), user=current_user.username)


#______________________ reviewing page of deck__________________________
@views.route('/review/<string:deck>', methods = ['GET', 'POST'])
@login_required
def review(deck):
    data=requests.get(f'http://127.0.0.1:5000/api/{current_user.username}/{deck}/card_review') 
    if data:
        return render_template('review.html', question = data.json()['front'], answer = data.json()['back'], deck=data.json()['deck'], card_id=data.json()['card_id'], data=True)
    else:
        return render_template('review.html', deck=deck, data=False)



#________________________ score postion page in review deck________________-
@views.route('/review/<string:deck>/<int:card_id>', methods = ['GET', 'POST'])
def score(deck,card_id):
    if request.method == 'POST':
        card= Card.query.filter_by(card_id=card_id).first()
        score_= int(request.form.get('score'))
        card.score = score_
        db.session.commit()
        deck_cards= Deck.query.filter_by(deck_name=deck, user=current_user.username).first()
        card_count= Card.query.filter_by(deck=deck).count()
        deck_cards.score = deck_cards.score + (card.score/card_count)
        db.session.commit()
        return redirect(f'/review/{deck}')



#____________________ for deleting deck in dashboard______________-
@views.route('/<string:user>/deck/<string:deck>/delete', methods=['GET','POST'])
def deletedeck(deck, user):
    print("line 1------------------------")
    deck_to_delete= Deck.query.filter_by(deck_name=deck, user=user).first()
    print("line 2------------------------")
    db.session.delete(deck_to_delete)
    print("line 3------------------------")
    db.session.commit()
    print("line 4------------------------")
    return redirect('/dashboard')


#______________________logout route___________
@views.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect('/')