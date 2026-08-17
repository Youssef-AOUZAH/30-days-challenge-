
def numBin8(n): # converting a number n into an 8 bits binary string,returning a list of two elements (first half and second half of the string)
    bin=format(n,'b')
    length=len(bin)
    if length<8:
        bin='0'*(8-length)+bin
    
    return [bin[:4],bin[4:]] 

def binToHex(stringHalfBinary): #takes the half binary string and turns the hex string
    
    sum=0
    for i in range(4):
        sum+=int(stringHalfBinary[i])*(2**(3-i))
    return format(sum,'X')



def hexEnc(text):
    s=""
    for c in text:
        ascii_c=ord(c)
        
        binary_halves_list=numBin8(ascii_c)
        first_half_hex=binToHex(binary_halves_list[0])
        second_half_hex=binToHex(binary_halves_list[1])

        s+=first_half_hex+second_half_hex
    return s.lower()

def hex_bin(hexElement):#this fctn takes as input the hexElement and convertes it to a 4 bits binary string
    return format(int(hexElement,16),'04b')


def hexDec(textHex):
    if textHex[1].lower()=='x':
        textHex=textHex[2:]
    outputString=''
    for i in range(0,len(textHex)-1,2):
        ascii_num=int(hex_bin(textHex[i])+hex_bin(textHex[i+1]),2)
        outputString+=chr(ascii_num)
    return outputString




        
