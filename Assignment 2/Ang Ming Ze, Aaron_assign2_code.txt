#import libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plot
plot.style.use('fivethirtyeight')

#loading data and reading data from excel file
df = pd.read_excel (r'C:\Users\draco\OneDrive - Nanyang Technological University\Desktop\Python Assignment 2\SPY_2016_2021.xlsx') 
#place "r" before the path string to address special character, such as '\'. Don't forget to put the file name at the end of the path + '.xlsx'

df['Close']= round(df['Close'],2)
print (df)


#Visually show the stock price (graphical figure)

plot.figure(figsize=(15,5))
plot.plot(df['Close'], label='Close')
plot.xticks(rotation=0) #rotate the x axis 45 degrees downwards
plot.title('Close Price History')
plot.xlabel('Date')
plot.ylabel('Close Price (in $)')

#Show stock buy and sell signals
def plotbuySell():
    #Show the stock buy and sell signals
    plot.figure(figsize=(15,5))

    #instantiate a buy signal if MACD line goes over Signal Line, show the signal with a upper triangle
    plot.scatter(df.index, df['Buy_Signal_price'], color= 'blue', label= 'Buy', marker='^', alpha=1)
    #instantiate a sell signal if MACD line goes under Signal Line, show the signal with a lower triangle
    plot.scatter(df.index, df['Sell_Signal_price'], color= 'red', label= 'Sell', marker='v', alpha=1)

    plot.plot(df['Close'], label='Close Price (in$)', alpha=0.35)
    plot.title('Close Buy & Sell Signals')
    plot.xlabel('Data')
    plot.ylabel('Close Price (in $)')
    plot.legend(loc= 'lower right')
    plot.show()
    return 0

#define function buySell for EMA calculation of buy signal and sell signals
#Function to signal when to buy and sell
def buySell(signal):
    Buy= []
    Sell= []
    flag= -1
    totalCapital = 100000.00
    Sum=0
    netGain= []
    tradeCounter=0
    for i in range(0, len(signal)):
        if signal['MACD line'][i]> signal['Signal line'][i]:
            Sell.append(np.nan)
            
            if flag !=1:
                Buy.append(signal['Close'][i])
                Sum = round((Sum -(1.125) *(signal['Close'][i])),2)
                netGain.append(Sum)
                tradeCounter+=1
                flag=1
            else:
                Buy.append(np.nan)
                netGain.append(np.nan)
        elif signal['MACD line'][i]< signal['Signal line'][i]:
            Buy.append(np.nan)
            
            if flag !=0:
                Sell.append(signal['Close'][i])
                Sum = round((Sum + 0.875*(signal['Close'][i])),2)
                netGain.append(Sum)
                tradeCounter+=1
                flag=0
            else:
                Sell.append(np.nan)
                netGain.append(np.nan)
                
        else:
            Buy.append(np.nan)
            Sell.append(np.nan)
            netGain.append(np.nan)
            
    return (Buy, Sell, netGain, tradeCounter)
                
        
