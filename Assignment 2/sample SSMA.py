import queue
sma5 = queue.Queue(5) # The max size is 26

for i in range (5):
    sma5.put(i)
    print("pushed iterm: ", i)
    
#sma5.put(1)
#sma5.put(2)
#sma5.put(3)
#sma5.put(4)
#sma5.put(5)

print(sma5.full())

#for i in range (5):
#    D = sma5.get()
#    print("popped item is:", D)

#print(sma5.full())
#print(sma5)
print(sma5.empty())

MA5 = (1+2+3+4)/5
print("MA5 is: ", MA5)
New = 20
Old = sma5.get()
MA5_new = (MA5*5 - Old + New)/5
print("Queue full? after pop: ", end=" ")
print(sma5.full())
sma5.put(New) # push new data
print("Queue full?after update: ", end=" ")
print(sma5.full())
MA5 = MA5_new
print("New updated MA5: ", MA5)
    

