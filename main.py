from flask import Flask
from flask_login import LoginManager, login_manager
from flask_restful import Api
from application.config import LocalDevelopementConfig
from application.db_init import db
from os import path
from flask_cors import CORS

#-------------initialization-------------------
# db = SQLAlchemy()
# data_base= "final_project.sqlite3"

#---------------creating app ------------------
def create_app():
    app = Flask(__name__, template_folder="template")
    CORS(app)
    app.config['SECRET_KEY'] = 'ajay'
    # app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{data_base}'
    app.config.from_object(LocalDevelopementConfig)
    db.init_app(app)
    api = Api(app)

#-----------------adding api resources----------------
    from application.api import UserAPI, DeckAPI, CardAPI, DeckExportAPI, DeckDeleteAPI,DeckEditAPI,CardDeleteEditAPI
    api.add_resource(UserAPI, '/api/user_registration')   
    api.add_resource(DeckAPI, '/api/deck/<string:username>', '/api/delete/<string:username>/<string:deck_name>')
    api.add_resource(CardAPI, '/api/<string:username>/<string:deck>/card_review','/api/<string:deck>/card_post')
    api.add_resource(DeckExportAPI, "/api/export/<string:deck_name>")
    api.add_resource(DeckDeleteAPI, "/api/deck_delete_api/<string:username>/<string:deck_name>")
    api.add_resource(DeckEditAPI, "/api/deck_edit_api/<string:username>/<string:deck_name>")
    api.add_resource(CardDeleteEditAPI,"/api/card_delete_edit/<string:deck_name>/<int:card_id>")

#------------- creating view blue prints--------------
    from application.controllers import views
    app.register_blueprint(views, url_prefix="/")

#---------------importing models(tabels)-------------
    from application.models import User, Deck, Card

#---------------creating db--------------------------
    # create_db(app)

#-----------------login manager--------------
    login_manager = LoginManager()
    login_manager.login_view = "views.login"
    login_manager.init_app(app)
    @login_manager.user_loader
    def load_user(id):
        return User.query.get(int(id))

#---------------- returnind app, api----------------
    return  app, api

if __name__ == "__main__":
    app, api = create_app()   
    app.run(debug=True, host="0.0.0.0", port=5000)


#-----------------------creating db function-----------
# def create_db(app):
#     if not path.exists("main_folder/"+ data_base):
#         db.create_all(app=app)
#     print('DATABASE ALREADY EXISTS')