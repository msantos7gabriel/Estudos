def longest(a1, a2):
    return ''.join(sorted(set((a1+a2))))


a1, a2 = "aretheyhere", "yestheyarehere"
print(longest(a1, a2))
