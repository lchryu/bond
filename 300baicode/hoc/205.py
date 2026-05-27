def longest_word(s: str):
    words = s.split()
    longest = min(words, key=len)
    return longest

s = input()
print(longest_word(s))

