print("\n *** List Operations *** \n")

class check():
    def __init__(self):
        self.n = []
    def add(self, a):
        return self.n.append(a)
    def remove(self, b):
        self.n.remove(b)
    def display(self):
        return (self.n)

if __name__ == '__main__':
    # Creating object called obj for class check
    obj = check()
    print(" List Operations \n 1. Add \t 2. Remove \t 3. Display \t 4. Exit")
    while True:
        choice = int(input("\n Enter your choice (1-4): "))
        if choice == 1:
            n = int(input("\n Enter number to append : "))
            obj.add(n)
        elif choice == 2:
            n = int(input("\n Enter number to remove : "))
            obj.remove(n)
        elif choice == 3:
            print("\n List : {} ".format(obj.display()))
        elif choice == 4:
            print("\n Exiting!")
            exit(0)
    else:
        print("\n Invalid Choice, Please try again..")
