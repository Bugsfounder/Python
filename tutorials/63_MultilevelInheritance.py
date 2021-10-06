class Dad:
    basketball = 1


class Son(Dad):
    dance = 1

    def isDance(self):
        return f"Yes I can Dance {self.dance} Number of Times"


class GrandSon(Son):
    dance = 6

    def isDance(self):
        return f"Jackson Yeah! Yes I will Dance Very Incredibly {self.dance} Number of Times"


darry = Dad()
larry = Son()
harry = GrandSon()

print(darry.basketball)
print(larry.isDance())
print(harry.isDance())
print(harry.basketball)


# QUICK QUIZ: CREATE THREE CLASSES NAMED ELECTRONIC DEVICE, POCKET GADGET AND PHONE

class Laptop:
    motherBoart = True
    exMouse = False
    tMouse = True
    speaker = True


class RaspberryPi(Laptop):
    tMouse = False
    tool = True
    speaker = False


class Phone(RaspberryPi):
    gps = True
    camera = True
    speaker = True


eDev = Laptop()
pDev = RaspberryPi()
phone = Phone()

print(eDev.speaker)
print(pDev.speaker)
print(phone.speaker)
