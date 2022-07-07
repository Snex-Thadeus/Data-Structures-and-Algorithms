# QUESTION 1: Alice has some cards with numbers written on them. She arranges the cards in decreasing order, and lays them
# out face down in a sequence on a table. She challenges Bob to pick out the card containing a given number by turning over
# as few cards as possible. Write a function to help Bob locate the card.
# LINEAR & BINARY SEARCH
# Here's a systematic strategy we'll apply for solving problems:
#
# 1.State the problem clearly. Identify the input & output formats.

# In this case, for instance, we can represent the sequence of cards as a list of numbers. Turning over a specific card is
# equivalent to accessing the value of the number at the corresponding position the list.
#
#
# The problem can now be stated as follows:
# We need to write a program to find the position of a given number in a list of numbers arranged in decreasing order. We
# also need to minimize the number of times we access elements from the list.

# 2.Come up with some example inputs & outputs. Try to cover all edge cases.
# Before we start implementing our function, it would be useful to come up with some example inputs and outputs which we
# can use later to test out problem. We'll refer to them as test cases.
#
# Here's the test case described in the example above.
#
# cards = [13, 11, 10, 7, 4, 3, 1, 0]
# query = 7
# output = 3
# We can test our function by passing the inputs into function and comparing the result with the expected output.
#
# result = locate_card(cards, query)
# print(result)
# None
# result == output
# False
# Obviously, the two result does not match the output as we have not yet implemented the function.
#
# We'll represent our test cases as dictionaries to make it easier to test them once we write implement our function.' \
#   ' For example, the above test case can be represented as follows:
#
test = {
    'input': {
        'cards': [13, 11, 10, 7, 4, 3, 1, 0],
        'query': 7
    },
    'output': 3
}
# The function can now be tested as follows.
#
# locate_card(**test['input']) == test['output']
# False
# Our function should be able to handle any set of valid inputs we pass into it. Here's a list of some possible variations we might encounter:
#
# The number query occurs somewhere in the middle of the list cards.
# query is the first element in cards.
# query is the last element in cards.
# The list cards contains just one element, which is query.
# The list cards does not contain number query.
# The list cards is empty.
# The list cards contains repeating numbers.
# The number query occurs at more than one position in cards.
# (can you think of any more variations?)
# Edge Cases: It's likely that you didn't think of all of the above cases when you read the problem for the first time.
# Some of these (like the empty array or query not occurring in cards) are called edge cases, as they represent rare or extreme examples.

# While edge cases may not occur frequently, your programs should be able to handle all edge cases, otherwise they may fail in unexpected ways.
# Let's create some more test cases for the variations listed above. We'll store all our test cases in an list for easier testing.

tests = []
# query occurs in the middle
tests.append(test)

tests.append({
    'input': {
        'cards': [13, 11, 10, 7, 4, 3, 1, 0],
        'query': 1
    },
    'output': 6
})
# query is the first element
tests.append({
    'input': {
        'cards': [4, 2, 1, -1],
        'query': 4
    },
    'output': 0
})
# query is the last element
tests.append({
    'input': {
        'cards': [3, -1, -9, -127],
        'query': -127
    },
    'output': 3
})
# cards contains just one element, query
tests.append({
    'input': {
        'cards': [6],
        'query': 6
    },
    'output': 0
})

# The problem statement does not specify what to do if the list cards does not contain the number query.
#
# Read the problem statement again, carefully.
# Look through the examples provided with the problem.
# Ask the interviewer/platform for a clarification.
# Make a reasonable assumption, state it and move forward.
# We will assume that our function will return -1 in case cards does not contain query.

# cards does not contain query
tests.append({
    'input': {
        'cards': [9, 7, 5, 2, -9],
        'query': 4
    },
    'output': -1
})
# cards is empty
tests.append({
    'input': {
        'cards': [],
        'query': 7
    },
    'output': -1
})
# numbers can repeat in cards
tests.append({
    'input': {
        'cards': [8, 8, 6, 6, 6, 6, 6, 3, 2, 2, 2, 0, 0, 0],
        'query': 3
    },
    'output': 7
})
# In the case where query occurs multiple times in cards, we'll expect our function to return the first occurrence of query.

# While it may also be acceptable for the function to return any position where query occurs within the list, it would be
# slightly more difficult to test the function, as the output is non-deterministic.

# query occurs multiple times
tests.append({
    'input': {
        'cards': [8, 8, 6, 6, 6, 6, 6, 6, 3, 2, 2, 2, 0, 0, 0],
        'query': 6
    },
    'output': 2
})

