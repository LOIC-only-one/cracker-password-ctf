import hashlib

while True:

    try:

        wordlist_user = raw_input('Name of worlists: ')
        wordlist = open(wordlist_user)
        hash = raw_input('Entre ton hash: ')

        break

    except:

        print('[-] Nom de fichier introuvable ;( !')

for word in wordlist.readlines():
    
    word = word.strip("\n")
    wordlist_hash = hashlib.sha224(word).hexadigest()

    if hash == wordlist_hash:

        print('[+] HASH FOUND ====> ',word)

    else:

        print('[-] NOT HASH FOUND')