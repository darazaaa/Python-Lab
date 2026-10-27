fin = open('mailbox.txt', 'r')
lines = fin.readlines()
fout = open('output15.txt', 'w')

for line in lines:
    if 'java' in line:
        print(line.strip())
        fout.write(line)

fin.close()
fout.close()
