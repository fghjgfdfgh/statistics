import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from sklearn import metrics
from sklearn.metrics import r2_score
def number_of_occurence(numpy_array:np.array):
    """function that checks the number of times each value occurs in an array
       Arguments:
       numpy_array: One dimensional numpy array
    """
    values_checked_list = [] # this list keeps track of values that have been checked so that no value is checked twice
    new_array = np.array([ # this is a two dimensional array, the top row will be the value and the row below it will correspond to the 
        [],                # the number of times that value occurs in the data set
        []
    ])
    for i in numpy_array: # checks each value in array
        if i not in values_checked_list: # if the value has not been checked
            values_checked_list.append(i) # adds value to the list of checked values
            count = 0 # initializes count variable
            for value in numpy_array:
                if value == i: # if the value matches the valuable we are checking for
                    count += 1 # increment the count variable
            append_array = np.array([[i],[count]]) # two dimensional array with row one being the value checked and row two being the number of times the value occurs in the data set
            new_array = np.append(new_array, values=append_array, axis=1) # append the above array to the main array
    return new_array # return the two dimensional new array
            
            
test_array = np.array([1,2,3,4,5,6,7,5,3,3,4,6,32,2,4,6,3,43,56,6,7,8,4,3,5,6,7,8,9,54,6])
def get_function(numpy_array:np.array):
    """Returns optimal polynomial regression function
       Issues - Can sometimes fuck up if your data is really shit but unless theres some really fucked up data you will be fine
       If u wanna fix it stick in some simple error handling    
    """
    list_of_values = [] #stores nested lists that contain the order of the polynomial, the r^2 score(how good the line of best fit is and the eqution of the polynomial)
    for i in range(10):
        model = np.poly1d(np.polyfit(x=numpy_array[0], y=numpy_array[1], deg=i)) # create an equation of polynomial degree i
        score = r2_score(numpy_array[1], model(numpy_array[0])) # check how well this eqution fits the data
        list_of_values.append([i, score, model]) # append sublist to main list
    df = pd.DataFrame(list_of_values, columns=['degree', 'score', 'model']) # create a pandas data frame from the main list
    row = 0 # variable to increment in below loop
    model_found = False
    max = df['score'].max() # finds maximum r^2 score
    for i in df['score']: # this loop checks for the polynomial that matches the highest r^2 score
        if i == max:      # it also ensures that if there are multiple equtions with the same r^2 score it will pick the eqaution with lower order
            if not model_found: # this should give the pretttiest line of best fit
                final_model = df.iloc[row]['model']
                score = i
                model_found=True
        row += 1
    if model_found:
        return(final_model, score) # return the final model and its r^2 score


