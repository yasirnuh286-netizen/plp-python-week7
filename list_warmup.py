fruits = ["Apple", "Banana", "Mango", "Orange"]

# Print the first and last item using indexes
print(f"First fruit: {fruits[0]}")
print(f"Last fruit: {fruits[-1]}")

# Append a fifth fruit
fruits.append("Pineapple")
print(f"List after adding a fruit: {fruits}")

# Remove one fruit
fruits.remove("Banana")
print(f"List after removing Banana: {fruits}")

# Print how many fruits remain
print(f"Number of fruits remaining: {len(fruits)}")