#--------------------------
# HTML to MD
# Author: rey.olivier@gmail.com
# License: GPL v3
#--------------------------
import re

from html.parser import HTMLParser

DO_NOTHING_BEGIN = ["HTML", "HEAD", "META", "STYLE", "BODY", "FONT", "P",
                    "COL", "TR", "TD", "A"]

DO_NOTHING_END = ["HTML", "HEAD", "META", "STYLE", "BODY", "FONT",
                    "COL", "TR", "TD", "BR", "A"]

REMOVE_CONTENT = ["STYLE", "COL", "TR", "TD"]


BLANK_LINE = ["TITLE", "H1", "H2", "H3", "H4", "H5", "P"]


class MyHTMLParser(HTMLParser):
    out = None
    currenttag = ""
    tablenb = 0
    intable = False
    verbose = False
    imagelog = open("imagelog.txt", "w")

    def setOutputFile(self, out, verbose=False):
        self.out = out
        self.verbose = verbose
        
    
    def handle_starttag(self, tag, attrs):
        if (self.verbose):
            print("Encountered a start tag:", tag)
        thetag = tag.upper()
        self.currenttag = thetag
        self.currentattrs = attrs
        if (thetag in DO_NOTHING_BEGIN):
            if (self.verbose):
                print("Doing nothing")
            return
        if (thetag == "TITLE"):
            self.out.write("# ")
            return
        if (thetag == "H1"):
            self.out.write("## ")
            return
        if (thetag == "H2"):
            self.out.write("### ")
            return
        if (thetag == "H3"):
            self.out.write("#### ")
            return
        if (thetag == "H4"):
            self.out.write("##### ")
            return
        if (thetag == "H5"):
            self.out.write("###### ")
            return
        if (self.currenttag == "A"):
            print("tag a")
            print("href = " + self.currentattrs["href"])
            self.out.write("[" + removeBlanks(data) + "](" + self.currentattrs["href"] + "]")
            return
        if (thetag == "BR"):
            if (self.intable):
                return
            else:
                self.out.write("\n\n")
                return
        if (thetag == "B"):
            if (self.intable):
                return
            else:
                self.out.write("**")
                return
        if (thetag == "TABLE"):
            # protecting table from other tags
            self.out.write("\n\n")
            self.tablenb += 1
            self.intable = True
            return
        if (self.verbose):
            print("No treatment for tag: " + tag)
        

    def handle_endtag(self, tag):
        if (self.verbose):
            print("Encountered an end tag :", tag)
        thetag = tag.upper()
        if (thetag in DO_NOTHING_END):
            if (self.verbose):
                print("Doing nothing")
            return
        if (thetag in BLANK_LINE):
            self.out.write("\n\n")
            return
        if (thetag == "B"):
            if (self.intable):
                return
            else:
                self.out.write("**")
                return
        if (thetag == "P"):
            if (self.ntable):
                return
            else:
                self.out.write("\n\n")
                return
        if (thetag ==  "TABLE"):
            imagename = self.out.name.split('.')[0] \
                + '-Table' + str(self.tablenb).zfill(2) + ".png"
            self.out.write("![" + imagename + "](" + imagename + ")\n\n")
            self.intable = False
            self.imagelog.write(imagename + "\n")
            return
        if (self.verbose):
            print("No treatment for tag: " + tag)

        
    def handle_data(self, data):
        #print("Encountered some data  :", data)
        if (self.intable):
            return
        if (not (self.currenttag in REMOVE_CONTENT)):
            self.out.write(removeBlanks(data))


'''
class Table:
    # row numbers start at 0
    rows = [][]
    def addCell(self, rownumber, value):
        self.rows[rownumber].append(value)
    def serialize(self):
        output = ""
        # first row determines the number of columns
        nbcol = len(rows[0])
        nbrows = len(rows)
        print(" The table has " + str(nbcol + " columns and " + str(nbroxs) + " rows.")
        # writing header
        for (value in rows[0]):
            output += "| " + value + " "
        output += " |\n"
        # writing separator
        for (i in range(0, nbcol)):
            output += "| --- "
        output += " |\n"
        # some lines may not have the right amount of columns
        for (i in range(1,nbrows)):
            therow = row[i]
            if (len(therow) < nbcol):
              print("Error")
            print(therow)
            break;
'''
        

