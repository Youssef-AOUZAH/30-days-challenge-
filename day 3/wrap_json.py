import json
def wrap_json(output,path):
    with open(path,'w') as f:
        json.dump(output,f,indent=3)