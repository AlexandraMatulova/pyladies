key = int(input('What key do you want to use? '))
plaintext = input('What text do you want to encrypt? ')
ciphertext = ''

if key <= 0:
    print('Please use positive numbers only')

plaintext_list = list(plaintext)
for i in range(len(plaintext)):
    pi = ord(plaintext_list[i])
    #small letters
    if pi >= 97 and pi <= 122:
        key = key % 26
        if pi + key <= 122:
            ci = pi + key
        else:
            ci = 97 + (pi + key) % 123
    #capital letters
    elif pi >= 65 and pi <= 90:
        if pi + key <= 90:
            ci = pi + key   
        else:
            ci = 65 + (pi + key) % 91    
    else:
        ci = pi
    ciphertext = ciphertext + chr(ci)

print('result', ciphertext)
