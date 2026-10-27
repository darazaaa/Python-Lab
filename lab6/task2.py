fin = open('mailbox.txt', 'r')
lines = fin.readlines()
fout = open('output2.txt', 'w')

revisions = set()
for line in lines:
    if 'Details:' in line and 'rev=' in line:
        rev = line.split('rev=')[-1].strip()
        revisions.add(rev)

sorted_revisions = sorted(list(revisions))
for rev in sorted_revisions:
    print(rev)
    fout.write(rev + '\n')

fin.close()
fout.close()