# 3.Come up with a correct solution for the problem. State it in plain English.

### 3. Come up with a correct solution for the problem. State it in plain English.

# Our first goal should always be to come up with a _correct_ solution to the problem, which may necessarily be the most _efficient_ solution.
# The simplest or most obvious solution to a problem, which generally involves checking all possible answers is called the _brute force_ solution.
#
# In this problem, coming up with a correct solution is quite easy: Bob can simply turn over cards in order one by one,
# till he find a card with the given number on it. Here's how we might implement it:
#
# 1. Create a variable `position` with the value 0.
# 3. Check whether the number at index `position` in `card` equals `query`.
# 4. If it does, `position` is the answer and can be returned from the function
# 5. If not, increment the value of `position` by 1, and repeat steps 2 to 5 till we reach the last position.
# 6. If the number was not found, return `-1`.
#
# Linear Search Algorithm**: Congratulations, we've just written our first _algorithm_! An algorithm is simply a list of ' \
# 'statements which can be converted into code and executed by a computer on different sets of inputs. This particular algorithm' \
# ' is called linear search, since it involves searching through a list in a linear fashion i.e. element after element.
#
#
# **Tip:** Always try to express (speak or write) the algorithm in your own words before you start coding. It can be as
# brief or detailed as you require it to be. Writing is a great tool for thinking clearly. It's likely that you will find' \
#         ' some parts of the solution difficult to express, which suggests that you are probably unable to think about it clearly. ' \
#         'The more clearly you are able to express your thoughts, the easier it will be for you to turn into code.

# 4.Implement the solution and test it using example inputs. Fix bugs, if any.
### 4. Implement the solution and test it using example inputs. Fix bugs, if any.
# Phew! We are finally ready to implement our solution. All the work we've done so far will definitely come in handy, as' \
# ' we now exactly what we want our function to do, and we have an easy way of testing it on a variety of inputs.
#
# Here's a first attempt at implementing the function.

def locate_card(cards, query):
    # Create a variable position with the value 0
    position = 0

    # Set up a loop for repetition
    while True:

        # Check if element at the current position matche the query
        if cards[position] == query:
            # Answer found! Return and exit..
            return position

        # Increment the position
        position += 1

        # Check if we have reached the end of the array
        if position == len(cards):
            # Number not found, return -1
            return -1

# *******************************To solve test case 6******************************************************
def locatee_card(cards, query):
    position = 0
    while position < len(cards):
        if cards[position] == query:
            return position
        position += 1
    return -1
# 5.Analyze the algorithm's complexity and identify inefficiencies, if any.

### 5. Analyze the algorithm's complexity and identify inefficiencies, if any.

    # Recall this statement from  original question: _"Alice challenges Bob to pick out the card containing a given number by" \
    # " **turning over as few cards as possible**."_ We restated this requirement as: _"Minimize the number of times we access elements " \
    #                                                                                  "from the list `cards`"_
    #
    # <img src="https://i.imgur.com/mazym6s.png" width="480">
    #
    # Before we can minimize the number, we need a way to measure it. Since we access a list element once in every iteration,
    # for a list of size `N` we access the elements from the list up to `N` times. Thus, Bob may need to overturn up to `N` cards
    # in the worst case, to find the required card.
    #
    # Suppose he is only allowed to overturn 1 card per minute, it may take him 30 minutes to find the required card if 30 cards
    # are laid out on the table. Is this the best he can do? Is a way for Bob to arrive at the answer by turning over just 5 cards, instead of 30?
    #
    # The field of study concerned with finding the amount of time, space or other resources required to complete the execution
    # of computer programs is called _the analysis of algorithms_. And the process of figuring out the best algorithm to solve a
    # given problem is called _algorithm design and optimization_.
    #
    #
    # ### Complexity and Big O Notation
    #
    # > **Complexity** of an algorithm is a measure of the amount of time and/or space required by an algorithm for an input of
    # a given size e.g. `N`. Unless otherwise stated, the term _complexity_ always refers to the worst-case complexity (i.e. the
    # highest possible time/space taken by the program/algorithm to process an input).
    #
    # In the case of linear search:

    # 1. The _time complexity_ of the algorithm is `cN` for some fixed constant `c` that depends on the number of operations we
    # perform in each iteration and the time taken to execute a statement. Time complexity is sometimes also called the _running
    # time_ of the algorithm.
    #
    # 2. The _space complexity_ is some constant `c'` (independent of `N`), since we just need a single variable `position` to' \
    #                                             c' iterate through the array, and it occupies a constant space in the computer's memory (RAM).
    #
    #
    # > **Big O Notation**: Worst-case complexity is often expressed using the Big O notation. In the Big O, we drop fixed
    # constants and lower powers of variables to capture the trend of relationship between the size of the input and the complexity of
    # the algorithm i.e. if the complexity of the algorithm is `cN^3 + dN^2 + eN + f`, in the Big O notation it is expressed as **O(N^3)**
    #
    # Thus, the time complexity of linear search is **O(N)** and its space complexity is **O(1)**.


