fin = open('mailbox.txt', 'r')
lines = fin.readlines()
fout = open('output14.txt', 'w')

counter = len(lines)

print(counter)
fout.write(str(counter) + '\n')

fin.close()
fout.close()
