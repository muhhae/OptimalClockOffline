#### Datasets

🧾 Basic Info:
------------------------------------------------------------
<class 'pandas.core.frame.DataFrame'>
Index: 322558820 entries, 77401861 to 53643052
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
memory usage: 19.2 GB
None

📊 Summary Statistics (Numerical Columns):
------------------------------------------------------------
         clock_time  clock_time_between  ...  lifetime_freq        wasted
count  3.225588e+08        3.225588e+08  ...   3.225588e+08  3.225588e+08
mean   2.435926e+08        6.749270e+02  ...   1.053301e+03  6.555248e-01
std    5.654069e+08        3.390020e+03  ...   2.592006e+04  4.751968e-01
min    0.000000e+00        0.000000e+00  ...   2.000000e+00  0.000000e+00
25%    2.985610e+05        1.000000e+01  ...   2.200000e+01  0.000000e+00
50%    7.488110e+05        8.600000e+01  ...   1.370000e+02  1.000000e+00
75%    1.624776e+06        5.860000e+02  ...   4.990000e+02  1.000000e+00
max    1.702944e+09        1.016680e+05  ...   1.523078e+07  1.000000e+00

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
clock_time            4371930
clock_time_between      43851
cache_size                 11
obj_size              1612797
clock_freq              10557
lifetime_freq          139272
wasted                      2
dtype: int64

🚫 Subset: wasted == 0
------------------------------------------------------------
         clock_time  clock_time_between  ...  lifetime_freq       wasted
count  1.111135e+08        1.111135e+08  ...   1.111135e+08  111113501.0
mean   2.039546e+08        4.947648e+02  ...   2.444733e+03          0.0
std    5.220235e+08        1.891631e+03  ...   4.404398e+04          0.0
min    0.000000e+00        0.000000e+00  ...   2.000000e+00          0.0
25%    2.848710e+05        4.700000e+01  ...   1.120000e+02          0.0
50%    6.144560e+05        1.100000e+02  ...   3.950000e+02          0.0
75%    1.417788e+06        5.860000e+02  ...   1.184000e+03          0.0
max    1.702944e+09        9.146000e+04  ...   1.523078e+07          0.0

[8 rows x 7 columns]

✅ Subset: wasted == 1
------------------------------------------------------------
         clock_time  clock_time_between  ...  lifetime_freq       wasted
count  2.114453e+08        2.114453e+08  ...   2.114453e+08  211445319.0
mean   2.644222e+08        7.696014e+02  ...   3.221109e+02          1.0
std    5.858468e+08        3.952843e+03  ...   1.989338e+03          0.0
min    0.000000e+00        0.000000e+00  ...   2.000000e+00          1.0
25%    3.032770e+05        1.000000e+00  ...   1.100000e+01          1.0
50%    8.784270e+05        7.600000e+01  ...   7.000000e+01          1.0
75%    1.736061e+06        5.860000e+02  ...   2.970000e+02          1.0
max    1.702943e+09        1.016680e+05  ...   2.478141e+06          1.0

[8 rows x 7 columns]
#### Model
[1 1 1 ... 1 1 1]
Classification Report:
              precision    recall  f1-score   support

           0       0.00      0.00      0.00  27778376
           1       0.66      1.00      0.79  52861330

    accuracy                           0.66  80639706
   macro avg       0.33      0.50      0.40  80639706
weighted avg       0.43      0.66      0.52  80639706

Accuracy: 0.6555248353708035
Confusion Matrix:
[[       0 27778376]
 [       0 52861330]]
Confusion Matrix (%):
[[ 0.         34.44751646]
 [ 0.         65.55248354]]
