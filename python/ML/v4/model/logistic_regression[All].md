#### Datasets

🧾 Basic Info:
------------------------------------------------------------
<class 'pandas.core.frame.DataFrame'>
Index: 1032000711 entries, 920681155 to 799040871
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
memory usage: 61.5 GB
None

📊 Summary Statistics (Numerical Columns):
------------------------------------------------------------
         clock_time  clock_time_between  ...  lifetime_freq        wasted
count  1.032001e+09        1.032001e+09  ...   1.032001e+09  1.032001e+09
mean   2.495316e+08        1.756577e+04  ...   1.616014e+03  5.983040e-01
std    5.726711e+08        4.895633e+04  ...   5.545170e+04  4.902411e-01
min    0.000000e+00        0.000000e+00  ...   2.000000e+00  0.000000e+00
25%    2.944620e+05        2.000000e+00  ...   6.000000e+00  0.000000e+00
50%    8.686110e+05        2.160000e+02  ...   2.900000e+01  1.000000e+00
75%    1.909579e+06        4.503000e+03  ...   1.930000e+02  1.000000e+00
max    1.702944e+09        1.024021e+06  ...   1.523123e+07  1.000000e+00

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
clock_time            4766329
clock_time_between     691564
cache_size                 55
obj_size              1913731
clock_freq              21227
lifetime_freq          504457
wasted                      2
dtype: int64

🚫 Subset: wasted == 0
------------------------------------------------------------
         clock_time  clock_time_between  ...  lifetime_freq       wasted
count  4.145506e+08        4.145506e+08  ...   4.145506e+08  414550586.0
mean   2.802330e+08        2.541315e+04  ...   2.377971e+03          0.0
std    5.974743e+08        5.558733e+04  ...   7.021536e+04          0.0
min    0.000000e+00        0.000000e+00  ...   2.000000e+00          0.0
25%    3.917690e+05        6.900000e+01  ...   1.100000e+01          0.0
50%    1.038587e+06        1.063000e+03  ...   4.900000e+01          0.0
75%    1.995452e+06        1.950800e+04  ...   2.910000e+02          0.0
max    1.702944e+09        1.024021e+06  ...   1.523078e+07          0.0

[8 rows x 7 columns]

✅ Subset: wasted == 1
------------------------------------------------------------
         clock_time  clock_time_between  ...  lifetime_freq       wasted
count  6.174501e+08        6.174501e+08  ...   6.174501e+08  617450125.0
mean   2.289189e+08        1.229711e+04  ...   1.104442e+03          1.0
std    5.544442e+08        4.315310e+04  ...   4.276217e+04          0.0
min    0.000000e+00        0.000000e+00  ...   2.000000e+00          1.0
25%    2.462340e+05        1.000000e+00  ...   4.000000e+00          1.0
50%    6.905440e+05        6.300000e+01  ...   1.900000e+01          1.0
75%    1.815871e+06        1.113000e+03  ...   1.460000e+02          1.0
max    1.702944e+09        9.229410e+05  ...   1.523123e+07          1.0

[8 rows x 7 columns]
#### Model
[1 1 1 ... 1 1 1]
Classification Report:
              precision    recall  f1-score   support

           0       0.00      0.00      0.00 103637647
           1       0.60      1.00      0.75 154362531

    accuracy                           0.60 258000178
   macro avg       0.30      0.50      0.37 258000178
weighted avg       0.36      0.60      0.45 258000178

Accuracy: 0.5983039709375705
Confusion Matrix:
[[        0 103637647]
 [        0 154362531]]
Confusion Matrix (%):
[[ 0.         40.16960291]
 [ 0.         59.83039709]]
