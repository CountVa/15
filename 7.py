def check(lst, sub):
   for i in range(0, len(lst)):
       if lst[i:i+len(sub)] == sub:
           return True
   return False

print(check([1,3,2,4,6], [1,2])) # False
print(check([4,5,6,1,2], [1,2])) # True