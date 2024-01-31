import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import calendar
from scipy.stats import zscore

pd.set_option('display.max_colwidth', None)
pd.set_option('display.max_columns', None)
pd.set_option('display.max_rows', None)
pd.set_option('display.expand_frame_repr', False)

# =========================================================================================================================================================

staff_Names = ['Aaron', 'Adam Sauer', 'Alex Barton', 'Ally', 'Andgil', 'Andrew',
               'Asisipho', 'Asisipho', 'Awakhiwe', 'Belinda', 'Binold', 'Bongani',
               'Bonisile', 'Bonisile', 'Brian', 'Brian', 'Brian Mtshali', 'Charlton',
               'Cindy', 'Dario', 'Dean', 'Denley', 'Dennis', 'Dudu', 'Elle', 'Evans',
               'F C W', 'Staff', 'GAAP', 'Giovanni', 'Godwin', 'Gugu', 'Hazel', 'Hloni',
               'Irvin', 'Joseph', 'Josh', 'Joyce', 'Keith', 'Keith', 'Kelvin', 'Kimberley',
               'Linda', 'Lingani', 'Lisa', 'MC Ntuli', 'MIKE', 'Mkhuliseni', 'Mark', 'Mel',
               'Michael Lembke', 'Misheck', 'Mtshali', 'Nelton', 'Nkosinathi', 'Nkosinathi',
               'Ntokozo', 'Oliver', 'Oscar', 'Patrick', 'Pension', 'Petronella', 'Prince',
               'Rakim', 'Sandile', 'Shaelyn', 'Shadreck', 'Siya', 'Siya Sibanda', 'Sylvester',
               'Tawanda', 'Tembela', 'Thabo', 'Themba', 'Themba','Vic', 'Wandi', 'Wonderboy',
               'Xolani', 'King']

months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']

# Function that simplifies the names of staff members in the respective cells
def simplify_Name(name):
    for staff_name in staff_Names:
        if staff_name in name:
            return staff_name
    return None

# =========================================================================================================================================================

# Find path to Data
file_path_Voids = r'C:\Users\bossb\OneDrive\Documents\test\pythonProject\Data Science\Voids.csv'
file_path_CTC = r'C:\Users\bossb\OneDrive\Documents\test\pythonProject\Data Science\Cash VS Card.xlsx'
file_path_Jan = r'C:\Users\bossb\OneDrive\Documents\test\pythonProject\Data Science\Staff_Income_Jan.csv'
file_path_Feb = r'C:\Users\bossb\OneDrive\Documents\test\pythonProject\Data Science\Staff_Income_Feb.csv'
file_path_Mar = r'C:\Users\bossb\OneDrive\Documents\test\pythonProject\Data Science\Staff_Income_Mar.csv'
file_path_Apr = r'C:\Users\bossb\OneDrive\Documents\test\pythonProject\Data Science\Staff_Income_Apr.csv'
file_path_May = r'C:\Users\bossb\OneDrive\Documents\test\pythonProject\Data Science\Staff_Income_May.csv'
file_path_June = r'C:\Users\bossb\OneDrive\Documents\test\pythonProject\Data Science\Staff_Income_June.csv'
file_path_July = r'C:\Users\bossb\OneDrive\Documents\test\pythonProject\Data Science\Staff_Income_July.csv'
file_path_Aug = r'C:\Users\bossb\OneDrive\Documents\test\pythonProject\Data Science\Staff_Income_Aug.csv'
file_path_Sep = r'C:\Users\bossb\OneDrive\Documents\test\pythonProject\Data Science\Staff_Income_Sep.csv'
file_path_Oct = r'C:\Users\bossb\OneDrive\Documents\test\pythonProject\Data Science\Staff_Income_Oct.csv'
file_path_Nov = r'C:\Users\bossb\OneDrive\Documents\test\pythonProject\Data Science\Staff_Income_Nov.csv'
file_path_Dec = r'C:\Users\bossb\OneDrive\Documents\test\pythonProject\Data Science\Staff_Income_Dec.csv'

# =========================================================================================================================================================

# Creating a DataFrame of all voids, tallying up the total number of authorized voids by mangers
df_Total_Voids = pd.read_csv(file_path_Voids, header=1, skiprows=[0])
manager_total_authorized_voids = df_Total_Voids[' Staff'].value_counts()

