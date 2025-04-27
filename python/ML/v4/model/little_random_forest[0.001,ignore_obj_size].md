#### Datasets

🧾 Basic Info:
------------------------------------------------------------
<class 'pandas.core.frame.DataFrame'>
Index: 197020424 entries, 87104649 to 64871190
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
memory usage: 11.7 GB
None

📊 Summary Statistics (Numerical Columns):
------------------------------------------------------------
         clock_time  clock_time_between  ...  lifetime_freq        wasted
count  1.970204e+08        1.970204e+08  ...   1.970204e+08  1.970204e+08
mean   2.428179e+08        3.776541e+01  ...   1.158148e+04  7.967440e-01
std    5.694149e+08        4.444025e+02  ...   1.819066e+05  4.024214e-01
min    0.000000e+00        0.000000e+00  ...   2.000000e+00  0.000000e+00
25%    1.370340e+05        0.000000e+00  ...   1.400000e+01  1.000000e+00
50%    5.227220e+05        1.000000e+00  ...   1.480000e+02  1.000000e+00
75%    1.776801e+06        3.000000e+01  ...   1.821000e+03  1.000000e+00
max    1.702944e+09        7.242200e+04  ...   1.524333e+07  1.000000e+00

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
clock_time            4277682
clock_time_between       8897
cache_size                 11
obj_size                    1
clock_freq               6020
lifetime_freq          812909
wasted                      2
dtype: int64

🚫 Subset: wasted == 0
------------------------------------------------------------
         clock_time  clock_time_between  ...  lifetime_freq      wasted
count  4.004558e+07        4.004558e+07  ...   4.004558e+07  40045575.0
mean   5.298216e+08        6.154703e+01  ...   4.044861e+04         0.0
std    7.418602e+08        5.645872e+02  ...   3.581918e+05         0.0
min    0.000000e+00        0.000000e+00  ...   2.000000e+00         0.0
25%    2.992500e+05        1.000000e+01  ...   3.320000e+02         0.0
50%    1.511830e+06        3.000000e+01  ...   2.526000e+03         0.0
75%    1.577888e+09        6.000000e+01  ...   1.292300e+04         0.0
max    1.702944e+09        4.776800e+04  ...   8.801872e+06         0.0

[8 rows x 7 columns]

✅ Subset: wasted == 1
------------------------------------------------------------
         clock_time  clock_time_between  ...  lifetime_freq       wasted
count  1.569748e+08        1.569748e+08  ...   1.569748e+08  156974849.0
mean   1.696009e+08        3.169852e+01  ...   4.217242e+03          1.0
std    4.900746e+08        4.078930e+02  ...   9.237970e+04          0.0
min    0.000000e+00        0.000000e+00  ...   2.000000e+00          1.0
25%    1.241920e+05        0.000000e+00  ...   9.000000e+00          1.0
50%    4.617170e+05        1.000000e+00  ...   8.300000e+01          1.0
75%    1.481643e+06        1.200000e+01  ...   6.360000e+02          1.0
max    1.702944e+09        7.242200e+04  ...   1.524333e+07          1.0

[8 rows x 7 columns]
#### Model
[1 1 0 ... 1 1 0]
Classification Report:
              precision    recall  f1-score   support

           0       0.78      0.48      0.59  10011394
           1       0.88      0.96      0.92  39243713

    accuracy                           0.87  49255107
   macro avg       0.83      0.72      0.76  49255107
weighted avg       0.86      0.87      0.85  49255107

Accuracy: 0.8661169896555092
Confusion Matrix:
[[ 4797521  5213873]
 [ 1380549 37863164]]
Confusion Matrix (%):
[[ 9.74014938 10.5854465 ]
 [ 2.80285453 76.87154958]]
