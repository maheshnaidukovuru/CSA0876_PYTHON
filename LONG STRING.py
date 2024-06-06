s = "abcabcbb"
start = max_length = 0
used_chars = {}
i = 0
while i < len(s):
    char = s[i]
    if char in used_chars and start <= used_chars[char]:
        start = used_chars[char] + 1
    else:
        max_length = max(max_length, i - start + 1)
    used_chars[char] = i
    i += 1
print(max_length)