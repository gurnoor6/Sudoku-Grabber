# Sudoku-Grabber
This is a self project aimed at using Computer Vision to detect and solve sudokus from images. This was done by me during Summer 2020, with aim of understanding the application Machine Learning.

The structure of the project was as follows - 
1. First train a convolutional neural network on the MNIST dataset for handwritten digit recognition. This was done using Keras.
2. Segment the sudoku in images. This was a hard task and employed various functions in OpenCV. This is described in detail later
3. Solving the recognized sudoku. This was done by a backtracking algorithm written in Python.
