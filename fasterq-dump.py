import os

print('Enter 1st file name including SRR')
print('ex)SRR413000')
a=input('Enter : ')
print('Enter last file name')
b=input('Enter : ')

c=a[3:]
d=b[3:]

first_file=int(c)
last_file=int(d)

for i in range (first_file,last_file+1):
    os.system('.\\fasterq-dump.exe --split-files --gzip SRR{}.sra'.format(i))
    print('fasterq-dump done for file SRR{}'.format(i)
