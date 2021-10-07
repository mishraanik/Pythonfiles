age = 24
print("My age is " + str(age) + " years")

#print("My age is " + age + " years")
#it gives out false because string and number can not be concatenated

print("my age is {0} years".format(age))
#string replacement by {0} here

print("there is {0} days in {1}, {2}, {3}, {4}, {5}, {6} and {7}".format(31, "jan", "mar", "may", "jul", "sept", "oct", "dec"))
#there is 31 days in jan, mar, may, jul, sept, oct and dec

print("there are {0} days in jan, mar, may, jul, aug, oct, dec".format(31))
#there are 31 days in jan, mar, may, jul, aug, oct, dec

print("jan: {1}, feb: {0}, mar: {2}, april: {1}, may: {2}, june: {1}, july: {2}".format(28,30,31))

