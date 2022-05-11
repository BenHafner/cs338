import hashlib
import binascii

words = [line.strip().lower() for line in open('words.txt')]

# create dictionary to associate each hash digest with a list of accounts
# that have that hash digest 
hashDict = {}
for line in open('passwords1.txt'):
    account = line.split(':')[0]
    digest = line.split(':')[1]
    if digest not in hashDict: hashDict.update({digest:[]})
    hashDict.get(digest).append(account)

hashesComputed = 0
passwordsCracked = 0

for word in words:
    hasher = hashlib.sha256(word.encode('utf-8'))
    digest = binascii.hexlify(hasher.digest()).decode('utf-8')
    hashesComputed += 1
    if digest in hashDict:
        for account in hashDict.pop(digest):
            print(account, end=':')
            print(word)
            passwordsCracked += 1

print(hashesComputed)
print(passwordsCracked)
