with open("sample.txt") as better_open_file:
    better_contents = better_open_file.read().lower() #.replace(",", "")
excluded = "'1234567890,.?;:'[]{}!"
excluded_words = ("""a,able,about,across,after,all,almost,also,am,among,an,and,any,are,as,at,be,
because,been,but,by,can,cannot,could,dear,did,do,does,either,else,ever,every,
for,from,get,got,had,has,have,he,her,hers,him,his,how,however,i,if,in,into,is,
it,its,just,least,let,like,likely,may,me,might,most,must,my,neither,no,nor,
not,of,off,often,on,only,or,other,our,own,rather,said,say,says,she,should,
since,so,some,than,that,the,their,them,then,there,these,they,this,tis,to,too,
twas,us,wants,was,we,were,what,when,where,which,while,who,whom,why,will,with,
would,yet,you,your"""
)
for x in excluded:
    if x in better_contents:
        better_contents = better_contents.replace(x,"")
hard_list = []


ls = better_contents.split()

for x in ls:
    if x in excluded_words:
        pass
    else:
        hard_list.append(x)


new = []
dict = {}


for word in hard_list:
    if word in dict.keys():
        dict[word] += 1
    else:
        dict[word] = 1

new = sorted(dict.items(), key=lambda x: x[1] )

top_group = []


for number in range(19):
    top_group.append(new.pop())

for burn in top_group:
    print(*burn)
