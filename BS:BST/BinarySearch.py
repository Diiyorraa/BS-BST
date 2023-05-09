def linear_search(data, target):
	for i in range(len(data)):
		if data[i] == target:
			return True
	return False

def bin_search_iterative(data, target):
	low = 0
	high = len(data) - 1

	while low <= high:
		mid = (low + high) // 2
		if target == data[mid]:
			return True
		elif target < data[mid]:
			high = mid - 1
		else:
			low = mid + 1
	return False 

# Recursive Binary Search 
def bin_search_recursive(data, target, low, high):
	if low > high:
		return False
	else:
		mid = (low + high) // 2
		if target == data[mid]:
			return True
		elif target < data[mid]:
			return bin_search_recursive(data, target, low, mid-1)
		else:
			return bin_search_recursive(data, target, mid+1, high)


data = [1,3,4,6,7,12,13,16,17,20,21,22,24,28,33,39]
target = 34
print(bin_search_iterative(data, target))
target = 12
print(bin_search_recursive(data, target, 0, len(data)-1))
#find the closet number
def find_cls_num(data, target):
	min_diff= min_diff_right= min_diff_left = float('inf')
	low = 0
	high = len(data)-1
	cl_num = None
	if len(data)== 0:
		return None
	elif len(data)== 1:
		return data[0]

	while low<= high:
		mid = (low+high) //2
		if mid<= len(data) -1:
			min_diff_right = abs(data[mid+1]- target)
		if mid > 0:
			min_diff_left = abs(data[mid-1] - target)

		#checking is the abs val between left and right elements

		if min_diff_left<min_diff:
			min_diff = min_diff_left
			cl_num = data[mid-1]

		if min_diff_right< min_diff:
			min_diff = min_diff_right
			cl_num = data[mid+1]

		if data[mid]< target:
			low = mid +1
		elif data[mid] > target :
			high = mid -1
			if high < 0 :
				return data[mid]
		else:
			return data[mid]
	return cl_num


print(find_cls_num(data, 19))

# find fixed num
def fixed_num_linear(data):
	for i in range(len(data)):
		if data[i] == i :
			return data[i]
	return None
def find_fix_point(data):
	low = 0
	high = len(data) -1
	while low <= high:
		mid = (low+high) // 2

		if data[mid] < mid:
			low = mid+1
		elif data[mid] > mid:
			high = mid -1
		else:
			return data[mid]
	return None
#fixed point is 3
data  = [ -10 , -5 , 0 , 3 , 7]
#fixed point is 4
data1 = [-5,-1,0,2,4, 6, 9]
dat2 = [1,2,5,9,11] # here no fixed point

print("Linear Approach ")
print(data)
print(fixed_num_linear(data))
print(data1)
print(fixed_num_linear(data1))
print(dat2)
print(fixed_num_linear(dat2))

print("Using binary search approach ")
print(data)
print(find_fix_point(data))
print(data1)
print(find_fix_point(data1))
print(dat2)
print(find_fix_point(dat2))
