import array

# creates array with 3 signed integer
arr = array.array('i', [1, 2, 3])
print("initial values:", end=' ')
for i in arr:
    print(i, end=' ')
print("\r")
# append to array
arr.append(4)
print("after append 4:", end=' ')
for i in arr:
    print(i, end=' ')
print("\r")
# pop
arr.pop()
print("after popping up:", end=' ')
for i in arr:
    print(i, end=' ')
print("\r")
# insert at
arr.insert(2, 3)
print("after inserting 3 in the second position:", end=' ')
for i in arr:
    print(i, end=' ')
print("\r")
# remove first occurrence
arr.remove(3)
print("after removing first occurrence of 3:", end=' ')
for i in arr:
    print(i, end=' ')
print("\r")
# reverse the array
arr.reverse()
print("after reversion:", end=' ')
for i in arr:
    print(i, end=' ')
print("\r")
