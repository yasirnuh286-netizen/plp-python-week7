# Week 7 Assignment: Shopping List Manager

## File Descriptions
* **list_warmup.py**: Demonstrates basic Python list operations including index access, `.append()`, `.remove()`, and `len()`.
* **shopping_list.py**: An interactive terminal app that manages a dynamic shopping list using a loop and safer list operations.
* **list_report.py**: Analyzes a static list by generating a numbered report, counting specific string lengths, and calculating the longest item name without built-in helper functions.
* **screenshots/**: Folder containing screenshots of the execution outputs for each program.

## Reflection Question
### Why is it safer to check `in` before calling `.remove()`?
In Python, invoking `.remove(item)` on a list when the specified item does not exist raises an unhandled `ValueError`, causing the entire program to crash. Checking `in` first acts as a guard condition, ensuring the item exists before removal and allowing the application to display a clean warning message instead of crashing.