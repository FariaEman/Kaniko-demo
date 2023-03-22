#!/usr/bin/env python
# coding: utf-8

# # Faria Eman_19i-0634_A
#     

# # 1. Lists and Dictionaries

# # a)

# In[1]:


def book_a_car(bookings):
    count=1
    x1 = bookings[0][1]
    for i in range(1,len(bookings)):
        if x1 > bookings[i][0]:
             count+=1
    print(f'Input: bookings={bookings}')
    print(f'No. of cars required to fulfil the booking: {count}')


# In[2]:


car_bookings= [[2,10], [5,9], [7, 11], [11, 15]]
book_a_car(car_bookings)


# # b)

# In[122]:


def most_frequent_elements_in_lis(elem_list, left, right, frequency):

    new_li = []
    new_list = []
    for i in range(left,right):
        new_list.append(elem_list[i])
#  declared an empty dictionary
    frequence = {}
    for item in new_list:
            if (item in frequence):
                frequence[item] += 1           
            else:
                frequence[item] = 1
#      here value is the frequeny and  key is its respective number    
    for key, value in frequence.items():     
        if(value >= frequency):
            new_li.append(key)   
    print(new_li)


# In[123]:


# arr = [1,2,1,2,7,1,8,8]
arr = [2,2,4,2,4,5,6, 1,1]
most_frequent_elements_in_lis(arr, 0, 6, 2)


# # c)(i)

# In[303]:


def get_student_marks(Student_Data):
    Marks = {}

    for student in Student_Data:
        roll_no = student['roll_no']
        
# roll no's of students are mapped in new student marks dictionary
        Marks[roll_no] = {}
    
# for loop to iterate all courses in student marks
        for course in student['marks']:
            cum_marks = 0
        
# for loop to iterate student marks of all courses
            for score in student['marks'][course]:
                if score:
                    cum_marks += score

            Marks[roll_no][course] = cum_marks
    return Marks


# In[304]:


student_data = [{'roll_no': 'p18-1001', 'marks': {
'english': (1.4, 2.5, 15, 9.6, 33),
'calculus': (2.4, 1.5, 12, 1.6, 21),
}, 'attendance': 88.4
},
{'roll_no': 'p18-1002', 'marks': {
'english': (2.4, 1.5, 12, 1.6, 21),
'programming fundaments': (2.4, 1.5, 12, 1.6, 21),
}, 'attendance': 79.4
},
{'roll_no': 'p18-1003', 'marks': {
'calculus': (2.4, 1.5, 12, None, 21),
'programming fundamentals': (2.4, 1.5, 12, 1.6, 21),
}, 'attendance': 79.4 }]

get_student_marks(student_data)


# #  c)(ii)

# In[326]:


def get_grade(marks,grade_dic):
    for grade in grade_dic:
        if marks >= grade_dic[grade]:
            return grade
    return 'F'


# In[329]:


dic = {'A': 80, 'B': 70, 'C': 60, 'D': 50}
get_grade(65,dic)


# # 2. Numpy Matrix

# # a)

# In[372]:


import numpy as np
Matrix = np.random.randint(1, 10, size=(7, 7)) 
print(f'Matrix: \n{Matrix}')


# # a)(i)

# In[391]:


def second_Max_RowSum(Matrix):
# find sums of each row in 2D matrix
    sumRow = np.sum(Matrix, axis=1)
# sort the array in assending order
    sumRow.sort()
# return second largest sum row
    return sumRow[-2]


# In[392]:


print(f'Second maximum sum of rows: {second_Max_RowSum(Matrix)}')


# # a)(ii)

# In[393]:


def lower_or_upper(Matrix):
# built in function of Numpy to find the lower triangle
    if np.all(np.tril(Matrix) == Matrix):
        return "lower"
# built in function of Numpy to find the upper triangle
    elif np.all(np.triu(Matrix) == Matrix):
        return "upper"
# If neither of the above, return None
    else:
        return None


# In[394]:


print(f'Matrix is {lower_or_upper(Matrix)} triangle')


# # a)(iii)

# In[387]:


