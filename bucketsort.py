import random

def sort_list(list_to_sort):
    def for_first_iteration():
        buckets = {'0':[], '1': [], '2': [], '3': [], '4': [], '5': [], '6': [], '7': [], '8': [], '9': []}
        for item in list_to_sort:
            string_nummer = str(item)
            buckets[string_nummer[-1]].append(string_nummer)
        
        del list_to_sort[:]
        for bucket in buckets:
            numbers_to_sort = buckets[bucket]
            for element in numbers_to_sort:
                list_to_sort.append(element)
        return list_to_sort
    

    def second_to_n_iteration():
        eenheid = 1
        while True:
            buckets = {'0':[], '1': [], '2': [], '3': [], '4': [], '5': [], '6': [], '7': [], '8': [], '9': []}
            index_in_list_to_sort = 0
            while index_in_list_to_sort < len(list_to_sort):
                item = list_to_sort[index_in_list_to_sort]
                if len(item) > eenheid:
                    buckets[item[-1 -eenheid]].append(item)
                    del list_to_sort[index_in_list_to_sort]
                else:
                    index_in_list_to_sort += 1 
                    #Moet alleen als een item niet wordt verwijderd want als dat wel zo is dan wordt de lijst kleiner.
                    #En zit het volgende nummer op de vorige index 

            
            if buckets == {'0':[], '1': [], '2': [], '3': [], '4': [], '5': [], '6': [], '7': [], '8': [], '9': []}:
                break
            
            for bucket in buckets:
                numbers_to_sort = buckets[bucket]
                for element in numbers_to_sort:
                    list_to_sort.append(element)
            eenheid += 1
        
        return list_to_sort
    
    list_to_sort = for_first_iteration()
    list_to_sort = second_to_n_iteration()

    return list_to_sort

random_list = [random.randint(1, 10000) for x in range(1, 1000)]
print(sort_list(random_list))
            

    

    