def EMA():
    #Calculation for MACD line and signal lines

    #Calculation of SEMA and LEMA (short and long term exponential moving average)
    #SMA N=12, LMA=26
    SEMA= round((df.Close.ewm(span=12, adjust=False).mean()),2)
    LEMA= round((df.Close.ewm(span=26, adjust= False).mean()),2)

    print("The SEMA column is:\n", SEMA)
    print("The LEMA column is:\n",LEMA)
    df['SEMA']= SEMA
    df['LEMA']= LEMA

    #Calculation of MACD line
    MACD= round((SEMA - LEMA),2)

    #Calculation of Signal line
    Signal= round((MACD.ewm(span=9, adjust=False).mean()),2)

    #Show the MACD line and Signal line in the graph
    plot.figure(figsize=(15,5))
    plot.plot(df.index, MACD, label= 'MACD line', color= 'green')
    plot.plot(df.index, Signal, label= 'Signal line', color= 'yellow')
    plot.legend(loc='lower left') #legend is at the lower left hand corner
    plot.show()

    #Write new columns in excel file for MACD line and signal line
    df['MACD line']= MACD
    df['Signal line']= Signal


    #write buy and sell columns in excel file given
    a= buySell(df)
    df['Buy_Signal_price'] = a[0]
    df['Sell_Signal_price'] = a[1]
    df['NetGain']= a[2]
    print(df)
    #Call function to show the plot for buy and sell signals
    plotbuySell()

    #transfer and write all new data into an excel sheet
    df.to_excel('Updated_SPY_2016_2021.xlsx')
    #print summary of code run:
    print("Summary of code run:\n")
    tradeCounter=a[3]
    print("The total number of trades is", tradeCounter)
    grandTotal= df['NetGain'].sum()
    avgReturn= round((grandTotal/tradeCounter),2)
    print("The average return per trade is", avgReturn)
    longBuyHoldSell=(468.14*0.875)-(201.36*1.125)
    relativeGainLoss=  round((((grandTotal-longBuyHoldSell)/ longBuyHoldSell) *100),2)
    print("The relative gain/loss against the long term Buy-Hold-Sell strategy is ", relativeGainLoss, end='%')
    return 0



choice= int(input("Enter choice to use EMA (exponential moving average) or SSMA (Standard Simple Moving Average):\n"))

if choice==1:
    EMA()
elif choice==2:
    def SMA(inputed, length):
    
        movingAvg= []
        if length ==12 or length==26:
            for i in range(length-1):
                movingAvg.append(0.00)
        if length ==9:
            for i in range (33-1):
                movingAvg.append(0.00)
        i=0
            
        while i < len(inputed) - length + 1:
        
        # Store elements from i to i+length
        # in list to get the current window
            window = inputed[i : i + length]
    
        # Calculate the average of current window
            computed = round(np.sum(inputed[i:i+length]) / length, 2)
        
        # Store the average of current in movingAvg
            movingAvg.append(computed)
        
        # Shift the window of size length to right by one position
            i += 1
        #assign NaN to data without a value   
        result= np.array(movingAvg)
        MA= pd.Series(result)
        return MA
    
    def SSMA():
    #calculate SSMA and LSMA
        inputed= df['Close']
        SSMA= round((SMA(inputed, 12)),2)
        LSMA= round((SMA(inputed, 26)),2)
        #calculate MACD line
        MACD= round((SSMA- LSMA),2)
        df['MACD line']= MACD
        #calculate signal line
        inputed= MACD
        Signal= round((SMA(inputed, 9)),2)
        df['Signal line']= Signal

         #Show the MACD line and Signal line in the graph
        plot.figure(figsize=(15,5))
        plot.plot(df.index, MACD[0:1511], label= 'MACD line', color= 'green')
        plot.plot(df.index, Signal[0:1511], label= 'Signal line', color= 'yellow')
        plot.legend(loc='lower left') #legend is at the lower left hand corner
        plot.show()

        #write buy and sell columns in excel file given
        #calling function buySell to initiate buy and sell signals
        a= buySell(df)
        df['Buy_Signal_price'] = a[0]
        df['Sell_Signal_price'] = a[1]
        df['NetGain']= a[2]
        
        #Call function to show the plot for buy and sell signals
        plotbuySell()
        #Write updated file to excel file
        df.to_excel('UpdatedSSMA_SPY_2016_2021.xlsx')
        print(df)

        #print summary of code run:
        print("Summary of code run:\n")
        tradeCounter=a[3]
        print("The total number of trades is", tradeCounter)
        grandTotal= df['NetGain'].sum()
        avgReturn= round((grandTotal/tradeCounter),2)
        print("The average return per trade is", avgReturn)
        longBuyHoldSell=(450*0.875)-(185.65*1.125)
        relativeGainLoss=  round((((grandTotal-longBuyHoldSell)/ longBuyHoldSell) *100),2)
        print("The relative gain/loss against the long term Buy-Hold-Sell strategy is ", relativeGainLoss, end='%')
    SSMA()
    
