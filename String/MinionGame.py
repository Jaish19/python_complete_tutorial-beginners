__author__ = 'Sanjay'

# Kevin and Stuart want to play the 'The Minion Game'.
#
# Game Rules
#
# Both players are given the same string, SS.
# Both players have to make substrings using the letters of the string SS.
# Stuart has to make words starting with consonants.
# Kevin has to make words starting with vowels.
# The game ends when both players have made all possible substrings.
#
# Scoring
# A player gets +1 point for each occurrence of the substring in the string SS.
#
# For Example:
# String SS = BANANA
# Kevin's vowel beginning word = ANA
# Here, ANA occurs twice in BANANA. Hence, Kevin will get 2 Points.
#
# For better understanding, see the image below:
#
# banana.png
#
# Your task is to determine the winner of the game and their score.
#
# Input Format
#
# A single line of input containing the string SS.
# Note: The string SS will contain only uppercase letters: [A?Z][A?Z].
#
# Constraints
#
# 0<len(S)?1060<len(S)?106
#
# Output Format
#
# Print one line: the name of the winner and their score separated by a space.
#
# If the game is a draw, print Draw.
#
# Sample Input
#
# BANANA
# Sample Output
#
# Stuart 12

s = input()

vowels = 'AEIOU'

kevsc = 0
stusc = 0
for i in range(len(s)):
    if s[i] in vowels:
        kevsc += (len(s)-i)
    else:
        stusc += (len(s)-i)

if kevsc > stusc:
    print ("Kevin", kevsc)
elif kevsc < stusc:
    print ("Stuart", stusc)
else:
    print ("Draw")