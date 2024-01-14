print("CALCULATOR")
a=int(input("""1.ADD
2.SUBTRACT
3.MULTIPLY
4.DIVIDE
Select the operaion to be performed(1,2,3 or 4)"""))
b=int(input("Enter your first number"))
print(b)
c=int(input("Enter your second number"))
print(c)
add=b+c
sub=b-c
mul=b*c
div=b/c
txt="Your answer is {}"
if a is 1:
    print(txt.format(add))
elif a is 2:
    print(txt.format(sub))
elif a is 3:
    print(txt.format(mul))
elif a is 4 :
    print(txt.format(div))
else:
    print("ERROR")
