#### Datasets

🧾 Basic Info:
------------------------------------------------------------
<class 'pandas.core.frame.DataFrame'>
Index: 223909974 entries, 109405185 to 185263798
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
memory usage: 13.3 GB
None

📊 Summary Statistics (Numerical Columns):
------------------------------------------------------------
         clock_time  clock_time_between  ...  lifetime_freq        wasted
count  2.239100e+08        2.239100e+08  ...   2.239100e+08  2.239100e+08
mean   3.745251e+08        1.166496e+04  ...   1.040144e+02  5.487696e-01
std    6.660470e+08        2.151667e+04  ...   4.106832e+03  4.976158e-01
min    0.000000e+00        0.000000e+00  ...   2.000000e+00  0.000000e+00
25%    3.564260e+05        8.200000e+01  ...   6.000000e+00  0.000000e+00
50%    1.124407e+06        1.697000e+03  ...   2.100000e+01  1.000000e+00
75%    3.225452e+06        1.073900e+04  ...   7.500000e+01  1.000000e+00
max    1.702944e+09        5.556150e+05  ...   1.346081e+07  1.000000e+00

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
clock_time            4291812
clock_time_between     206071
cache_size                 11
obj_size              1614727
clock_freq               9999
lifetime_freq           42605
wasted                      2
dtype: int64

🚫 Subset: wasted == 0
------------------------------------------------------------
         clock_time  clock_time_between  ...  lifetime_freq       wasted
count  1.010350e+08        1.010350e+08  ...   1.010350e+08  101034986.0
mean   4.347707e+08        1.192942e+04  ...   1.801406e+02          0.0
std    6.968411e+08        2.120536e+04  ...   6.015915e+03          0.0
min    1.000000e+00        0.000000e+00  ...   2.000000e+00          0.0
25%    4.414340e+05        5.180000e+02  ...   1.600000e+01          0.0
50%    1.230593e+06        2.648000e+03  ...   4.800000e+01          0.0
75%    1.538379e+09        1.114500e+04  ...   1.240000e+02          0.0
max    1.702944e+09        5.556150e+05  ...   1.346081e+07          0.0

[8 rows x 7 columns]

✅ Subset: wasted == 1
------------------------------------------------------------
         clock_time  clock_time_between  ...  lifetime_freq       wasted
count  1.228750e+08        1.228750e+08  ...   1.228750e+08  122874988.0
mean   3.249877e+08        1.144751e+04  ...   4.141904e+01          1.0
std    6.353511e+08        2.176690e+04  ...   9.834168e+02          0.0
min    0.000000e+00        0.000000e+00  ...   2.000000e+00          1.0
25%    3.043270e+05        6.000000e+00  ...   3.000000e+00          1.0
50%    9.677370e+05        8.900000e+02  ...   1.000000e+01          1.0
75%    3.065385e+06        1.009800e+04  ...   3.500000e+01          1.0
max    1.702939e+09        3.142830e+05  ...   2.223401e+06          1.0

[8 rows x 7 columns]
#### Model
[1 1 1 ... 1 0 1]
Classification Report:
              precision    recall  f1-score   support

           0       0.53      0.28      0.37  25258747
           1       0.57      0.79      0.67  30718747

    accuracy                           0.56  55977494
   macro avg       0.55      0.54      0.52  55977494
weighted avg       0.55      0.56      0.53  55977494

Accuracy: 0.5618147000292654
Confusion Matrix:
[[ 7078216 18180531]
 [ 6347984 24370763]]
Confusion Matrix (%):
[[12.64475326 32.47828672]
 [11.34024328 43.53671674]]
