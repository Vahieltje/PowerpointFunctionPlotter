import matplotlib.pyplot as plt
import numpy as np
import sys


import math
from numpy import *
import re


# Get arguments passed from VBA
function_expr = sys.argv[1]  # Function expression
img_path = sys.argv[2]       # Image save path
function_color = sys.argv[3] # Function color
xmin = float(sys.argv[4])    # X axis min
xmax = float(sys.argv[5])    # X axis max
ymin = float(sys.argv[6])    # Y axis min
ymax = float(sys.argv[7])    # Y axis max
show_grid = sys.argv[8] == 'True'  # Whether to show grid
show_axes = sys.argv[9] == 'True'  # Whether to show axes
show_ticks = sys.argv[10] == 'True'  # Whether to show ticks
show_boundingbox = sys.argv[11] == 'True'  # Whether to show bounding box

print(f"show_grid: {show_grid}, show_axes: {show_axes}, show_ticks: {show_ticks}, show_boundingbox: {show_boundingbox}")

# Replace '^' with '**' in the function expression
function_expr = re.sub(r'\^', '**', function_expr)

# Example: use eval to evaluate the function expression
x = np.linspace(xmin, xmax, 400)
y = eval(function_expr)  # This will evaluate the function as a Python expression

# Plot the function with the selected color
plt.plot(x, y, color=function_color)

# Set axis limits
plt.xlim(xmin, xmax)
plt.ylim(ymin, ymax)

if not show_boundingbox:
    # Remove the bounding box (spines)
    for spine in plt.gca().spines.values():
        spine.set_visible(False)

# Add grid and axes if selected
if show_grid:
    plt.grid(True)
if show_axes:
    plt.axhline(0, color='black',linewidth=0.5)  # X-axis
    plt.axvline(0, color='black',linewidth=0.5)  # Y-axis
    
        
# Show or hide ticks
if not show_ticks:
    plt.xticks([])
    plt.yticks([])


# plt.title(f'Plot of {function_expr}')

# Save the plot to the specified image path as SVG
plt.savefig(img_path, format='svg', transparent=True)
plt.close()
