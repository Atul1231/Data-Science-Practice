import numpy as np
#printing array is more efficient than printing list
print_array=np.array([1,2,3,4,5,6])
print(print_array)

#creating a 2D array
print_2d_array=np.array([[1,2,3],[4,5,6],[7,8,9]])
print(print_2d_array)

#creating a 3D array
print_3d_array=np.array([[[1,2,3],[4,5, 6]],[[7,8,9],[10,11,12]]])
print(print_3d_array)

#creating an array of zeros(shape)
print_zeros=np.zeros((3,4)) 
print(print_zeros)

#creating an array of ones ones(shape)
print_ones=np.ones((3,4))
print(print_ones)

#sorting an array
print_sort=np.array([3,1,2,5,4])
print(np.sort(print_sort))

#full array   full(shape,value)
filled_array=np.full((2,3),7)  # 2 rows, 3 columns, filled with 7
print(filled_array)

#arange function
#arange(start, stop, step)

arrange_array=np.arange(0,10,2)  # start=0, stop=10, step=2
print(arrange_array)

#identity matrix        
#eye(shape)
identity_matrix=np.eye(3)  # 3x3 identity matrix
print(identity_matrix)


#attributes of an array
#-------------------------------------------------------------------######
#array.shape
#array.size
#array.ndim

####-------------------------------------------------------------------######
#shape of an array
#array.shape
shpe_array=np.array([[1,2,4]])
print(shpe_array.shape) #returns the shape of an above array that is (1,3) 1 row and 3 columns

#size of an array
#array.size
size_array=np.array([[1,2,4]])
print(size_array.size)  # returns the size or we can say the number of elements of the array that is 3

#ndimensions of an array
#array.ndim
ndim_array1=np.array([1,2,3])
ndim_array2=np.array([[1,2,4]])
ndim_array3=np.array([[[1,2,3],[4,5,6]]])
print(ndim_array1.ndim)  # returns the number of dimensions of the array that is 1D array so it returns 1
print(ndim_array2.ndim)  # returns the number of dimensions of the array that is 2D array so it returns 2
print(ndim_array3.ndim)  # returns the number of dimensions of the array that is 3D array so it returns 3

#dtype of an array
#array.dtype

dtype_array=np.array([1,2,3.4,5,3])
print(dtype_array.dtype) # returns the data type of the array that is float64 because it contains float values

#astype function
#array.astype(dtype)
astype_array=np.array([1,2,3,4,5])
print(astype_array.astype(float))  # converts the array to float type

#mathematical operations on arrays
#-------------------------------------------------------------------######
#addition
add_array1 = np.array([1, 2, 3])
add_array2 = np.array([4, 5, 6])
print("addition:",add_array1 + add_array2)

add_ones =np.ones((1,3))
#in the above if i want it to be the int i can use dtype int
# add_ones = np.ones((1, 3), dtype=int)
print("addition with ones:",add_array1 + add_ones)

#aggregation functions means when i need to summarize the data
#sum
#mean
#min
#max
#std
#var

sum_array=np.array([12,3,5])
print("sum: ",np.sum(sum_array))
print("min: ",np.min(sum_array))
print("mean: ",np.mean(sum_array))
print("max: ",np.max(sum_array))
print("standard deviation: ",np.std(sum_array))
print("variance: ",np.var(sum_array))

#indexing and slicing


#fancy indexing : selecting multiple elements at once

#indexing and slicing 
arr=np.array([10,20,30,40,50])
print(arr[0])
print(arr[-1])  #prints the last element 
print(arr[1:5])
print(arr[::2])
print(arr[::-1])  #this will reverse the array

#boolean masking : filtering data based on a condition
#useful in filtering data based on a condition
#for example, if you want to filter elements greater than a certain value
array=np.array([1, 2, 3, 4, 5, 6])
print(array[array > 3])  # prints elements greater than 3


#reshaping and manipulation 
#reshaping does not make a copy of the data, it just changes the view of the data
#reshaping an array change the shape of an array without changing its data
array = np.array([1, 2, 3, 4, 5, 6])
reshaped_array = array.reshape((2, 3))  # reshaping to 2 rows and 3 columns
print("reshaped array:\n", reshaped_array)

#flattening an array
#flattening an array converts a multi-dimensional array to a 1D array
array_2d = np.array([[1, 2, 3], [4, 5, 6]])
print(array_2d.flatten()) # flatten() returns a copy of the original array, so modifying it won't affect the original array
print(array_2d.ravel())  # ravel() returns a flattened array, but it may return a view of the original array hence affect the original array if modified


