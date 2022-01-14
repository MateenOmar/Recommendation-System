import csv

t = {1: [4, 3], 3: [2, 8], 2: [10, 11], 10: [5, 5]}
x = ["a", "b", "c", "d", "e", "f", "g", "h"]
y = ["b", "d", "f", "h"]
print(t)

print(sorted(t.items(), key=lambda x: x[1][1], reverse=True))
# print(sorted(t.items(), key=lambda x: x[1], reverse=True)[0][1])

print(len([1, 2, 3, 4]))

print(x[0 : -(len(x) // -2)])
print(len(x[0 : -(len(x) // -2)]))

with open("ml-25m/moviesEx.csv", "r", encoding="utf-8") as file:
    reader = csv.reader(file)
    for row in reader:
        print(row)
