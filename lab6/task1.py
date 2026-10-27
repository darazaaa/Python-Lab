fin = open('mailbox.txt', 'r')
lines = fin.readlines()
fout = open('output1.txt', 'w')

accounts = set()
for line in lines:
    if line.startswith('From: '):
        email = line.split()[1]
        account = email.split('@')[0]
        accounts.add(account)

sorted_accounts = sorted(list(accounts))
for acc in sorted_accounts:
    print(acc)
    fout.write(acc + '\n')

fin.close()
fout.close()
