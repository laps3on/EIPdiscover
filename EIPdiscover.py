#!/usr/bin/python

import sys
from codecs import encode, decode
import os
import re

try:
	argone, argtwo, argthree, argfour = sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4]
	string = str(argone + argtwo + argthree + argfour)
	code = decode(string, "hex")
	decoded = decode(code, "utf-8")
	padrao = ""
	stronger = str(padrao.index(decoded))
	resp = (re.sub(r"[\[]", "(", stronger))
	print(resp + " BYTES TO BOF!")
except:
	print("Fuck the system!")
	print("Mode of use: 'python EIPdiscover.py 34 45 66 17'")
	print("Developed by Leonardo S")