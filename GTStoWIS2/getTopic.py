import json
from sys import argv

########### functions   ########
################################
# filename
#A_ISID01LZIB190300_C_EDZW_20200619030401_18422777
def getCCCCfromFilename(filename):
    cccc = filename[8:12]
    return cccc

def getTTAAiiFromFilename(filename):
    TTAAii = filename[2:8]
    return TTAAii


# get CCCC subtopic
def getSubtopic_CCCC(c):
    global CCCC
    if c in CCCC.keys():
        #print(CCCC[c])
        country = CCCC[c]["country_short"]
        centre = CCCC[c]["centre"]
        subtopic = country + separator + centre
        return subtopic
    else:
        print(c + " not found.")
        
        
def getSubtopicTableT2(myT1, myT2, myA1, myii, mytableT2):
    subTopicT2 = ""
    if "B" in mytableT2:
        #print("tableT2 = B")
        keyList = B[myT1].keys()
        #print(keyList)
        if myT2 in keyList:
            subTopicT2 = B[myT1][myT2]
    else:
        if "C7" in mytableT2:
            #print("tableT2 = C7")
            TTA = myT1 + myT2 + myA1
            if TTA in C7.keys():
                if "ii" in C7[TTA]:
                    iiKey = ""
                    iiKeyList = C7[TTA]["ii"].keys()
                    for key in iiKeyList:
                        if int(myii) < int(key):
                            if iiKey == "":
                                iiKey = key
                            else:
                                if int(iiKey) > int(key):
                                    iiKey = key
                    if iiKey != "":
                        subTopicT2 = C7[TTA]["ii"][iiKeys[count-1]]
                else:
                    subTopicT2 = C7[TTA]
    return subTopicT2

def getSubtopicTableA1(myT1, myT2, myA1, myA2, myii, mytableA1):
    subTopicA1 = ""
    if mytableA1 == "C1":
        #print("tableA1 = C1")
        AA = myA1 + myA2 
        if AA in C1.keys():
            subTopicA1 = C1[AA]["topic"]
    else:
        if mytableA1 == "C3":
            #print("tableA1 = C3")
            subTopicA1 = C3[myA1]
        else:
            if mytableA1 == "C6":
                #print("tableA1 = C6")
                iiKey = ""
                TT = myT1 + myT2
                if TT in C6.keys():
                    if A1 in C6[TT].keys():
                        if "ii" in C6[TT][A1]:
                            iiKeyList = C6[TT][A1]["ii"].keys()
                            for key in iiKeyList:
                                if int(myii) < int(key):
                                    if iiKey == "":
                                        iiKey = key
                                    else:
                                        if int(iiKey) > int(key):
                                            iiKey = key
                            if iiKey != "":
                                subTopicA1 = C6[TT][myA1]["ii"][iiKey]
                        else:
                            subTopicA1 = C6[TT][myA1]
    return subTopicA1

def getSubtopicTableA2(myA2, mytableA2):
    subTopicA2 = ""
    if mytableA2 == "C4":
        #print("tableA2 = C4")
        subTopicA2 = C4[myA2]
    else:
        if mytableA2 == "C3":
            #print("tableA2 = C3")
            subTopicA2 = C3[myA2]
        else:
            if mytableA2 == "C5":
                #print("tableA2 = C5")
                if myA2 in C5.keys():
                    subTopicA2 = C5[myA2]
    return subTopicA2

########### read files   #######
################################
#read file CCCC
cf=open("TableCCCC.json","r")
CCCC=json.load(cf)
cf.close()

# read WMO Tables
fromTableA = open("TableA.json","r")
A = json.load(fromTableA)
fromTableA.close()

fromTableB = open("TableB.json","r")
B = json.load(fromTableB)
fromTableB.close()

fromTableC1 = open("TableC1.json","r")
C1 = json.load(fromTableC1)
fromTableC1.close()

fromTableC2 = open("TableC2.json","r")
C2 = json.load(fromTableC2)
fromTableC2.close()

fromTableC3 = open("TableC3.json","r")
C3 = json.load(fromTableC3)
fromTableC3.close()

fromTableC4 = open("TableC4.json","r")
C4 = json.load(fromTableC4)
fromTableC4.close()

fromTableC5 = open("TableC5.json","r")
C5 = json.load(fromTableC5)
fromTableC5.close()

fromTableC6 = open("TableC6.json","r")
C6 = json.load(fromTableC6)
fromTableC6.close()

fromTableC7 = open("TableC7.json","r")
C7 = json.load(fromTableC7)
fromTableC7.close()


#### programm ####
##################
inputTTAAii = ""
input_c = ""
deparator = "/"

# read TTAAii and CCCC from args
try:
    inputTTAAii = getTTAAiiFromFilename(str(argv[1]))
    input_c = getCCCCfromFilename(str(argv[1]))
except IndexError:
    print('missing argument')
except ValueError:
    print('argument must be a string for a filename like A_ISID01LZIB190300_C_EDZW_*')

# test default filename
if inputTTAAii == "":
    inputTTAAii = getTTAAiiFromFilename("A_ISID01LZIB190300_C_EDZW_20200619030401_18422777")  

if input_c == "":
    input_c = getCCCCfromFilename("A_ISID01LZIB190300_C_EDZW_20200619030401_18422777")

T1 = inputTTAAii[0:1]
T2 = inputTTAAii[1:2]
A1 = inputTTAAii[2:3]
A2 = inputTTAAii[3:4]
ii = inputTTAAii[4:6]

tableT2 = A[T1]["T2"]
tableA1 = A[T1]["A1"]
tableA2 = A[T1]["A2"]
topic = A[T1]["topic"]

separator = "/"

subtopic_cccc = getSubtopic_CCCC(input_c)
subtopicT2 = ""
subtopicA1 = ""
subtopicA2 = ""

fulltopic = subtopic_cccc + separator + topic

subtopicT2 = getSubtopicTableT2(T1, T2, A1, ii, tableT2)
if subtopicT2 != "":
    fulltopic = fulltopic + separator + subtopicT2
else:
    print("subtopicT2 is empty")

subtopicA1 = getSubtopicTableA1(T1, T2, A1, A2, ii, tableA1)
if subtopicA1 != "":
    fulltopic = fulltopic + separator + subtopicA1
else:
    print("subtopicA1 is empty")

subtopicA2 = getSubtopicTableA2(A2, tableA2)
if subtopicA2 != "":
    fulltopic = fulltopic + separator + subtopicA2
else:
    print("subtopicA2 is empty")
    
print(fulltopic)

