import pandas as pd

data = {"Name": ["Alice", "Bob"], "Age": [25, 30]}
df = pd.DataFrame(data)

print(df)
print("\n")  # newline

# column access
print(df["Name"])
print("\n")

# first row
print(df.iloc[0])
print("\n")

# slicing rows so from item 1 to item 2
print(df.iloc[0:2])
print("\n")

numbers = [10, 20, 30, 40, 50]
print(numbers[1:4])    # from index 1 to 3
print(numbers[-1])     # last element
print(numbers[-2:])    # last 2 elements
print("\n")


import numpy as np
import statistics as stats

data = [1, 2, 3, 4, 5, 5]

print("Mean:", np.mean(data))
print("Median:", np.median(data))
print("Mode:", stats.mode(data))

"""
| Type         | Example          | Description                 |
| ------------ | ---------------- | --------------------------- |
| **Nominal**  | Colors, names    | No order or ranking         |
| **Ordinal**  | Grades (A, B, C) | Has order, no equal spacing |
| **Interval** | Temperature (°C) | Equal spacing, no true zero |
| **Ratio**    | Weight, height   | Has true zero               |
"""

import matplotlib.pyplot as plt
import numpy as np

# Example e-commerce data (amounts spent)
data = np.random.normal(loc=50, scale=10, size=100)  # 100 transactions

# Create histogram
plt.hist(data, bins=10, color='skyblue', edgecolor='black')
plt.title("Transaction Amounts Histogram")
plt.xlabel("Amount Spent ($)")
plt.ylabel("Number of Transactions")
plt.show()


x = [1, 2, 3, 4, 5]
y = [10, 20, 15, 25, 30]

plt.plot(x, y, marker='o', linestyle='-', color='blue')
plt.title("Line Graph Example")
plt.xlabel("X-axis")
plt.ylabel("Y-axis")
plt.show()

categories = ["Apples", "Bananas", "Cherries"]
values = [10, 15, 7]

plt.bar(categories, values, color='orange')
plt.title("Bar Graph Example")
plt.ylabel("Quantity")
plt.show()
#horisontal
plt.barh(categories, values, color='green')
plt.show()

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Create random e-commerce data
data = np.random.normal(loc=50, scale=10, size=100)

# Put data into a pandas DataFrame
df = pd.DataFrame({
    'Amount_Spent': data
})

# Display the first 5 rows
print(df.head())

# Create a histogram using pandas
df['Amount_Spent'].plot(kind='hist', bins=10, color='skyblue', edgecolor='black')

plt.title('E-commerce Transaction Amounts')
plt.xlabel('Amount Spent ($)')
plt.ylabel('Number of Transactions')
plt.show()


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Create data
data = np.random.normal(50, 10, 100)
df = pd.DataFrame({'Amount_Spent': data})

# Save the graph object in a variable
x = df['Amount_Spent'].plot(kind='hist', bins=10, color='lightgreen', edgecolor='black')

# You don’t have to show it yet
print("Graph object saved as:", type(x))

# Later in the code...
plt.title("E-commerce Data")
plt.xlabel("Amount Spent ($)")
plt.ylabel("Transactions")

# 💡 Show the same graph later
plt.show()

#Save graphs for later

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Example data
data = np.random.normal(50, 10, 100)
df = pd.DataFrame({'Amount_Spent': data})

# Create first figure for histogram
plt.figure()  # start a new figure
x = df['Amount_Spent'].plot(kind='hist', bins=10, color='skyblue', edgecolor='black')
x.set_title("Histogram of Amount Spent(x)")
x.set_xlabel("Amount ($)")
x.set_ylabel("Transactions")
plt.show()  # shows histogram

# Create second figure for boxplot
plt.figure()  # start a new figure
z = df['Amount_Spent'].plot(kind='hist', color='lightgreen',edgecolor='black')
z.set_title("Boxplot of Amount Spent(z)")
z.set_ylabel("Amount ($)")
plt.show()  # shows boxplot

#example showing how X and Y are determined for different kinds of plots using Pandas.
import pandas as pd
import matplotlib.pyplot as plt

# Example data
data = {
    'Day': ['Mon', 'Tue', 'Wed', 'Thu', 'Fri'],
    'Sales': [120, 340, 180, 270, 310],
    'Visitors': [30, 45, 25, 50, 40]
}
df = pd.DataFrame(data)

# --- 1. Bar plot ---
# X = 'Day', Y = 'Sales'
bar_plot = df.plot(kind='bar', x='Day', y='Sales', color='skyblue')
bar_plot.set_title("Sales per Day")
bar_plot.set_ylabel("Sales ($)")
bar_plot.set_xlabel("Day")
plt.show()

# --- 2. Line plot ---
# X = 'Day', Y = 'Visitors'
line_plot = df.plot(kind='line', x='Day', y='Visitors', marker='o', color='green')
line_plot.set_title("Visitors per Day")
line_plot.set_ylabel("Number of Visitors")
line_plot.set_xlabel("Day")
plt.show()

# --- 3. Histogram ---
# Single column → X = values bins, Y = frequency
hist_plot = df['Sales'].plot(kind='hist', bins=5, color='orange', edgecolor='black')
hist_plot.set_title("Histogram of Sales")
hist_plot.set_xlabel("Sales ($)")
hist_plot.set_ylabel("Frequency")
plt.show()

# --- 4. Box plot ---
# Single column → X = position, Y = values
box_plot = df['Sales'].plot(kind='box', color='lightgreen')
box_plot.set_title("Boxplot of Sales")
box_plot.set_ylabel("Sales ($)")
plt.show()


