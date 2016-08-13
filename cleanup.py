import fileinput


authormapping = {"adamkosik":"adam kosik", 
"third-party":"", 
"msteigemann":"martin steigemann",
"oneliefleft":"toby d. young",
"tcclevenger":"conrad clevenger",
"agrayver":"alexander grayver",
"amola":"andrea mola",
"baerbel jannsen":"baerbel janssen",
"dakshinai":"dakshina ilangovan",
"dakshina.ilangova":"dakshina ilangovan",
"deal":"",
"nicolacavallini":"nicola cavallini",
"no-author":"",
"oneliefleft":"toby d. young",
"praveen c":"praveen chandrashekar",
"cvs":"",
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
    if "2015" in name:
        return ""
    return name



for line in fileinput.input():
    date,name = line.replace("\n","").split(" ",1)
    yearmonth = date[0:7]
    name = make_name(name)
    #print yearmonth, name
    if len(name)>1:
        print date,name
