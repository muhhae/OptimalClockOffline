#### Datasets

🧾 Basic Info:
------------------------------------------------------------
<class 'pandas.core.frame.DataFrame'>
Index: 182421133 entries, 109609189 to 207259788
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
memory usage: 10.9 GB
None

📊 Summary Statistics (Numerical Columns):
------------------------------------------------------------
         clock_time  clock_time_between  ...  lifetime_freq        wasted
count  1.824211e+08        1.824211e+08  ...   1.824211e+08  1.824211e+08
mean   2.209629e+08        3.657296e+04  ...   5.571882e+01  4.473076e-01
std    5.453183e+08        4.673440e+04  ...   3.364517e+03  4.972158e-01
min    0.000000e+00        0.000000e+00  ...   2.000000e+00  0.000000e+00
25%    3.616540e+05        2.260000e+02  ...   4.000000e+00  0.000000e+00
50%    9.964110e+05        8.729000e+03  ...   1.000000e+01  0.000000e+00
75%    1.990034e+06        8.397000e+04  ...   2.800000e+01  1.000000e+00
max    1.702944e+09        6.492780e+05  ...   1.482811e+07  1.000000e+00

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
clock_time            4153990
clock_time_between     308070
cache_size                 11
obj_size              1556838
clock_freq              10907
lifetime_freq           28579
wasted                      2
dtype: int64

🚫 Subset: wasted == 0
------------------------------------------------------------
         clock_time  clock_time_between  ...  lifetime_freq       wasted
count  1.008228e+08        1.008228e+08  ...   1.008228e+08  100822770.0
mean   2.559379e+08        4.119993e+04  ...   8.226523e+01          0.0
std    5.766284e+08        4.515594e+04  ...   4.431557e+03          0.0
min    1.000000e+00        0.000000e+00  ...   2.000000e+00          0.0
25%    4.623550e+05        1.395000e+03  ...   7.000000e+00          0.0
50%    1.214200e+06        1.566700e+04  ...   1.700000e+01          0.0
75%    2.086661e+06        8.628000e+04  ...   5.000000e+01          0.0
max    1.702944e+09        6.492780e+05  ...   1.482811e+07          0.0

[8 rows x 7 columns]

✅ Subset: wasted == 1
------------------------------------------------------------
         clock_time  clock_time_between  ...  lifetime_freq      wasted
count  8.159836e+07        8.159836e+07  ...   8.159836e+07  81598363.0
mean   1.777478e+08        3.085589e+04  ...   2.291813e+01         1.0
std    5.005884e+08        4.800192e+04  ...   1.019528e+03         0.0
min    0.000000e+00        0.000000e+00  ...   2.000000e+00         1.0
25%    2.761980e+05        1.000000e+01  ...   2.000000e+00         1.0
50%    7.890170e+05        1.893000e+03  ...   5.000000e+00         1.0
75%    1.757975e+06        5.783400e+04  ...   1.300000e+01         1.0
max    1.702922e+09        4.695840e+05  ...   1.959682e+06         1.0

[8 rows x 7 columns]
#### Model
[0 1 0 ... 1 0 0]
Classification Report:
              precision    recall  f1-score   support

           0       0.77      0.81      0.79  25205693
           1       0.75      0.70      0.72  20399591

    accuracy                           0.76  45605284
   macro avg       0.76      0.76      0.76  45605284
weighted avg       0.76      0.76      0.76  45605284

Accuracy: 0.7608522073889508
Confusion Matrix:
[[20422152  4783541]
 [ 6122862 14276729]]
Confusion Matrix (%):
[[44.78023205 10.48900605]
 [13.42577321 31.30498869]]
