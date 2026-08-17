import ceasarEncDec


def shiftList(keyWord):
    shifts=[]
    cipher=''
    for c in keyWord:
        if c in ceasarEncDec.lowerAlphabets:
            shifts.append(ceasarEncDec.lowerAlphabets.index(c))
        elif c in ceasarEncDec.upperAlphabets:
            shifts.append(ceasarEncDec.upperAlphabets.index(c))
    return shifts

def vigenereEnc(text,keyWord):
    shifts=shiftList(keyWord)
    cipher=''
    numberShifts=len(shifts)
    currentIndex=0
    for c in text:
        cipher=cipher+ceasarEncDec.shifter(c,shifts[currentIndex%numberShifts])
        currentIndex+=1
    return cipher

def vigenereDec(cipher,keyWord):
    shifts=shiftList(keyWord)
    numberShifts=len(shifts)
    text=''
    currentIndex=0
    for c in cipher:
        text=text+ceasarEncDec.ceasarDec(c,shifts[currentIndex%numberShifts])
        currentIndex+=1
    return text


    

    
