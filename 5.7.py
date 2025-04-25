def push(stack, item):
    stack.append(item)
    print(f"{item} pushed onto the stack.")

def pop(stack):
    if len(stack) == 0:
        print("Stack is empty! Cannot pop.")
    else:
        print(f"Popped item: {stack.pop()}")

def peek(stack):
    if len(stack) == 0:
        print("Stack is empty!")
    else:
        print(f"Top item: {stack[-1]}")

def display(stack):
    if len(stack) == 0:
        print("Stack is empty!")
    else:
        print("Stack contents:", stack)  

def main():
    stack = []
    while True:
        print("1. Push")
        print("2. Pop")
        print("3. Peek")
        print("4. Display")
        print("5. Exit")
        choice = input("Enter your choice (1-5): ")

        if choice == '1':
            item = input("Enter item to push: ")
            push(stack, item)
        elif choice == '2':
            pop(stack)
        elif choice == '3':
            peek(stack)
        elif choice == '4':
            display(stack)
        elif choice == '5':
            print("Exiting program.")
            break
        else:
            print("Invalid choice")


main()
