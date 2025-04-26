def my_generator():
    yield 1
    yield 2
    yield 3
a=my_generator() 
print(next(a))
print(next(a))




def my_generator():
    yield 1
    yield 2

a = my_generator()

for value in a:
    print(value)




def banana_generator():
    for i in range(1, 3):  # machine ke andar loop
        yield f"Banana {i}"   # har baar ek banana de rahi hai


for banana in banana_generator():  # machine se ek ek banana le rahe hain
    print(banana)




def pizza_chef():
    pizzas = ["Margherita", "Pepperoni", "Veggie", "Cheese", "BBQ Chicken"]
    for pizza in pizzas:
        yield pizza
for order in pizza_chef():
    print(f"Delivering: {order}")






def ammi_rotiyan_banati_hain():
    for i in range(1, 6):
        yield f"Roti {i}"  # "Roti 1", "Roti 2", "Roti 3", etc.

# `for` loop yeh kar raha hai:
for roti in ammi_rotiyan_banati_hain():
    print(f"Table par rakhi gayi: {roti}")




def website_create():
    for i in range(1,3):
        yield f"website {i}"

for give in website_create():
    print(f" your website is ready: {give}")









def simple_generator():
    yield 1
    yield 2
    yield 3

# Create a generator object
gen = simple_generator()

print(gen, " : ", type(gen))

# Iterate over the generator
for value in gen:
    print(value, " : ", type(value))