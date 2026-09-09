shopping_list = []

while True:
    print("\n--- Shopping List Manager ---")
    action = input("Choose an action (add / remove / show / done): ").strip().lower()

    if action == "add":
        item = input("Enter item to add: ").strip()
        shopping_list.append(item)
        print(f"'{item}' has been added to your shopping list.")

    elif action == "remove":
        item = input("Enter item to remove: ").strip()
        # Check membership before removing to avoid ValueError
        if item in shopping_list:
            shopping_list.remove(item)
            print(f"'{item}' has been removed from your shopping list.")
        else:
            print("That item is not on your list.")

    elif action == "show":
        if not shopping_list:
            print("Your shopping list is currently empty.")
        else:
            print("\nYour Current Shopping List:")
            for item in shopping_list:
                print(item)

    elif action == "done":
        print("Thank you for using Shopping List Manager. Goodbye!")
        break

    else:
        print("Invalid choice. Please choose: add, remove, show, or done.")