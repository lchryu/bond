
def longest_word(s: str):
    words = s.split()
    longest = max(words, key=len)
    return longest

s = input()
print(longest_word(s))

