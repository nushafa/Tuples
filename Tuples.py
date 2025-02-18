#Empty tuple
tuple = ()
print(tuple)

#Tuple having integers
tuple = (1, 2, 3)
print(tuple)

#tuple with mixed datatypes
tuple = (1, "Hello", 3.4)
print(tuple)

#nested tuple
tuple = ("mouse", [8, 4, 6], (1, 2, 3))
print(tuple)

#Accessing tuple elements using indexing
tuple = ('p', 'e', 'r', 'm', 'i', 't')
print(tuple[0])
print(tuple[5])

#nested tuple
n_tuple = ("mouse", [8, 4, 6], (1, 2, 3))

#nested index
print(n_tuple[0][3])
print(n_tuple[1][1])

#Slicing
print("Sliced:", tuple[1:4])

#Iterating through a tuple
for letter in (tuple):
    print("Hello", letter)