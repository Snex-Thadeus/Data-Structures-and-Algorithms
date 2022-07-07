# An array A consisting of N integers is given. It contains daily prices of a stock share for a period of N consecutive days.
# If a single share was bought on day P and sold on day Q, where 0 ≤ P ≤ Q < N, then the profit of such transaction is equal
# to A[Q] − A[P], provided that A[Q] ≥ A[P]. Otherwise, the transaction brings loss of A[P] − A[Q].
#
# Write a function,
# def solution(A)
# that, given an array A consisting of N integers containing daily prices of a stock share for a period of N consecutive days,
# returns the maximum possible profit from one transaction during this period. The function should return 0 if it was impossible to gain any profit.
# For example, given array A consisting of six elements such that:
#
#   A[0] = 23171
#   A[1] = 21011
#   A[2] = 21123
#   A[3] = 21366
#   A[4] = 21013
#   A[5] = 21367
# the function should return 356, as explained above.

def solution(A):
  if len(A)==0:
    return 0
  mymin=A[0]
  mymax=0
  s=0 #Sum of the differences

  for i in range(1, len(A)):
    if A[i]<mymin: #Is a new min value
      mymin=A[i]
      s=0
    else:
      s+=(A[i]-A[i-1])
    if mymax<s:
      mymax=s

  return mymax