# 6.Apply the right technique to overcome the inefficiency. Repeat steps 3 to 6.
### 6. Apply the right technique to overcome the inefficiency. Repeat steps 3 to 6.

    # At the moment, we're simply going over cards one by one, and not even utilizing the face that they're sorted. This is called
    # a *brute force* approach.
    #
    # It would be great if Bob could somehow guess the card at the first attempt, but with all the cards turned over
    # it's simply impossible to guess the right card.
    #
    #
    # <img src="https://i.imgur.com/mazym6s.png" width="480">
    #
    # The next best idea would be to pick a random card, and use the fact that the list is sorted, to determine whether the
    # target card lies to the left or right of it. In fact, if we pick the middle card, we can reduce the number of additional
    # cards to be tested to half the size of the list. Then, we can simply repeat the process with each half. This technique is
    # called binary search. Here's a visual explanation of the technique:
    #
    #
    # <img src="https://miro.medium.com/max/494/1*3eOrsoF9idyOp-0Ll9I9PA.png" width="480">

#7. Come up with a correct solution for the problem. State it in plain English
### 7. Come up with a correct solution for the problem. State it in plain English.
    # Here's how binary search can be applied to our problem:
    #
    # 1. Find the middle element of the list.
    # 2. If it matches queried number, return the middle position as the answer.
    # 3. If it is less than the queried number, then search the first half of the list
    # 3. If it is greater than the queried number, then search the second half of the list
    # 4. If no more elements remain, return -1.
# 8. Implement the solution and test it using example inputs. Fix bugs, if any.
#     Here's an implementation of binary search for solving our problem. We also print the relevant variables in each iteration of the while loop.
def locateee_card(cards, query):
    lo, hi = 0, len(cards) - 1 #First and last items in an array

    while lo <= hi:
        mid = (lo + hi) // 2
        mid_number = cards[mid]

        print("lo:", lo, ", hi:", hi, ", mid:", mid, ", mid_number:", mid_number)

        if mid_number == query:
            return mid
        elif mid_number < query:
            hi = mid - 1
        elif mid_number > query:
            lo = mid + 1

    return -1

    # Seems like we did locate a 6 in the array, it's just that it wasn't the first 6. As you can guess, this is because in binary
    # search, we don't go over indices in a linear order.
    #
    # So how do we fix it?
    #
    # When we find that `cards[mid]` is equal to `query`, we need to check whether it is the first occurrence of `query` in the
    # list i.e the number that comes before it.
    #
    # `[8, 8, 6, 6, 6, 6, 6, 6, 3, 2, 2, 2, 0, 0, 0]`
    #
    # To make it easier, we'll define a helper function called `test_location`, which will take the list `cards`, the `query` and `mid` as inputs.


def test_location(cards, query, mid):
    mid_number = cards[mid]
    print("mid:", mid, ", mid_number:", mid_number)
    if mid_number == query:
        if mid - 1 >= 0 and cards[mid - 1] == query:
            return 'left'
        else:
            return 'found'
    elif mid_number < query:
        return 'left'
    else:
        return 'right'


def locate_card(cards, query):
    lo, hi = 0, len(cards) - 1

    while lo <= hi:
        print("lo:", lo, ", hi:", hi)
        mid = (lo + hi) // 2
        result = test_location(cards, query, mid)

        if result == 'found':
            return mid
        elif result == 'left':
            hi = mid - 1
        elif result == 'right':
            lo = mid + 1
    return -1

    # In fact, once we have written out the algorithm, we may want to add a few more test cases:
    #
    # 1. The number lies in first half of the array.
    # 2. The number lies in the second half of the array.
# Here is the final code for the algorithm (without the `print` statements):

