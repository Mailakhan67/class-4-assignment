
# import sys
# print(sys.getrecursionlimit())
# sys.setrecursionlimit(200)
# print(sys.getrecursionlimit())
# i=0
# def demo():
#     global i
#     i+=1
#     print("Hello",i)
#     demo()
    

# demo()





# def search_room(room):
#     if room == "mera_room":
#         print("Room mil gaya!")  # agar sahi room hai
#     else:
#         print(f"Yeh '{room}' nahi hai, ander jao...")
#         search_room("mera_room")  # next baar correct room bhej rahe hain


# search_room("mera_room")




# def search_room(room):
#     print(f"Tum abhi '{room}' mein ho.")
    
#     if room == "mera_room":
#         print("✅ Yeh mera room hai! Room mil gaya!")
#     else:
#         print(f"❌ Yeh '{room}' mera room nahi hai, ander jao next room mein...")
#         search_room("mera_room")  # Ab agla room sahi bhej rahe hain

# # Start searching from a wrong room
# search_room("kitchen")



# def my_house(home):
#     print(f"my {home}")
#     if home == 'my home':
#         print("this is my home")
#     else:
#         print("not my home")
#         my_house('my home')

# my_house('not my home')



# def recursive(n):
#     if n == 1:
#         return 1
#     return 2 ** (n-1) + recursive(n - 1)

# n =5
# print(recursive(n))





# def factorial(n):
#     # Base case
#     if n == 0:
#         return 1
#     # Recursive case
#     else:
#         return n * factorial(n - 1)

# # Example usage
# print(factorial(5))  # Output: 120



# def fibo(n):
#     if n== 0:
#         return 0
#     if n==1:
#         return 1
#     return (fibo(n-2) + fibo(n-1))

# n=int(input("Enter number of terms"))
# for i in range( n):
#     print(fibo(i))







def fibonacci(n):
    # Base cases
    if n == 0:
        return 0
    elif n == 1:
        return 1
    # Recursive case
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)

# Example usage
print(fibonacci(10))  # Output: 8





def factorial(n):
      if n == 0:
       return 1
      else:
       return n * factorial(n-1)

number = 5
result = factorial(number)
print(f"The factorial of {number} is {result}")





def example_function(a: int, b: int = 0, *args: float, **kwargs: str) -> Tuple[int, List[float], Dict[str, str]]:
    """Example function demonstrating various parameter types.
    Args:
        a: An integer.
        b: An integer with a default value of 0.
        *args: Variable-length positional arguments of type float.
        **kwargs: Variable-length keyword arguments of type string.
    Returns:
        A tuple containing:
        - The sum of 'a' and 'b'.
        - A list of the variable-length positional arguments ('args').
        - A dictionary of the variable-length keyword arguments ('kwargs').
    """
    sum_ab = a + b
    args_list = list(args)  # Convert tuple to a list
    return sum_ab, args_list, kwargs

# Example usage
result = example_function(1, 2, 3.14, 2.71, name="Alice", city="New York")
print(result)

result = example_function(10, *[1.0, 2.0, 3.0], **{"country": "USA", "language": "English"})
result