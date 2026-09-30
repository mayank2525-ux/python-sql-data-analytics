#importing libraries, reading csv & making changes
import sys
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
pd.set_option('display.max_columns',None)
pd.set_option('display.width',None)
df=pd.read_csv('Wolrd Population Data.csv')
df=df.dropna(how='all')
df=df.dropna(axis=1,how='all')


#main menu coding
def menu():
       while True:
           print("""most populated countries in the world analyses
1 Data Visualisation
2 Data Analysis
3 Data Modification
4 Exit""")
           i=int(input('Enter your choice'))
           if i==1:
               data_visual()
           elif i==2:
               data_analysis()
           elif i==3:
               data_modify()
           elif i==4:
                  sys.exit(0)

def data_visual():
       while True:
              print("""
data visualisation
1. line chart- countries vs population
2. line chart- population vs net change
3. bar graph- land area vs world share
4. bar graph- population va world share
5. exit to menu""")
              n=int(input('enter choice'))
              if n==1:
                     linechart1()
              elif n==2:
                     linechart2()
              elif n==3:
                     barchart1()
              elif n==4:
                     barchart2()
              elif n==5:
                     break

#plotting line charts
#first
def linechart1():
       pd.set_option('display.max_columns',None)
       pd.set_option('display.width',None)
       df=pd.read_csv('Wolrd Population Data.csv')
       df=df.dropna(how='all')
       df=df.dropna(axis=1,how='all')
       df.sort_values(by='Population (2024)', ascending = False, inplace= True)
       df1=df.head(7)
       a=df1['Country']
       b=df1['Population (2024)']
       plt.plot(a,b,color='r',linestyle='-.',marker='*')
       plt.xlabel('countries')
       plt.ylabel('population')
       plt.show()

#second
def linechart2():
       pd.set_option('display.max_columns',None)
       pd.set_option('display.width',None)
       df=pd.read_csv('Wolrd Population Data.csv')
       df=df.dropna(how='all')
       df=df.dropna(axis=1,how='all')
       df.sort_values(by='Net Change', ascending = False, inplace= True)
       df1=df.head(7)
       c=df1['Population (2024)']
       d=df1['Net Change']
       plt.plot(c,d,color='blue',linestyle=':',marker='o')
       plt.xlabel('population')
       plt.ylabel('net change')
       plt.show()

#plotting barchart
#third
def barchart1():
       pd.set_option('display.max_columns',None)
       pd.set_option('display.width',None)
       df=pd.read_csv('Wolrd Population Data.csv')
       df=df.dropna(how='all')
       df=df.dropna(axis=1,how='all')
       df.sort_values(by='World Share', ascending = False, inplace= True)
       df1=df.head(7)
       e=df1['Land Area (Km²)']
       f=df1['World Share']
       plt.bar(e,f,color='blue',edgecolor='green')
       plt.xlabel('land area')
       plt.ylabel('world share')
       plt.show()

#fourth
def barchart2():
       pd.set_option('display.max_columns',None)
       pd.set_option('display.width',None)
       df=pd.read_csv('Wolrd Population Data.csv')
       df=df.dropna(how='all')
       df=df.dropna(axis=1,how='all')
       df.sort_values(by='World Share', ascending = False, inplace= True)
       df1=df.head(7)
       e=df1['Population (2024)']
       f=df1['World Share']
       plt.bar(e,f,color='blue',edgecolor='green')
       plt.xlabel('population')
       plt.ylabel('world share')
       plt.show()


def data_analysis():
       while True:
              pd.set_option('display.max_columns',None)
              pd.set_option('display.width',None)
              df=pd.read_csv('Wolrd Population Data.csv')
              df=df.dropna(how='all')
              df=df.dropna(axis=1,how='all')
              print("""data analysis
1. to show top populated countries
2. to show net changes in top countries
3. to show top country's land area
4. to show top country's world share
5. to show least country's land area
6. to print specified column name
7. to describe data frame
8. to go back menu""")
              p=int(input('enter choice'))
              if p==1:
                     df.sort_values('Population (2024)',ascending=False,inplace=True)
                     df1=df.head(3)
                     print(df1[['Country','Population (2024)']])
              elif p==2:
                     df.sort_values('Net Change',ascending=False,inplace=True)
                     df1=df.head(3)
                     print(df1[['Country','Net Change']])
              elif p==3:
                     df.sort_values('Land Area (Km²)',ascending=False,inplace=True)
                     df1=df.head(3)
                     print(df1[['Country','Land Area (Km²)']])
              elif p==4:
                     df.sort_values('World Share',ascending=False,inplace=True)
                     df1=df.head(3)
                     print(df1[['Country','World Share']])
              elif p==5:
                     df.sort_values('Land Area (Km²)',ascending=True,inplace=True)
                     df1=df.head(3)
                     print(df1[['Country','Land Area (Km²)']])
              elif p==6:
                     print('name of columns',df.columns)
                     c1=eval(input('enter any column'))
                     print(df[c1])
              elif p==7:
                     print(df.describe())
              elif p==8:
                     break


def data_modify():
       while True:
              pd.set_option('display.max_columns',None)
              pd.set_option('display.width',None)
              df=pd.read_csv('Wolrd Population Data.csv')
              df=df.dropna(how='all')
              df=df.dropna(axis=1,how='all')
              print(""" data modification
1. delete rows
2. insert columns
3. delete columns
4. rename columns
5. to go back menu""")
              u=int(input('enter choice'))
              if u==1:
                     d=int(input('enter which row axis:'))
                     df=df.drop(d,axis=0)
                     print(df)
              elif u==2:
                     x=len(df.columns)
                     co=input('enter new column name')
                     df[co]='NaN'
                     print(df)
              elif u==3: 
                      a=str(input('column to delete'))
                      df=df.drop(a,axis=1)
                      print(df)
              elif u==4:
                      l=input('enter column to change')
                      lc=input('enter new name')
                      df=df.rename(columns={l:lc})
                      print(df)
              elif u==5:
                      break
menu()
data_visual()
data_analysis()
data_modify()

                     
              
       



       
       
       
               
