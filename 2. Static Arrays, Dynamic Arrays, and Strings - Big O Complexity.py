a = [1, 2, 3, 4, 5]

for i in a:
    for j in a:
        print(i, j)

# append - insert element at end of array - on average O(1)
a.append(6)
print(a)

# popping - O(1)
a.pop()
print(a)

# insert - O(n)
a.insert(5, 3)
print(a)

# modify - O(1)
a[0] = 7
print(a)

# accessing - O(1)
print(a[1])

#checking if array has element - O(n)
if 7 in a:
    print(True)

# Strings
# append the string - O(n) - create a new string + add new char

s = 'hello'
n = s+"z"
print(n)


# check if smth in a string - O(n)

if "f" in s:
    print(True)