# Movie Model
class Movie(object):
	# Movie Constructor
	def __init__(self, title, story_line, poster_image, trailer_youtube, year):
		self.title = title
		self.storyline = story_line
		self.poster_image_url = poster_image
		self.trailer_youtube_url = trailer_youtube
		self.year = year
