fin = open('mailbox.txt', 'r')
lines = fin.readlines()
fout = open('output.txt', 'w')

counter = 0
for line in lines:
    if line.startswith('From '):
        counter += 1

print(counter)
fout.write(str(counter))

fin.close()
fout.close()
