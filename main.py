def filter_custom(l, f):
    '''Filter a list using a function

    Return a new list that contains all the elements e of l 
    for which f(e) is True

    :param l: a list
    :param f: a function that takes one argument and returns either
        True of False
    '''
    new_list =[]
    for e in l:
        if f(e): 
           new_list.append(e)
    return new_list 
   

def map_custom(l, f):
    '''Map a list using a function

    Return a new list that applies f(e) for every element in e in l

    :param l: a list
    :param f: a function that takes one argument and returns a value
    '''
    new_list =[]
    for e in l:
        new_list.append(f(e))
    return new_list

def reduce_custom(l, f, starting_value):
    '''Reduce a list using a reducer function and a starting value

    Return a single value that applies f(v, e) for every 
    e in l from left to right. The initial vale for v 
    should be starting_value, and subsequent values should 
    be the previously calculated value from f(v, e)

    :param l: a list
    :param f: a function that takes one argument and returns a value
    :param starting_value: the beginning value for the reducer function 
        computation
    '''
    v = starting_value
    for e in l: 
        v = f(v,e)
    return v
     

if __name__ == '__main__':
    l = [7,8,9]
    f = lambda x: x *10
    print(map_custom(l, f))

if __name__ == '__main__':
   # Take a list, add 10 to each item, remove items that are 
   # divisib;e by 7, and sum the results
    my_list = [i for i in range(200)]
    sum_results = reduce_custom(
        filter_custom(
            map_custom(my_list, lambda x: x + 10).
            lambda x: not x % 7 == 0
        ), lambda x, y: x + y, 0
    )
    print(sum_result) 
