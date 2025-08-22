import fileinput
import sys
import os

n = 1
 
for line in fileinput.input('./README.md', inplace = True):
    if '커밋' in line:
        null_text = " " * n
        line = line.replace(line, f'자동으로 하루에 한번 커밋{null_text}')
        
    sys.stdout.write(line)
    
os.system("clear")