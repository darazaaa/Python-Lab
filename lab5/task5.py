fin = open('mailbox.txt', 'r')
lines = fin.readlines()
fout = open('output5.txt', 'w')

for line in lines:
    if 'X-DSPAM-Confidence:' in line:
        value = line.split(':')[1].strip()
        print(value)
        fout.write(value + '\n')

fin.close()
fout.close()
