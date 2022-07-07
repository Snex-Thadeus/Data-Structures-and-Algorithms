import unittest

'''Write a function:
def solution(A)
that, given an array A of N integers, returns the smallest positive integer (greater than 0) that does not occur in A.
For example, given A = [1, 3, 6, 4, 1, 2], the function should return 5.
Given A = [1, 2, 3], the function should return 4.
Given A = [−1, −3], the function should return 1.
Write an efficient algorithm for the following assumptions:
* N is an integer within the range [1..100,000];
* each element of array A is an integer within the range [−1,000,000..1,000,000].
'''


def solution_a(A):
    # If max value in A is negative, just return 1.
    if max(A) <= 0:
        return 1

    # Make the sorted list with positive integer numbers only.
    A.sort()
    sorted_positive_list = [x for x in A if x > 0]

    # Find the list of pair of integer with the difference between two numbers are bigger than 2.
    for i in range(len(sorted_positive_list) - 1):
        diff = sorted_positive_list[i + 1] - sorted_positive_list[i]
        if diff >= 2:
            # Assume the pair is (A, B) and there is the gap, then return A+1
            return sorted_positive_list[i] + 1
    # If no element of this list of pair, just return max(sorted numbers) + 1
    return max(sorted_positive_list) + 1


class TestSolutionA(unittest.TestCase):

    # Use code to generate random integer list.
    # random.sample(range(-1000000, 1000000), 10)

    def test_case0(self):
        input_list = [1, 3, 6, 4, 1, 2]
        val = solution_a(input_list)
        self.assertEqual(val, 5)

    def test_case1(self):
        input_list = [1, 2, 3]
        val = solution_a(input_list)
        self.assertEqual(val, 4)

    def test_case2(self):
        input_list = [-1, -3]
        val = solution_a(input_list)
        self.assertEqual(val, 1)

    def test_case3(self):
        input_list = [100000, 500, 10]
        val = solution_a(input_list)
        self.assertEqual(val, 11)

    def test_case4(self):
        input_list = [-5, -10, -2, 0]
        val = solution_a(input_list)
        self.assertEqual(val, 1)

    def test_case5(self):
        input_list = [-5, -10, -2, 0]
        val = solution_a(input_list)
        self.assertEqual(val, 1)

    def test_case6(self):
        input_list = [-266959, -559850, 667410, -370471, -695927, 170911, 658702, -737673, 370182, -285767]
        val = solution_a(input_list)
        self.assertEqual(val, 170912)

    def test_case7(self):
        input_list = [860108, 591722, -969778, -439377, -511718, \
                      -207087, -457298, 908118, 311622, 519103, -975605, -157567, \
                      -318617, -634176, 264219, -82032, -277682, -364746, -788141, \
                      584287]
        val = solution_a(input_list)
        self.assertEqual(val, 264220)


if __name__ == '__main__':
    unittest.main()


def solution(A):
    # write your code in Python 3.6
    n = max(A)
    if n <= 0:
        return 1
    possible = set(e for e in range(1, n+2)) - set(A)
    return min(possible)


def solution1(A):
    B = [x for x in A if x > 0]
    B = sorted(B)
    if 1 not in B:
        return 1
    for i in range(0, len(B) - 1):
        if B[i+1] - B[i] > 1:
            return B[i] + 1
    return max(B) + 1