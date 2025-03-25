def find_pair_with_sum(arr, target):
    seen = set() # hashset
    for num in arr:
        if target - num in seen:
            print(f"Pair found: ({num}, {target - num})")
            return
        seen.add(num)
    print("No pair found")

arr = [1, 3, 5, 2, 4]
target_sum = 9
find_pair_with_sum(arr, target_sum)
