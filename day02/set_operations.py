# SET OPERATIONS

list1 = list(map(int, input("Enter values for first list: ").split()))
list2 = list(map(int, input("Enter values for second list: ").split()))

# To find the elements that are common to both
common = set(list1) & set(list2)
print(f"The common values to both the lists are: {common}")
