import re

pattern = re.compile(r"\((.*) (\d{2,4}/\d{2}/\d{2}).*\)")

for i, line in enumerate(open('changelog.in')):
    for match in re.finditer(pattern, line):
        date = match.groups()[1].replace("/","-")
        #print "line:", line, "no:", i, " date:", date
        names = []
        for name in match.groups()[0].split(","):
            name = name.replace(",","").strip()
            if len(name)>0:
                print date, name

