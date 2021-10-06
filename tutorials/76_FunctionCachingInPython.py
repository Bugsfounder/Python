import time
from functools import lru_cache


# @lru_cache(maxsize=3)
# def some_work(n):
#     # SOME TASKS TAKING N SECONDS
#     time.sleep(n)
#     return n
#
#
# if __name__ == '__main__':
#     print("Now Running Some Work")
#     some_work(3)
#     print("Done... Calling Again")
#     some_work(3)
#     print("Called Again")
#
# n = int(input("Enter how many time you want to call: "))
#
#
# @lru_cache(maxsize=n)
# def workDone(n):
#     s = 32 + 32
#     return n
#
#
# print("Working....")
# print("Now Running Some Work")
# workDone(5)
# print("Done... Calling Again")
# workDone(2)
# print("Called Again")


@lru_cache(maxsize=10)
def calling(sec):
    time.sleep(sec)
    return sec


call = input("Enter 'call' to call your friend: ")
calling(3)
calling(2)
calling(1)
print("Your call is connecting.")
calling(2)
print("Ringing......")
