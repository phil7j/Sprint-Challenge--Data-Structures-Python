import time
from binary_search_tree import BinarySearchTree
# The runtime is currenty O(n2)
start_time = time.time()

f = open('names_1.txt', 'r')
names_1 = f.read().split("\n")  # List containing 10000 names
f.close()

f = open('names_2.txt', 'r')
names_2 = f.read().split("\n")  # List containing 10000 names
f.close()


duplicates = []
# Initialize Binary Tree Here
BST1 = BinarySearchTree("Philip Johnson")
# Insert all the names of list 1 into the BST
for name_1 in names_1:
    BST1.insert(name_1)
# Loop through all the names in List 2 and for each name check if the BST contains it
for name_2 in names_2:
    if BST1.contains(name_2):
# If it contains the name, append it to the duplicates List
        duplicates.append(name_2)



end_time = time.time()
print (f"{len(duplicates)} duplicates:\n\n{', '.join(duplicates)}\n\n")
print (f"runtime: {end_time - start_time} seconds")

