#To determine the mean color of the shirts worn throughout the week,
#we first need to extract all the colors from the table and calculate the mean.
#Here's some Python code to achieve that:


import re

# Extract colors from table
colors = []
with open('python_class_question.html', 'r') as f:
    html = f.read()
    matches = re.findall(r'<td>(\w+)(?:,\s*\w+)*</td>', html)
    for match in matches:
        colors.extend(match.split(', '))

# Calculate mean color
mean_color = max(set(colors), key=colors.count)
print("Mean color:", mean_color)




#----------------------------------------------------------------------------------------#

#To determine the color that was mostly worn throughout the week,
#we can use a similar approach. Here's some Python code to achieve that:

# Calculate most worn color
most_worn_color = max(set(colors), key=colors.count)
print("Most worn color:", most_worn_color)


#----------------------------------------------------------------------------------------#

#To determine the median color, we first need to sort the list of colors,
#then select the middle color (or the average of the two middle colors if there are an even number of colors).
#Here's some Python code to achieve that:


# Calculate median color
sorted_colors = sorted(colors)
middle_index = len(sorted_colors) // 2
if len(sorted_colors) % 2 == 0:
    median_color = (sorted_colors[middle_index - 1] + sorted_colors[middle_index]) / 2
else:
    median_color = sorted_colors[middle_index]
print("Median color:", median_color)




#----------------------------------------------------------------------------------------#

#To calculate the variance of the colors,
#we can use the statistics module in Python.
#Here's some code to achieve that:


import statistics

# Calculate variance
variance = statistics.variance(colors)
print("Variance:", variance)

#----------------------------------------------------------------------------------------#

#To determine the probability that a color chosen at random is red,
#we first need to count the number of times that the color red appears,
#then divide that by the total number of colors. Here's some code to achieve that:

# Calculate probability of red
num_red = colors.count('RED')
probability_red = num_red / len(colors)
print("Probability of red:", probability_red)


#----------------------------------------------------------------------------------------#
