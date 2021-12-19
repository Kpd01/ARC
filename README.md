# Student Information
- `Student ID`: 16233039
- `Student Name`: Krishna Ravichandran 


# Task 1 - 3c9b0459.json
This ARC problem is of grid size 3x3.  From the training examples, it is clear that the solution for this problem can be achieved by:

- `Column operation`: Swaping the 1st column with the third column.
- `Row Operation`: Swapping the 1st row with third row.

<img width="462" alt="image" src="https://user-images.githubusercontent.com/46656717/146688747-71068136-3d60-49ce-80b7-db337a7eba0d.png">


# Task 2 - 5bd6f4ac.json

This ARC task involves with slicing and dicing of the numpy array where the input of size 9x9 is sliced to 3x3. The result can be achieved by.
    
- `Numpy array Slicing`: Slicing the first three rows and last three columns of the np array  

<img width="463" alt="image" src="https://user-images.githubusercontent.com/46656717/146688708-ef48e81e-eddc-4f55-abcf-8cc3b7196f67.png">

# Task 3 - 08ed6ac7.json

The ARC task involves replacing the grey grids with colors in order as follows,
    1st highest number of grey grids = blue
    2nd highest number of grey grids = red
    3rd highest number of grey grids = green
    4th highest number of grey grids = yellow
The solution for this ARC task is acheieved by:

- Initiating the color code for blue (higher order) as 1. 
- Determine the shape of the array and assign it to rows and columns variables. 
- Loop from 0th to mth row and 0th to nth column
- Search for the grey color which is coded as 5,if the color matches
         - replace the current column with color code from the row until the end of the row
         - increase the color code by 1 so as to change the color when iteration encounters next time 

<img width="459" alt="image" src="https://user-images.githubusercontent.com/46656717/146688955-edd808b9-61b0-4b3c-b3a0-3755b46fb4b3.png">

# Task 4 - 1cf80156.json
This ARC problem involves extracting the array values that are non zero and create a new array.
This ARC task solution is achieved by removing all columns and rows containing zero values only.

- find all the rows and columns with np.all function which generates boolean 1D array
- indexes of nonzero value columns can be identified from the array with np.where function.
- slicing the matrix from the row and columns indexes will give us the result.

<img width="470" alt="image" src="https://user-images.githubusercontent.com/46656717/146689113-6664aef4-efeb-4014-b754-71c8bd451e13.png">


# Task 5 - beb8660c.json
This ARC task involves rearranging the rows from largest at the bottom of the array to the smallest at the top. The rows should be aligned to right side 
This ARC problem involves extracting the array values that are non zero and create a new array and map the values based on the count to the corresponding color.
This ARC task solution is achieved by 

- Creating two lists, one for counting the occureneces of colors, another for colors itself by iterating over the nd array.
- np.count_zero function is used to find the number of non-zero values.
- 
- slicing the matrix from the row and columns indexes will give us the result.















# The Abstraction and Reasoning Corpus (ARC)

This repository contains the ARC task data, as well as a browser-based interface for humans to try their hand at solving the tasks manually.

*"ARC can be seen as a general artificial intelligence benchmark, as a program synthesis benchmark, or as a psychometric intelligence test. It is targeted at both humans and artificially intelligent systems that aim at emulating a human-like form of general fluid intelligence."*

A complete description of the dataset, its goals, and its underlying logic, can be found in: [The Measure of Intelligence](https://arxiv.org/abs/1911.01547).

As a reminder, a test-taker is said to solve a task when, upon seeing the task for the first time, they are able to produce the correct output grid for *all* test inputs in the task (this includes picking the dimensions of the output grid). For each test input, the test-taker is allowed 3 trials (this holds for all test-takers, either humans or AI).


## Task file format

The `data` directory contains two subdirectories:

- `data/training`: contains the task files for training (400 tasks). Use these to prototype your algorithm or to train your algorithm to acquire ARC-relevant cognitive priors.
- `data/evaluation`: contains the task files for evaluation (400 tasks). Use these to evaluate your final algorithm. To ensure fair evaluation results, do not leak information from the evaluation set into your algorithm (e.g. by looking at the evaluation tasks yourself during development, or by repeatedly modifying an algorithm while using its evaluation score as feedback).

The tasks are stored in JSON format. Each task JSON file contains a dictionary with two fields:

- `"train"`: demonstration input/output pairs. It is a list of "pairs" (typically 3 pairs).
- `"test"`: test input/output pairs. It is a list of "pairs" (typically 1 pair).

A "pair" is a dictionary with two fields:

- `"input"`: the input "grid" for the pair.
- `"output"`: the output "grid" for the pair.

A "grid" is a rectangular matrix (list of lists) of integers between 0 and 9 (inclusive). The smallest possible grid size is 1x1 and the largest is 30x30.

When looking at a task, a test-taker has access to inputs & outputs of the demonstration pairs, plus the input(s) of the test pair(s). The goal is to construct the output grid(s) corresponding to the test input grid(s), using 3 trials for each test input. "Constructing the output grid" involves picking the height and width of the output grid, then filling each cell in the grid with a symbol (integer between 0 and 9, which are visualized as colors). Only *exact* solutions (all cells match the expected answer) can be said to be correct.


## Usage of the testing interface

The testing interface is located at `apps/testing_interface.html`. Open it in a web browser (Chrome recommended). It will prompt you to select a task JSON file.

After loading a task, you will enter the test space, which looks like this:

![test space](https://arc-benchmark.s3.amazonaws.com/figs/arc_test_space.png)

On the left, you will see the input/output pairs demonstrating the nature of the task. In the middle, you will see the current test input grid. On the right, you will see the controls you can use to construct the corresponding output grid.

You have access to the following tools:

### Grid controls

- Resize: input a grid size (e.g. "10x20" or "4x4") and click "Resize". This preserves existing grid content (in the top left corner).
- Copy from input: copy the input grid to the output grid. This is useful for tasks where the output consists of some modification of the input.
- Reset grid: fill the grid with 0s.

### Symbol controls

- Edit: select a color (symbol) from the color picking bar, then click on a cell to set its color.
- Select: click and drag on either the output grid or the input grid to select cells.
    - After selecting cells on the output grid, you can select a color from the color picking to set the color of the selected cells. This is useful to draw solid rectangles or lines.
    - After selecting cells on either the input grid or the output grid, you can press C to copy their content. After copying, you can select a cell on the output grid and press "V" to paste the copied content. You should select the cell in the top left corner of the zone you want to paste into.
- Floodfill: click on a cell from the output grid to color all connected cells to the selected color. "Connected cells" are contiguous cells with the same color.

### Answer validation

When your output grid is ready, click the green "Submit!" button to check your answer. We do not enforce the 3-trials rule.

After you've obtained the correct answer for the current test input grid, you can switch to the next test input grid for the task using the "Next test input" button (if there is any available; most tasks only have one test input).

When you're done with a task, use the "load task" button to open a new task.
