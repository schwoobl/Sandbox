values = [True, False, 1, 0, -3, "", "Python", [], [1], None, bool]

for value in values:
    if value:
        print(f"{value!r:10} -> truthy")
    else:
        print(f"{value!r:10} -> falsy")