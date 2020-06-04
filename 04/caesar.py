key = int(input('What key do you want to use? '))
plaintext = input('What text do you want to encrypt? ')
ciphertext = ''

plaintext_list = list(plaintext)
for i in range(len(plaintext)):
    #print(plaintext_list[i])
    #print(ord(plaintext_list[i]))
    #print(key)
    pi = ord(plaintext_list[i])
    if pi >= 97 and pi <= 122:
        print(pi)
        print((pi + key) % pi)
        if pi + key > 122:
            ci = 97 + (pi + key) % 123
        else:
            ci = pi + key
    elif pi >= 65 and pi <= 90:
        if pi + key > 90:
            ci = 65 + (pi + key) % 91
        else:
            ci = pi + key
    else:
        ci = pi
    ciphertext = ciphertext + chr(ci)

print(ciphertext)
