import random

random_list = [random.randint(15, 100) for x in range(1, 100)]

# empty_dict = {1:[], 2: []}
# other_empty = {1: [], 2: []}
# not_empty_dict = {1: [1,2,3], 2: []}

# print(empty_dict == not_empty_dict)
# print(empty_dict == other_empty)

def sort_list(list_to_sort):
    def for_first_iteration():
        buckets = {'0':[], '1': [], '2': [], '3': [], '4': [], '5': [], '6': [], '7': [], '8': [], '9': []}
        for item in list_to_sort:
            string_nummer = str(item)
            buckets[string_nummer[-1]].append(string_nummer)
        del random_list[:]
        for bucket in buckets:
            numbers_to_sort = buckets[bucket]
            for element in numbers_to_sort:
                list_to_sort.append(element)
        return list_to_sort
    

    def second_to_n_iteration():
        buckets = {'0':[], '1': [], '2': [], '3': [], '4': [], '5': [], '6': [], '7': [], '8': [], '9': []}
        eenheid = 1
        counter_list_to_sort_loc = 0
        while True:
            for item in list_to_sort:
                if len(item) > eenheid:
                    buckets[item[-1 - eenheid]].append(item)
                    del list_to_sort[counter_list_to_sort_loc]
                    counter_list_to_sort_loc += 1
            
            if buckets == {'0':[], '1': [], '2': [], '3': [], '4': [], '5': [], '6': [], '7': [], '8': [], '9': []}:
                break

            for bucket in buckets:
                numbers_to_sort = buckets[bucket]
                for element in numbers_to_sort:
                    list_to_sort.append(element)
            eenheid += 1
            buckets = {'0':[], '1': [], '2': [], '3': [], '4': [], '5': [], '6': [], '7': [], '8': [], '9': []}
        
        return list_to_sort
    
    
    list_to_sort = for_first_iteration()
    list_to_sort = second_to_n_iteration()

    return list_to_sort

print(sort_list(random_list))
            

    

    


