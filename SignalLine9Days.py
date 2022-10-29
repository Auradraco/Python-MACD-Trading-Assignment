#Signal Line 9days EMA

import queue
sma9 = queue.Queue(9) # The max size is 9


#add item in a queue
for i in range (9):
    sma9.put(i)
    print("pushed item: ", i)
    



print(sma9.full())

#empty the queue with first in last out
# for i in range (9):
#    D = sma9.get()
#    print("popped item is:", D)

print(sma9.full()) #after emptying, the queue is empty, returns False
print(sma9)
print(sma9.empty()) #after emptying, the queue is empty, returns True

MA9 = (1+2+3+4+5+6+7+8)/9
print("MA9 is: ", MA9)
New = 20     #i think it is a changeable field
Old = sma9.get()
MA9_new = (MA9*9 - Old + New)/9
print("Queue full? after pop: ", end=" ")
print(sma9.full())
sma9.put(New) # push new data
print("Queue full?after update: ", end=" ")
print(sma9.full())
MA9 = MA9_new
print("New updated MA9: ", MA9)