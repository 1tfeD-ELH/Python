count = 0
while count < 10:
    count += 1
    if count < 4:
        continue
    if count == 8:
        break
print(count)