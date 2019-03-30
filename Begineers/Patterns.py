import sys

def star_pattern1(n):
    for i in range(1, n+1):
        print("* "*i)

def star_pattern2(n):
    k = 2*n - 2
    for i in range(0, n):
        for j in range(0, k):
            print(end=" ")
            k = k - 2
        for j in range(0, i+1):
            print("* ", end="")
            print("\r")

def star_pattern3(n):
    for i in range(0, n):
        for j in range(n, i, -1):
            print("* ", end="")
        print()

def pyramid_pattern1(n):
    k = 0
    for i in range(1, n+1):
        for space in range(1, (n-i)+1):
            print(end="  ")
        while k != (2*i-1):
            print("* ", end="")
            k = k + 1
        k = 0
        print()

def pyramid_pattern2(n):
    k = 1
    for i in range(0, n):
        for j in range(0, k):
            print("* ", end="")
        k = k + 2
        print()

def pyramid_pattern3(n):
    k, tim = 36, 1
    for i in range(0, n):
        for j in range(0, k):
            print(end=" ")
        k = k - 4
        for j in range(0, tim):
            print("* ", end="")
        tim = tim + 2
        print()

def number_pattern1(n):
    k = 1
    for i in range(0, n):
        for j in range(0, i+1):
            print(k, end=" ")
            k = k + 1
        print()

def number_pattern2(n):
    num = 1
    for i in range(0, n):
        num = 1
        for j in range(0, i+1):
            print(num, end=" ")
            num = num + 1
        print()

def number_pattern3(n):
    num = 1
    for i in range(0, n):
        for j in range(n, i, -1):
            print(num, end=" ")
            num = num + 1
        print()
        num = 1

def number_pattern4(n):
    num, incr = 1, 1
    for i in range(0, n):
        for j in range(0, incr):
            print(num, end=" ")
            num = num + 1
        print()
        incr = incr + 2

def number_pattern5(n):
    num, count, decr = 1, 0, 8
    for i in range(0, n):
        for k in range(0, decr):
            print(end=" ")
        for j in range(0, i):
            count = count + 1
        num = count
        temp = num
        for j in range(0, i):
            print(num, end=" ")
            num = num - 1
        print()
        num = temp
        decr = decr - 2

def alphabet_pattern1(n):
    val = 65
    for i in range(0, n):
        for j in range(0, i+1):
            ch = chr(val)
            print(ch, end=" ")
            val = val + 1
        print()

def alphabet_pattern2(n):
    val = 65
    for i in range(0, n):
        for j in range(0, i+1):
            ch = chr(val)
            print(ch, end=" ")
        val = val + 1
        print()

def alphabet_pattern3(n):
    incr, val = 1, 65
    for i in range(0, n):
        for j in range(0, incr):
            ch = chr(val)
            print(ch, end=" ")
            val = val + 1
        incr = incr + 2
        print()

def alphabet_pattern4(n):
    decr = 8
    count = 64
    val = 65
    for i in range(0, 5):
        for k in range(0, decr):
            print(end=" ")
        for j in range(0, i+1):
            count = count + 1
        val = count
        temp = val
        for j in range(0, i+1):
            ch = chr(val)
            print(ch, end=" ")
            val = val - 1
        val = temp
        decr = decr - 2
        print()

def star_patterns():
    print("\n Star Patterns \n 1. Star Pattern 1 \t 2. Star Pattern 2 \t 3. Star Pattern 3 \t 0. Exit")
    choice = int(input("\n Enter your choice (Exit = 0) : "))
    getvalue = int(input("\n How many element : "))
    if choice==1:
        star_pattern1(getvalue)
    elif choice==2:
        star_pattern2(getvalue)
    elif choice==3:
        star_pattern3(getvalue)
    elif choice==0:
        print("\n Exiting..")
        sys.exit()

def alphabet_patterns():
    print("\n Alphabet Patterns \n 1. Alphabet Pattern 1 \t 2. Alphabet Pattern 2 \t 3. Alphabet Pattern 3 \t 4. Aphabet Pattern 4 \t 0. Exit")
    choice = int(input("\n Enter your choice (Exit = 0) : "))
    getvalue = int(input("\n How many element : "))
    if choice==1:
        alphabet_pattern1(getvalue)
    elif choice==2:
        alphabet_pattern2(getvalue)
    elif choice==3:
        alphabet_pattern3(getvalue)
    elif choice==4:
        alphabet_pattern4(getvalue)
    elif choice==0:
        print("\n Exiting..")
        sys.exit()

def pyramid_patterns():
    print("\n Pyramid Patterns \n 1. Pyramid Pattern 1 \t 2. Pyramid Pattern 2 \t 3. Pyramid Pattern 3 \t 0. Exit")
    choice = int(input("\n Enter your choice (Exit = 0) : "))
    getvalue = int(input("\n How many element : "))
    if choice==1:
        pyramid_pattern1(getvalue)
    elif choice==2:
        pyramid_pattern2(getvalue)
    elif choice==3:
        pyramid_pattern3(getvalue)
    elif choice==0:
        print("\n Exiting..")
        sys.exit()

def number_patterns():
    print("\n Number Patterns \n 1. Number Pattern 1 \t 2. Number Pattern 2 \t 3. Number Pattern 3 \t 4. Number Pattern 4 \t 5. Number Pattern 5 \t 0. Exit")
    choice = int(input("\n Enter your choice (Exit = 0) : "))
    getvalue = int(input("\n How many element : "))
    if choice==1:
        number_pattern1(getvalue)
    elif choice==2:
        number_pattern2(getvalue)
    elif choice==3:
        number_pattern3(getvalue)
    elif choice==4:
        number_pattern4(getvalue)
    elif choice==5:
        number_pattern5(getvalue)
    elif choice==0:
        print("\n Exiting..")
        sys.exit()


for i in range(0,6):
    print("\n Patterns \n 1. Star Patterns \t 2. Number patterns \t 3. Alphabet Patterns \t 4. Pyramid Patterns \t 0. Exit")
    main_choice = int(input("\n Enter your Main choice (Exit = 0) : "))
    if main_choice==1:
        star_patterns()
    elif main_choice==2:
        number_patterns()
    elif main_choice==3:
        alphabet_patterns()
    elif main_choice==4:
        pyramid_patterns()
    elif main_choice==0:
        print("\n Exiting..")
        sys.exit()
