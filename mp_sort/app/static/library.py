from org.transcrypt.stubs.browser import *
import random

array = []


def gen_random_int(number, seed):
    result = list(range(number))
    random.seed(seed)
    random.shuffle(result)
    return result


def generate():
    global array

    number = 10
    seed = 200

    # call gen_random_int() with the given number and seed
    # store it to the global variable array
    pass

    array = None
    # convert the items into one single string
    # the number should be separated by a comma
    # and a full stop should end the string.
    array = gen_random_int(number, seed)

    array_str = ','.join(array) + '.'

    # This line is to placed the string into the HTML
    # under div section with the id called "generate"
    document.getElementById("generate").innerHTML = array_str


def bubble_sort(array):
    array = array[::]
    count = 0

    for k in range(1, len(array)):
        for i in range(1, len(array)):
            prev_val = array[i - 1]
            next_val = array[i]
            count += 1

            if array[i - 1] > array[i]:
                array[i] = prev_val
                array[i - 1] = next_val

    return array


def sortnumber1():
    """
    This function is used in Exercise 1.
    The function is called when the sort button is clicked.

    You need to do the following:
    - get the list of numbers from the global variable array and
        copy it to a new list
    - call your sort function, either bubble sort or insertion sort
    - create a string of the sorted numbers and store it in array_str
    """
    raw_data = document.getElementById("generate").innerHTML
    raw_data = raw_data.strip().replace('.', '').split(',')
    unsorted_array = [int(x) for x in raw_data]
    sorted_array = bubble_sort(unsorted_array)
    array_str = ','.join(sorted_array)

    document.getElementById("sorted").innerHTML = array_str


def sortnumber2():
    """
    This function is used in Exercise 2.
    The function is called when the sort button is clicked.

    You need to do the following:
    - Get the numbers from a string variable "value".
    - Split the string using comma as the separator and convert them to
        a list of numbers
    - call your sort function, either bubble sort or insertion sort
    - create a string of the sorted numbers and store it in array_str
    """
    # The following line get the value of the text input called "numbers"
    # 1, 4, 23, 23, 2242, 2, 44
    value = document.getElementsByName("numbers")[0].value
    value = value.strip()

    # Throw alert and stop if nothing in the text input
    if value == "":
        window.alert("Your textbox is empty")
        return

    # Your code should start from here
    # store the final string to the variable array_str
    raw_data = value.strip().split(',')
    unsorted_array = [int(x) for x in raw_data]
    sorted_array = bubble_sort(unsorted_array)
    array_str = ','.join(sorted_array)

    document.getElementById("sorted").innerHTML = array_str
