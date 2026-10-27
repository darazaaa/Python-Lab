fin = open('mailbox.txt', 'r')
lines = fin.readlines()
fout = open('output1.txt', 'w')

accounts = []

for line in lines:
    if line.startswith('From: '):
        words = line.split()
        email = words[1]
        account = email.split('@')[0]
        if account not in accounts:
            accounts.append(account)

accounts.sort()

for acc in accounts:
    print(acc)
    fout.write(acc + '\n')

fin.close()
fout.close()
