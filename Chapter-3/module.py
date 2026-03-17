name = "Pritom"
nameshort = name[0:3] # start from index 0 all the way till 3 ( Excluding 3 )

print(name)
print(nameshort)
nameminus = name[-4:-1] # start from index -4 all the way till -1 ( Excluding -1 ) and skip 1 character
print(nameminus)    
word = "Python"
print(word[0:6:2]) # start from index 0 all the way till 6 ( Excluding 6 ) and skip 2 character

print(len(name)) # length of the string
print(name.endswith("tom")) # check if the string ends with "tom"
print(name.startswith("Pri")) # check if the string starts with "Pri"
print(name.capitalize()) # capitalize the first letter of the string
s= "Hello World"
print(s.split()) # split the string into a list of words
print(s.replace("World", "Python")) # replace "World" with "Python"
print(s.upper()) # convert the string to uppercase
print(s.lower()) # convert the string to lowercase
print(s.count("o")) # count the number of occurrences of "o" in the string
print(s.find("o")) # find the index of the first occurrence of "o" in the string
print(s.find("o", 5)) # find the index of the first occurrence of "o" in the string starting from index 5  
a = "Pritom is a Good Boy\n He is a \"Student\""
print(a) # print the string with a new line
print(a.splitlines()) # split the string into a list of lines
