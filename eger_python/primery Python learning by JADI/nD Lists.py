### Global List 
my_list=[[20,7],[9,10]]
### Tamrin 1 sum 2D list
def sum_list(my_list):
    s=0
    for list in my_list:
        total=0
        
        for i in range(len(list)):
            total += list[i]
        s+=total
    return s
### Tamrin 2 Average 2D List 
def average_list(my_list):
    s=0
    long=0      ## Count each list item
    for list in my_list:
        total=0
        
        for i in range(len(list)):
            total += list[i]
        long+= len(list)
        s+=total
        average = s/long
    return average

### Tamrin 3   Max even  
def maxeven(my_list):
    def maxeven1D(oneD):
        result = None
        for element in oneD:
            if element %2==0:
                if result == None or element > result:
                    result = element
        return result
    result = None
    for row in my_list:
        maximum_row= maxeven1D(row)
        if maximum_row :
            if result == None or maximum_row > result:
                result = maximum_row
    if not my_list: return None
    return result

### Tamrin 4 sum number in rows
def anuual_row(my_list):
    total = []
    for row in my_list:
        z=0
        for item in row:
           z += item
        total.append(z)
    return total
### Tamrin 5 sum number in column
def _sum_of_columns_sample_(sample_list):
    # Solution type 1:
    # return [max(col) for col in zip(*sample_list)]
    # Alternative Solution
    cols = len(sample_list[0])
    mylist = []
    for c in range(cols):
        column_sum = 0
        for row in sample_list:
            column_sum += row[c]
        mylist.append(column_sum)
    return mylist
### Tamrin 6 count amd sum Even or Odd rows

def _count_even_sum_sample_(sample_2d_list):
    even_count = 0
    odd_count = 0
    # For each row
    for rows in sample_2d_list:
        row_sum = sum(rows)
        if row_sum % 2 == 0:
            even_count = even_count + 1
        else:
            odd_count = odd_count + 1
    return [even_count, odd_count]

### Tamrin 7: maximum number in each Row
def max_num_in_row(my_list):
    result=[]
    for row in my_list: #range(len(_list)):
        c=max(row)
        #print(row)
        result.append(c)
    return result

### Tamrin 8: maximum number in each Column
def max_num_in_column(my_list):
    def exchange_column_to_row(my_list):
        col = len(my_list)
        print('col and range ',col , range(col))
        result = []
        for c  in range(col):
            maximum=0
            xx=[]
            print('c ' , c)
            for element in my_list:  
                maximum = element[c]
                print(maximum)
                xx.append(maximum)
            result.append(xx)
        return result
    ex = exchange_column_to_row(my_list)
    result = []
    for i in ex:
        result.append(max(i))
    return result
### Tamrin 9: change 2D to 1D sorted list
def chande_dimension_and_sort(my_list):
    result=[]
    for list in my_list:
        for e in list:
            result.append(e)
    result.sort()
    return result
### Tamrin 10: sorted Rows
def sorted_rows(my_list):
    result = []
    for list in my_list:
        list.sort(reverse=True)
        print(list)
        result.append(list)
    return result
### Tamrin 11: is Multiplication two Matrix possible
a = [[2, 3, 4],
     [3, 4, 5]]
b = [[4, -3, 12],
     [1, 1, 5],
     [1, 3, 2]]
def is_Multiplication_Matrixs_possible(a,b):
    a_row=len(a)
    for list in a:
        a_column = len(list)
    #print(a_row, a_column)
    
    b_row=len(b)
    for list in b:
        b_column = len(list)
    #print(b_row, b_column)

    a_D = a_row * a_column
    b_D = b_row * b_column
    return True if a_column == b_row else False

### Tamrin 12: Multiplication Matrixs
def _product_of_two_vectors_sample_(a, b):
    if len(a[0]) != len(b):
        return None
    # Create the result matrix and fill it with zeros
    output_list=[]
    temp_row=len(b[0])*[0]
    for r in range(len(a)):
        output_list.append(temp_row[:])
    for row_index in range(len(a)):
        for col_index in range(len(b[0])):
            sum=0
            for k in range(len(a[0])):
                sum=sum+a[row_index][k]*b[k][col_index]
            output_list[row_index][col_index]=sum
    return output_list
def _product_of_two_vectors_sample_(a, b):
    import numpy
    product = (numpy.mat(a) * numpy.mat(b))     # returns a numpy array
    product_to_list = product.tolist()          # convert the numpy array to a standard list
    return product_to_list  
    
        
