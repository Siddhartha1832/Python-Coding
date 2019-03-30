
def encrypt(plaintext, key):
   ciphertext = ""
   # traverse the plain texdt
   for i in range(len(plaintext)):
      char = plaintext[i]
      # Encrypt uppercase characters in plain texdt
      if (char.isupper()):
         ciphertext += chr((ord(char) + key - 65) % 26 + 65)
      else:
         # Encrypt lowercase characters in plain texdt
         ciphertext += chr((ord(char) + key - 97) % 26 + 97)
   return ciphertext

def brute_force_attack(plaintext):
   LETTERS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
   for key in range(len(LETTERS)):
      ciphertext = encrypt(plaintext, key)
      print(f' Key #{key} --> {ciphertext}')

if __name__ == '__main__':
   print('\n *** Caesar Cipher *** \n')
   plaintext = input(' Enter plaintext: ')
   key = int(input(' Enter key: '))
   print('\n MainMenu \n 1. Caesar Cipher Encryption \n 2. Hack Caesar Cipher Algorithm \n 3. Exit')
   choice = 1
   while choice:
      if choice == 1:
         print(f' --> Ciphertext : {encrypt(plaintext, key)}')
      elif choice == 2:
         #ciphertext = input(' Enter ciphertext: ')
         brute_force_attack(plaintext)
      else:
         print(' Thankyou.. Exiting..')
         exit(0)
      choice = int(input('\n Enter your choice (1-3): '))

