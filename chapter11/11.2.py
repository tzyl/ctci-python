# Write a method to sort an array of strings so that all the anagrams are
# next to each other.
from collections import defaultdict


def sort_anagarams(strings):
    anagrams = defaultdict(list)
    for s in strings:
        anagrams["".join(sorted(s))].append(s)
    i = 0
    for group in anagrams.values():
        for s in group:
            strings[i] = s
            i += 1

if __name__ == '__main__':
    strings = ["abc", "ent", "cba", "etn", "bac", "ten"]
    print strings
    sort_anagarams(strings)
    print strings
