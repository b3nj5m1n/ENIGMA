import random
import time

# Insert alphabet for which you want to generate the wiring tables
alp = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789.,?!: '
# Initalize empty array
alphabet = []
# Add numbers for every char in alphabet (A,B,C = 0,1,2)
for i in range(0, len(alp)):
    alphabet.append(i)
# Make sure there is an even number of chars
if not len(alphabet) % 2 == 0:
    print("Even number of chars.")
    exit()
# Ask how many wiring tables for normal/grw walzen should be generated
print("Generate how many (normal) wirings?")
# Loop over how many should be generated
for i in range(0, int(input())):
    # Shuffle the alphabet
    p = random.sample(alphabet, len(alphabet))
    a = ""
    # Convert the integers to chars and add to a
    for integer in p:
        a += alp[integer]
    # Print wiring table
    print(str(i) + ". " + "".join(a))
# Ask how many etw wiring tables should be generated (These have to match 2 chars at a time)
print("Generate how many ETW wirings?")
# Loop over how many should be generated
for i in range(0, int(input())):
    # Initalize UKW inital varibale as alphabet (Array of ints)
    UKW_i = alphabet
    # Initalize empty UKW final variable
    UKW_f = []
    # While there are still objects in inital UKW variable
    while len(UKW_i) > 0:
        # Generate two random numbers
        i1 = random.randint(0, len(UKW_i) - 1)
        i2 = random.randint(0, len(UKW_i) - 1)
        # The two numbers cant be the same
        if i1 == i2:
            continue
        # Get object at index of thoose two random numbers
        t1 = UKW_i[i1]
        t2 = UKW_i[i2]
        # Generate the two pairs
        a1 = [t1, t2]
        a2 = [t2, t1]
        # Add the pairs to UKW final varibale
        UKW_f.append(a1)
        UKW_f.append(a2)
        # Remove the objects from the inital varibale, make sure the higher index will be removed first so the index for the second object doesn't change
        if i1 > i2:
            UKW_i = UKW_i[:i1] + UKW_i[(i1+1):]
            UKW_i = UKW_i[:i2] + UKW_i[(i2+1):]
        else:
            UKW_i = UKW_i[:i2] + UKW_i[(i2+1):]
            UKW_i = UKW_i[:i1] + UKW_i[(i1+1):]
    result = ""
    # Create result varibale and print it
    for char in alphabet:
        for pair in UKW_f:
            if pair[0] == char:
                result += alp[pair[1]]
    print(str(i) + ". " + result)
