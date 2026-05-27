# This exercise was completed as part of a training video with Sarah Holderness
# in Python Foundations (Lists & Loops) on Plural Sight.
expenses = [10.50, 8, 5, 15, 20, 5, 3]

total = 0
for expense in expenses:
     total +=expense

print(f"Total expenses: ${total:.2f}")