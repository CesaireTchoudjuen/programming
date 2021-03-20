# Author: Cesaire Tchoudjuen


import random
rangeTo=100
numberOfNumbers=10
queue = []

# Program that puts 10 random numbers into a queue(list), the program should then output all the values in the queue
for n in range(0, numberOfNumbers): 
    queue.append(random.randint(0, rangeTo))  # random.randint is the same method as randrange(0, rangeTo)
print("Queue is {}".format(queue)) 

# Take the numbers from the queue one at a time, print it and the current numbers still in the queue

while len(queue) != 0:
    currentNumber = queue.pop(0) # queue.pop() removes from ther list the element at the specified location
    print ("The current Number is {} and the queue is now {}".format(currentNumber, queue))

print ("The queue is now empty.")