#!/usr/bin/python

import os, sys
import json
import numpy as np
import re

from colorama import Fore, Style, init
init() # this colorama init helps Windows 

###### STUDENT NAME: KRISHNA RAVICHANDRAN
######  STUDENT ID: 16233039

###### GITHUB URL : https://github.com/Kpd01/ARC
    

### YOUR CODE HERE: write at least three functions which solve
### specific tasks by transforming the input x and returning the
### result. Name them according to the task ID as in the three
### examples below. Delete the three examples. The tasks you choose
### must be in the data/training directory, not data/evaluation.
def solve_3c9b0459(x):
    """
    This ARC problem is of grid size 3x3 where from the training examples it is clear that
    it solution is achieved by swaping the 1st column with the third and followed by rows as same.
    """
    x[:,[2, 0]] = x[:,[0, 2]]   # first swap the column 3 with column 1
    x[[2, 0],:] = x[[0, 2],:]   # swap the row 3 with the row 1
    return x  #return the result

def solve_5bd6f4ac(x):
    """
    This ARC task involves with slicing and dicing of the numpy array where the input 
    of size 9x9 is sliced to 3x3. The result is from first row till 3rd and last three columns 
    from the training example.
    Step1- slice the np matrix for first three rows and last three columns
    return x  #return the result
    """
    x = x[:3,-3:] #slice the np matrix for first three rows and last three columns
    return x  #return the result

def solve_08ed6ac7(x):
    """
    The ARC task involves replacing the grey grids with colors in order as follows,
    1st higher grey grid = blue
    2nd higher grey grid = red
    3rd higher grey grid = green
    4th grey grid = yellow

    The solution for this ARC task is acheieved by:

    Step1- Initiating the color code for blue (higher order) as 1. 
    Step2- Determine the shape of the array and assign it to rows and columns variables. 
    Step3- Loop from 0th to mth row and 0th to nth column
    Step4- Search for the grey color which is coded as 5,if the color matches
         - replace the current column with color code from the row until the end of the row
         - increase the color code by 1 so as to change the color when iteration encounters next time 
    """
    
    color = 1 # the intial color blue as per color code
    m = x.shape[0] # determine the no. of rows
    n = x.shape[1] # determine the no. of coloumns
    for i in range(0,m):
        for j in range(0,n):
            #search for the grey color which is coded as 5
            if  x[i][j] == 5: #if the color matches
                x[i:m,j] = color #replace the current column with color code from the row until the end of the row
                color += 1  #increase the color code by 1 so as to change the color when iteration encounters next time 
    return x #return the output array

def solve_1cf80156(x):
    """
    This ARC task solution is achieved by removing all columns and rows containing zero values only.

    The approach is to find all the rows and columns with np.all function which generates boolean 1D array
    from which, indexes of nonzero value columns can be identified with np.where function.

    Further slicing the matrix from the row and columns indexes will give us the result.

    Step1- finding boolean result for zero values in rows(m_array)
    Step2- finding the indexes of the non-zero elements(m_idx)
    Step3- finding the boolean result for zero values in columns(n_array)
    Step4- finding the indexes of the non-zero elements (n_idx)
    Step5- Slicing the array x with the indices containing non-zero values

    np.all() function is used to 
    np.where()function is used

    x = x[m_idx[0][0]:m_idx[0][-1]+1, n_idx[0][0]:n_idx[0][-1]+1] #slice the matrix with the indexes containing non_zero values.
    """

    m_array = np.all(x==0, axis=1)  #find boolean reslut for zero values in rows
    m_idx = np.where(m_array == False) #find the indexes of the non-zero elements
    n_array = np.all(x==0, axis=0) #find the boolean result for zero values in columns
    n_idx = np.where(n_array == False) #find the indexes of the non-zero elements 

    x = x[m_idx[0][0]:m_idx[0][-1]+1, n_idx[0][0]:n_idx[0][-1]+1] #slice the matrix with the indexes containing non_zero values.
    return x

def solve_beb8660c(x):
    """
This ARC task involves rearranging the rows from largest at the bottom of the array to the smallest at the top. The rows should be aligned to right side 
This ARC problem involves extracting the array values that are non zero and create a new array and map the values based on the count to the corresponding color.
This ARC task solution is achieved by 

- Step1 - Creating two lists, one for counting the occureneces of colors, another for colors itself by iterating over the nd array.
- Step2 - Count the non-zero occurences of color using np.count_zero and append to the count list created in step 1
- Step3 When the count of occureneces is greater than 0, find the correct value corresponding to the occurence using np.max() function. _(np.max() function is used for simplicity purposes, the row values are same but returns the value even while using np.max() function )_

- Step4 -  Get the index of the counts in ascending order,  np.argsort is used to retuyrn the indices of the counts list
- Step 5 - Rearrnage the color and count lists accordingly
- Step 6 - Using enumerate function, create a index which will be used to add it with nth row in array - color list row such that the least count of color comes at the top though non-colored row exists still.
- Step 7 - Replace all other places with respective color
    """
    color_list = list()  #make a list for colors and counts of the colors
    count_list = list()
    for i in x: #loop over each row in x
        cnt = np.count_nonzero(i, axis=0)  #find the count of non_zero elements
        #print(cnt)
        if cnt > 0:
            row_color = np.max(i)   #find the correct value corresponding to the occurence using np.max() function. (np.max() function is used for simplicity purposes, the row values are same but returns the value even while using np.max() function )

            #print('r', row_color)
            color_list.append(row_color)    #append the count and color to the list
            count_list.append(cnt)

    #print('colors before', color_list)
    #print('counts before', count_list)
    ids = np.argsort(count_list)      #get the index of the counts in the ascending order
    #print('sorted index',ids)
    count_list = np.array(count_list)[ids]   #rearrange the counts and color based on the np.argsort

    color_list = np.array(color_list)[ids]
    #print('colors after', color_list)
    #print('counts after',count_list)
    x = np.zeros_like(x)    #make an empty array of zeros with the shape of x
    #print(x)
    for j, (count, color) in enumerate(zip(count_list, color_list)):   
        row = j + x.shape[0] - color_list.shape[0]  #find the rows of the color supposed to be in
        #print(row)
        x[row, -count:] = color   #replace the row with the color in the respective places
        #print(x)
    return x   #return the output 


