is_correct=False
low=0
high=100

while not is_correct and low <= high:
    mid = (low + high) // 2
    answer= input(f"is it {mid} ?")
    if answer=="YES":
        print("i win")
        is_correct=True
    else:
        if answer=="UP":
            low = mid
        else:
            high=mid


