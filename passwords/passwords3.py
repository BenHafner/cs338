import hashlib
import binascii

words = [line.strip().lower() for line in open('words.txt')]

hashesComputed = 0
passwordsCracked = 0

for line in open('passwords3.txt'):
    salt = line.split(':')[1].split('$')[2]
    digest = line.split(':')[1].split('$')[3]
    for word in words:
        hasher = hashlib.sha256((salt + word).encode('utf-8'))
        hashesComputed += 1
        if digest == binascii.hexlify(hasher.digest()).decode('utf-8'):
            print(line.split(':')[0], end=':')
            print(word)
            passwordsCracked += 1
            break

print(hashesComputed)
print(passwordsCracked)
