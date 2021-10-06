class A:
    classVar1 = "I am a class variable in Class A"

    def __init__(self):
        self.var1 = "I am in class A Constructor"
        self.classVar1 = "Instance variable in class A"
        self.special = "Special"


class B(A):
    classVar1 = "I am a class variable in Class B"

    def __init__(self):
        # super(B, self).__init__()
        self.var1 = "I am in class B Constructor"
        self.classVar1 = "Instance variable in class B"
        super(B, self).__init__()
        print(super().classVar1)


a = A()
b = B()

print(b.classVar1)
print(b.special, b.var1, b.classVar1)
