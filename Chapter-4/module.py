friends = ["Rolf", "Charlie", "Anna", "Bob"]

print(friends[0])  # Rolf

friends[0] = "Smith"
print(friends[0])  # Smith

print(friends[1:5])  # ['Charlie', 'Anna', 'Bob']

friends.append("Pritom")
print(friends)  # ['Smith', 'Charlie', 'Anna', 'Bob', 'Pritom']

l1 = [11, 2, 31, 4, 5]
l1.sort()
print(l1)  # [2, 4, 5, 11, 31]

l1.insert(2, 306)# 2 is the index and 3 is the value
print(l1)  # [2, 4, 3, 5, 11, 31]

l1.pop(2)  # removes the element at index 2
print(l1)  # [2, 4, 5, 11,

l1.remove(11)  # removes the first occurrence of 11
print(l1)  # [2, 4, 5, 31]

a = (1, 2, 3, 4, 5, "Pritom", False) # tuples are immutable, meaning you cannot change their elements after they are created
print(type(a))  # <class 'tuple'>
print(a)

#a[0] = 10  # This will raise a TypeError because tuples are immutable   

no = a.count(5)  # 5
print(no)
print(a.index("Pritom"))  # 5
print(len(a))  # 7


