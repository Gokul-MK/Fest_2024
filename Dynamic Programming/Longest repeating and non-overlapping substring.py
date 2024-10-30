# Python 3 program to find the longest repeated
# non-overlapping substring

# Returns the longest repeating non-overlapping
# substring in str
def longestRepeatedSubstring(str):

	n = len(str)
	LCSRe = [[0 for x in range(n + 1)] 
				for y in range(n + 1)]

	res = "" # To store result
	res_length = 0 # To store length of result

	# building table in bottom-up manner
	index = 0
	for i in range(1, n + 1):
		for j in range(i + 1, n + 1):
			
			# (j-i) > LCSRe[i-1][j-1] to remove
			# overlapping
			if (str[i - 1] == str[j - 1] and
				LCSRe[i - 1][j - 1] < (j - i)):
				LCSRe[i][j] = LCSRe[i - 1][j - 1] + 1

				if (LCSRe[i][j] > res_length):
					res_length = LCSRe[i][j]
					index = max(i, index)
				
			else:
				LCSRe[i][j] = 0


	if (res_length > 0):
		for i in range(index - res_length + 1,
									index + 1):
			res = res + str[i - 1]

	return res

