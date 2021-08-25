# Data Programming Lesson 4: Plotting With Matplotlib

# matplotlib.pyplot: collection of functions that from matplotlib library
# Some functions can create a figure, decorate the plot with labels, etc.
import matplotlib.pyplot as plt

# We are using the plot() function to plot a list of numbers from 1-4
plt.plot([1, 2, 3, 4])

# We are using the ylabel() function to label the y axis as "some numbers"
plt.ylabel('some numbers')

# We are using the show() function to display our graph!
plt.show()

# We are plotting the x and y axis with 2 lists
# x-axis: [1, 2, 3, 4]
# y-axis: [1, 4, 9, 16]
plt.plot([1, 2, 3, 4], [1, 4, 9, 16])


# Plotting with barplots, discrete values, and linear regression
# Names of each category for one plot
names = ['group_a', 'group_b', 'group_c']

# Data points for each category
values = [1, 10, 100]

plt.figure(figsize=(9, 3))

plt.subplot(131)

# barplot with names as the x-axis, values as the y-axis
plt.bar(names, values)

plt.subplot(132)

# scatter plot with names as the x-axis, values as the y-axis
plt.scatter(names, values)

plt.subplot(133)

# linear plot with names as the x-axis, values as the y-axis
plt.plot(names, values)
plt.suptitle('Categorical Plotting')

# display graph
plt.show()
