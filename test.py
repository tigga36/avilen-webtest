"""
このファイルに解答コードを書いてください
"""

import sys 
sys.stdin = open('input.txt', 'r')  
sys.stdout = open('output.txt', 'w') 

hash_dict = {}
no_match = True

while(True):
	reading = input()
	if(":" not in reading):
		n = int(reading)
		break
	num, letter = reading.split(":")
	num = int(num)
	hash_dict[num] = letter

num_str = ""
for key in sorted(hash_dict.keys()):
	if(n%key==0):
		no_match = False
		num_str += hash_dict[key]
		hash_dict[key] = ""

if(no_match):
	print(n)
else:
	print(num_str)