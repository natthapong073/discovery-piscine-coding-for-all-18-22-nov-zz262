#!/usr/bin/env python3
original_array = [2, 8, 9, 48, 8, 22, -12, 2]
new_array = []
for x in original_array:
    if x > 5:
        new_array.append(x + 2)
    else:
        pass

print(new_array)