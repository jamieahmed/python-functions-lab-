# step one 

def sum_to(num):
  sum = 0
  for n in range(1, num + 1):
    sum += n
  return sum

# step two
def largest(nums):
  largest = 0
  for num in nums:
    if num > largest:
      largest = num
  return largest
  
# Sort the list approach
def largest(nums):
  nums.sort()
  return nums[-1]
# step three
def occurances(string, substr):
  # remove each occuance of substr
  stripped_string = string.replace(substr, '')
  # compute based on length of the strings
  return (len(string) - len(stripped_string)) // len(substr)
	
# Python actually has a method to solve this too!
def occurances(string, substr):
  return string.count(substr)
# step four
def product(*args):
  product = 1
  for arg in args:
    product *= arg
  return product
