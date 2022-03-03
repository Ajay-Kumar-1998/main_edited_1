from flask.helpers import flash
from flask.templating import render_template
from flask_restful import Resource, Api
from flask_restful import fields, marshal_with
from flask_restful import reqparse
from application.models import User, Deck, Card
from application.db_init import db
from flask import current_app as app
import werkzeug
from flask import abort, redirect, url_for
import random
import imp
import pandas as pd
import sqlite3
from unittest import result



user_post_args = reqparse.RequestParser()
user_post_args.add_argument('user_name')
user_post_args.add_argument('password')

card_put_args = reqparse.RequestParser()
card_put_args.add_argument('score')

deck_post_args = reqparse.RequestParser()
deck_post_args.add_argument('deck_name')

card_post_args = reqparse.RequestParser()
card_post_args.add_argument('front')
card_post_args.add_argument('back')


class UserAPI(Resource):
    #_____________________________api for registration/sign-up from(register.html)_____________________
    def post(self):
        args = user_post_args.parse_args()
        user_check = User.query.filter_by(username=args['user_name']).first()
        if user_check:
            flash('Username is already in use.', category='error')
            print("inside user_check-----------")
            return redirect('/register')             
        new_user = User(username=args['user_name'], password = args['password'])
        try:
            print("line 1------------------")
            db.session.add(new_user)
            print("line 2------------------")
            db.session.commit()
            print("line 3------------------")
            return redirect('/login')
        except:
            print("inside except-------------")
            return redirect('/register')


#______________deck apis_________________--
class DeckAPI(Resource):

    #________________used in dashboard for showing decks of user___________________   
    def get(self, username):
        decks = Deck.query.filter_by(user=username)

        r=[]
        for deck in decks:
            r.append({'deck_name':deck.deck_name, 'score':deck.score, 'last_rev':str(deck.last_rev)})         
        return r
        
#_______________________used for adding decks in dashboard__________________
    def post(self, username):
        print("entered post----------------------")
        args = deck_post_args.parse_args()
        current_decks = Deck.query.filter_by(user=username)
        deck_list=[]
        for deck_ in current_decks:
            deck_list.append(deck_.deck_name)
        new_deck_name=args['deck_name']
        if args['deck_name'] in deck_list:
            new_deck_name=str(args['deck_name'])+" - " +str(random.randint(100,10000))
        deck_to_add= Deck(deck_name=new_deck_name, user=username)
        db.session.add(deck_to_add)
        db.session.commit()
        return redirect('/dashboard')



#_______________________card apis______________________
class   CardAPI(Resource):

    #________api used for getting cards in review_______
    def get(self, deck, username):
        
        decks = Deck.query.filter_by(user=username, deck_name = deck)
        decknames=[d.deck_name for d in decks]
        if deck in decknames:
            cards = Card.query.filter_by(deck=deck)
            card_list=[]
            if cards:
                for c in cards:
                    card_list.append(c)
                random.shuffle(card_list)
                current_card= card_list.pop()
                return {
                    "card_id": current_card.card_id,
                    "deck": current_card.deck,
                    "front": current_card.front,
                    "back": current_card.back
                }
            return {}


#_______________________api for adding card in review page______
    def post(self, deck):
        args = card_post_args.parse_args()
        new_card = Card(front=args['front'], back = args['back'], deck=deck)
        db.session.add(new_card)
        db.session.commit()
        return redirect(f'/review/{deck}')


class DeckExportAPI(Resource):
# ----   /api/export/<string:deck_name>
    def get(sels, deck_name):
        print("line 1--------------------")
        connection=sqlite3.connect("dataBase/final_project.sqlite3")
        print("line 2--------------------")
        cursor=connection.cursor()
        print("line 3--------------------")
        query="select * from card where deck= '%s'" % deck_name
        print("line 4--------------------")
        cursor.execute(query)
        print("line 5--------------------")
        result=cursor.fetchall()
        print("line 6--------------------")
        for it in result:
            print(it)
        df=pd.read_sql_query(query,connection)
        print("line 7-------------------")
        df.to_csv('static/CSV/deck.csv')
        print("line 8--------------------")
        return redirect("/dashboard")
