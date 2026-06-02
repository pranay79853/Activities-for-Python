import array as arr
# Create a array

array_1 = [1, 3, 5, 3, 7, 9, 3]
# Then find the number of occurance of number 3

array_num = arr.array('i', [1, 3, 5, 3, 7, 9, 3])
print("Original array: "+str(array_num))
print("Number of occurrences of the number 3 in the said array: "+str(array_num.count(3)))
array_num.reverse()
print("Reverse the order of the items:")
print(str(array_num))