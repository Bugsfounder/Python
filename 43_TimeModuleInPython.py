import time

initial = time.time()
# print(initial)

k = 0
while k < 45:
    time.sleep(0.2)
    print(f"{k + 1}. This is Harry Bhai")
    k += 1
print(f"while loop Runtime: {time.time() - initial} Seconds")

initial2 = time.time()
for i in range(45):
    print(f"{i + 1}. This is Harry Bhai")
print(f"for loop Runtime: {time.time() - initial2} Seconds")

# localTime = time.asctime(time.localtime(time.time()))
# print(localTime)
