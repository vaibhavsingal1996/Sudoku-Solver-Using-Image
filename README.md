# Sudoku-Solver-Using-Image
It solves the sudoku which is given as an image for input.

# Algorithm
It uses Knuth Dancing Links Algorithm to solve the sudoku as an exact cover problem.

# Image Recognition
An image of sudoku is first preprocessed to identify the sudoku grid.  
Then after the grid is extracted, straightened and flattened.  
Then each digit box is separated out and ran through the digit recognition model to obtain the numerical it repesents.  
Which is then formed as a 2D array and passed to algorithm to obtain the solution.  
  
Model is trained on a dataset of digital numbers using Convolutional Neural Network.

# Dependencies
Python 2.7  
Keras  
Numpy

# Build
Run following command at the root folder  
"python Sudoku+Solver.py image.jpeg"
