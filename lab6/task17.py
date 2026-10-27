fin = open('mailbox.txt', 'r')
lines = fin.readlines()
fout = open('output17.txt', 'w')

recipients = set()
for line in lines:
    if line.startswith('To: '):
        email = line.split()[1]
        account = email.split('@')[0]
        recipients.add(account)

sorted_recipients = sorted(list(recipients))
for r in sorted_recipients:
    print(r)
    fout.write(r + '\n')

fin.close()
fout.close()
