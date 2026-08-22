#when i come back i need to import stuff and do the usual for the cli
import hash_discover
import argparse
import cracker

def which_hash(args):
    print("Finding hash type...")
    hash_type=hash_discover.which_hash(args.hash)
    print(f"Hash type: {hash_type}")
    return hash_type

def main():
    print("Hash Cracker v1.2")
    
    parser=argparse.ArgumentParser()
    parser.add_argument("hash",help="The hash")
    parser.add_argument("--type",nargs=1,choices=['md5','sha1','sha256','sha512'],help="Type of hash if known,not required tho")
    parser.add_argument("--path",required=True,nargs=1,type=str,help="Path for the dict list")
    args=parser.parse_args()
    
    
    if args.hash is not None:
        if args.type is None:
            hashType=which_hash(args)
            print("Cracking...")
            output=cracker.crack(args.path[0],args.hash,hashType)
        elif args.type is not None:
            print("Cracking...")
            output=cracker.crack(args.path[0],args.hash,args.type[0])
        if output is not False:
            print(f"A word producing this hash is: {output}")
        else:
            print('no such a word corresponds to this hash in the currently used list')

            
            

if __name__=='__main__':
    main()