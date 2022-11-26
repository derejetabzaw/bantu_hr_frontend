import fileinput
import pandas as pd
import numpy as np
import os


#accepting csv input and reading it in data frame
df = pd.read_csv('emplist.csv', encoding = "ISO-8859-1") 
#exporting in excel form
df.to_excel('Attendance.xlsx')