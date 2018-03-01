unsorted_list = [90, 89, 79, 14, 9, 6, 71, 91, 4, 45]

operations = 0

for i in range(1, len(unsorted_list)):
    current = unsorted_list[i]

    for index, val in enumerate(unsorted_list):
        if i == index:
            break
        if current < unsorted_list[index]:
            del unsorted_list[i]
            unsorted_list.insert(index, current)
            operations += 1 
            break


for val in unsorted_list:
    print str(val)            
        

print 'TOTAL OPERATIONS: {}'.format(str(operations))         