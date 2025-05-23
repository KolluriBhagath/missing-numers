nums=list(map(int,input().split(" ")))
missing_number=sum(range(len(nums)+1)) - sum(nums)
print("missing number is:",missing_number)

