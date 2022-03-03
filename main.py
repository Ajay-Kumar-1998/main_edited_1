from flask import Flask
from flask_login import LoginManager, login_manager
from flask_restful import Api
from application.config import LocalDevelopementConfig
from application.db_init import db
from os import path

#-------------initialization-------------------
# db = SQLAlchemy()
# data_base= "final_project.sqlite3"

#---------------creating app ------------------
def create_app():
    app = Flask(__name__, template_folder="template")
    app.config['SECRET_KEY'] = 'ajay'
    # app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{data_base}'
    app.config.from_object(LocalDevelopementConfig)
    db.init_app(app)
    api = Api(app)

#-----------------adding api resources----------------
    from application.api import UserAPI, DeckAPI, CardAPI, DeckExportAPI
    api.add_resource(UserAPI, '/api/user', '/api/user/<string:username>')   
    api.add_resource(DeckAPI, '/api/deck/<string:username>')
    api.add_resource(CardAPI, '/api/<string:username>/<string:deck>/card', '/api/card/<string:card_id>','/api/<string:deck>')
    api.add_resource(DeckExportAPI, "/api/export/<string:deck_name>")

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