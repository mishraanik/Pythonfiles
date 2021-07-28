#Multiplication and division has equal precedence. Addition and substraction has also equal precedence
#Addition and substraction also have equal precedence
#in an expression that mixes equal precendence,they are evaluated from left to right.
a=12
b=3

print(a+(b/3)-(4*12))  #48-13
print((((a+b)/3)-4)*12)  #12

c=a+b
d=c/3
e=d-4

print(e*12)