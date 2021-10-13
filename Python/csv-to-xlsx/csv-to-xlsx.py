import pandas as pd

# Reading CSV file
csv_filename = input('Enter the name of CSV file (without extension): ')
csv_df = pd.read_csv(csv_filename+'.csv')
print('Read successful for '+csv_filename+'.csv')

# Saving as Excel file
xlsx_file = pd.ExcelWriter(csv_filename+'.xlsx')
csv_df.to_excel(xlsx_file, index = False)
xlsx_file.save()
print(csv_filename+'.xlsx created successfully.')