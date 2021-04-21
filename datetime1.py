import time

print(time.localtime(time.time()))  #Only display time

print(time.asctime(time.localtime(time.time())))  #Formatted time

for i in range(1,5):
    print(i)
    #Each element will print after 1 second
    time.sleep(1)

