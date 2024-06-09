def reverse_string(s, ei):
    if ei < 0:
        return
    print(s[ei], end = "")
    reverse_string(s, ei - 1)

s = "Coding Ninjas"
reverse_string(s, len(s) - 1)
