def show():
    y = 5   # local variable
    print("y ki value:", y)

show()
#print("y global:", y)  # ❌ error dega




def my_function(**student):
      print("\nHis last name is " + student["lname"])

      for key, value in student.items():
       print(key, value)

      print(student)

my_function(fname = "Ali", lname = "Osman")

my_function(fname = "Ali", lname = "Osman", course = "Python - 101", day="Saturday", time="1400 - 1800")

my_dict = {"fname": "Arif", "lname": "Rozani", "course":"101 - 201", "day":"Saturday | Sunday", "role":"Student"}

#my_function(my_dict) # uncomment to see TypeError
my_function(**my_dict) # use ** to unpack the dictionary. 




def creater1():
    i=1
    while i <=200:
        yield i
        i +=1

print(creater1())
x=creater1()



def main(**args):
    for key,value in args.items():
        print(key,value)

main(name='maila',age=22,educ='graduation')


