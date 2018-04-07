import re

pattern = re.compile(r"\((.*) (\d{2,4}/\d{2}/\d{2}).*\)")

def print_names(date, names):
    #print "*", names
    
    xx = names.replace(" and ", ",").replace("& "," and ").replace(" 20",",20").split(",")
    for x in xx:
        name = x.strip()
        if len(name)>0 and "20" not in name:
            print date, name.lower()



for i, line in enumerate(open('changelog.in')):
    for match in re.finditer(pattern, line):
        date = match.groups()[1].replace("/","-")
        #print "line:", line, "no:", i, " date:", date
        names = []
        print_names(date, match.groups()[0])