#--------------------------------
# Utilities
#--------------------------------
        
def removeBlanks(s):
    # removing Windows CR/LF
    ns = s.replace("\r\n", " ")
    # removing Unix LF
    ns = ns.replace("\n", " ")
    # stripping white spaces left and right
    ns = ns.strip()
    return re.sub(' +', ' ', ns)


#--------------------------------
# A little brutal - did not have time to package it in a shell
#--------------------------------

FILES = [
    "00 Legal.html",
    "01 Basics.html",
    "02 Description.html",
    "03 Races.html",
    "04 ClassesI.html",
    "05 ClassesII.html",
    "06 SkillsI.html",
    "07 SkillsII.html",
    "08 Feats.html",
    "09 Equipment.html",
    "10 SpecialMaterials.html",
    "11 CombatI.html",
    "12 CombatII.html",
    "13 AbilitiesandConditions.html",
    "14 NPCClasses.html",
    "15 PrestigeClasses.html",
    "16 MagicOverview.html",
    "17 SpellListI.html",
    "18 SpellListII.html",
    "19 SpellsA-B.html",
    "20 SpellsC.html",
    "21 SpellsD-E.html",
    "22 SpellsF-G.html",
    "23 SpellsH-L.html",
    "24 SpellsM-O.html",
    "25 SpellsP-R.html",
    "26 SpellsS.html",
    "27 SpellsT-Z.html",
    "28 MagicItemsI.html",
    "29 MagicItemsII.html",
    "30 MagicItemsIII.html",
    "31 MagicItemsIV.html",
    "32 MagicItemsV.html",
    "33 MagicItemsVI.html",
    "34 MonstersIntro-A.html",
    "35 MonstersB-C.html",
    "36 MonstersD-De.html",
    "37 MonstersDi-Do.html",
    "38 MonstersDr-Dw.html",
    "39 MonstersE-F.html",
    "40 MonstersG.html",
    "41 MonstersH-I.html",
    "42 MonstersK-L.html",
    "43 MonstersM-N.html",
    "44 MonstersO-R.html",
    "45 MonstersS.html",
    "46 MonstersT-Z.html",
    "47 MonstersAnimals.html",
    "48 MonstersVermin.html",
    "49 TypesSubtypesAbilities.html",
    "50 Improving Monsters.html",
    "51 MonsterFeats.html",
    "52 MonstersasRaces.html",
    "53 CarryingandExploration.html",
    "54 Treasure.html",
    "55 WildernessandEnvironment.html",
    "56 Traps.html",
    "57 Planes.html",
    "58 PsionicRaces.html",
    "59 PsionicClasses.html",
    "60 PsionicSkills.html",
    "61 PsionicsFeats.html",
    "62 PowersOverview.html",
    "63 PowerList.html",
    "64 PsionicPowersA-C.html",
    "65 PsionicPowersD-F.html",
    "66 PsionicPowersG-P.html",
    "67 PsionicPowersQ-W.html",
    "68 PsionicMonsters.html",
    "69 PsionicItems.html",
    "70 PsionicSpells.html",
    "71 EpicLevelBasics.html",
    "72 EpicClasses.html",
    "73 EpicPrestigeClasses.html",
    "74 EpicSkills.html",
    "75 EpicFeats.html",
    "76 EpicSpells.html",
    "77 EpicMagicItems1.html",
    "78 EpicMagicItems2.html",
    "79 EpicMonsters(A-E).html",
    "80 EpicMonsters(G-W).html",
    "81 EpicObstacles.html",
    "82 DivineRanksandPowers.html",
    "83 DivineAbilitiesandFeats.html",
    "84 DivineDomainsandSpells.html",
    "85 DivineMinions.html"
]


if __name__ ==  "__main__":
    for infile in FILES:
        print("Converting: " + infile)
        outfile = "./converted/" + infile.split('.')[0] + ".md"
        inf  = open(infile,  "r")
        outf = open(outfile, "w")
        parser = MyHTMLParser()
        parser.setOutputFile(outf)
        parser.feed(inf.read())
        inf.close()
        outf.close()
    print("Done")

