with open("sample.txt") as better_open_file:
    better_contents = better_open_file.read().lower()

ls = better_contents.split()



new = []
dict = {}


for word in ls:
    if word in dict.keys():
        dict[word] += 1
    else:
        dict[word] = 1

# print(dict)
# print(dict.items())
print(sorted(dict.items(), key=lambda x: x[1] ))
