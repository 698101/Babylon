import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import calendar
from scipy.stats import zscore

pd.set_option('display.max_colwidth', None)
pd.set_option('display.max_columns', None)
pd.set_option('display.max_rows', None)
pd.set_option('display.expand_frame_repr', False)

staff_Names = ['Aaron', 'Adam Sauer', 'Alex Barton', 'Ally', 'Andgil', 'Andrew', 'Asisipho', 'Asisipho', 'Awakhiwe', 'Belinda', 'Binold',
                    'Bongani', 'Bonisile', 'Bonisile', 'Brian', 'Brian', 'Brian Mtshali', 'Charlton', 'Cindy', 'Dario', 'Dean', 'Denley', 'Dennis',
                    'Dudu', 'Elle', 'Evans', 'F C W', 'Staff', 'GAAP', 'Giovanni', 'Godwin', 'Gugu', 'Hazel', 'Irvin', 'Joseph', 'Josh', 'Joyce',
                    'Keith', 'Keith', 'Kelvin', 'Kimberley', 'Linda', 'Lingani', 'Lisa', 'MC Ntuli', 'MIKE', 'Mkhuliseni', 'Mark', 'Mel', 'Michael Lembke',
                    'Misheck', 'Mtshali', 'Nelton', 'Nkosinathi', 'Nkosinathi', 'Ntokozo', 'Oliver', 'Oscar', 'Patrick', 'Pension', 'Petronella',
                    'Prince', 'Rakim', 'Sandile', 'Shaelyn', 'Siya', 'Siya Sibanda', 'Sylvester', 'Tawanda', 'Tembela', 'Thabo', 'Themba', 'Themba',
                    'Vic', 'Wandi', 'Wonderboy', 'Xolani', 'King']
#=========================================================================================================================================================
#Find path to Data
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
#=========================================================================================================================================================

#Creating a DataFrame to a corresponding path
df_Voids = pd.read_csv(file_path_Voids, header=1, skiprows=[0])
staff_counts = df_Voids[' Staff'].value_counts()

# print(staff_counts)
print(df_Voids)

#=========================================================================================================================================================
#CTC
df_CTC_Dict = pd.read_excel(file_path_CTC, sheet_name=None, skiprows=[0, 1], header=1)

columns_to_remove_CTC = [3, 9, 10]

for sheet_name, df in df_CTC_Dict.items():
    if isinstance(df, pd.DataFrame):
        df_CTC_Dict[sheet_name] = df.drop(df.columns[columns_to_remove_CTC], axis=1)

for sheet_name, df in df_CTC_Dict.items():
    if isinstance(df, pd.DataFrame):
        filtered_df = df[~df['Bartenders'].str.contains('Total|NaN|LEFT|WAITERS', case=False, na=False) & ~df['Bartenders'].isna()]
        df_CTC_Dict[sheet_name] = filtered_df

df_CTC_Jan = df_CTC_Dict['Jan 23']
df_CTC_Feb = df_CTC_Dict['Feb 23']
df_CTC_Mar = df_CTC_Dict['Mar 23']
df_CTC_Apr = df_CTC_Dict['Apr 23']
df_CTC_May = df_CTC_Dict['May 23']
df_CTC_Jun = df_CTC_Dict['June 23']
df_CTC_Jul = df_CTC_Dict['July 23']
df_CTC_Aug = df_CTC_Dict['Aug 23']
df_CTC_Sep = df_CTC_Dict['Sep 23']
df_CTC_Oct = df_CTC_Dict['Oct 23']
df_CTC_Nov = df_CTC_Dict['Nov 23']
df_CTC_Dec = df_CTC_Dict['Dec 23']
def simplify_Name(name):
    for staff_name in staff_Names:
        if staff_name in name:
            return staff_name
    return None

months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
column_names_CTC = ['Name', 'Cash Amount', 'Cash Percentage', 'Card Amount', 'Card Percentage', 'Total Amount', 'Decrease', 'Increase']

for month in months:
    df_name = f'df_CTC_{month}'
    current_df = locals()[df_name]
    current_df['Bartenders'] = current_df['Bartenders'].apply(simplify_Name)
    current_df.columns = column_names_CTC
    current_df = current_df.fillna(0)
    current_df = current_df
    # print(f"DataFrame {df_name}:")
    # print(current_df)
    # print()

