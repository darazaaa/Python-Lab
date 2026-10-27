fin = open('mailbox.txt', 'r')
lines = fin.readlines()
fout = open('output17.txt', 'w')

recipients = []

for line in lines:
    if line.startswith('To: '):
        words = line.split()
        email = words[1]
        account = email.split('@')[0]
        if account not in recipients:
            recipients.append(account)

recipients.sort()

for r in recipients:
    print(r)
    fout.write(r + '\n')

fin.close()
fout.close()
