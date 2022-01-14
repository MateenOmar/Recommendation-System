class Movies:
    def __init__(db):
        db.__IDToTitle = {}
        db.__titleToID = {}

    def addMovie(db, ID, name, genres):
        db.__IDToTitle[ID] = name
        db.__titleToID[name] = [ID, genres.split("|"), 0, 0]

    def addRating(db, ID, rating):
        db.__titleToID[db.getNameWithYear(ID)][2] = (
            db.__titleToID[db.getNameWithYear(ID)][2] + rating
        )
        db.__titleToID[db.getNameWithYear(ID)][3] = (
            db.__titleToID[db.getNameWithYear(ID)][3] + 1
        )

    def getName(db, ID):
        return db.__IDToTitle[ID].rsplit(" ", 1)[0]

    def getNameWithYear(db, ID):
        return db.__IDToTitle[ID]

    def getID(db, name):
        return db.__titleToID[name][0]

    def getGenres(db, name):
        return db.__titleToID[name][1]

    def getYear(db, ID):
        return db.__IDToTitle[ID].rsplit(" ", 1)[1].strip("()")

    def getRating(db, name):
        if db.__titleToID[name][3] == 0:
            return 0.0

        return db.__titleToID[name][2] / db.__titleToID[name][3]

    def __getGenreSimilarity(db, movieGenres, favGenres):
        movieLen = len(movieGenres)
        favLen = len(favGenres)

        sameGenres = []

        if movieLen >= favLen:
            for m in movieGenres:
                if m in favGenres:
                    sameGenres.append(m)
        else:
            for m in favGenres:
                if m in movieGenres:
                    sameGenres.append(m)

        return sameGenres

    def __calculateGenreSimilarity(db, movieGenres, favGenres, comparee):
        similar = db.__getGenreSimilarity(movieGenres, favGenres)

        if len(similar) / len(comparee) >= 0.75:
            return 1

        return 0

    def getSimilarMovies(db, movie, year):
        recommendations = []

        genres = db.getGenres(movie + " (" + str(year) + ")")

        for m in db.__titleToID:
            if db.__calculateGenreSimilarity(db.__titleToID[m][1], genres, genres) == 1:
                if m != (movie + " (" + str(year) + ")"):
                    recommendations.append(m)

        return recommendations

    def getSimilarGenreMovies(db, favGenres):
        recommendations = []

        for m in db.__titleToID:
            if (
                db.__calculateGenreSimilarity(
                    db.__titleToID[m][1], favGenres, db.__titleToID[m][1]
                )
                == 1
            ):
                recommendations.append(m)

        return recommendations

    def printing(db):
        for i in range(1, 11):
            print("--MOVIE INFO--")
            print(db.getName(i))
            print(db.getYear(i))
            print(db.getNameWithYear(i))
            print(db.getGenres(db.getNameWithYear(i)))
            print(round(db.getRating(db.getNameWithYear(i)), 2))
            print("----\n")
