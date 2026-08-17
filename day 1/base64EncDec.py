import string
import base64

base64List=string.ascii_uppercase+string.ascii_lowercase+string.digits+"+/"
def numBin8(n): # converting a number n into an 8 bits binary string
    bin=format(n,'b')
    length=len(bin)
    if length<8:
        bin='0'*(8-length)+bin
    return bin

def sequencesOf6(binSequence):
   
    m=len(binSequence)//6
    diff=len(binSequence)-m*6
    listSequences=[binSequence[6*i:6*(i+1)] for i in range(m)]
    if len(binSequence)>6*m:
       
        
        listSequences.append(binSequence[6*m:]+"0"*(6-diff))
       
    return diff,listSequences
    


def base64Enc(text):
    outputText=''
    binSequence=''
    
    for c in text:
        bin_num=numBin8(ord(c))
        binSequence+=bin_num
    diff,sequencesList=sequencesOf6(binSequence)
   
    
    for c in sequencesList:
        
        outputText+=base64List[int(c,2)]
    return outputText+"="*((3-(len(text)%3))%3)

def base64Dec(text):
   
    if text=='' or text=='=' or text=='==':
        return ''
    n=0
    numberEqu=0
    if text[-1]=='=' and text[-2]=='=':
        n=1
        numberEqu=2
    elif text[-1]=='=':
        n=2
        numberEqu=1
    else:
        n=0
        numberEqu=0
    length=len(text)
    text=text[:length-numberEqu]
    length=length-2
   
    binSequence=''
    for c in text:
        order_bin=format(base64List.index(c),'06b')
       
        binSequence+=order_bin
 
    lengthSequence=len(binSequence)
    if numberEqu==2:
        binSequence=binSequence[:lengthSequence-2]
    elif numberEqu==1:
        binSequence=binSequence[:lengthSequence-1]
    lengthSequence=len(binSequence)
    listBytes=[binSequence[8*i:8*(i+1)] for i in range(lengthSequence//8)]
   
    listInt=[chr(int(listBytes[i],2)) for i in range(len(listBytes))]
    
    return ''.join(listInt)












    
   

