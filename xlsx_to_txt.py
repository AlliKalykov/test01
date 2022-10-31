# Import pandas
import pandas as pd
import re

# # Load the xlsx file
# excel_data = pd.read_excel('chan.xlsx', index_col=0)
# print(excel_data)
# with open('chat.txt', 'w') as f:

#     for i in excel_data.index:
#         # re delete https://t.me/
#         print(i)
#         f.writelines(re.sub(r'https://t.me/', '', i)+'\n')

# excel_data = pd.read_excel('chan.xlsx', index_col=0, sheet_name='Каналы')
# with open('channels.txt', 'w') as f:

#     for i in excel_data.index:
#         # re delete https://t.me/
#         print(i)
#         f.writelines(re.sub(r'https://t.me/', '', i)+'\n')

with open('channels.txt') as file:
    lines = file.readlines()
    print(lines)
