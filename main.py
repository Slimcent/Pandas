import pandas as pd

#  Series, these are columns
a = [1, 7, 2]
mySeries = pd.Series(a)
print(mySeries)

a = [1, 7, 2]
mySeries = pd.Series(a, index=["x", "y", "z"])  # Adding labels to a series, which then serves as the index
print(mySeries)

print(mySeries["y"])  # using label "y" to get a series value

calories = {"day1": 420, "day2": 380, "day3": 390}  # Using a dictionary, the keys then serves as the index
mySeries = pd.Series(calories)
print(mySeries)

calories = {"day1": 420, "day2": 380, "day3": 390}  # Using a dictionary, the keys then serves as the index
mySeries = pd.Series(calories, index=["day1", "day2"])  # Displaying the keys we want to output
print(mySeries)

print()


