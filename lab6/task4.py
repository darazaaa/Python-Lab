fin = open('mailbox.txt', 'r')
lines = fin.readlines()
fout = open('output4.txt', 'w')

domains = set()
for line in lines:
    if line.startswith('From: '):
        email = line.split()[1]
        domain = email.split('@')[1]
        domains.add(domain)

sorted_domains = sorted(list(domains))
for d in sorted_domains:
    print(d)
    fout.write(d + '\n')

fin.close()
fout.close()
