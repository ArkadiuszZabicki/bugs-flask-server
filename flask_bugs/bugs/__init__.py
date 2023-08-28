from flask import Flask
import pymongo
from dotenv import dotenv_values
config = dotenv_values('.env')
mongo = pymongo.MongoClient(config['MONGO_URI'])
db = pymongo.database.Database(mongo, config['DB_NAME'])
col = pymongo.collection.Collection(db, config['DB_COLLECTION'])


def create_app():
    app = Flask(__name__)
    from bugs.main.routes import main
    app.register_blueprint(main)
    return app