# Renaming the columns in the Voids DataFrame, sorting through the Voids DataFrame and removing certain columns
column_names_Voids = ['Quantity', 'Item Code', 'Table', 'Invoice Number', 'Time', 'Date', 'Value', 'Name', 'Authorised By', 'Invoice Number', 'NaN']
df_Total_Voids.columns = column_names_Voids
columns_to_remove_Voids = ['Item Code', 'Invoice Number', 'Table', 'NaN']
df_Total_Voids = df_Total_Voids.drop(columns=columns_to_remove_Voids)

# Convert 'Date' column to datetime type
df_Total_Voids['Date'] = pd.to_datetime(df_Total_Voids['Date'])

# Extract month from 'Date' column and create a new column called 'Month'
df_Total_Voids['Month'] = df_Total_Voids['Date'].dt.month_name()

# -- CHECKED

# =========================================================================================================================================================

# Creating a DataFrame of all Cash to Card ratios of staff members
df_CTC_Dict = pd.read_excel(file_path_CTC, sheet_name=None, skiprows=[0, 1], header=1)

# Sorting the DataFrame by removing certain columns
columns_to_remove_CTC = [3, 9, 10]
for sheet_name, df in df_CTC_Dict.items():
    if isinstance(df, pd.DataFrame):
        df_CTC_Dict[sheet_name] = df.drop(df.columns[columns_to_remove_CTC], axis=1)

# Sorting the DataFrame by removing certain rows; Rows that contain 'Total', 'NaN', 'Left', 'Waiters'
for sheet_name, df in df_CTC_Dict.items():
    if isinstance(df, pd.DataFrame):
        filtered_df = df[~df['Bartenders'].str.contains('Total|NaN|LEFT|WAITERS', case=False, na=False) & ~df['Bartenders'].isna()]
        df_CTC_Dict[sheet_name] = filtered_df

# Dictionary to store the Cash to Card month DataFrames
df_CTC_Dict_Months = {}

# Iterate over months list and create individual corresponding Cash to Card DataFrames per month
for month in months:
    if month == 'Jun':
        df_CTC_Dict_Months[f'df_CTC_{month}'] = df_CTC_Dict['June 23']
    elif month == 'Jul':
        df_CTC_Dict_Months[f'df_CTC_{month}'] = df_CTC_Dict['July 23']
    else:
        df_CTC_Dict_Months[f'df_CTC_{month}'] = df_CTC_Dict[f'{month} 23']

column_names_CTC = ['Name', 'Cash Amount', 'Cash Percentage', 'Card Amount', 'Card Percentage', 'Total Amount', 'Decrease', 'Increase']

# Iterating over the Cash to Card month DataFrames, simplifying staff member names, changing column names, arranging names in alphabetical order and resetting the index
for month in months:
    df_name = f'df_CTC_{month}'
    current_df = df_CTC_Dict_Months[df_name]
    current_df['Bartenders'] = current_df['Bartenders'].apply(simplify_Name)
    current_df.columns = column_names_CTC
    current_df = current_df.fillna(0)
    current_df['Name'] = current_df['Name'].astype(str)  # Convert 'Name' column to string
    current_df = current_df.sort_values(by='Name').reset_index(drop=True)

# -- CHECKED

# =========================================================================================================================================================

# Dictionary to store the Sales and Tips month DataFrames
df_Sales_Tips_Dict_Months = {}

# Sorting the DataFrame by removing certain columns; 'No.', 'SL', 'Breakages', 'Cust', 'Earnings', 'Time', 'Levy', 'comm% 1%', 'Ave/Head', 'comm %2', ' CC Levy', ' Ave/Inv'
columns_to_remove_Sales_Tips = ['No.', 'SL', 'Breakages', 'Cust', 'Earnings', 'Time', 'Levy', 'comm% 1%', 'Ave/Head', 'comm %2', ' CC Levy', ' Ave/Inv ']

