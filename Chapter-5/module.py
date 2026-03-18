marks ={
    "Maths": 85,
    "Science": 90,
    "English": 78,
    "History": 92,
    "Geography": 88
}
print(marks, type(marks))
print("\n")
print("Marks in Maths:", marks["Maths"])
print("\n")

print(marks.items())
print("\n")
print(marks.keys())
print("\n")
print(marks.values())
print("\n")
marks.update({"Maths": 95, "Renuka": 85})
print(marks)
print("\n")
print(marks.get("Science")) # This will correctly return the value for "Science" which is 90.
print("\n")
print(marks["Science"]) # This will also correctly return the value for "Science" which is 90.


marks.pop("Maths", None) # This will not raise an error because "Maths" is not in the dictionary after clear(), and the default value None is returned.
print(marks)
print("\n")
marks.clear()
print(marks)
print("\n")


d= {} #Empty dictionary

s = {1, 2, 3,5,5,5} #Set #Duplicates are not allowed in sets, so the repeated '5' will only be stored once.
print(s, type(s))

e = set() #Empty set
print("\n")
s.add(10)
print(s)

print(len(marks)) # This will print 0 because the dictionary has been cleared and contains no key-value pairs.
print(len(s))
s.remove(2) # This will remove the element '2' from the set 's'.
print(s)

print("\n")

s1 = {1, 2, 3} 
s2 = {3, 4, 5}

print(s1.union(s2)) # This will print the union of sets s1 and s2, which includes all unique elements from both sets: {1, 2, 3, 4, 5}.
print(s1.intersection(s2)) # This will print the intersection of sets s1 and

print(s1.difference(s2)) # This will print the difference of sets s1 and s2, which includes elements that are in s1 but not in s2: {1, 2}.
print(s1.symmetric_difference(s2)) # This will print the symmetric difference of sets s1