def Mini_sumRow(Matrix):
# find sums of each row in 2D matrix
    sumRow = np.sum(Matrix, axis=1)
# sort the array in assending order
    sumRow.sort()
# return minimum sum row
    return sumRow[0]


# In[388]:


print(f'Minimum sum row of matrix: {Mini_sumRow(Matrix)}')


# # a)(iv)

# In[385]:


def swap_Odd_Row(Matrix):
# mat[::2, :] is used to get all the odd rows in the matrix
# mat[::-2, :] is used to get all the odd rows but in reverse order
# It will pick all the odd rows and swap them with odd rows in reverse order
    Matrix[::2, :] = Matrix[::-2, :]
# Return the matrix
    return Matrix


# In[386]:


print(f'Odd rows are swapped: {swap_Odd_Row(Matrix)}')


# # a)(v)

# In[383]:


def mean_of_rows(Matrix):
# find the mean of each row
    Mean_rows = np.mean(Matrix, axis=1)
# Return the mean of each row
    return Mean_rows


# In[384]:


print(f'Mean of Rows: {mean_of_rows(Matrix)}')


# # a)(vi)

# In[381]:


def sortColumns(Matrix):
# this will Sort each column in the matrix in ascending order
# mat.sort() is used to sort the matrix. here axis=0 means bcz columns need to be sorted
    Matrix.sort(axis=0)
    return Matrix


# In[382]:


print("Columns are sorted in assending order: ")
sortColumns(Matrix)


# # (b)

# In[410]:


import numpy as np

def Make_String(mat, str):
    picked = {}

    # Check if first character of string is present in row 1
    if str[0] not in mat[0]:
        return False

    # Initialize the first character of string as picked from row 1
    picked[0] = set([str[0]])

    # count of characters matched with string
    count = 1
    index = 1

    # Iterate over the rows of matrix 
    while index < len(mat):
        # Check if the character picked from row inddex is present in the string
        if str[count] not in mat[index]:
            return False

        # Check if the character picked from row idx is already picked
        if index in picked and str[count] in picked[index]:
            return False

        if index not in picked:
            picked[index] = set([str[count]])
        else:
            picked[index].add(str[count])

        # Increment the count of characters matched with string
        count += 1
        index += 1
        if count == len(str):
            return True
        if index == len(mat):
            index = 0


# In[411]:


matrix = np.array([['f', 'n', 't'], ['a', 'e', 'c'], ['i', 'l', 's']])
s1 = 'nelfa'
s2 = 'nele'

# print the matrix
print(f'Matrix:\n {matrix}')

# print the string
print("\nString1:")
print(s1)
print(Make_String(matrix, s1))

# print the string
print("\nString2:")
print(s2)
print(Make_String(matrix, s2))


# # (c)An hour Glass Problem:

# In[433]:


rows = 6
columns = 6
 
# Function to find the maximum sum of hour glass
def MaxSum(arr):
 
    # Considering the matrix also contains
    max_sum = 0
#     iterates to find each hour glass
    for i in range(0, rows-2):
        for j in range(0, columns-2):
                     
            # Indexes of each hour cells            
            # sum of cells of hour glass.
            sum = (arr[i][j] + arr[i][j + 1] + arr[i][j + 2]) + (arr[i + 1][j + 1]) + (arr[i + 2][j] + arr[i + 2][j + 1] + arr[i + 2][j + 2])
 
    # find the sum of all hourglasses and update new sum in max_sum
            if(sum > max_sum):
                max_sum = sum
            else:
                continue
    return max_sum


# In[435]:


arr = [[1, 1, 1, 0, 0,0],
       [0, 1, 0, 0, 0,0],
       [1, 1, 1, 0, 0,0],
       [0, 0, 2, 4, 4,0],
       [0, 0, 0, 2, 0,0],
       [0, 0, 1, 2, 4,0]]
res = MaxSum(arr)
 
if(res == -1):
        print("Invalid")
else:
        print(f"Maximum sum of hourglass = {res}")


# # d) Numpy manipulation

# # d)(i)

# In[289]:


arr = np.array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
print(f'Orignal array: {arr}')   
arr[arr % 2 != 0] = -1
print(f'Updated array: {arr}')   


