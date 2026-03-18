s = set()
s.add(18) # This will add the integer 18 to the set 's'.
s.add(18.0) # This will not be added to the set because 18 and 18.0 are considered equal in Python, and sets do not allow duplicate elements.
s.add("18") # This will add the string "18" to the set 's' because it is a different type and value from the integer 18 and the float 18.0.
print(s)
print(len(s)) # This will print 2 because the set 's' contains two unique elements: the integer 18 and the string "18". The float 18.0 is not added as it is considered equal to the integer 18.