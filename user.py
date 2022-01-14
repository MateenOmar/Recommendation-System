import random

# from movieDB import Movies


class User:
    def __init__(user, number):
        user.__number = number
        user.__movies = {}
        user.__genres = {}

    def addMovie(user, movie, rating, genres):
        user.__movies[movie] = rating

        for genre in genres:

            if user.__genres.get(genre) is None:
                user.__genres[genre] = 0

            user.__genres[genre] = user.__genres[genre] + rating / 5

    def getRating(user, movie):
        return user.__movies.get(movie)

    def getRatedGenres(user):
        print(user.__genres)
        return user.__genres

    def getFavouriteGenres(user):
        keys = list(user.__genres.items())
        random.shuffle(keys)
        d = dict(keys)

        genres = sorted(d.items(), key=lambda x: x[1], reverse=True)

        favGenres = []

        for i in genres:
            favGenres.append(i[0])

        print(favGenres[0 : -(len(genres) // -4)])
        return favGenres[0 : -(len(genres) // -4)]

    def test(user):
        print("my name ", user.__number)

        for x in user.__movies:
            print(x, user.__movies[x])

    def computeMovieSimilarity(user, user2, movie):
        if user2.getRating(movie) is not None:
            return user.getRating(movie) / user2.getRating(movie)

        return 0.0

    def computeMoviesSimilarity(user, user2):
        total = 0
        count = 0

        for x in user.__movies:
            if user2.getRating(x) is not None:
                total = total + user.getRating(x) / user2.getRating(x)
                count = count + 1

        if count != 0:
            total = total / count

        return [total, count]

    def computeMoviesSimilarity2(user, user2):
        total = 0
        count = 0

        for x in user.__movies:
            if user2.getRating(x) is not None:
                total = total + user.getRating(x) * user2.getRating(x)
                count = count + 1

        if count != 0:
            total = total / count

        return [total, count]

    def similarGenres(user, db):
        return db.getSimilarGenreMovies(user.getFavouriteGenres())

    def similarMovie(user, db, movie, year):
        return db.getSimilarMovies(movie, year)
