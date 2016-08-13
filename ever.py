import fileinput

names = {}

lines = []
for line in fileinput.input():
    lines.append(line)

for line in lines:
    date,name = line.replace("\n","").split(" ",1)
    if len(name)>0:
        names[name] = 1 + (names[name] if name in names else 0)

if False:
    for line in lines:
        date,name = line.replace("\n","").split(" ",1)
        print date, name



# names, we might need to map authors!
if False:
    for n in names:
        print n

ever={}
bymonth = {}

for line in lines:
    date,name = line.replace("\n","").split(" ",1)
    yearmonth = date[0:7]
    if len(name)>1 and name not in ever:
        if not yearmonth in bymonth:
            bymonth[yearmonth]=set()
        ever[name]=1
        bymonth[yearmonth].add(name)


for s in bymonth:
    print s, len(bymonth[s])

