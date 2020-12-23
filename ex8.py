formatter = "{} {} {} {}"

print(formatter.format(1, 2, 3, 4)) # 1 2 3 4
# one two three four
print(formatter.format("one", "two", "three", "four"))
# True False False True
print(formatter.format(True, False, False, True))
# {} {} {} {} {} {} {} {} {} {} {} {} {} {} {} {}
print(formatter.format(formatter, formatter, formatter, formatter))
# Try your Own text here Maybe a poem Or a song about fear
print(formatter.format(
    "Try your",
    "Own text here",
    "Maybe a poem",
    "Or a song about fear"
))
