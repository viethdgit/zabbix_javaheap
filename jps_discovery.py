#!/usr/bin/python
import os
import json
if __name__=="__main__":
	java_process=str(os.popen("sudo jps | grep -v 'Jps' | grep -v 'Jstat'").read()).rstrip().split('\n'):
	data = [{"{#PID}": pid} for pid in java_process]
	print(json.dumps({"data": data}, indent=4))
