import pandas as pd

# Q1: Five functions of pandas library with execution
# Example of pandas functions
data = {'A': [1, 2, 3], 'B': [4, 5, 6]}
df = pd.DataFrame(data)

# 1. head():
print("head():\n", df.head())

# 2. describe():
print("describe():\n", df.describe())

# 3. info():
print("info():")
df.info()

# 4. isnull():
print("isnull():\n", df.isnull())

# 5. drop():
dropped_df = df.drop('A', axis=1)
print("drop():\n", dropped_df)

# Q2: Re-index DataFrame
def reindex_df(df):
    new_index = range(1, len(df)*2, 2)
    return df.set_index(pd.Index(new_index))

# Example usage
print(reindex_df(df))

# Q3: Calculate the sum of the first three values in 'Values'
def sum_first_three(df):
    total = df['Values'].iloc[:3].sum()
    print("Sum of first three values:", total)

# Example usage
values_df = pd.DataFrame({'Values': [10, 20, 30, 40, 50]})
sum_first_three(values_df)

# Q4: Add 'Word_Count' column
def add_word_count(df):
    df['Word_Count'] = df['Text'].apply(lambda x: len(x.split()))
    return df

# Example usage
text_df = pd.DataFrame({'Text': ["Vishal Kumar", "Data science is fun"]})
print(add_word_count(text_df))

# Q5: Difference between DataFrame.size and DataFrame.shape
print("DataFrame.size:", df.size)
print("DataFrame.shape:", df.shape)

# Q6: Function to read an Excel file
# df1 = pd.read_excel("D:\Data Science\Pandas\Lecture 2\Basic.xlsx", engine='openpyxl', file_format='xlrd')
# print(df1.head())


# Q7: Extract username from email
def extract_username(df):
    df['Username'] = df['Email'].apply(lambda x: x.split('@')[0])
    return df

# Example usage
email_df = pd.DataFrame({'Email': ["vishalkrxyz@gmail.com", "vishal2221416@gmail.com"]})
print(extract_username(email_df))

# Q8: Select rows based on column conditions
def filter_rows(df):
    return df[(df['A'] > 5) & (df['B'] < 10)]

# Example usage
example_df = pd.DataFrame({'A': [3, 8, 6, 2, 9], 'B': [5, 2, 9, 3, 1], 'C': [1, 7, 4, 5, 2]})
print(filter_rows(example_df))

# Q9: Calculate mean, median, and standard deviation
def calculate_stats(df):
    mean_val = df['Values'].mean()
    median_val = df['Values'].median()
    std_val = df['Values'].std()
    return mean_val, median_val, std_val

# Example usage
print(calculate_stats(values_df))

# Q10: Calculate 7-day moving average
def add_moving_average(df):
    df['MovingAverage'] = df['Sales'].rolling(window=7, min_periods=1).mean()
    return df

# Example usage
sales_df = pd.DataFrame({'Sales': range(1, 15)})
print(add_moving_average(sales_df))

# Q11: Add 'Weekday' column
def add_weekday(df):
    df['Weekday'] = pd.to_datetime(df['Date']).dt.day_name()
    return df

# Example usage
date_df = pd.DataFrame({'Date': ["2023-01-01", "2023-01-02", "2023-01-03", "2023-01-04", "2023-01-05"]})
print(add_weekday(date_df))

# Q12: Select rows within a date range
def filter_by_date(df):
    return df[(pd.to_datetime(df['Date']) >= "2023-01-01") & (pd.to_datetime(df['Date']) <= "2023-01-31")]

# Example usage
print(filter_by_date(date_df))

# Q13: Necessary library for pandas
# Answer: import pandas as pd
