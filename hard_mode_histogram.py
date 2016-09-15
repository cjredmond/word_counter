with open("sample.txt") as better_open_file:
    better_contents = better_open_file.read().lower() #.replace(",", "")
excluded = "'1234567890,.?;:'[]{}!"
for x in excluded:
    if x in better_contents:
        better_contents = better_contents.replace(x,"")
ls = better_contents.split()
new = []
dict = {}
for word in ls:
    if word in dict.keys():
        dict[word] += 1
    else:
        dict[word] = 1

def make_hash(number):
    hashes = []
    for burn in range(0,number):
        hashes.append("#")
    return "".join(hashes)


new = sorted(dict.items(), key=lambda x: x[1] )
top_group = []
for number in range(19):
    top_group.append(new.pop())
scale = []
for word in top_group:
    scale.append((word[0], (word[1] / 69)))
for x in scale:
    print(x[0],"\t",make_hash(int(x[1])))
