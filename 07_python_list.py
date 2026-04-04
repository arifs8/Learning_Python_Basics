test_score = [80, 90, 70, 60, 50]

print(test_score)
print(test_score[1])
print(test_score[2])
print(test_score[3])
print(test_score[4])


print("XXXXXXXXXXXXXXXXXXXXXXXX")


test_resukt = ["pass", "pass", "fail", "pass", "fail"]

print(test_resukt)
print(test_resukt[0])
print(test_resukt[1])
print(test_resukt[2])
print(test_resukt[3])
print(test_resukt[4])


print("XXXXXXXXXXXXXXXXXXXXXXXX")

test_fruits = ["apple", "banana", "cherry", "date", "fig"]

print(test_fruits)
print(test_fruits[0])
print(test_fruits[1])
print(test_fruits[2])
print(test_fruits[3])
print(test_fruits[4])

print("XXXXXXXXXXXXXXXXXXXXXXXX")

test_mixlist = ["apple", 1, True, 3.14, None]

print(test_mixlist)
print(test_mixlist[0])
print(test_mixlist[1])
print(test_mixlist[2])
print(test_mixlist[3])
print(test_mixlist[4])

print("XXXXXXXXXXXXXXXXXXXXXXXX")

#List Functions
print(test_score)

#Append object to the end of the list.
test_score.append(100)
print(test_score)

#Insert object before index.
test_score.insert(1, 95)
print(test_score)

#Remove object from the list.
test_score.remove(70)
print(test_score)

#Remove object from the list by index.
test_score.pop()
print(test_score)

#Remove and return item at index (default last).
test_score.pop(1)
print(test_score)

#Sort the list in ascending order and return None
test_score.sort()
print(test_score)

##Sort the list in descending order and return None
test_score.reverse()
print(test_score)

#Return number of occurrences of value.
test_score.count(90)
print(test_score)

#Return first index of value.
test_score.index(90)
print(test_score)

#Return a shallow copy of the list.
test_score.copy()
print(test_score)

##Remove all items from the list.
test_score.clear()
print(test_score)