# importing Movie data
import app.db.movie as db

# importing fresh_tomatoes library
from app.lib import fresh_tomatoes

##################################################
# start generating the index.html
# write index.html at app/http
# start web server at app/http
# open browser with http://127.0.0.1:13579
##################################################
fresh_tomatoes.open_movies_page(db.movie_data)
