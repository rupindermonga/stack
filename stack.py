
stack = []

def pushit():
    stack.append(input("Enter new string: ").strip())

def popit():
    if len(stack) == 0:
        print("Can't pop from an empty stack")
    else:
        print("Removed [",stack.pop(),"]")

def viewstack():
    print(stack)

CMDs = {'u' : pushit, 'o' : popit, 'v' : viewstack}

def showmenu():
    pr = """
    p(u)sh
    p(o)p
    (v)iew
    (q)uit

    Enter choice: """

    while True:
        while True:
            try:
                choice = input(pr).strip()[0].lower()
            except (EOFError, KeyboardInterrupt, IndexError):
                choice = 'q'
            
            print("\nYou picked: [%s]" % choice)
            if choice not in 'uovq':
                print("Invalid choice, try again")
            else:
                break
        
        if choice == "q":
            break
        CMDs[choice]()

if __name__ == '__main__':
    showmenu()