def selection_sort(x):
	for to_fill in range(len(x)):
		min_pos = to_fill
		for step in range(to_fill,len(x)):
			if x[step] < x[min_pos]:
				min_pos = step
		x[to_fill],x[min_pos]=x[min_pos],x[to_fill]
	return x 

def bubble_sort(x):
	if (len(x))>1:
		for bottom in range(1,len(x)):
			bubble = bottom
			while bubble > 0 and x[bubble] <x[bubble-1]:
				x[bubble] ,x[bubble-1] = x[bubble-1],x[bubble]
				bubble-=1
	return x

def quicksort(x):
	if len(x) > 3:
		pivot  = x[int(len(x)/2)]
		small  = [x[n] for n in range(len(x)) if x[n] < pivot ]
		medium = [x[n] for n in range(len(x)) if x[n] == pivot ]
		large  = [x[n] for n in range(len(x)) if x[n] > pivot ]
		return quicksort(small) + medium + quicksort(large)
	else:
		return x
