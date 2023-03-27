# Planning Breadth First Search

## 8 Puzzle

### Name
- Shantanu Parab

### ID
- sparab@umd.edu

## Installation Instructions
- To install numpy, run `pip install numpy` in your terminal.
- To install pygame, run `pip install pygame` in your terminal.

## Source Code Files
- [`puzzle.py`](puzzle.py) - Contains the implementation of Breadth First Search algorithm to solve the puzzle.
  + Run the program and it will generate 3 text files containing the path to goal,explored nodes, and node info.
  + The folder already consist these files with a test run.
  + There are a few start states that can be used to get the solution quickly which are as follows
    * start 1 : 8 2 6 0 4 7 1 3 5
    * start 2 : 7 2 5 0 1 4 8 3 6 
    * start 3 : 2 3 5 6 1 2 0 7 8
    * start 4 : 0 3 8 5 7 2 1 6 4 
  + The start states can be changed by passing a argument -ss to the program which is a string with 9 elements that depict the elements of the matrix column wise.
    * test_case 1 : 4 7 8 2 1 5 3 6 0
    * test_case 2 : 1 6 7 2 0 5 4 3 8
  
  Test Node 1 will be  
       -------------  
        | 4 | 2 | 3 |   
        -------------  
        | 7 | 1 | 6 |   
        -------------  
        | 8 | 5 | 0 |     
        -------------  
- [`plot_path.py`](plot_path.py) - Contains the implementation provided to print the states from the nodePath.txt file

- [`game.py`](game.py) - Contains the implementation of the 8 Puzzle game using Pygame. 
  This is just a fun visualization of the puzzle. It takes the values from the nodePath.txt file to simulate the path.

- [`Source Code`] - Contains the source code as pdf for plagiarism check

## How to Run the Program:
To run the program, open the command prompt/terminal and navigate to the directory where the source code files are located. Then, type the following command: python [filename].py.
eg: python puzzle.py -ss "4 7 8 2 1 5 3 6 0"




