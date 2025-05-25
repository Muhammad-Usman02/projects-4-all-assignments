def list_practice(fruit_list):
    print("\n--- List Practice ---")
    print("Initial fruit list:", fruit_list)
    print("Length of list:", len(fruit_list))

    fruit_list.append('mango')
    print("Added 'mango' to the list.")
    print("Updated fruit list:", fruit_list)


def access_element(lst, index):
    try:
        return f"Element at index {index}: {lst[index]}"
    except IndexError:
        return "Index out of range."


def modify_element(lst, index, new_value):
    try:
        old_value = lst[index]
        lst[index] = new_value
        return f"Replaced '{old_value}' with '{new_value}'."
    except IndexError:
        return "Index out of range."


def slice_list(lst, start, end):
    try:
        return f"Sliced list: {lst[start:end]}"
    except Exception:
        return "Invalid slice range."


def index_game(fruit_list):
    print("\n--- Index Game ---")
    while True:
        print("\nChoose an operation: access / modify / slice / quit")
        choice = input("Your choice: ").strip().lower()

        if choice == "access":
            index = int(input("Enter index to access: "))
            print(access_element(fruit_list, index))

        elif choice == "modify":
            index = int(input("Enter index to modify: "))
            new_value = input("Enter new value: ")
            print(modify_element(fruit_list, index, new_value))

        elif choice == "slice":
            start = int(input("Enter start index: "))
            end = int(input("Enter end index: "))
            print(slice_list(fruit_list, start, end))

        elif choice == "quit":
            print("Exiting the game.")
            break

        else:
            print("Invalid choice. Try again.")

        print("Current list:", fruit_list)


def main():
    fruit_list = ['apple', 'banana', 'orange', 'grape', 'pineapple']
    list_practice(fruit_list)
    index_game(fruit_list)


if __name__ == "__main__":
    main()
