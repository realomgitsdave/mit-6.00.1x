#s = 'azcbobobegghakl' example str
#s = input('Enter a string: ') testing done
#Longest substring in alphabetical order is: beggh example answer
'''
Iterate through the string s
If next letter is greater then it is an alphabetical sequence
Iterate until next letter is lesser
We need a rotating "best match" string
We need a test string
highest wins
first index wins
Let's do this
'''

bestStr = s[0]
testStr = s[0]

for i in range(1, len(s)):
    if s[i] >= s[i-1]:
        testStr = testStr + s[i]
    else:
        testStr = s[i]
    if len(testStr) > len(bestStr):
        bestStr = testStr
        #The bestStr is the testStr?

print ('Longest substring in alphabetical order is: ' + bestStr)