df_CTC_Jan = df_CTC_Jan.sort_values(by='Name').reset_index(drop=True)
df_CTC_Feb = df_CTC_Feb.sort_values(by='Name').reset_index(drop=True)
df_CTC_Mar = df_CTC_Mar.sort_values(by='Name').reset_index(drop=True)
df_CTC_Apr = df_CTC_Apr.sort_values(by='Name').reset_index(drop=True)
df_CTC_May = df_CTC_May.sort_values(by='Name').reset_index(drop=True)
df_CTC_Jun = df_CTC_Jun.sort_values(by='Name').reset_index(drop=True)
df_CTC_Jul = df_CTC_Jul.sort_values(by='Name').reset_index(drop=True)
df_CTC_Aug = df_CTC_Aug.sort_values(by='Name').reset_index(drop=True)
df_CTC_Sep = df_CTC_Sep.sort_values(by='Name').reset_index(drop=True)
df_CTC_Oct = df_CTC_Oct.sort_values(by='Name').reset_index(drop=True)
df_CTC_Nov = df_CTC_Nov.sort_values(by='Name').reset_index(drop=True)
df_CTC_Dec = df_CTC_Dec.sort_values(by='Name').reset_index(drop=True)



#=========================================================================================================================================================
#Sales and Tips

df_Jan = pd.read_csv(file_path_Jan, sep=',', skiprows=[0, 1, 2, 3, 4, 5, 6, 7])
df_Feb = pd.read_csv(file_path_Feb, sep=',', skiprows=[0, 1, 2, 3, 4, 5, 6, 7])
df_Mar = pd.read_csv(file_path_Mar, sep=',', skiprows=[0, 1, 2, 3, 4, 5, 6, 7])
df_Apr = pd.read_csv(file_path_Apr, sep=',', skiprows=[0, 1, 2, 3, 4, 5, 6, 7])
df_May = pd.read_csv(file_path_May, sep=',', skiprows=[0, 1, 2, 3, 4, 5, 6, 7])
df_June = pd.read_csv(file_path_June, sep=',', skiprows=[0, 1, 2, 3, 4, 5, 6, 7])
df_July = pd.read_csv(file_path_July, sep=',', skiprows=[0, 1, 2, 3, 4, 5, 6, 7])
df_Aug = pd.read_csv(file_path_Aug, sep=',', skiprows=[0, 1, 2, 3, 4, 5, 6, 7])
df_Sep = pd.read_csv(file_path_Sep, sep=',', skiprows=[0, 1, 2, 3, 4, 5, 6, 7])
df_Oct = pd.read_csv(file_path_Oct, sep=',', skiprows=[0, 1, 2, 3, 4, 5, 6, 7])
df_Nov = pd.read_csv(file_path_Nov, sep=',', skiprows=[0, 1, 2, 3, 4, 5, 6, 7])
df_Dec = pd.read_csv(file_path_Dec, sep=',', skiprows=[0, 1, 2, 3, 4, 5, 6, 7])

#Sorting and Filtering all Data
column_names_Voids = ['Quantity', 'Item Code', 'Table', 'Invoice Number', 'Time', 'Date', 'Value', 'Name', 'Authorised By', 'Invoice Number', 'NaN']
df_Voids.columns = column_names_Voids
columns_to_remove_Voids = ['Item Code', 'Invoice Number', 'Table', 'NaN']
columns_to_remove_Income = ['No.', 'SL', 'Breakages', 'Cust', 'Earnings', 'Time', 'Levy', 'comm% 1%', 'Ave/Head', 'comm %2', ' CC Levy', ' Ave/Inv ']

df_Voids = df_Voids.drop(columns=columns_to_remove_Voids)
df_Jan = df_Jan.drop(columns=columns_to_remove_Income)
df_Feb = df_Feb.drop(columns=columns_to_remove_Income)
df_Mar = df_Mar.drop(columns=columns_to_remove_Income)
df_Apr = df_Apr.drop(columns=columns_to_remove_Income)
df_May = df_May.drop(columns=columns_to_remove_Income)
df_June = df_June.drop(columns=columns_to_remove_Income)
df_July = df_July.drop(columns=columns_to_remove_Income)
df_Aug = df_Aug.drop(columns=columns_to_remove_Income)
df_Sep = df_Sep.drop(columns=columns_to_remove_Income)
df_Oct = df_Oct.drop(columns=columns_to_remove_Income)
df_Nov = df_Nov.drop(columns=columns_to_remove_Income)
df_Dec = df_Dec.drop(columns=columns_to_remove_Income)

dfs = [df_Jan, df_Feb, df_Mar, df_Apr, df_May, df_June, df_July, df_Aug, df_Sep, df_Oct, df_Nov, df_Dec]
months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']

for i, df in enumerate(dfs):
    month_name = months[i]

    for column in ['Current', '(Ex) Tips', 'Service']:
        old_column_name = column
        new_column_name = f'{column}_{month_name}'
        df.rename(columns={old_column_name: new_column_name}, inplace=True)

#Merging the seperate Income DataFrames to 1
df_Income = dfs[0]
for df in dfs[1:]:
    df_Income = pd.merge(df_Income, df, on='Name', how='outer')

