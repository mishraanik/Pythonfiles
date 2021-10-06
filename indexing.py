string1 = "he's"
string2 = "probabbly"
string3 = "ass"
string4 = "mad"
string5 = "dumb and deaf"
#mannual spaces can be created when using string value: DEMONSTRATING as { string1 = "he's "
print(string1 + ' ' +  string2 + ' ' + string3 + ' ' + string5)
#creating spaces while going to run for output
print("he's" "probbbly " "ass " "mad " "deaf and dumb")

print("Hello" * 5)
#this will iterate Hello word 5 number of times

print("Hello " * 5)
#creating space in string Hello

#print("Hello " *5 + 4)
#Expected type 'str', got 'int' instead ;; it doesn"t concatinates because of + plus sign

print("Hello " * (5+4))

print("Hello " * 5 + "4")

today = "friday"
print("fri" in today) #true
print("day" in today) #true
print("thurs" in today) #false
print("hey" in today) #false
