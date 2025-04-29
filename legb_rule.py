
# x=100
# def outer():
#     global x
#    # x=x+20
#     print(x)

#     x=10
#     print(x)

# outer()






x=100
def outer():
    x=20   #nonlocal-variable
    def inner():
        nonlocal x
        x=x+20
        print(x)
        x=200  #local variable
        print(x)
    
    inner()



outer()