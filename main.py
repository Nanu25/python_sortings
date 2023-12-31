#Generate n random number between [0, 100]

import random
def generateNRandomNumbers(n : int) -> list:
    generate_list = []
    for i in range(n):
        generate_list.append(random.randint(0, 100))
    return generate_list


#function for the insertion sort

def insertionSort(n : int, number_list : list, step : int) -> list:
    sorted_list = number_list
    number_of_steps = 0
    for i in range(n):
        j = i - 1
        number = sorted_list[i]
        while j >= 0 and sorted_list[j] > number:
            sorted_list[j + 1] = sorted_list[j]
            j = j - 1

            number_of_steps = number_of_steps + 1
            if number_of_steps % step == 0:
                print(sorted_list)

        sorted_list[j + 1] = number

        number_of_steps = number_of_steps + 1
        if number_of_steps % step == 0:
            print(sorted_list)

    return sorted_list

#function for the heap sort.

def printHeap(heap_list : list):
    for i in range(1, len(heap_list)):
        print(heap_list[i], end = " ")
    print("")

def HeapAdd(n : int, heap_list : list, step : int, levelHeap : int, number_steps : int):
    if(levelHeap > 1):
        father = levelHeap // 2
        if heap_list[father] < heap_list[levelHeap]:
            (heap_list[father], heap_list[levelHeap]) = (heap_list[levelHeap], heap_list[father])

            number_steps = number_steps + 1;
            if number_steps % step == 0:
                printHeap(heap_list)

        HeapAdd(n, heap_list, step, father, number_steps)

def HeapExtract(n : int, heap_list : list, step : int, levelHeap : int, node : int, number_steps : int):
    if 2 * node <= levelHeap:
        left_son = heap_list[2 * node]
        right_son = -1
        which_son = 2 * node

        # if i have a right son
        if 2 * node + 1 <= levelHeap:
            right_son = heap_list[2 * node + 1]

        # i choose the best son
        if(right_son >= left_son):
            which_son = 2 * node + 1

        if(heap_list[node] < heap_list[which_son]):
            (heap_list[node], heap_list[which_son]) = (heap_list[which_son], heap_list[node])

            number_steps = number_steps + 1
            if number_steps % step == 0:
                printHeap(heap_list)

            HeapExtract(n, heap_list, step, levelHeap, which_son, number_steps)


def HeapSort(n : int, heap_list : list, step : int, number_steps : int) -> list:
    for i in range(1, n + 1):
        # i move the maximum element to the last position
        (heap_list[1], heap_list[n - i + 1]) = (heap_list[n - i + 1], heap_list[1])

        number_steps = number_steps + 1;
        if number_steps % step == 0:
            printHeap(heap_list)

        # find the maximum from the elements remains.
        HeapExtract(n, heap_list, step, n - i,  1, number_steps)

    return heap_list

def BuildHeapList(n : int, number_list : list, number_steps : int) -> list:
    heap_list = number_list
    for i in range(2, n + 1):
        HeapAdd(n, heap_list, step, i, number_steps)

    return  heap_list

#selection sort function

def selectionSort(n : int, number_list : int, step : int) -> list:
    number_step = 0
    for i in range(n):
        for j in range(i, n):
            if number_list[i] > number_list[j]:
                (number_list[i], number_list[j]) = (number_list[j], number_list[i])
                number_step = number_step + 1
                if number_step % step == 0:
                    print(number_list)

    return number_list


#bubble sort function

def bubbleSort(n : int, number_list : int,  step : int) -> list:
    number_step = 0
    sorted = 0
    while(sorted == 0):
        sorted = 1
        for i in range(n - 1):
            if number_list[i] > number_list[i + 1]:
                (number_list[i], number_list[i + 1]) = (number_list[i + 1], number_list[i])
                sorted = 0

                number_step = number_step + 1
                if number_step % step == 0:
                    print(number_list)


    return number_list


#bogosort function, shuffle the list till it s sorted

def TestIfSort(n : int, number_list : int) -> bool:
    for i in range(n - 1):
        if number_list[i] > number_list[i + 1]:
            return 0
    return 1

def randomize_list(n : int, number_list : list) -> list:
    for i in range(n):
        index = random.randint(0, n - 1)
        (number_list[i], number_list[index]) = (number_list[index], number_list[i])
    return number_list

def bogoSort(n : int, number_list : list) -> list:
    while TestIfSort(n, number_list) == 0:
        print(number_list)
        number_list = randomize_list(n, number_list)

    return number_lists

#cocktail sort is like the bubble sort but from both sides
def cocktailSort(n : int, number_list : int, step : int):
    number_step = 0
    start = 0
    end = n - 1
    sorted = 0
    while sorted == 0:
        sorted = 1
        for i in range(start, end):
            if number_list[i] > number_list[i + 1]:
                (number_list[i], number_list[i + 1]) = (number_list[i + 1], number_list[i])
                sorted = 0

                number_step = number_step + 1
                if number_step % step == 0:
                    print(number_list)

        if(sorted == 1):
            break

        sorted = 1
        end = end - 1
        for i in range(end - 1, start, -1):
            if number_list[i] > number_list[i + 1]:
                (number_list[i], number_list[i + 1]) = (number_list[i + 1], number_list[i])
                sorted = 0

                number_step = number_step + 1
                if number_step % step == 0:
                    print(number_list)

        start = start + 1

    return number_list

