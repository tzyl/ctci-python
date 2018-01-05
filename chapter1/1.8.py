def is_rotation(s1, s2):
    """Returns True if s2 is a rotation of s1 using only one call to
    isSubstring (in)."""
    if len(s1) != len(s2):
        return False
    return s2 in s1 * 2

print is_rotation("waterbottle", "erbottlewat")
