fin = open('mailbox.txt', 'r')
lines = fin.readlines()
fout = open('output4.txt', 'w')

domains = []

for line in lines:
    if line.startswith('From: '):
        words = line.split()
        email = words[1]
        domain = email.split('@')[1]
        if domain not in domains:
            domains.append(domain)

domains.sort()

for d in domains:
    print(d)
    fout.write(d + '\n')

fin.close()
fout.close()