#permutation sort, like it's name says

from itertools import permutations

def Generate_permutation(n : int, number_list : int):
    listOfPermutation = list(permutations(range(0, len(number_list))))
    for i in listOfPermutation:
        #create the array with the index i generated.
        sorted_list = [None] * n
        for j in range(n):
            sorted_list[j] = number_list[i.index(j)]

        #test if the permutation makes a sorted array.
        sorted = 1
        for j in range(n - 1):
            if sorted_list[j] > sorted_list[j + 1]:
                sorted = 0
                break

        if sorted == 1:
            return sorted_list

        print(sorted_list)


#comb sort is like the bubble sort but you don t took every consecutive numbers

def getNextgap(gap : int) -> int:
    gap = (gap * 10) // 13
    if gap < 1:
        return 1
    return gap

def combSort(n : int, number_list : int, step : int) -> list:
    gap = n
    swapped = 1
    number_steps = 0
    while gap != 1 or swapped == 1:
        gap = getNextgap(gap)
        swapped = False
        for i in range(n - gap):
            if number_list[i] > number_list[i + gap]:
                (number_list[i], number_list[i + gap]) = (number_list[i + gap], number_list[i])
                swapped = True

                number_steps = number_steps + 1
                if number_steps % step == 0:
                    print(number_list)

    return number_list


#function for gnomeSort

def gnomeSort(n : int, number_list : int, step : int) -> list:
    number_steps = 0
    i = 0
    while i < n:
        if i == 0:
            i = i + 1
        if number_list[i] >= number_list[i - 1]:
            i = i + 1
        else:
            (number_list[i], number_list[i - 1]) = (number_list[i - 1], number_list[i])
            i = i - 1

            number_steps = number_steps + 1
            if number_steps % step == 0:
                print(number_list)

    return number_list


#function for shell sort: Insertion sort a much way better
def shellSort(n : int, number_list : int, step : int) -> list:
    number_steps = 0
    gap = n // 2
    while gap > 0:
        j = gap
        while j < n:
            i = j - gap
            while i >= 0:
                if number_list[i + gap] > number_list[i]:
                    break
                else:
                    (number_list[i + gap], number_list[i]) = (number_list[i], number_list[i + gap])
                    number_steps  += 1
                    if number_steps % step == 0:
                        print(number_list)

                i -= gap
            j += 1
        gap = gap // 2

    return number_list

def stoogeSort(n : int, number_list : int, step : int, left : int, right : int, number_steps : int) -> list:
    if left < right:
        if number_list[left] > number_list[right]:
            (number_list[left], number_list[right]) = (number_list[right], number_list[left])

            number_steps += 1
            if number_steps % step == 0:
                print(number_list)
        if right - left + 1 > 2:
            lenght = (right - left + 1) // 3

            stoogeSort(n, number_list, step, left, right - lenght, number_steps)
            stoogeSort(n, number_list, step, left + lenght, right, number_steps)
            stoogeSort(n, number_list, step, left, right - lenght, number_steps)

    return number_list

#main program

print("Press the option do you want to choose ")
print("1 for insertion sort")
print("2 for  heap sort")
print("3 for selection sort")
print("4 for bubble sort")
print("5 for bogo sort")
print("6 for cocktail sort")
print("7 for permutation sort")
print("8 for comb sort")
print("9 for gnome sort")
print("10 for Shell sort")
print("11 for Stooge sort")
which_sort = int(input(">"))

n = int(input("Write the number of numbers you want to generate: "))
list_of_numbers = generateNRandomNumbers(n)

print("There is the list of numbers: ", list_of_numbers)
step = int(input("Write the step you want to see the partially sorted list "))

if which_sort == 1:
    list_of_numbers = insertionSort(n, list_of_numbers, step)
    print(list_of_numbers)
elif which_sort == 2:
    #Index the list from 1.
    list_of_numbers.insert(0, 0)

    number_steps = 0
    heap_list = BuildHeapList(n, list_of_numbers, number_steps)
    heap_list = HeapSort(n, heap_list, step, number_steps)
    printHeap(heap_list)
elif which_sort == 3:
    list_of_numbers = selectionSort(n, list_of_numbers, step)
    print(list_of_numbers)
elif which_sort == 4:
    list_of_numbers = bubbleSort(n, list_of_numbers, step)
elif which_sort == 5:
    print("At bogo sort i will print at every randomize")
    list_of_numbers = bogoSort(n, list_of_numbers)
    print(list_of_numbers)
elif which_sort == 6:
    list_of_numbers = cocktailSort(n, list_of_numbers, step)
    print(list_of_numbers)
elif which_sort == 7:
    print("At permutation sort i will print at every permutation")
    list_of_numbers = Generate_permutation(n, list_of_numbers)
    print(list_of_numbers)
elif which_sort == 8:
    list_of_numbers = combSort(n, list_of_numbers, step)
    print(list_of_numbers)
elif which_sort == 9:
    list_of_numbers = gnomeSort(n, list_of_numbers, step)
    print(list_of_numbers)
elif which_sort == 10:
    list_of_numbers = shellSort(n, list_of_numbers, step)
    print(list_of_numbers)
else:
    number_steps = 0
    list_of_numbers = stoogeSort(n, list_of_numbers, step, 0, n - 1, number_steps)
    print(list_of_numbers)