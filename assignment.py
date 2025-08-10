# 1. creating an empty list
my_list = []
print("My_list before appending:", my_list )

# 2. Appending 10,20,30,40 into the list
my_list.append(10)
my_list.append(20)
my_list.append(30)
my_list.append(40)
print("my_list after appending:", my_list)

# 3. inserting 15 into the list at second position 
my_list.insert(2, 15)
print("my_list after insertion:", my_list)

# 4. extending my_list with another list
list = [50, 60, 70]
my_list.extend(list)
print("my_list after extending:", my_list)

# 5. removiing the last item
my_list.remove(70)
print("my_list after removing last item:", my_list)

# 6. sorting list
my_list.sort()
print("my_list after sorting:", my_list)

# 7. finding the value of index 30
my_list = my_list.index(30)
print("Index of 30 is:", my_list)