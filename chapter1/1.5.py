def basic_string_compression(s):
    if not s:
        return s
    saved = 0
    compressed = []
    count = 0
    start = s[0]
    for i, c in enumerate(s):
        if c == start:
            count += 1
        if i == len(s) - 1 or c != start:
            compressed.append(start + str(count))
            saved += count - 2
            count = 1
            start = c
    return "".join(compressed) if saved > 0 else s

print basic_string_compression("aaabbcdddddefff")
print basic_string_compression("")