def main():
    # Find all the functions defined in this file whose names are
    # like solve_abcd1234(), and run them.

    # regex to match solve_* functions and extract task IDs
    p = r"solve_([a-f0-9]{8})" 
    tasks_solvers = []
    # globals() gives a dict containing all global names (variables
    # and functions), as name: value pairs.
    for name in globals(): 
        m = re.match(p, name)
        if m:
            # if the name fits the pattern eg solve_abcd1234
            ID = m.group(1) # just the task ID
            solve_fn = globals()[name] # the fn itself
            tasks_solvers.append((ID, solve_fn))

    for ID, solve_fn in tasks_solvers:
        # for each task, read the data and call test()
        directory = os.path.join("..", "data", "training")
        json_filename = os.path.join(directory, ID + ".json")
        data = read_ARC_JSON(json_filename)
        test(ID, solve_fn, data)


# ref https://stackoverflow.com/a/54955094
# Enum-like class of different styles
# these are the styles for background
class style():
    BLACK = '\033[40m'
    RED = '\033[101m'
    GREEN = '\033[42m'
    YELLOW = '\033[103m'
    BLUE = '\033[44m'
    MAGENTA = '\033[45m'
    CYAN = '\033[46m'
    WHITE = '\033[47m'
    RESET = '\033[0m'
    DARKYELLOW = '\033[43m'
    DARKRED = '\033[41m'
    # DARKYELLOW = '\033[2m' + '\033[33m'
    # DARKRED = '\033[2m' + '\033[31m'
    # DARKWHITE = '\033[2m' + '\033[37m'
    
# the order of colours used in ARC
# (notice DARKYELLOW is just an approximation)
cmap = [style.BLACK,
       style.BLUE,
       style.RED,
       style.GREEN,
       style.YELLOW,
       style.WHITE,
       style.MAGENTA,
       style.DARKYELLOW,
       style.CYAN,
       style.DARKRED]


def echo_colour(x):
    s = " " # print a space with a coloured background

    for row in x:
        for i in row:
            # print a character twice as grids are too "thin" otherwise
            print(cmap[int(i)] + s + s + style.RESET, end="")
        print("")

    
## TODO write a more convenient diff function, either for grids
## or for json files (because each task is stored as a single line
## of json in GitHub).

    
def read_ARC_JSON(filepath):
    """Given a filepath, read in the ARC task data which is in JSON
    format. Extract the train/test input/output pairs of
    grids. Convert each grid to np.array and return train_input,
    train_output, test_input, test_output."""
    
    # Open the JSON file and load it 
    data = json.load(open(filepath))

    # Extract the train/test input/output grids. Each grid will be a
    # list of lists of ints. We convert to Numpy.
    train_input = [np.array(data['train'][i]['input']) for i in range(len(data['train']))]
    train_output = [np.array(data['train'][i]['output']) for i in range(len(data['train']))]
    test_input = [np.array(data['test'][i]['input']) for i in range(len(data['test']))]
    test_output = [np.array(data['test'][i]['output']) for i in range(len(data['test']))]

    return (train_input, train_output, test_input, test_output)


def test(taskID, solve, data):
    """Given a task ID, call the given solve() function on every
    example in the task data."""
    print(taskID)
    train_input, train_output, test_input, test_output = data
    print("Training grids")
    for x, y in zip(train_input, train_output):
        yhat = solve(x)
        show_result(x, y, yhat)
    print("Test grids")
    for x, y in zip(test_input, test_output):
        yhat = solve(x)
        show_result(x, y, yhat)

        
def show_result(x, y, yhat):
    print("Input")
    echo_colour(x) # if echo_colour(x) doesn't work, uncomment print(x) instead
    #print(x)
    print("Correct output")
    echo_colour(y)
    #print(y)
    print("Our output")
    echo_colour(yhat)
    #print(yhat)
    print("Correct?")
    if y.shape != yhat.shape:
        print(f"False. Incorrect shape: {y.shape} v {yhat.shape}")
    else:
        print(np.all(y == yhat))


if __name__ == "__main__": main()

