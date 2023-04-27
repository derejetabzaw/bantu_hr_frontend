import fileinput
import pandas as pd
import numpy as np
import os
import pdfkit


def pdf_generator():
    #accepting csv input and reading it in data frame
    df = pd.read_csv('emplist.csv', encoding = "ISO-8859-1") 

    #exporting to pdf
    #converting to html
    f = open('exp.html','w', encoding = "ISO-8859-1")
    a = df.to_html()
    f.write(a)
    f.close()

    #converting the html to pdf
    pdfkit.from_file('exp.html', 'Attendance.pdf')
def excel_generator():
    #accepting csv input and reading it in data frame
    df = pd.read_csv('emplist.csv', encoding = "ISO-8859-1") 
    #exporting in excel form
    df.to_excel('Attendance.xlsx')