df_Income = df_Income.drop(df_Income.index[21:4118])
df_Income['Name'] = ['MC Ntuli', 'Thabo', 'Mike', 'Nkosinathi', 'Andrew', 'Xolani', 'Sylvester', 'Andgil', 'Brian Mtshali', 'Asisipho', 'Dario',
                     'Irvin', 'Dudu', 'Petronella', 'Gugu', 'Ntokozo', 'Micheal', 'Oscar', 'Binold', 'Dennis', 'Awakhiwe', 'Brian', 'Charlton',
                     'Shadreck', 'Cindy', 'Patrick', 'Themba', 'Hloni', 'Bonisile', 'Joyce', 'Linda', 'Wonderboy', 'Joseph', 'Staff', 'Mel',
                     'Bongani', 'King']

#Finding total Number of voids per Staff Member per month
df_Voids['Date'] = pd.to_datetime(df_Voids['Date'])
df_Voids['Month'] = df_Voids['Date'].dt.month
totalVoidsPMPE = df_Voids.groupby(['Name', 'Month'])['Quantity'].sum().reset_index()

#Modifying the Voids Dataframe to have the Month Columns
temp = df_Voids.groupby(['Name', 'Month'])['Quantity'].sum().reset_index()
df_Voids = temp.pivot(index='Name', columns='Month', values='Quantity').reset_index()
df_Voids.columns = ['Name'] + [f'Voids_{calendar.month_abbr[int(month)]}' for month in df_Voids.columns[1:]]
df_Voids = df_Voids.fillna(0)
df_Voids['Name'] = staff_Names

df_temp = pd.merge(df_Income, df_Voids, on='Name', how='outer')
df_temp = df_temp.sort_values(by='Name')
df_temp.at[11, 'Voids_Jun'] = 11
df_temp.at[4, 'Voids_Jun'] = 55
df_temp.at[4, 'Voids_Jul'] = 149
df_temp.at[4, 'Voids_Aug'] = 14
df_temp.at[4, 'Voids_Sep'] = 85
df_temp.at[4, 'Voids_Oct'] = 18
df_temp.at[4, 'Voids_Nov'] = 32
df_temp.at[4, 'Voids_Dec'] = 2
df_temp.at[24, 'Voids_Oct'] = 30
df_temp.at[32, 'Voids_Jun'] = 17
df_temp.at[30, 'Voids_May'] = 128
df_temp.at[30, 'Voids_Jun'] = 307
df_temp = df_temp.drop([3, 10, 23, 29, 33])
df_temp = df_temp.fillna(0)
df_Final = df_temp.reset_index(drop=True)

df_Total_Sales = df_Final[['Name'] + [col for col in df_Final.columns if col.startswith('Current')]]
df_Total_Voids = df_Final[['Name'] + [col for col in df_Final.columns if col.startswith('Voids')]]
df_Total_Tips = df_Final[['Name'] + [col for col in df_Final.columns if col.startswith('(Ex)')]]
df_Total_Service = df_Final[['Name'] + [col for col in df_Final.columns if col.startswith('Service')]]

for row in range(1, 75):
    for col in range(1, 13):
        df_Total_Tips.iat[row, col] = float(df_Total_Tips.iat[row, col]) + float(df_Total_Service.iat[row, col])

# print(df_Total_Sales, '\n', '\n',
#       df_Total_Tips, '\n', '\n',
#       df_Total_Voids, '\n', '\n')

# temp = df_Final.set_index(df_Final.columns[0]).transpose()
# print(temp[temp.index.str.startswith('Current')])
# print('\n')
# print(temp[temp.index.str.startswith('(Ex)')])
# print('\n')
# print(temp[temp.index.str.startswith('Voids')])
# print('\n')

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

    temp_Sales = df_Total_Sales[df_Total_Sales['Name'] == f'{name}']
    if not temp_Sales.empty:
        dfs_Staff_Members[f'{name}'].iloc[0, 1:] = temp_Sales.values[0, 1:]

    temp_Tips = df_Total_Tips[df_Total_Tips['Name'] == f'{name}']
    if not temp_Tips.empty:
        dfs_Staff_Members[f'{name}'].iloc[1, 1:] = temp_Tips.values[0, 1:]

    temp_Voids = df_Total_Voids[df_Total_Voids['Name'] == f'{name}']
    if not temp_Voids.empty:
        dfs_Staff_Members[f'{name}'].iloc[2, 1:] = temp_Voids.values[0, 1:]

    for month in months:
        df_month = globals()[f'df_CTC_{month}']
        if name in df_month['Name'].values:
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

    # print(dfs_relevant[name], '\n')

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
