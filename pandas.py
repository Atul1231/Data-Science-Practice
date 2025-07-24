#pandas is a data manipulation and analysis library for Python.
# It provides data structures like Series and DataFrame for handling structured data.
## It is widely used for data analysis, cleaning, and manipulation tasks.
#Mckinsey created pandas in 2008.

#series is a one-dimensional labeled array capable of holding any data type.
#dataframe is a two-dimensional labeled data structure with columns of potentially different types.
#first step is to import pandas library
import pandas as pd
#now first we will read a csv file using pandas
df=pd.read_csv("data.csv" ,encoding="utf-8" ) #or we can use latin1  # Assuming data.csv is in the same directory
#display the first 5 rows of the dataframe
print(df.head())
pn=pd.read_excel("data.xlsx")  # Assuming data.xlsx is in the same directory
#display the first 5 rows of the dataframe
print(pn.head())
np=pd.read_json("data.json")  # Assuming data.json is in the same directory
#display the first 5 rows of the dataframe
print(np.head())


#saving a dataframe to a csv file
#first we will create a dataframe
data={
    "Name": ["Alice", "Bob", "Charlie"],
    "Age": [25, 30, 35],
    "City": ["New York", "Los Angeles", "Chicago"]
}
# convert to dataframe
df=pd.DataFrame(data)
df.to_csv("output.csv", index=False)  # Save DataFrame to CSV without index
df.to_excel("output.xlsx", index=False)  # Save DataFrame to Excel without index
df.to_json("output.json", orient="records")  # Save DataFrame to JSON in records format


#head and tail methods
#head() returns the first n rows of the DataFrame or else it will givr the first 5 rows
#tail() returns the last n rows of the DataFrame or else it will give the last 5 rows

#decribing the dataframe
df.describe()  # Returns a statistical summary of the DataFrame
# This includes count, mean, std, min, 25%, 50%, 75%, max for numeric columns

#berfore manipulation we need to check how big is the dataset
#what are the name of the columns
print(df.shape)  # Returns the number of rows and columns in the DataFrame
print(df.columns)  # Returns the names of the columns in the DataFrame
print(df.info())  # Returns a concise summary of the DataFrame, including data types and non-null counts

#selecting columns
#we can select a single column or multiple columns
#single_column = df['Name']  # Select a single column
#multiple_columns = df[['Name', 'Age']]  # Select multiple columns
##filtering rows
#we can filter rows based on a condition
#filtered_rows = df[df['Age'] > 30]  # Select rows where Age
# is greater than 30

#multiple_conditions = df[(df['Age'] > 30) & (df['City'] == 'Chicago')]  # Multiple conditions

#advance pandas
data={
    "name":["ravi","kiran","suresh"],
    "age":[23,24,25],
    "salary":[1000,2000,3000],
    "performance":[1,2,3]
}

#adding a new column
df=pd.DataFrame(data)
df['bonus'] = df['salary'] * 0.1  # Adding a new column 'bonus' which is 10% of 'salary'
print(df)

#now using insert method to add a new column at a specific position
df.insert(2, 'department', ['HR', 'Finance', 'IT'])  # Insert 'department' column at index 2
print(df)

#updating values in a column
df.loc[df['name'] == 'ravi', 'salary'] = 1500  # Update salary for 'ravi'
print(df)

#deleting the column
df.drop(columns=["department"] , inplace=True)
print(df)

#handling the missing values
#we can check for missing values using isnull() method
is_null = df.isnull()  # Returns a DataFrame of boolean values indicating missing values
print(is_null)
#summing the missing values
print(df.isnull().sum())  # Returns the count of missing values in each column

#filling the missing values
df.fillna(value=0, inplace=True)  # Fill missing values with 0
print(df)

#interpolating the missing values
#method to fill missing values using interpolation
#linear interpolation
#1- preserve data integrity


#sorting the dataframe
df.sort_values(by='age', ascending=False , inplace=True)  # Sort by 'age' in ascending order
print(df)

#summarizing the data
df['salary'].sum()  # Returns the sum of the 'salary' column
print("variance: ", df['salary'].var())  # Returns the variance of the 'salary' column
print("mean: ", df['salary'].mean())  # Returns the mean of the 'salary' column
print("max: ", df['salary'].max())  # Returns the maximum value of the 'salary' column
print("standard deviation: ", df['salary'].std())  # Returns the standard deviation of the 'salary' column
print("min: ", df['salary'].min())  # Returns the minimum value of the 'salary' column

df.groupby('performance').mean()  # Group by 'performance' and calculate mean for each group

#merging and joining dataframes
#we can merge two dataframes using merge() method
#we can join two dataframes using join() method

df_customer = pd.DataFrame({
    'customer_id': [1, 2, 3],
    'customer_name': ['Alice', 'Bob', 'Charlie']
})

df_order = pd.DataFrame({
    'order_id': [101, 102, 103],
    'customer_id': [1, 2, 4],
    'order_amount': [250, 150, 300]
})

df_merged = pd.merge(df_customer, df_order, on='customer_id', how='inner')  # Inner join on 'customer_id' - returns only matching rows
print(df_merged)

df_merged_outer = pd.merge(df_customer, df_order, on='customer_id', how='outer')  # Outer join - returns all rows
print(df_merged_outer)

df_merged_left = pd.merge(df_customer, df_order, on='customer_id', how='left')  # Left join - returns all rows from df_customer
print(df_merged_left)

df_merged_right = pd.merge(df_customer, df_order, on='customer_id', how='right')  # Right join - returns all rows from df_order
print(df_merged_right)


#concatenating dataframes
pd.concat([df_customer, df_order], axis=0,ignore_index=True)  # Concatenate along rows - vertical stacking
pd.concat([df_customer, df_order], axis=1,ignore_index=True)  # Concatenate along columns  # - horizontal stacking




