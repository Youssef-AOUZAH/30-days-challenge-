from concurrent.futures import ThreadPoolExecutor
import os
import hashlib
import re

max_workers=os.cpu_count()
hashType=''
hash=''

def _equalHashes(hashed):
    global hash
    

    typeList=[chr(i) for i in range(ord('a'),ord('f')+1)]+[i for i in range(10)]
    if len(hashed)!=len(hash):
            return False
    for i in range(len(hash)):
        if hashed[i]!=hash[i]:
            return False
    return True

def compare(word):
    return eval(f'_equalHashes(hashlib.{hashType}(word.encode(\'utf-8\')).hexdigest())')


def path_to_list(path):
    wordList=[]
    with open(path,'r') as textFile:
        for line in textFile:
            wordList.append(line.strip())
    return wordList




def crack(path,_hash,_hashType):
    word=path_to_list(path)
    global hashType
    global hash
    hashType=_hashType
    hash=_hash
    with ThreadPoolExecutor(max_workers) as executor:
        
        output=list(executor.map(compare,word))
    try:
        return word[output.index(True)]
    except:
        return False


