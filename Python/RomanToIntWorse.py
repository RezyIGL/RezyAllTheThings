class Solution:
    def romanToInt(self, string: str) -> int:
        myDict = {
        "I": 1,
        "V": 5,
        "X": 10,
        "L": 50,
        "C": 100,
        "D": 500,
        "M": 1000
        }

        answerInt = 0
        twoDigits = False

        for i in range(len(string)):
            if not twoDigits:
                if string[i] == "I":
                    try:
                        if string[i+1] == "V":
                            answerInt += myDict["V"] - myDict["I"]
                            twoDigits = True
                        elif string[i+1] == "X":
                            answerInt += myDict["X"] - myDict["I"]
                            twoDigits = True
                        else:
                            answerInt += myDict["I"]
                    except:
                        answerInt += myDict["I"]
                    
                elif string[i] == "V":
                    answerInt += myDict["V"]

                elif string[i] == "X":
                    try:
                        if string[i+1] == "L":
                            answerInt += myDict["L"] - myDict["X"]
                            twoDigits = True
                        elif string[i+1] == "C":
                            answerInt += myDict["C"] - myDict["X"]
                            twoDigits = True
                        else:
                            answerInt += myDict["X"]
                    except:
                        answerInt += myDict["X"]

                elif string[i] == "L":
                    answerInt += myDict["L"]

                elif string[i] == "C":
                    try:
                        if string[i+1] == "D":
                            answerInt += myDict["D"] - myDict["C"]
                            twoDigits = True
                        elif string[i+1] == "M":
                            answerInt += myDict["M"] - myDict["C"]
                            twoDigits = True
                        else:
                            answerInt += myDict["C"]
                    except:
                        answerInt += myDict["C"]

                elif string[i] == "D":
                    answerInt += myDict["D"]

                elif string[i] == "M":
                    answerInt += myDict["M"]

            else:
                twoDigits = False

        return answerInt