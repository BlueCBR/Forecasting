# SARIMA example
from statsmodels.tsa.statespace.sarimax import SARIMAX
from random import random
import sys

dataA = [ 38.240, 38.386, 45.954, 48.152, 44.646, 42.456, 46.958, 42.402, 40.806, 39.546, 37.880, 42.738,
50.386, 49.998, 55.660, 62.814, 68.202, 72.322, 64.694, 71.180, 68.220, 66.306, 61.770, 62.270,
70.862, 68.612, 53.226, 58.780, 56.946, 68.590, 59.628, 60.332, 52.954, 67.464, 70.096, 66.560,
61.404, 63.976, 55.972, 47.738, 37.032, 44.692, 48.322, 45.122, 48.174, 62.984, 65.988, 83.666,
130.114, 133.598, 104.800, 156.376, 167.000, 215.962, 286.152, 498.320, 429.010, 388.040, 567.600, 705.670, 793.53, 675.5 ]

dataB = [ 108.310, 108.730, 113.800, 114.510, 111.320, 111.060, 111.740, 111.580, 112.350, 109.810, 105.890, 105.170,
107.980, 105.760, 106.520, 108.950, 112.440, 114.260, 118.420, 119.100, 118.140, 116.460, 119.040, 120.050, 
124.140, 122.000, 123.270, 120.850, 116.960, 116.900, 116.890, 116.210, 116.210, 113.170, 113.180, 114.820,
114.460, 113.690, 112.320, 112.120, 111.980, 113.890, 110.780, 110.100, 108.990, 111.520, 110.180, 112.220,
110.950, 110.280, 110.270, 109.430, 111.050, 112.350, 117.790, 119.370, 117.320, 116.780, 119.320, 122.160, 121.38, 120.72 ]

dataC = [1116.40, 1234.40, 1235.60, 1290.50, 1217.50, 1320.60, 1357.50, 1311.40, 1317.10, 1273.10, 1173.90, 1151.70,
1211.40, 1253.90, 1251.20, 1268.30, 1275.40, 1242.30, 1273.40, 1322.20, 1284.80, 1270.50, 1282.15, 1296.50,
1343.35, 1320.30, 1323.90, 1316.25, 1303.50, 1250.55, 1219.20, 1206.85, 1183.50, 1217.70, 1220.45, 1281.65,
1322.50, 1325.45, 1291.15, 1285.15, 1296.00, 1413.20, 1430.55, 1526.55, 1487.60, 1506.40, 1456.35, 1523.00,
1580.85, 1626.35, 1604.65, 1716.75, 1725.65, 1770.70, 1971.68, 1970.50, 1893.90, 1879.90, 1779.86 , 1895.10, 1849.7, 1728.8 ]

dataD = [ 206.700, 213.170, 218.300, 228.260, 209.550, 219.530, 222.150, 207.590, 221.050, 220.500, 262.470, 250.390,
272.750, 271.200, 265.250, 260.530, 258.000, 270.860, 289.150, 309.460, 295.500, 310.100, 304.420, 329.630,
319.550, 312.750, 302.550, 306.970, 306.500, 296.300, 283.150, 266.660, 280.500, 265.900, 278.270, 263.040,
278.450, 294.840, 293.600, 290.350, 264.000, 271.190, 266.600, 254.780, 257.850, 263.800, 264.840, 279.640,
251.700, 254.120, 222.800, 234.600, 242.550, 272.550, 286.800, 305.740, 303.250, 304.750, 342.570, 351.800, 355.6, 409.29 ]

dataE = [372.000, 356.300, 351.500, 391.450, 404.750, 364.150, 334.500, 312.700, 336.750, 354.750, 346.150, 352.000, 
359.750, 372.350, 364.250, 364.800, 372.000, 378.900, 370.750, 354.650, 355.250, 345.750, 352.950, 350.750,
361.500, 380.500, 387.750, 399.100, 394.000, 357.650, 372.250, 362.200, 356.250, 363.250, 375.500, 375.000,
376.500, 369.000, 356.500, 360.650, 427.000, 423.850, 400.250, 367.400, 388.000, 390.000, 379.250, 387.750,
381.250, 367.900, 340.750, 318.300, 325.750, 340.900, 316.000, 355.900, 379.000, 398.500, 424.750, 484.000, 547, 549.1 ]

