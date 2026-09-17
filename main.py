def containsDuplicate(nums):
        seen = set()
        for i in nums:
            if i in seen:
                return True
            seen.add(i)
        return False
print(containsDuplicate([1,2,3,4,5]))
print('hello world')
print(123)
print(1234)