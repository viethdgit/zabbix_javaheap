#!/usr/bin/python
import os
import json
if __name__=="__main__":
        process_id=[]
        process_id=str(os.popen("sudo jps | awk '{if (($2 != \"Jps\")&&($2 != \"stat\")) print $1}'").read()).rstrip().split('\n')
        data = [{"{#PID}": pid} for pid in process_id]
        print(json.dumps({"data": data}, indent=4))