#modifying an array
#inserting an element
#insert(array, index, value, axis=None)
#if axis is None, it will flatten the array and insert the value at the specified index
#if axis is specified, it will insert the value along the specified axis
#axis=0 means inserting along the rows
#axis=1 means inserting along the columns

insert_array = np.array([1, 2, 3])
inserted_array = np.insert(insert_array, 1, 4 , axis=None)  # inserting along the rows
print("inserted array:\n", inserted_array)

insert_array2d = np.array([[1, 2], [3, 4]])
inserted_array2d = np.insert(insert_array2d, 1, [5, 6], axis=0)  # inserting along the rows
print("inserted 2D array:\n", inserted_array2d)

inserted_array2d = np.insert(insert_array2d, 1, [7, 8], axis=1)  # inserting along the columns
print("inserted 2D array:\n", inserted_array2d)

#appending an element
#adding an element to the end of an array
#append(array, value, axis=None)
appended_array = np.append(insert_array, 4,axis=None)  # appending to the end of the array
print("appended array:\n", appended_array)

#concatenating arrays
#concatenate((array1, array2), axis=0)
concatenated_array = np.concatenate((insert_array, appended_array), axis=None)  # concatenating two arrays
print("concatenated array:\n", concatenated_array)
#axis =0 means concatenating along the rows (vertical stacking)
#axis =1 means concatenating along the columns (horizontal stacking)

#removing an element
#delete(array, index, axis=None)
deleted_array = np.delete(inserted_array, 1, axis=None)  # deleting the element at index 1
print("deleted array:\n", deleted_array)

#stacking arrays
#stacking arrays means combining multiple arrays into a single array
#vstack() : vertical stacking
#hstack() : horizontal stacking
arr1=np.array([1, 2, 3, 4])
arr2=np.array([5, 6, 7, 8])
print("vertical stacking:\n", np.vstack((arr1, arr2)))  # vertical stacking
print("horizontal stacking:\n", np.hstack((arr1, arr2)))  # horizontal stacking

#splitting arrays
#splitting arrays means dividing an array into multiple sub-arrays
#split(array, indices_or_sections, axis=0)
#hsplit() : horizontal splitting
#vsplit() : vertical splitting

split_array = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print("split array:\n", np.split(split_array, 3))  # splitting into 3 sub-arrays along the rows
print("horizontal split:\n", np.hsplit(split_array, 3))  # horizontal splitting into 3 sub-arrays
print("vertical split:\n", np.vsplit(split_array, 3))  # vertical splitting into 3 sub-arrays

#broadcasting
#broadcasting is a powerful mechanism that allows numpy to work with arrays of different shapes during arithmetic
#operations
prices = np.array([100, 200, 300])
discount=10
final_prices=prices-(prices * discount / 100)  # applying a discount of 10% to each price
print("final prices after discount:\n", final_prices)
#in broadcasting if size are not compatible numpy will throw an error
#for example, if you try to add a 1D array to a 2D array with incompatible shapes, it will raise an error

#vectorization
#vectorization is the process of converting operations that use loops into operations that use numpy's built-in functions 

array1 = np.array([1, 2, 3, 4, 5])
array2 = np.array([6, 7, 8, 9, 10])
#using vectorized operations instead of loops
result = array1 + array2  # adding two arrays element-wise
print("vectorized result:\n", result)

#handling missing values
#numpy uses np.nan to represent missing values
array_with_nan = np.array([1, 2, np.nan, 4, 5])
#checking for missing values
print("missing values in array:", np.isnan(array_with_nan))  # returns a boolean array indicating missing values
#filling missing values
filled_array_with_nan = np.nan_to_num(array_with_nan, nan=0)  # filling missing values with 0
print("filled array with nan:\n", filled_array_with_nan)  # filling missing values with 0

#infinite values
#numpy uses np.inf to represent infinite values
array_with_inf = np.array([1, 2 , np.inf , -np.inf, 4, 5])
#checking for infinite values   
print("infinite values in array:", np.isinf(array_with_inf))  # returns a boolean array indicating infinite values
#filling infinite values
filled_array_with_inf = np.nan_to_num(array_with_inf, posinf=10, neginf=20)  # filling infinite values with 0
print("filled array with inf:\n", filled_array_with_inf)  # filling infinite values with 0
