# LeetCode

TWO_SUMS.PY
	O(n) time complexity
	Create Dict and add all indexes of nums and retrieve only two nums whose total sum is equal to target.


REVERSE_INT.PY
    O(n) time complexity
    Standard reverse integer method or convert to string and [::-1] * (-1 or 1)

 	
IS_PALINDROME.PY
    Standard reverse integer method or convert to string and [::-1]


ROMAN_TO_INT.PY
    Store all the Roman values to the dict.
    Compare with next values when it is greater subtract the current value


longestCommonPrefix.PY
    store the first index of string to array
    compare with the rest list of strings
    maintain count and to get the minimum splicing from the original array


VALID_PARANTHESES.PY
    create empty stack
    create list with all open parentheses
    create dict for resp. closed paranthese
    if open paratheses push into the stack
    if closed paranthese check stack fornt has resp. open parantheses else false
    if stack empty true else false


MergeTwoSortedLists.py
    while l1 or l2: check for all conditions
    create new listnode and append the sorted values into it
    return list node


removeDuplicates.py
    check for current and next value in list if same del nums[i + 1] else i = i + 1