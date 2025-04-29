# try:
#     number = int(input("Enter a number: "))
#     result = 10 / number
#     print(result)
# except ZeroDivisionError:
#     print("Zero se divide nahi kar sakte!")
# except ValueError:
#     print("Sirf number input karo!")



# try:
#     number = int(input("Enter a number: "))  # Yahan tum input ko integer mein convert kar rahe ho
#     print(f"You entered: {number}")
# except ValueError:
#     print("Sirf number input karo!")  # Agar input mein text ya alphabet ho to yeh print hoga



def divide_num(a,b):
    try:
        result=a / b

    except ZeroDivisionError:
        print("zero division error")

    except TypeError:
        print("type error")
    else:
        print(f"try bloked is working . the result is: {result}")

    finally:
        print("the finally block always be execute")

divide_num(10,3)
divide_num(10,0)
divide_num(10,'2')




try:
    num1=int(input("Enter 1st number"))
    num2=int(input("Enter 2nd number"))

    result=num1 / num2
except ValueError:
    print("value error")

except ZeroDivisionError:
    print(" zero devision error", )

else:
    print(f"divide successfully {result}")

finally:
    print("thank you for using the program")






from typing import NoReturn

def terminate_program() -> NoReturn:
    """Terminate the program by raising an exception."""
    raise SystemExit("Terminating the program.")

# When you call terminate_program, it never returns normally:
try:
    terminate_program()
except SystemExit as e:
    print(f"Program terminated: {e}")





def terminate_program():
    """Terminates the program by raising an exception."""
    raise SystemExit("Program is terminating.")

terminate_program()