def enqueue(queue, item):
    queue.append(item)
    print(f"{item} added to the queue.")

def dequeue(queue):
    if len(queue) == 0:
        print("Queue is empty! Cannot dequeue.")
    else:
        print(f"Dequeued item: {queue.pop(0)}")  

def peek(queue):
    if len(queue) == 0:
        print("Queue is empty!")
    else:
        print(f"Front item: {queue[0]}")  

def display(queue):
    if len(queue) == 0:
        print("Queue is empty!")
    else:
        print("Queue contents:", queue)

def main():
    queue = []
    while True:
        print("\nQueue Operations:")
        print("1. Enqueue")
        print("2. Dequeue")
        print("3. Peek")
        print("4. Display")
        print("5. Exit")
        choice = input("Enter your choice (1-5): ")

        if choice == '1':
            item = input("Enter item to enqueue: ")
            enqueue(queue, item)
        elif choice == '2':
            dequeue(queue)
        elif choice == '3':
            peek(queue)
        elif choice == '4':
            display(queue)
        elif choice == '5':
            print("Exiting program")
            break
        else:
            print("Invalid choice")

main()
