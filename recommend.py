from user import User
from movieDB import Movies
import csv

# change into binary insert
def insertSimilarityArray(simScore, simArr, simDict, left, right):

    i = 0

    for i in range(0, right):
        altScore = abs(1 - simDict[simArr[i]][0])
        if altScore > simScore:
            return i
        i = i + 1

    # if(right == 0):
    #     return 0

    # index = left + (right - left) // 2

    # altScore = abs(1 - simDict[simArr[index]][0])

    # if(simScore <= altScore):
    #     insertSimilarityArray(simScore, simArr, simDict, left, index)

    # if(simScore > altScore):
    #     insertSimilarityArray(simScore, simArr, simDict, index, right)

    return i


moviesDB = Movies()
users = {}

print("\n\n------------------------------MOVIES------------------------------")

with open("ml-25m/movies.csv", "r", encoding="utf-8") as movies:
    reader = csv.reader(movies)
    next(reader, None)

    for x in reader:
        moviesDB.addMovie(int(x[0]), x[1], x[2])

print("------------------------------MOVIES FINISH------------------------------\n\n")


print("\n\n------------------------------RATINGS------------------------------")

with open("ml-25m/ratings.csv", "r", encoding="utf-8") as ratings:
    reader = csv.reader(ratings)
    next(ratings, None)

    for x in reader:
        usrNum = int(x[0])

        if users.get(usrNum) is None:
            users[usrNum] = User(usrNum)

        users[usrNum].addMovie(
            int(x[1]),
            float(x[2]),
            moviesDB.getGenres(moviesDB.getNameWithYear(int(x[1]))),
        )
        moviesDB.addRating(int(x[1]), float(x[2]))

# for x in users:
#     users[x].test()
#     users[x].getRatedGenres()
#     users[x].getFavouriteGenres()
#     print("\n")

users[1].test()
users[1].getRatedGenres()
users[1].getFavouriteGenres()
print("\n")

print("------------------------------RATINGS FINISH------------------------------\n\n")


# moviesDB.printing()


print(
    "\n\n------------------------------SIMILARITY SCORES------------------------------"
)

# simArr = []
# simDict = {}
# simArrLen = 0

# for x in users:
#     if users[1] != users[x]:
#         sim = users[1].computeMoviesSimilarity(users[x])
#         simDict[x] = sim

#         index = insertSimilarityArray(abs(1 - sim[0]), simArr, simDict, 0, simArrLen)
#         simArr.insert(index, x)
#         simArrLen = simArrLen + 1


# print(simArr)
# print(simDict)

print(
    "------------------------------SIMILARITY SCORES FINISH------------------------------\n\n"
)


print(
    "\n\n------------------------------SIMILAR TO A MOVIE------------------------------"
)
print(users[1].similarMovie(moviesDB, "Toy Story", 1995))

print(
    "------------------------------SIMILAR TO A MOVIE FINISH------------------------------\n\n"
)


print(
    "\n\n------------------------------SIMILAR TO FAV GENRES MOVIE------------------------------"
)
print(users[1].similarGenres(moviesDB))

print(
    "------------------------------SIMILAR TO FAV GENRES FINISH------------------------------\n\n"
)


# print(
#     "\n\n------------------------------SIMILAR TO A MOVIE------------------------------"
# )


# print(
#     "------------------------------SIMILAR TO A MOVIE FINISH------------------------------\n\n"
# )
