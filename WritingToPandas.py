import os
import pandas as pd
import re

# Master Dataframe
Cols = ['File Name', 'Impacted Line']
Mas_df = pd.DataFrame(columns=Cols)
# *****************Testing of Git*****************

def process_curr_file(path):
    Append_df = pd.DataFrame(columns=Cols)
    file = open(path, 'r')
    patt = re.compile(".*(import).*")
    try:
        for line in file:
            if re.search(patt, line):
                Append_df = Append_df.append({'File Name': path, 'Impacted Line': line}, ignore_index=True)
                # print(line)
    except UnicodeDecodeError:
        Append_df = Append_df.append({'File Name': 'Could not read ' + path, 'Impacted Line': '****Blank*****'},
                                     ignore_index=True)
    return Append_df


print("Enter Repo Name")
dir = input()

print("Looking into the repo " + dir + "........")

for path, Subdir, files in os.walk(dir):
    for name in files:
        # print(os.path.join(path,name))
        current_file = os.path.join(path, name)
        # if re.search(re.compile('(.java)$'), current_file) is not None:
        #     print(current_file)
        Mas_df = Mas_df.append(process_curr_file(os.path.join(path, name)))
des = 'OP_excel.xlsx'
print("Initiating Loading Data to " + des)
try:
    Mas_df.to_excel(des, index=False)
except:
    print("Something Went Wrong. **Look into Below Stacktrace**")
    print(Exception)
print("Extraction Completed :)")
# Reading a Directory

# for file in os.listdir(dir):

#     current_file = os.path.join(dir, file)

#     print(current_file)
