#Short MA 12 days

import queue
sma12 = queue.Queue(12) # The max size is 12


#add item in a queue
for i in range (12):
    sma12.put(i)
    print("pushed item: ", i)
    
#sma12.put(1)
#sma12.put(2)
#sma12.put(3)
#sma12.put(4)
#sma12.put(5)
#sma12.put(6)
#sma12.put(7)
#sma12.put(8)
#sma12.put(9)
#sma12.put(10)
#sma12.put(11)
#sma12.put(12)


print(sma12.full())

#empty the queue with first in last out
# for i in range (12):
#    D = sma12.get()
#    print("popped item is:", D)

print(sma12.full()) #after emptying, the queue is empty, returns False
print(sma12)
print(sma12.empty()) #after emptying, the queue is empty, returns True

MA12 = (1+2+3+4+5+6+7+8+9+10+11)/12 #sum of price divide by time period 
print("MA12 is: ", MA12)
New = 20
Old = sma12.get()
MA12_new = (MA12*12 - Old + New)/12
print("Queue full? after pop: ", end=" ")
print(sma12.full())
sma12.put(New) # push new data
print("Queue full?after update: ", end=" ")
print(sma12.full())
MA12 = MA12_new
print("New updated MA12: ", MA12)
    

