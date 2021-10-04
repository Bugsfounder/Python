# def function1():
#     print("Subscribe Now")
# func2 = function1
# del function1
# func2()

# def funcret(num):
#     if num == 0:
#         return print
#     if num == 1:
#         return sum

#  a = funcret(0)
# a = funcret(1)
# print(a)

# def executor(func1):
#     func1("This")

# executor(print)

def dec1(func1):
    def newexac():
        print("Executing Now...")
        func1()
        print("Executed")

    return newexac()


@dec1
def who_is_manisha():
    print("Manisha is good girl")


# who_is_manisha()
# who_is_manisha = dec1(who_is_manisha)
who_is_manisha()
