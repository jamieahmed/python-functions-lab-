# step one 
def sum_to(num):
  sum = 0
  for n in range(1, num + 1):
    sum += n
  return print(sum)



# step two
def largest(nums):
  largest = 0
  for num in nums:
    if num > largest:
      largest = num
  return print(largest)
  
def largest(nums):
  nums.sort()
  return print(nums[-1])


# step three
def occurances(string, substr):
  stripped_string = string.replace(substr, '')
  return (len(string) - len(stripped_string)) // len(substr)
def occurances(string, substr):
  return print(string.count(substr))


# step four
def product(*args):
  product = 1
  for arg in args:
    product *= arg
  return print(product)