# # d)(ii)

# In[297]:


Numpy_arr = np.random.randint(1, 17 , size=10) 
print(f'Input: {Numpy_arr}')
output = Numpy_arr[(Numpy_arr>5)*(Numpy_arr<10)]
print(f'Output: {output}')


# In[ ]:





# # 3. String manipulations:

# # (a)

# In[445]:


characters = 256
def Anagram(string1,string2):
     
    # Create a counter array and initialize all values as 0
    counter = [0 for i in range(characters)]
    i=0
#      for each charcter in the input string , increament in count
    for i in range(len(string1)):
        counter[ord(string1[i]) - ord('a')] += 1;
        counter[ord(string2[i]) - ord('a')] -= 1;
      
    if(len(string1) != len(string2)):
        return False;
     
    # check if there is any non-zero value in counter array
    for i in range(characters):
        if (counter[i] != 0):
            return False    
    return True
     


# In[446]:


s1="car"
s2="arc"
 
if (Anagram(s1, s2)):
    print("Both strings are anagram of each other")
else:
    print("Both strings are not anagram of each other")


# # (b)

# In[3]:


def Rotations(string1, string2):
    len1 = len(string1)
    len2 = len(string2)
    new_string = ''
 
    # to check weather two strings are same or not
    if len1 != len2:
        return 0
 
    # Create a temp string with value str1.str1
    new_string = string1 + string1
 
    # to check how many occurences of string2 in newstring
    if (new_string.count(string2)> 0):
        return 1
    else:
        return 0


# In[4]:


string1 = "XYZ"
string2 = "ZXY"
 
if Rotations(string1, string2):
    print ("Strings are rotations of each other:  True")
else:
    print ("False")
 


# # (c)

# In[47]:


def Super_String(Input):
    dic = {}
    asci_val = 26
# insert asci's of all characters in the dictionary
    for i in range(65,91):
        dic[chr(i)] = asci_val
        asci_val -= 1

    str = set(Input)
# initialize a falg
    flag = 0
# we will sort the array firat
    str = sorted(str)
# check if the input(string) count value (asci value) in the dictionary or not
    for i in str:
        if(Input.count(i) != dic[i]):
            flag=1
            break
    if(flag == 1):
        print("String is not Super String")
    else:
        print("String is Super String")


# In[48]:


print("Enter String: ")
str = input()
Super_String(str)


# # (d)

# In[38]:


def Sub_String_Palindromes(string):
    leng = len(string)
# create an array for palindromes of string
    Palindrome_arr = [[0 for x in range(leng)]
          for y in range(leng)]
    flag = [[False for x in range(leng)]
         for y in range(leng)]
    
    for i in range(leng):
        flag[i][i] = True
    
    for i in range(leng - 1):
        if (string[i] == string[i + 1]):
            flag[i][i + 1] = True
            Palindrome_arr[i][i + 1] = 1

    for space in range(2, leng):
        for i in range(leng - space):
            j = space + i

            if (string[i] == string[j] and flag[i + 1][j - 1]):
                flag[i][j] = True
           
            if (flag[i][j] == True):
                Palindrome_arr[i][j] = (Palindrome_arr[i][j - 1] + Palindrome_arr[i + 1][j] + 1 - Palindrome_arr[i + 1][j - 1])

            else:
                Palindrome_arr[i][j] = (Palindrome_arr[i][j - 1] + Palindrome_arr[i + 1][j] - Palindrome_arr[i + 1][j - 1])
    return Palindrome_arr[0][leng - 1]


# In[39]:


# str = "abaabeba"
string = input()
print(f'Number of sub_string palindromes: {Sub_String_Palindromes(string)}')


# In[ ]:





# # 4.OOP (Macau - card game)

# In[40]:


class Player:
    def __init__(self, name=''):
        self.name = name
        self.hand = []
        self.skip_turns = 0
        self.input = self.__input
        self.print = print
        self.gui = self.__gui_builder
        
    async def __input_method(self, msg):
        mov = input(msg)
        self.print_foo(f'{self.name} plays: {mov}.')
        return move


# In[ ]:




