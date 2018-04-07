import fileinput


authormapping = {"adamkosik":"adam kosik", 
"third-party":"", 
"msteigemann":"martin steigemann",
                 "alex":"alex kokomov",
                 "anne-glerum":"anne glerum",
                 "asartori86":"alberto sartori",
                 "barker29":"Andrew Barker",
                 "benjamin":"benjamin brands",
                 "darndt":"daniel arndt",
                 "elddle":"eldar khattatov",
                 "fsonner":"florian sonner",
                 "givalz":"giovanni alzetta",
                 "ikligge":"ingo kligge",
                 "jaeryunyim":"jaeryun yim",
                 "jason p. sheldon":"jason sheldon",
                 "jwitte":"julius witte",
                 "loylick":"alex kokomov",
                 "mfraters":"menno fraters",
                 "mike h":"mike harmon",
                 "mike":"mike harmon",
                 "nivesh":"nivesh dommaraju",
                 "o-sutton":"oliver sutton",
                 "rajat":"rajat arora",
                 "rombur":"bruno turcksin",
                 "sairajat":"rajat arora",
                 "simfeld":"samuel imfeld",
                 "vishalkenchan":"vishal boddu",
"oneliefleft":"toby d. young",
"tcclevenger":"conrad clevenger",
"agrayver":"alexander grayver",
"amola":"andrea mola",
"abner j. salgado":"abner salgado",
"baerbel jannsen":"baerbel janssen",
"dakshinai":"dakshina ilangovan",
"dakshina.ilangova":"dakshina ilangovan",
"deal":"",
"nicolacavallini":"nicola cavallini",
"no-author":"",
"oneliefleft":"toby d. young",
"praveen c":"praveen chandrashekar",
"cvs":"",
"yy":"",
"wb":"wolfgang bangerth",
"rh":"Ralf Hartmann",
"gk":"Guido Kanschat",
"<a href=\"mailto:or@winfos.com\">oliver rheinbach</a>":"Oliver Rheinbach"
}

def make_name(name):
    name = str.lower(name.strip()).replace("ä","ae").replace("ö","oe")
    nameparts = name.split(" ")
    if "@" in nameparts[-1]:
        name = " ".join(nameparts[0:-1])
    name = authormapping[name] if name in authormapping else name
    if "20" in name:
        return ""
    return name



for line in fileinput.input():
    date,name = line.replace("\n","").split(" ",1)
    yearmonth = date[0:7]
    cleanname = make_name(name)
    
    if len(cleanname)<2:
        continue
    
    #print "{} ({})".format(cleanname,name)   # for testing
    print date,cleanname
