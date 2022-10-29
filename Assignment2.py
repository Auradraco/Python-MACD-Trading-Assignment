

#import excel file to assignment2.py
import queue
import openpyxl
import pandas as pd
df = pd.read_excel (r'C:\Users\draco\OneDrive - Nanyang Technological University\Desktop\Python Assignment 2\SPY_2016_2021.xlsx') #place "r" before the path string to address special character, such as '\'. Don't forget to put the file name at the end of the path + '.xlsx'
df2= df[["Close"]]
print (df)
print (df2)

def SMA (inputfile, Length, computedfile):
    Length= int(input("Enter the number of days for moving average required: \n"))
    inputfile= df2
    sma= queue.Queue(Length)
    while (i<=1510):
        for i in range(Length):
            sma.put(df2)
            print("pushed item", sma)
            sum += sma[i]
            if sma.full():
                break
        computedfile= sum/Length

        

    
    

