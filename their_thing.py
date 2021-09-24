from matplotlib.style import use
import numpy as np
from scipy import stats
import matplotlib.pyplot as plt
from function import number_of_occurence, get_function
input_received = False   #state booleans
run = True
continue_decision_made = False
display_graph_decision_made = False

while run:
    continue_decision_made = False # resets state booleans
    display_graph_decision_made = False
    while not input_received: # loop to ensure correct data format is entered
        try:
            user_input_data = input("Enter numbers seperated by commas: ")
            user_input_data_list = list(map(float, user_input_data.split(",")))
            user_input_data_array1 = np.array(user_input_data_list) # one dimensional numpy array - basically a list of the numbers the user entered
            user_input_data_array2 = number_of_occurence(user_input_data_array1) # two dimensional numpy array if you wanna know more about this check functions
            input_received = True
        except ValueError:
            print("wrong input type")
    # print the statistics they want to the user
    print(f"the use entered {len(user_input_data_array1)} numbers") # uses length of the numpy array
    print(f"mode of the data is {stats.mode(user_input_data_array1).mode[0]} that occurs {stats.mode(user_input_data_array1).count[0]} times") # uses scipy to get mode
    print(f"mean of the data is {np.mean(user_input_data_array1)}") # get mean with numpy mean
    print(f"median of the data is {np.median(user_input_data_array1)}") # median with numpy median 
    print(f"range of the data is {np.ptp(user_input_data_array1, axis=0)}") # get range with this cool numpy function
    while not display_graph_decision_made:
        display_graph = input("display graph? y/n: ") # the user can choose wether or not they want the graph to be displayed
        if display_graph == "y":
            # all this shit is just setting up and plotting the graphs
            display_graph_decision_made = True
            figure, axis = plt.subplots(1, 2) # set up matplot lib figure of 1 row, two columns
            figure.patch.set_facecolor('#8D99A5') # changing some colours to find colours look here: https://matplotlib.org/stable/gallery/color/named_colors.html
            figure.suptitle('Graphs', fontsize=16) # figure title
            axis[0].hist(user_input_data_array1, color= "#190E4F") # make histogram in column 0
            axis[0].set(facecolor = "#DDD6D0") 
            axis[0].set(xlabel = 'value', ylabel = "Number of occurences") # axis titles for histogram
            axis[0].set_title("Histogram") # main title for histogram
            polyfunction, r_2_score = get_function(user_input_data_array2) # find the best function and r_score for second numpy arrau
            the_line = np.linspace(np.min(user_input_data_array2[0]), stop=np.max(user_input_data_array2[0]), num=200) # create a line that plots this equation
            axis[1].plot(the_line, polyfunction(the_line),color='#D28F4B',label=f"line of best fit\n y={polyfunction}\nr^2 score: {r_2_score}") # plot line and label
            axis[1].scatter(user_input_data_array2[0], user_input_data_array2[1], color ="#190E4F") # plot the scatter plot of numpy array 2
            axis[1].set(xlabel = 'value', ylabel = "Number of occurences") # axis titles
            axis[1].set(facecolor = "#DDD6D0") 
            axis[1].set_title("Scatter Plot") # main title
            axis[1].legend(loc='upper center') # legend
            plt.plot() # plot
            plt.show()


        if display_graph == "n":
            display_graph_decision_made = True
            continue
    while not continue_decision_made: # ask user if they want to continue and enter another set of data
        continue_decision = input("do you want to continue? y/n: ")
        if continue_decision == "n":
            run = False
            continue_decision_made = True
            quit # exit the program if they decide to quit
        if continue_decision == "y":
            input_received = False
            continue_decision_made = True # reset booleans