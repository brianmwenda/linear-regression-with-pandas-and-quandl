import pandas as pd
import quandl

df = quandl.get('WIKI/GOOGL')
#fetching data from wiki/googl statistics

print(df.head())
            #output

#             brian mwenda@DESKTOP-E6526TN MINGW64 /d/my tutorils/project/linear regression
# $ python data.py
#               Open    High     Low  ...   Adj. Low  Adj. Close  Adj. Volume
# Date                                ...
# 2004-08-19  100.01  104.06   95.96  ...  48.128568   50.322842   44659000.0
# 2004-08-20  101.01  109.08  100.50  ...  50.405597   54.322689   22834300.0
# 2004-08-23  110.76  113.48  109.05  ...  54.693835   54.869377   18256100.0
# 2004-08-24  111.24  111.60  103.57  ...  51.945350   52.597363   15247300.0
# 2004-08-25  104.76  108.00  103.88  ...  52.100830   53.164113    9188600.0

# [5 rows x 12 columns]

# brian mwenda@DESKTOP-E6526TN MINGW64 /d/my tutorils/project/linear regression



df = df[['Adj. Open', 'Adj. High' ,'Adj. Low','Adj. Close' , 'Adj. Volume']]
#define the special relationships for the data and use them as our features

df['HL_PCT'] = (df['Adj. High'] - df['Adj. Close']) / df['Adj. Close'] * 100.0
df['PCT_Change'] = (df['Adj. Close'] - df['Adj. Open']) / df['Adj. Open'] * 100.0

df = df[['Adj. Close', 'HL_PCT', 'PCT_Change', 'Adj. Volume']]

print(df.head())
        #output 

        
#         brian mwenda@DESKTOP-E6526TN MINGW64 /d/my tutorils/project/linear regression
# $ python data.py
#             Adj. Close    HL_PCT  PCT_Change  Adj. Volume
# Date
# 2004-08-19   50.322842  3.712563    0.324968   44659000.0
# 2004-08-20   54.322689  0.710922    7.227007   22834300.0
# 2004-08-23   54.869377  3.729433   -1.227880   18256100.0
# 2004-08-24   52.597363  6.417469   -5.726357   15247300.0
# 2004-08-25   53.164113  1.886792    1.183658    9188600.0

# brian mwenda@DESKTOP-E6526TN MINGW64 /d/my tutorils/project/linear regression
# $ ^C

# brian mwenda@DESKTOP-E6526TN MINGW64 /d/my tutorils/project/linear regression
# $
