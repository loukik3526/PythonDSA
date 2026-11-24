def find_name(names, target):
    left = 0
    right = len(names) - 1
    jumps = 0                      # <-- jump counter only to check the jump nothing else

    while left <= right:
        jumps += 1                 # <-- count this jump
        middle = (left + right) // 2
        print(f"Jump {jumps}: checking index {middle} ('{names[middle]}')")

        if names[middle] == target:
            print(f"Found after {jumps} jump(s)")
            return middle
        elif names[middle] < target:
            left = middle + 1  
        else:
            right = middle - 1

    print(f"Not found after {jumps} jump(s)")
    return -1


names = ["Sopan", "Topan", "Zopan", "Opan", "Ghopan"]
names.sort()
target_name = "Zopan"

result = find_name(names, target_name)

if result != -1:
    print("Name found at index", result)
else:
    print("Name not found")