def add(x,y):
    return x+y

def sub(x,y):
    return x-y

def multiply(x,y):
    return x*y

def divide(x,y):
    return x/y

print("Enter 'A' for Addition. ")
print("Enter 'S' for Subtract. ")
print("Enter 'M' for Multiply. ")
print("Enter 'D' for Division. ")


while True:

    choice =input('Enter Choice (A,S,M,D):')

    if choice.upper() in ('A','ADD','ADDITION','S','SUB','SUBTRACTION','M','MULTIPLY','MULTIPLICATION','D','DIVIDE','DIVISION'):
        num1=float(input('Enter first number:  '))
        num2=float(input('Enter second number:  '))

        if choice.upper() in ('A','ADD','ADDITION'):
            print('Result:',(num1), '+' ,(num2) , '=' ,add(num1,num2))
        
        elif choice.upper() in ('S','SUB','SUBTRACTION'):
            print('Result:',(num1), '-' ,(num2), '=',sub(num1,num2))

        elif choice.upper() in ('M','MULTIPLY','MULTIPLICATION'):
            print('Result:',(num1), '*' ,(num2) ,'=' ,multiply(num1,num2))

        elif choice.upper() in ('D','DIVIDE','DIVISION'):
            print('Result:',(num1), '/' ,(num2) ,'=' ,divide(num1,num2))

    else:
        print("Please input a correct choice.")

    
    next_calculation =input("Want to do another calculation")
    if next_calculation.lower() in ('no','n','nope'):
        break