# Iterate over months list, creating respective DataFrames for each month, assign new column names and filter out irreleveant rows
for month in months:
    if month == 'Jun':
        current_df = pd.read_csv(file_path_June, sep=',', skiprows=[0, 1, 2, 3, 4, 5, 6, 7])
    elif month == 'Jul':
        current_df = pd.read_csv(file_path_July, sep=',', skiprows=[0, 1, 2, 3, 4, 5, 6, 7])
    else:
        current_df = pd.read_csv(eval(f'file_path_{month}'), sep=',', skiprows=[0, 1, 2, 3, 4, 5, 6, 7])
    current_df = current_df.drop(columns=columns_to_remove_Sales_Tips)
    df_Sales_Tips_Dict_Months[f'df_Sales_Tips_{month}'] = current_df
    for column in ['Current', '(Ex) Tips', 'Service']:
        old_column_name = column
        new_column_name = f'{column}_{month}'
        current_df.rename(columns={old_column_name: new_column_name}, inplace=True)

# Extract DataFrames from the dictionary into a list
dfs = list(df_Sales_Tips_Dict_Months.values())

# Initialize df_Income with the first DataFrame
df_Sales_Tips = dfs[0]

# Loop through the remaining DataFrames and merge them with df_Income
for df in dfs[1:]:
    df_Sales_Tips = pd.merge(df_Sales_Tips, df, on='Name', how='outer')

# Dropping empty rows in the given interval
df_Sales_Tips = df_Sales_Tips.drop(df_Sales_Tips.index[21:4118])

# Simplifying the Name column
df_Sales_Tips['Name'] = df_Sales_Tips['Name'].apply(simplify_Name)

# Replacing all 'NaN' values with 0, resetting the index, removing old index column
df_Sales_Tips = df_Sales_Tips.fillna(0).reset_index().drop('index', axis=1)

for month in months:
    # Get the values from the respective columns
    tips = df_Sales_Tips[f'(Ex) Tips_{month}']
    service = df_Sales_Tips[f'Service_{month}']

    # Add tips and service together and assign to a new column
    df_Sales_Tips[f'Tips {month}'] = pd.to_numeric(tips, errors='coerce') + pd.to_numeric(service, errors='coerce')

    # Drop the original columns
    df_Sales_Tips.drop(columns=[f'Service_{month}', f'(Ex) Tips_{month}'], inplace=True)

    df_Sales_Tips.rename(columns={f'Current_{month}':f'Sales {month}'}, inplace=True)

# -- CHECKED

# =========================================================================================================================================================

# Creates new DataFrame where the month names are new columns and sorts all data to see total number of voids per staff member per month
temp = df_Total_Voids.groupby(['Name', 'Month'])['Quantity'].sum().reset_index()
df_Voids = temp.pivot(index='Name', columns='Month', values='Quantity').reset_index()

# Sort columns in ascending order of months
sorted_columns = ['Name'] + sorted(df_Voids.columns[1:], key=lambda x: pd.to_datetime(x, format='%B'))

# Reorder columns
df_Voids = df_Voids[sorted_columns]

# Simplifying the staff names
df_Voids['Name'] = df_Voids['Name'].apply(simplify_Name)

# Adds up the values of repeated names
df_Voids = df_Voids.groupby('Name').sum().reset_index()

# Fill NaN values with 0
df_Voids = df_Voids.fillna(0)

# Get abbreviated month names
full_month_names = df_Voids.columns[1:]
abbr_month_names = [calendar.month_abbr[pd.to_datetime(month, format='%B').month] for month in full_month_names]

# Rename columns to match the desired format
df_Voids.columns = ['Name'] + [f'Voids {abbr}' for abbr in abbr_month_names]

# -- CHECKED

# =========================================================================================================================================================

# Merge the Sales, Tips and Voids together into 1 DataFrame
df_temp = pd.merge(df_Sales_Tips, df_Voids, on='Name', how='outer')
df_temp = df_temp.sort_values(by='Name').fillna(0)
df_Sales_Tips_Voids = df_temp.reset_index(drop=True)

# Creating neat, seperate DataFrames for the sections: Sales, Tips and Voids
df_Total_Staff_Sales = df_Sales_Tips_Voids[['Name'] + [col for col in df_Sales_Tips_Voids.columns if col.startswith('Sales')]]
df_Total_Staff_Tips = df_Sales_Tips_Voids[['Name'] + [col for col in df_Sales_Tips_Voids.columns if col.startswith('Tips')]]
df_Total_Staff_Voids = df_Sales_Tips_Voids[['Name'] + [col for col in df_Sales_Tips_Voids.columns if col.startswith('Voids')]]

# -- CHECKED

