#### Datasets

🧾 Basic Info:
------------------------------------------------------------
<class 'pandas.core.frame.DataFrame'>
Index: 216025200 entries, 141712864 to 110418635
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
memory usage: 12.9 GB
None

📊 Summary Statistics (Numerical Columns):
------------------------------------------------------------
         clock_time  clock_time_between  ...  lifetime_freq        wasted
count  2.160252e+08        2.160252e+08  ...   2.160252e+08  2.160252e+08
mean   4.281879e+08        3.020862e+04  ...   8.419825e+01  4.843372e-01
std    6.953292e+08        4.331737e+04  ...   3.586441e+03  4.997546e-01
min    0.000000e+00        0.000000e+00  ...   2.000000e+00  0.000000e+00
25%    4.482328e+05        1.860000e+02  ...   4.000000e+00  0.000000e+00
50%    1.398167e+06        3.601000e+03  ...   1.300000e+01  0.000000e+00
75%    1.538376e+09        6.464000e+04  ...   5.100000e+01  1.000000e+00
max    1.702944e+09        5.373010e+05  ...   1.408850e+07  1.000000e+00

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
clock_time            4336142
clock_time_between     293922
cache_size                 11
obj_size                    1
clock_freq              10960
lifetime_freq           32806
wasted                      2
dtype: int64

🚫 Subset: wasted == 0
------------------------------------------------------------
         clock_time  clock_time_between  ...  lifetime_freq       wasted
count  1.113962e+08        1.113962e+08  ...   1.113962e+08  111396163.0
mean   3.781707e+08        3.691358e+04  ...   1.258468e+02          0.0
std    6.664204e+08        4.374384e+04  ...   4.881469e+03          0.0
min    1.000000e+00        0.000000e+00  ...   2.000000e+00          0.0
25%    5.245160e+05        1.009000e+03  ...   8.000000e+00          0.0
50%    1.393837e+06        1.079900e+04  ...   2.000000e+01          0.0
75%    3.318317e+06        8.601000e+04  ...   6.800000e+01          0.0
max    1.702944e+09        5.373010e+05  ...   1.408850e+07          0.0

[8 rows x 7 columns]

✅ Subset: wasted == 1
------------------------------------------------------------
         clock_time  clock_time_between  ...  lifetime_freq       wasted
count  1.046290e+08        1.046290e+08  ...   1.046290e+08  104629037.0
mean   4.814401e+08        2.307001e+04  ...   3.985597e+01          1.0
std    7.210382e+08        4.168981e+04  ...   1.087792e+03          0.0
min    0.000000e+00        0.000000e+00  ...   2.000000e+00          1.0
25%    3.868810e+05        1.700000e+01  ...   3.000000e+00          1.0
50%    1.407574e+06        1.000000e+03  ...   7.000000e+00          1.0
75%    1.538439e+09        2.428300e+04  ...   3.200000e+01          1.0
max    1.702922e+09        3.976120e+05  ...   1.955751e+06          1.0

[8 rows x 7 columns]
#### Model
[0 0 1 ... 1 0 1]
Classification Report:
              precision    recall  f1-score   support

           0       0.63      0.68      0.65  27849041
           1       0.63      0.58      0.60  26157259

    accuracy                           0.63  54006300
   macro avg       0.63      0.63      0.63  54006300
weighted avg       0.63      0.63      0.63  54006300

Accuracy: 0.6298834395246481
Confusion Matrix:
[[18800398  9048643]
 [10939983 15217276]]
Confusion Matrix (%):
[[34.81149051 16.75479157]
 [20.25686448 28.17685344]]
