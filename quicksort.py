import time
import numpy

def quick_sort(listToSort):
    """Sort the array with the quick sort method"""
    if len(listToSort) in [0,1]:
        return listToSort
    else:    
        pivot = listToSort[0]
        great, small = partition(listToSort[1:], pivot)
        
        # recurse on the arrays with the pivot in between
        return quick_sort(small) + [pivot] + quick_sort(great)
        

def partition(listToPartition, pivot):
    """Splits the array in values greater than and smaller than the pivot"""
    greater = []
    smaller = []
    
    for x in listToPartition:
        if x >= pivot:
            greater.append(x)
        else:
            smaller.append(x)
        
    return greater, smaller

def personal_timer(sort_algorime,list_of_list_to_sort):
   list_with_times = []
   for current_list in list_of_list_to_sort:
      start = time.perf_counter()
      sort_algorime(current_list)
      end = time.perf_counter()
      list_with_times.append(f"{end - start :0.4f}")

   return list_with_times

print(quick_sort(numpy.random.randint(low=0, high=100, size=100)))

random_duizend        = numpy.random.rand(1000)
random_tienduizend    = numpy.random.rand(10000)
random_dertigduizend  = numpy.random.rand(30000)

list_of_list = [random_duizend,random_tienduizend,random_dertigduizend]
times_list = personal_timer(quick_sort,list_of_list)
print("Sorted 1000 in {} seconds \nSorted 10000 in {} seconds\nSorted 3000 in {} seconds".format(times_list[0],times_list[1],times_list[2]))