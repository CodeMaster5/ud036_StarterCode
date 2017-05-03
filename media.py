class Video():
    """ This class contains the basic information of a media """

    def __init__(self, title, synopsis, poster, trailer, rating):
        self.title = title
        self.synopsis = synopsis
        self.poster_image_url = poster
        self.trailer_youtube_url = trailer
        self.rating = rating

class Movie(Video):
    """ This class contains the specific information of a movie """

    def __init__(self, title, synopsis, poster, trailer, rating, production):
        Video.__init__(self, title, synopsis, poster, trailer, rating)
        self.production = production

class TV_Show(Video):
    """ This class contains the specific information of a tv show """

    def __init__(self, title, synopsis, poster, trailer, rating, seasons):
        Video.__init__(self, title, synopsis, poster, trailer, rating)
        self.seasons = seasons
