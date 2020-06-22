import json
from sys import argv

inputTTAAii = ""
# read TTAAii from args
try:
    if len(str(argv[1])) == 6:
        inputTTAAii = str(argv[1])
    else:
        inputTTAAii = getTTAAiiFromFilename(str(argv[1]))
except IndexError:
    print('missing argument')
except ValueError:
    print('argument must be a string for the TTAAii or a filename like A_ISID01LZIB190300_C_EDZW_*')

# filename
#A_ISID01LZIB190300_C_EDZW_20200619030401_18422777
def getTTAAiiFromFilename(filename):
    TTAAii = filename[2:8]
    return TTAAii

if inputTTAAii == "":
    inputTTAAii = getTTAAiiFromFilename("A_ISID01LZIB190300_C_EDZW_20200619030401_18422777")
    print(inputTTAAii)

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


# programm
T1 = inputTTAAii[0:1]
#print("T1: " + T1)
T2 = inputTTAAii[1:2]
#print("T2: " + T2)
A1 = inputTTAAii[2:3]
#print("A1: " + A1)
A2 = inputTTAAii[3:4]
#print("A2: " + A2)
ii = inputTTAAii[4:6]
#print("ii: " + ii)

tableT2 = A[T1]["T2"]
#print("TableT2: " + tableT2)

tableA1 = A[T1]["A1"]
#print("TableA1: " + tableA1)

tableA2 = A[T1]["A2"]
#print("TableA2: " + tableA2)

topic = A[T1]["topic"]
#print("topic: " + topic)


def getSubtopicTableT2(T1, T2, A1, ii, tableT2):
    subTopicT2 = ""
    if "B" in tableT2:
        print("tableT2 = B")
        keyList = B[T1].keys()
        #print(keyList)
        if T2 in keyList:
            subTopicT2 = B[T1][T2]
    else:
        if "C7" in tableT2:
            print("tableT2 = C7")
            TTA = T1 + T2 + A1
            if TTA in C7.keys():
                if "ii" in C7[TTA]:
                    iiKey = ""
                    iiKeyList = C7[TTA]["ii"].keys()
                    for key in iiKeyList:
                        if int(ii) < int(key):
                            if iiKey == "":
                                iiKey = key
                            else:
                                if int(iiKey) > int(key):
                                    iiKey = key
                    if iiKey != "":
                        subtopicT2 = C7[TTA]["ii"][iiKeys[count-1]]
                        print(subtopicT2)
                else:
                    subtopicT2 = C7[TTA]
    return subTopicT2

def getSubtopicTableA1(T1, T2, A1, A2, ii, tableA1):
    subTopicA1 = ""
    if tableA1 == "C1":
        print("tableA1 = C1")
        AA = A1 + A2 
        if AA in C1.keys():
            subTopicA1 = C1[AA]["topic"]
    else:
        if tableA1 == "C3":
            print("tableA1 = C3")
            subTopicA1 = C3[A1]
        else:
            if tableA1 == "C6":
                print("tableA1 = C6")
                iiKey = ""
                TT = T1 + T2
                if TT in C6.keys():
                    if A1 in C6[TT].keys():
                        if "ii" in C6[TT][A1]:
                            iiKeyList = C6[TT][A1]["ii"].keys()
                            for key in iiKeyList:
                                if int(ii) < int(key):
                                    if iiKey == "":
                                        iiKey = key
                                    else:
                                        if int(iiKey) > int(key):
                                            iiKey = key
                            if iiKey != "":
                                subTopicA1 = C6[TT][A1]["ii"][iiKey]
                        else:
                            subTopicA1 = C6[TT][A1]
        return subTopicA1

def getSubtopicTableA2(T1, T2, A1, A2, ii, tableA2):
    subTopicA2 = ""
    if tableA2 == "C4":
        print("tableA2 = C4")
        subTopicA2 = C4[A2]
    else:
        if tableA2 == "C3":
            print("tableA2 = C3")
            subTopicA2 = C3[A2]
        else:
            if tableA2 == "C5":
                print("tableA2 = C5")
                if A2 in C5.keys():
                    subTopicA2 = C5[A2]
        return subTopicA2

#### programm ####
##################
subtopicT2 = ""
subtopicA1 = ""
subtopicA2 = ""

fulltopic = topic

subtopicT2 = getSubtopicTableT2(T1, T2, A1, ii, tableT2)
if subtopicT2 != "":
    fulltopic = fulltopic + "/" + subtopicT2
else:
    print("subtopicT2 is empty")

subtopicA1 = getSubtopicTableA1(T1, T2, A1, A2, ii, tableA1)
if subtopicA1 != "":
    fulltopic = fulltopic + "/" + subtopicA1
else:
    print("subtopicA1 is empty")

subtopicA2 = getSubtopicTableA2(T1, T2, A1, A2, ii, tableA2)
if subtopicA2 != "":
    fulltopic = fulltopic + "/" + subtopicA2
else:
    print("subtopicA2 is empty")
    
print(fulltopic)