def test_location(cards, query, mid):
    if cards[mid] == query:
        if mid-1 >= 0 and cards[mid-1] == query:
            return 'left'
        else:
            return 'found'
    elif cards[mid] < query:
        return 'left'
    else:
        return 'right'

def locate_card(cards, query):
    lo, hi = 0, len(cards) - 1
    while lo <= hi:
        mid = (lo + hi) // 2
        result = test_location(cards, query, mid)
        if result == 'found':
            return mid
        elif result == 'left':
            hi = mid - 1
        elif result == 'right':
            lo = mid + 1
    return -1

## Generic Binary Search

# Here is the general strategy behind binary search, which is applicable to a variety of problems:
#
# 1. Come up with a condition to determine whether the answer lies before, after or at a given position
# 1. Retrieve the midpoint and the middle element of the list.
# 2. If it is the answer, return the middle position as the answer.
# 3. If answer lies before it, repeat the search with the first half of the list
# 4. If the answer lies after it, repeat the search with the second half of the list.
#
# Here is the generic algorithm for binary search, implemented in Python:
def binary_search(lo, hi, condition):
    """TODO - add docs"""
    while lo <= hi:
        mid = (lo + hi) // 2
        result = condition(mid)
        if result == 'found':
            return mid
        elif result == 'left':
            hi = mid - 1
        else:
            lo = mid + 1
    return -1

# The worst-case complexity or running time of binary search is **O(log N)**, provided the complexity of the condition used
# to determine whether the answer lies before, after or at a given position is **O(1)**.
#
# Note that `binary_search` accepts a function `condition` as an argument. Python allows passing functions as arguments to
# other functions, unlike C++ and Java.
#
# We can now rewrite the `locate_card` function more succinctly using the `binary_search` function.
def locate_card(cards, query):
    def condition(mid):
        if cards[mid] == query:
            if mid > 0 and cards[mid - 1] == query:
                return 'left'
            else:
                return 'found'
        elif cards[mid] < query:
            return 'left'
        else:
            return 'right'

    return binary_search(0, len(cards) - 1, condition)

# The `binary_search` function can now be used to solve other problems too. It is a tested piece of logic.
# > **Question**: Given an array of integers nums sorted in ascending order, find the starting and ending position of a given number.
#
# This differs from the problem in only two significant ways:
#
# 1. The numbers are sorted in increasing order.
# 2. We are looking for both the start index and the end index.
#
# Here's the full code for solving the question, obtained by making minor modifications to our previous function:

def first_position(nums, target):
    def condition(mid):
        if nums[mid] == target:
            if mid > 0 and nums[mid-1] == target:
                return 'left'
            return 'found'
        elif nums[mid] < target:
            return 'right'
        else:
            return 'left'
    return binary_search(0, len(nums)-1, condition)

def last_position(nums, target):
    def condition(mid):
        if nums[mid] == target:
            if mid < len(nums)-1 and nums[mid+1] == target:
                return 'right'
            return 'found'
        elif nums[mid] < target:
            return 'right'
        else:
            return 'left'
    return binary_search(0, len(nums)-1, condition)

def first_and_last_position(nums, target):
    return first_position(nums, target), last_position(nums, target)


def findFirstOccurrence(nums, target):
    # Left snd right pointers
    left, right = 0, len(nums) - 1
    # Index of first occurrence
    firstOccurrence = -1
    # Loop until the two pointers meet
    while left <= right:
        # Middle index
        middle = left + (right - left) // 2
        # Check if we have found the value
        if target == nums[middle]:
            firstOccurrence = middle
            right = middle - 1
        # If the target is less than the element
        # at the middle index
        elif target < nums[middle]:
            right = middle - 1
        # If the target is greater than the element
        # at the middle index
        else:
            left = middle + 1
    return firstOccurrence


def findLastOccurrence(nums, target):
    # Left snd right pointers
    left, right = 0, len(nums) - 1
    # Index of first occurrence
    lastOccurrence = -1
    # Loop until the two pointers meet
    while left <= right:
        # Middle index
        middle = left + (right - left) // 2
        # Check if we have found the value
        if target == nums[middle]:
            lastOccurrence = middle
            left = middle + 1
        # If the target is less than the element
        # at the middle index
        elif target < nums[middle]:
            right = middle - 1
        # If the target is greater than the element
        # at the middle index
        else:
            left = middle + 1
    return lastOccurrence


def searchRange(nums, target):
    return [findFirstOccurrence(nums, target), findLastOccurrence(nums, target)]

