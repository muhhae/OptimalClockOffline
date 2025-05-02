#### Datasets

🧾 Basic Info:
------------------------------------------------------------
<class 'pandas.core.frame.DataFrame'>
Index: 1032000711 entries, 920681155 to 799040871
Data columns (total 5 columns):
 #   Column              Dtype
---  ------              -----
 0   clock_time_between  int64
 1   clock_freq          int64
 2   lifetime_freq       int64
 3   obj_size_relative   int64
 4   wasted              int64
dtypes: int64(5)
memory usage: 46.1 GB
None

📊 Summary Statistics (Numerical Columns):
------------------------------------------------------------
       clock_time_between    clock_freq  ...  obj_size_relative        wasted
count        1.032001e+09  1.032001e+09  ...       1.032001e+09  1.032001e+09
mean         1.913647e+04  7.891091e+00  ...       4.074668e+01  5.983040e-01
std          1.568890e+06  6.108729e+02  ...       3.959964e+02  4.902411e-01
min          0.000000e+00  1.000000e+00  ...       0.000000e+00  0.000000e+00
25%          2.000000e+00  2.000000e+00  ...       0.000000e+00  0.000000e+00
50%          2.160000e+02  3.000000e+00  ...       0.000000e+00  1.000000e+00
75%          4.503000e+03  5.000000e+00  ...       6.000000e+00  1.000000e+00
max          1.702943e+09  6.157091e+06  ...       6.361800e+04  1.000000e+00

[8 rows x 5 columns]

📌 Missing Values:
------------------------------------------------------------
clock_time_between    0
clock_freq            0
lifetime_freq         0
obj_size_relative     0
wasted                0
dtype: int64

🆔 Unique Values per Column:
------------------------------------------------------------
clock_time_between    691564
clock_freq             21227
lifetime_freq         504457
obj_size_relative      14461
wasted                     2
dtype: int64

🚫 Subset: wasted == 0
------------------------------------------------------------
       clock_time_between    clock_freq  ...  obj_size_relative       wasted
count        4.145506e+08  4.145506e+08  ...       4.145506e+08  414550586.0
mean         2.541315e+04  1.255181e+01  ...       1.249257e+01          0.0
std          5.558733e+04  9.570601e+02  ...       1.473540e+02          0.0
min          0.000000e+00  1.000000e+00  ...       0.000000e+00          0.0
25%          6.900000e+01  2.000000e+00  ...       0.000000e+00          0.0
50%          1.063000e+03  3.000000e+00  ...       0.000000e+00          0.0
75%          1.950800e+04  7.000000e+00  ...       5.000000e+00          0.0
max          1.024021e+06  6.157091e+06  ...       6.361800e+04          0.0

[8 rows x 5 columns]

✅ Subset: wasted == 1
------------------------------------------------------------
       clock_time_between    clock_freq  ...  obj_size_relative       wasted
count        6.174501e+08  6.174501e+08  ...       6.174501e+08  617450125.0
mean         1.229711e+04  4.761923e+00  ...       5.971624e+01          1.0
std          4.315310e+04  9.333403e+01  ...       4.966108e+02          0.0
min          0.000000e+00  1.000000e+00  ...       0.000000e+00          1.0
25%          1.000000e+00  2.000000e+00  ...       0.000000e+00          1.0
50%          6.300000e+01  3.000000e+00  ...       0.000000e+00          1.0
75%          1.113000e+03  4.000000e+00  ...       6.000000e+00          1.0
max          9.229410e+05  7.299890e+05  ...       6.361800e+04          1.0

[8 rows x 5 columns]
#### Model
[1 0 1 ... 1 1 1]
Classification Report:
              precision    recall  f1-score   support

           0       0.60      0.43      0.50 103637647
           1       0.68      0.81      0.74 154362531

    accuracy                           0.66 258000178
   macro avg       0.64      0.62      0.62 258000178
weighted avg       0.65      0.66      0.64 258000178

Accuracy: 0.6572790271485782
Confusion Matrix:
[[ 44174975  59462672]
 [ 28959400 125403131]]
Confusion Matrix (%):
[[17.12207152 23.04753139]
 [11.2245659  48.60583119]]
