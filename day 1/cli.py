
import argparse
import ceasarEncDec
import hexEncDec
import base64EncDec
import vigenereEncDec

def ceasar(args):
    if args.shift is None:
        print(ceasarEncDec.ceasarBruteForce(args.cipher))
    elif args.cipher is not None:
        print(ceasarEncDec.ceasarDec(args.cipher,args.shift))
    elif args.text is not None:
        print(ceasarEncDec.ceasarEnc(args.text,args.shift))


def base64(args):
    if args.cipher is not None:
        print(base64EncDec.base64Dec(args.cipher))
    elif args.text is not None:
        print(base64EncDec.base64Enc(args.text))
    

def hexf(args):
    if args.cipher is not None:
        print(hexEncDec.hexDec(args.cipher))
    elif args.text is not None:
        print(hexEncDec.hexEnc(args.text))

def vigenere(args):
    if (args.text is not None) and (args.key is not None):
        print(vigenereEncDec.vigenereEnc(args.text,args.key))
    elif (args.cipher is not None) and (args.key is not None):
        print(vigenereEncDec.vigenereDec(args.cipher,args.key))



def main():
    print("ceasar | hex | base64 | vigenere")
    parser=argparse.ArgumentParser()
    parser.add_argument("--mode",required=True,type=str,choices=['ceasar','base64','hex','vigenere'],help='The mode of enc/dec')
    parser.add_argument("--cipher",type=str,help="The cipher to decrypt or decode")
    parser.add_argument("--text",type=str,help="The text to encrypt or encode")
    parser.add_argument("--shift",type=int,help="The shift for ceasar")
    parser.add_argument("--key",type=str,help="the key for vigenere")
    args=parser.parse_args()

    if args.mode is not None:
        if args.mode=='ceasar':
            ceasar(args)

        elif args.mode=='base64':
            base64(args)
        
        elif args.mode=='hex':
            hexf(args)

        elif args.mode=='vigenere':
            vigenere(args)


            
if __name__=="__main__":
    main()
            