marks=[88,72,95,61,79]

#Access O(1)
print(marks[0])
print(marks[2])


#add to the end, append O(1)
marks.append(100)
print(marks)

#add on specific location, insert O(n)
marks.insert(2,69)
print(marks)

#remove last element,pop O(1)
marks.pop()
print(marks)

#remove specific num,remove
marks.remove(69)
print(marks)