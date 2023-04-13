import os
from flask import (
  Flask,
  request,
  abort,
  jsonify
)
from models import setup_db, Movie, Actor
from flask_cors import CORS

def create_app(test_config=None):

    app = Flask(__name__)
    setup_db(app)
    CORS(app)

    @app.route('/')
    def get_greeting():
        excited = os.environ['EXCITED']
        greeting = "Hi" 
        if excited == 'true': 
            greeting = greeting + "!!!!! You are doing great in this Udacity project."
        return greeting

    @app.route('/coolkids')
    def be_cool():
        return "Be cool, man, be coooool! You're almost a FSND grad!"
    
    @app.route('/movies', methods=['GET'])
    def get_movies():
        return "this is movies endpoint"
        # try:
        #     select_movies = Movie.query.order_by(Movie.id).all()   
        #     format_movies = [movies.format() for movies in select_movies]
        #     print("Select movies:",select_movies)
        #     print("format movies:",format_movies)
        #     if len(select_movies) ==0:
        #         abort(404)
        #     else:    
        #         return jsonify({
        #         'success':True,
        #         'movies':format_movies
        #     })
        # except Exception as e:
        #     print("get movies exception",e)

    return app

app = create_app()

if __name__ == '__main__':
    app.run()
