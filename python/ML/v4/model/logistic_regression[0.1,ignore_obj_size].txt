#### Datasets

🧾 Basic Info:
------------------------------------------------------------
<class 'pandas.core.frame.DataFrame'>
Index: 225672187 entries, 270584384 to 202669305
Data columns (total 7 columns):
 #   Column              Dtype
---  ------              -----
 0   clock_time          int64
 1   clock_time_between  int64
 2   cache_size          int64
 3   obj_size            int64
 4   clock_freq          int64
 5   lifetime_freq       int64
 6   wasted              int64
dtypes: int64(7)
memory usage: 13.5 GB
None

📊 Summary Statistics (Numerical Columns):
------------------------------------------------------------
         clock_time  clock_time_between  ...  lifetime_freq        wasted
count  2.256722e+08        2.256722e+08  ...   2.256722e+08  2.256722e+08
mean   3.924619e+08        1.049025e+04  ...   1.691080e+02  5.981141e-01
std    6.771902e+08        1.944156e+04  ...   6.092365e+03  4.902791e-01
min    0.000000e+00        0.000000e+00  ...   2.000000e+00  0.000000e+00
25%    3.646300e+05        5.400000e+01  ...   6.000000e+00  0.000000e+00
50%    1.162137e+06        1.198000e+03  ...   2.200000e+01  1.000000e+00
75%    1.538326e+09        9.849000e+03  ...   7.900000e+01  1.000000e+00
max    1.702944e+09        2.029590e+05  ...   1.516512e+07  1.000000e+00

[8 rows x 7 columns]

📌 Missing Values:
------------------------------------------------------------
clock_time            0
clock_time_between    0
cache_size            0
obj_size              0
clock_freq            0
lifetime_freq         0
wasted                0
dtype: int64

🆔 Unique Values per Column:
------------------------------------------------------------
clock_time            4381762
clock_time_between     135740
cache_size                 11
obj_size                    1
clock_freq              11064
lifetime_freq           50955
wasted                      2
dtype: int64

🚫 Subset: wasted == 0
------------------------------------------------------------
         clock_time  clock_time_between  ...  lifetime_freq      wasted
count  9.069446e+07        9.069446e+07  ...   9.069446e+07  90694465.0
mean   3.307622e+08        1.140952e+04  ...   3.443646e+02         0.0
std    6.354337e+08        1.886404e+04  ...   9.522605e+03         0.0
min    1.000000e+00        0.000000e+00  ...   2.000000e+00         0.0
25%    3.939670e+05        2.090000e+02  ...   1.600000e+01         0.0
50%    1.054440e+06        3.022000e+03  ...   4.900000e+01         0.0
75%    2.081245e+06        1.117000e+04  ...   1.550000e+02         0.0
max    1.702944e+09        2.029590e+05  ...   1.516512e+07         0.0

[8 rows x 7 columns]

✅ Subset: wasted == 1
------------------------------------------------------------
         clock_time  clock_time_between  ...  lifetime_freq       wasted
count  1.349777e+08        1.349777e+08  ...   1.349777e+08  134977722.0
mean   4.339193e+08        9.872569e+03  ...   5.134924e+01          1.0
std    7.008127e+08        1.979620e+04  ...   1.045082e+03          0.0
min    0.000000e+00        0.000000e+00  ...   2.000000e+00          1.0
25%    3.531730e+05        9.000000e+00  ...   4.000000e+00          1.0
50%    1.253968e+06        5.190000e+02  ...   1.200000e+01          1.0
75%    1.538400e+09        7.896000e+03  ...   4.500000e+01          1.0
max    1.702938e+09        1.725990e+05  ...   1.959682e+06          1.0

[8 rows x 7 columns]
#### Model
[1 1 1 ... 1 1 1]
Classification Report:
              precision    recall  f1-score   support

           0       0.61      0.36      0.46  22673616
           1       0.66      0.84      0.74  33744431

    accuracy                           0.65  56418047
   macro avg       0.63      0.60      0.60  56418047
weighted avg       0.64      0.65      0.63  56418047

Accuracy: 0.6494531794055189
Confusion Matrix:
[[ 8260366 14413250]
 [ 5363917 28380514]]
Confusion Matrix (%):
[[14.64135403 25.54723314]
 [ 9.50744892 50.30396391]]
