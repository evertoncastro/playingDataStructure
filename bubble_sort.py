unsorted_list = [90, 89, 79, 14, 9, 6, 71, 91, 4, 45]

operations = 0

for i in range(0, len(unsorted_list)):
    skip = False
    for t in range(0, len(unsorted_list)):
        operations += 1
        if (t+1) < len(unsorted_list): 
            _current = unsorted_list[t]
            _next = unsorted_list[t+1]
            if _current > _next:                
                unsorted_list[t+1] = _current
                unsorted_list[t] = _next
                skip = True

    if not skip:
        break        
        
for val in unsorted_list:
    print str(val)

print 'TOTAL OPERATIONS: {}'.format(str(operations))    


# The algorithm consist of a matrix with outer and inner array
# In bubble sort the number of operations depends on the unsorted list size
# Using the skip resource it is possible to identify when the list is already sorted
# This avoid the unnecessary operations in the algorithim
# We can identify that the listed is alreary sorted if no change was made in the inner array iteration