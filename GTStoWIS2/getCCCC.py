import json
from sys import argv

separator = "/"

def search_CCCC (c):
    global CCCC
    if c in CCCC.keys():
        #print(CCCC[c])
        country = CCCC[c]["country_short"]
        centre = CCCC[c]["centre"]
        subtopic = country + separator + centre
        return subtopic
    else:
        print(c + " not found.")

# filename
#A_ISID01LZIB190300_C_EDZW_20200619030401_18422777
def getCCCCfromFilename(filename):
    cccc = filename[8:12]
    return cccc


input_c = ""
# read CCCC from args
try:
    if len(str(argv[1])) == 4:
        input_c = str(argv[1])
    else:
        input_c = getCCCCfromFilename(str(argv[1]))
except IndexError:
    print('missing argument')
except ValueError:
    print('argument must be a string CCCC or a filename like A_ISID01LZIB190300_C_EDZW_*')

if input_c == "":
    input_c = getCCCCfromFilename("A_ISID01LZIB190300_C_EDZW_20200619030401_18422777")

#read file in CCCC
cf=open("TableCCCC.json","r")
CCCC=json.load(cf)
cf.close()

# programm
#input_c = input("Please insert CCCC to search for: ")
#c_corr = str(input_c[0:4].upper())
    
if input_c != "":
    #print( input_c )
    c_corr = str(input_c[0:4].upper())
    subtopic_cccc = search_CCCC(c_corr)
    print(subtopic_cccc)