timeseries = [dataA, dataB, dataC, dataD, dataE]
# fit model
result = []

#for data in timeseries:
#    model = SARIMAX(data, order=my_order, seasonal_order=my_seasonal_order)
#    model_fit = model.fit(disp=False) # , method='nm')
#    # yhat = model_fit.predict(len(data), len(data))
#    yhat = model_fit.forecast()
#    print ('---------------')
#    print(yhat)
#    result.append(yhat[0])

# my_order=(2, 4, 4)
# my_seasonal_order=(1, 2, 1, 12)

# A

#myloss = 1000

#for i in range(0,4):
#    for j in range (0,6):
#        for k in range (0,6):
#            for q in range (2,4):
#                my_order=(i, j, k) # war 2, 3, 4
#                my_seasonal_order=(1, q, 1, 12)
#                model = SARIMAX(dataB, order=my_order, seasonal_order=my_seasonal_order)
#                model_fit = model.fit(disp=False, method='powell')
#                yhat = model_fit.forecast()   # model_fitA.predict(len(dataA), len(dataA))
#                if (abs(yhat[0] - 120.72 ) < myloss):
#                    myloss = abs(yhat[0] - 120.72 )
#                    print ( 'i {} , j {} , k {} , q {} forcast {}'.format(i,j,k,q, yhat[0]) )  #  print (i,j,k + '-------------- : ' + yhat[0])


# A
my_order=(0, 3, 1)   # 0 3 1    oder 1 2 2
my_seasonal_order=(1, 2, 1, 12)   # 1 2 1 12
model = SARIMAX(dataA, order=my_order, seasonal_order=my_seasonal_order)
model_fit = model.fit(disp=False, method='nm')
yhat = model_fit.forecast()   # model_fitA.predict(len(dataA), len(dataA))
print ('---------------')
print(yhat)
result.append(yhat[0])


# B
my_order=(0, 1, 3)   # war 2 4 1
my_seasonal_order=(1, 2, 1, 12)   # war 1 2 1 12
model = SARIMAX(dataB, order=my_order, seasonal_order=my_seasonal_order)
model_fit = model.fit(disp=False, method='powell')
yhat = model_fit.forecast()   # model_fitB.predict(len(dataB), len(dataB))
print ('---------------')
print(yhat)
result.append(yhat[0])

# C
my_order=(2, 5, 0)  # war 2 5 6
my_seasonal_order=(1, 2, 1, 12)   # war 1 2 1 12
model = SARIMAX(dataC, order=my_order, seasonal_order=my_seasonal_order)
model_fit = model.fit(disp=False, method='powell')
yhat = model_fit.forecast()   # model_fitB.predict(len(dataB), len(dataB))
print ('---------------')
print(yhat)
result.append(yhat[0])

# D
my_order=(1, 4, 4) # war 2 1 1
my_seasonal_order=(1, 3, 1, 12)   
model = SARIMAX(dataD, order=my_order, seasonal_order=my_seasonal_order)
model_fit = model.fit(disp=False, method='powell')    # 'bfgs')
yhat = model_fit.forecast()   # model_fitB.predict(len(dataB), len(dataB))
print ('---------------')
print(yhat)
result.append(yhat[0])

# E
my_order=(0, 1, 1)   # war 2, 3, 4
my_seasonal_order=(1, 2, 1, 12)   
model = SARIMAX(dataE, order=my_order, seasonal_order=my_seasonal_order)
model_fit = model.fit(disp=False, method='powell')
yhat = model_fit.forecast()   # model_fitB.predict(len(dataB), len(dataB))
print ('---------------')
print(yhat)
result.append(yhat[0])

print ('Maerz:')
print(result)
print ('Februar A: 675.5    B: 120.72   C: 1728.8   D: 409.29   E: 549.1  ')
