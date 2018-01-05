def replace_spaces(s):
    characters = list(s)
    for i, c in enumerate(characters):
        if c == " ":
            characters[i] = "%20"
    return "".join(characters)

print replace_spaces("Mr John Smith   ")
