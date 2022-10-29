#Long EMA 26 Days
import queue
lma26 = queue.Queue(26) # The max size is 26


#add item in a queue
for i in range (26):
    lma26.put(i)
    print("pushed item: ", i)
    



print(lma26.full())

#empty the queue with first in last out
# for i in range (26):
#    D = lma26.get()
#    print("popped item is:", D)

print(lma26.full()) #after emptying, the queue is empty, returns False
print(lma26)
print(lma26.empty()) #after emptying, the queue is empty, returns True

#Standard simple moving average formula
MA26 = (1+2+3+4+5+6+7+8+9+10+11+12+13+14+15+16+17+18+19+20+21+22+23+24+25)/26
print("MA26 is: ", MA26)
New = 20     #I think New it is a changeable field
Old = lma26.get()
MA26_new = (MA26*26 - Old + New)/26
print("Queue full? after pop: ", end=" ")
print(lma26.full())
lma26.put(New) # push new data
print("Queue full?after update: ", end=" ")
print(lma26.full())
MA26 = MA26_new
print("New updated MA26: ", MA26)
    

