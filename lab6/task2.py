fin = open('mailbox.txt', 'r')
lines = fin.readlines()
fout = open('output2.txt', 'w')

revisions = []

for line in lines:
    if 'Details:' in line and 'rev=' in line:
        parts = line.split('rev=')
        rev = parts[1].strip()
        if rev not in revisions:
            revisions.append(rev)

revisions.sort()

for rev in revisions:
    print(rev)
    fout.write(rev + '\n')

fin.close()
fout.close()
