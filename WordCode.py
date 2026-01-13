word = input("Enter your word: ")
i = word
j = int(len(i))

print("Your word(s) contain(s) " + str(j) + " characters!")

p = input("Do you wish to proceed? Type Y for yes and N for no: ")
if p == "Y":
    for k in range(len(word), 0, -1):       # len reads no. of letters, 0 to -1 gives full read
        print(word[:k]) 
    for k in range(2, len(word) + 1):       # Starts at letter 2 (XX) and prints out 1 extra letter
        print(word[:k])
if p == "N":
    print("Complete.")

asterisk = input("Do you want it in asterisk form? Type Y for yes and N for no: ")
if asterisk == "Y":
    for a in range(len(word), 0, -1):
        print(a * "*")
    for a in range(2, len(word) + 1):
        print(a * "*")
if asterisk == "N":
    print("Complete.")

special = input("Do you want it in special form? Type Y for yes and N for no: ")
if special == "Y":
    c = input("Enter your character of choice: ")
    for s in range(len(word), 0, -1):
        print(s * c)
    for s in range(2, len(word) + 1):
        print(s * c)
if special == "N":
    print("Complete.")

reverse = input("Do you wish to reverse your word(s)? Type Y for yes and N for no: ")
if reverse == "Y":
    print(i[::-1])
if reverse == "N":
    print("Complete.")