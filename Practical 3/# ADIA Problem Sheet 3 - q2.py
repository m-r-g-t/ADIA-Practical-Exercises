# bubble down

unsorted = [8, 7, 5, 6, 3, 1, 2, 4]

iterationNumber = 0
while iterationNumber <= len(unsorted)-1:
    for i in range(len(unsorted - iterationNumber - 1)):
        if unsorted[i] > unsorted[i+1]:
            our_list[i], our_list[i+1] = our_list[i+1], our_list[i]
        print(unsorted)
    iterationNumber+=1

# bubble up
unsorted = [8, 7, 5, 6, 3, 1, 2, 4]

iterationNumber = 0
while iterationNumber <= len(unsorted)-1:
    for i in range(0, len(unsorted - iterationNumber - 1), -1):
        if unsorted[i] > unsorted[i+1]:
            our_list[i], our_list[i+1] = our_list[i+1], our_list[i]
        print(unsorted)
    iterationNumber+=1