#=========================================================================================================================================================
dfs_Staff_Members = {}
dfs_relevant = {}
relevant_names = []
dfs_irrelevant = {}
irrelevant_names = []

#Creates a DataFrame for each staff member and records their  total sales, tips, voids and CTC
for name in staff_Names:
    data = {
        f'{name} Analysis': ['Total Sales', 'Total Tips', 'Total Voids', 'Total Cash', 'Cash Percentage', 'Total Card', 'Card Percentage', 'Total CTC Sum'],
        'Jan': [0, 0, 0, 0, 0, 0, 0, 0],
        'Feb': [0, 0, 0, 0, 0, 0, 0, 0],
        'Mar': [0, 0, 0, 0, 0, 0, 0, 0],
        'Apr': [0, 0, 0, 0, 0, 0, 0, 0],
        'May': [0, 0, 0, 0, 0, 0, 0, 0],
        'Jun': [0, 0, 0, 0, 0, 0, 0, 0],
        'Jul': [0, 0, 0, 0, 0, 0, 0, 0],
        'Aug': [0, 0, 0, 0, 0, 0, 0, 0],
        'Sep': [0, 0, 0, 0, 0, 0, 0, 0],
        'Oct': [0, 0, 0, 0, 0, 0, 0, 0],
        'Nov': [0, 0, 0, 0, 0, 0, 0, 0],
        'Dec': [0, 0, 0, 0, 0, 0, 0, 0]
    }
    df_person = pd.DataFrame(data)
    dfs_Staff_Members[name] = df_person

    temp_Sales = df_Total_Staff_Sales[df_Total_Staff_Sales['Name'] == f'{name}']
    if not temp_Sales.empty:
        dfs_Staff_Members[f'{name}'].iloc[0, 1:] = temp_Sales.values[0, 1:]

    temp_Tips = df_Total_Staff_Tips[df_Total_Staff_Tips['Name'] == f'{name}']
    if not temp_Tips.empty:
        dfs_Staff_Members[f'{name}'].iloc[1, 1:] = temp_Tips.values[0, 1:]

    temp_Voids = df_Total_Staff_Voids[df_Total_Staff_Voids['Name'] == f'{name}']
    if not temp_Voids.empty:
        dfs_Staff_Members[f'{name}'].iloc[2, 1:] = temp_Voids.values[0, 1:]

    for month in months:
        df_month = f'df_CTC_{month}'
        current_df = df_CTC_Dict_Months[df_month]
        if name in current_df['Name'].values:
            name_index = (df_month.index[df_month['Name'].str.startswith(name).fillna(False)]).values[0]
            values_row = df_month.loc[name_index, 'Cash Amount':'Total Amount'].values
            for i in range(0, 5):
                dfs_Staff_Members[f'{name}'].loc[i+3, month] = values_row[i]

    num_zeros_in_any_row = (dfs_Staff_Members[name] == 0).sum(axis=1) >= 6

    if num_zeros_in_any_row.any():
        dfs_irrelevant[name] = dfs_Staff_Members[name]
        irrelevant_names.append(name)
        # print(name, ' was added to the irrelevant list')
    else:
        dfs_relevant[name] = dfs_Staff_Members[name]
        relevant_names.append(name)
        dfs_relevant[name].to_csv(f'{name}_df.csv', index=False)
        # print(name, ' was added to the relevant list')

for name in relevant_names:
    df = dfs_relevant[name]
    selected_columns = df.iloc[:, 1:13]
    selected_columns = selected_columns.apply(pd.to_numeric, errors='coerce')

    print(dfs_relevant[name], '\n')

    for index, row in selected_columns.iterrows():
        non_zero_values_row = [value for value in row if value != 0]
        mean = np.mean(non_zero_values_row)
        Q1 = np.percentile(non_zero_values_row, 25)
        Q3 = np.percentile(non_zero_values_row, 75)
        IQR = Q3 - Q1
        lower_fence = Q1 - 1.5*IQR
        upper_fence = Q3 + 1.5*IQR
        outliers = [value for value in non_zero_values_row if value > upper_fence or value < lower_fence]
        # print('The stats for', name)
        # print(df.at[index, f'{name} Analysis'])
        # print('Mean: ', mean)
        # print('Q1:', Q1)
        # print('Q3:', Q3)
        # print('IQR:', IQR)
        # print('Outliers: ', outliers, '\n')
