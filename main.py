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

#  DataFrames, this is a whole table of rows and columns
myDataset = {
    'cars': ["BMW", "Volvo", "Ford"],
    'passings': [3, 7, 2]
}
myVar = pd.DataFrame(myDataset)
print(myVar)

print(myVar.loc[0])  # loc is used to print a row, here we are printing the first row
print(myVar.loc[[0, 1]])  # here we are printing the first and second row

data = {
    "calories": [420, 380, 390],
    "duration": [50, 40, 45]
}
df = pd.DataFrame(data, index=["day1", "day2", "day3"])  # Using names to hold the indexes
print(df)

print(df.loc["day2"])  # Locating a row using a named index
