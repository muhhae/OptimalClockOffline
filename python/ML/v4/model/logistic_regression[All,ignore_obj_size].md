#### Datasets

🧾 Basic Info:
------------------------------------------------------------
<class 'pandas.core.frame.DataFrame'>
Index: 1066932149 entries, 1206026114 to 1274848070
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
memory usage: 63.6 GB
None

📊 Summary Statistics (Numerical Columns):
------------------------------------------------------------
         clock_time  clock_time_between  ...  lifetime_freq        wasted
count  1.066932e+09        1.066932e+09  ...   1.066932e+09  1.066932e+09
mean   2.945036e+08        1.679599e+04  ...   2.805817e+03  6.187268e-01
std    6.111596e+08        4.773598e+04  ...   8.538144e+04  4.856994e-01
min    0.000000e+00        0.000000e+00  ...   2.000000e+00  0.000000e+00
25%    3.035960e+05        1.000000e+00  ...   6.000000e+00  0.000000e+00
50%    9.456240e+05        1.980000e+02  ...   3.100000e+01  1.000000e+00
75%    2.177943e+06        4.223000e+03  ...   2.040000e+02  1.000000e+00
max    1.702944e+09        9.204590e+05  ...   1.524333e+07  1.000000e+00

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
clock_time            4791289
clock_time_between     682390
cache_size                 55
obj_size                    1
clock_freq              20829
lifetime_freq          861333
wasted                      2
dtype: int64

🚫 Subset: wasted == 0
------------------------------------------------------------
         clock_time  clock_time_between  ...  lifetime_freq       wasted
count  4.067926e+08        4.067926e+08  ...   4.067926e+08  406792603.0
mean   3.178642e+08        2.508733e+04  ...   5.066243e+03          0.0
std    6.271170e+08        5.534679e+04  ...   1.256790e+05          0.0
min    0.000000e+00        0.000000e+00  ...   2.000000e+00          0.0
25%    3.935880e+05        7.000000e+01  ...   1.100000e+01          0.0
50%    1.112397e+06        1.082000e+03  ...   5.000000e+01          0.0
75%    2.097473e+06        1.869200e+04  ...   3.060000e+02          0.0
max    1.702944e+09        9.188250e+05  ...   1.523123e+07          0.0

[8 rows x 7 columns]

✅ Subset: wasted == 1
------------------------------------------------------------
         clock_time  clock_time_between  ...  lifetime_freq       wasted
count  6.601395e+08        6.601395e+08  ...   6.601395e+08  660139546.0
mean   2.801082e+08        1.168669e+04  ...   1.412893e+03          1.0
std    6.006632e+08        4.155482e+04  ...   4.520839e+04          0.0
min    0.000000e+00        0.000000e+00  ...   2.000000e+00          1.0
25%    2.630130e+05        0.000000e+00  ...   4.000000e+00          1.0
50%    7.783830e+05        5.700000e+01  ...   2.200000e+01          1.0
75%    3.009562e+06        1.012000e+03  ...   1.610000e+02          1.0
max    1.702944e+09        9.204590e+05  ...   1.524333e+07          1.0

[8 rows x 7 columns]
#### Model
[0 1 1 ... 0 1 0]
Classification Report:
              precision    recall  f1-score   support

           0       0.37      0.59      0.45 101698151
           1       0.60      0.38      0.47 165034887

    accuracy                           0.46 266733038
   macro avg       0.49      0.48      0.46 266733038
weighted avg       0.51      0.46      0.46 266733038

Accuracy: 0.4598983909897206
Confusion Matrix:
[[ 60031317  41666834]
 [102396109  62638778]]
Confusion Matrix (%):
[[22.50614226 15.62117476]
 [38.38898614 23.48369683]]
