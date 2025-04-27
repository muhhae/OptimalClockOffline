#### Datasets

🧾 Basic Info:
------------------------------------------------------------
<class 'pandas.core.frame.DataFrame'>
Index: 301410930 entries, 88985620 to 333159863
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
memory usage: 18.0 GB
None

📊 Summary Statistics (Numerical Columns):
------------------------------------------------------------
         clock_time  clock_time_between  ...  lifetime_freq        wasted
count  3.014109e+08        3.014109e+08  ...   3.014109e+08  3.014109e+08
mean   1.767591e+08        5.187065e+02  ...   2.172799e+03  6.995941e-01
std    4.944108e+08        2.512572e+03  ...   6.456875e+04  4.584345e-01
min    0.000000e+00        0.000000e+00  ...   2.000000e+00  0.000000e+00
25%    2.551680e+05        1.000000e+00  ...   2.100000e+01  0.000000e+00
50%    6.701900e+05        8.500000e+01  ...   1.400000e+02  1.000000e+00
75%    1.503881e+06        5.830000e+02  ...   4.950000e+02  1.000000e+00
max    1.702944e+09        1.051850e+05  ...   1.523123e+07  1.000000e+00

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
clock_time            4352461
clock_time_between      30217
cache_size                 11
obj_size                    1
clock_freq               6677
lifetime_freq          207667
wasted                      2
dtype: int64

🚫 Subset: wasted == 0
------------------------------------------------------------
         clock_time  clock_time_between  ...  lifetime_freq      wasted
count  9.054564e+07        9.054564e+07  ...   9.054564e+07  90545636.0
mean   1.495786e+08        5.286403e+02  ...   4.338141e+03         0.0
std    4.567212e+08        1.663018e+03  ...   1.164757e+05         0.0
min    0.000000e+00        0.000000e+00  ...   2.000000e+00         0.0
25%    2.421940e+05        3.700000e+01  ...   9.500000e+01         0.0
50%    7.260500e+05        2.290000e+02  ...   3.210000e+02         0.0
75%    1.395515e+06        6.030000e+02  ...   7.300000e+02         0.0
max    1.702944e+09        8.723900e+04  ...   1.523123e+07         0.0

[8 rows x 7 columns]

✅ Subset: wasted == 1
------------------------------------------------------------
         clock_time  clock_time_between  ...  lifetime_freq       wasted
count  2.108653e+08        2.108653e+08  ...   2.108653e+08  210865294.0
mean   1.884304e+08        5.144409e+02  ...   1.243000e+03          1.0
std    5.092952e+08        2.799322e+03  ...   1.144428e+04          0.0
min    0.000000e+00        0.000000e+00  ...   2.000000e+00          1.0
25%    2.600830e+05        1.000000e+00  ...   1.200000e+01          1.0
50%    6.448060e+05        4.800000e+01  ...   8.400000e+01          1.0
75%    1.568997e+06        5.280000e+02  ...   3.780000e+02          1.0
max    1.702943e+09        1.051850e+05  ...   8.746613e+06          1.0

[8 rows x 7 columns]
#### Model
[1 1 1 ... 1 1 1]
Classification Report:
              precision    recall  f1-score   support

           0       0.20      0.02      0.03  22636409
           1       0.70      0.97      0.81  52716324

    accuracy                           0.68  75352733
   macro avg       0.45      0.49      0.42  75352733
weighted avg       0.55      0.68      0.58  75352733

Accuracy: 0.6841690400267234
Confusion Matrix:
[[  402465 22233944]
 [ 1564782 51151542]]
Confusion Matrix (%):
[[ 0.53410803 29.50648651]
 [ 2.07660948 67.88279597]]
