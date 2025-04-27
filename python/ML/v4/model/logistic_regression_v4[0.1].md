#### Datasets

🧾 Basic Info:
------------------------------------------------------------
<class 'pandas.core.frame.DataFrame'>
Index: 223909974 entries, 109405185 to 185263798
Data columns (total 5 columns):
 #   Column              Dtype
---  ------              -----
 0   clock_time_between  int64
 1   clock_freq          int64
 2   lifetime_freq       int64
 3   obj_size_relative   int64
 4   wasted              int64
dtypes: int64(5)
memory usage: 10.0 GB
None

📊 Summary Statistics (Numerical Columns):
------------------------------------------------------------
       clock_time_between    clock_freq  ...  obj_size_relative        wasted
count        2.239100e+08  2.239100e+08  ...       2.239100e+08  2.239100e+08
mean         1.166496e+04  7.692850e+00  ...       8.473398e-01  5.487696e-01
std          2.151667e+04  4.648830e+02  ...       3.604047e+00  4.976158e-01
min          0.000000e+00  1.000000e+00  ...       0.000000e+00  0.000000e+00
25%          8.200000e+01  2.000000e+00  ...       0.000000e+00  0.000000e+00
50%          1.697000e+03  3.000000e+00  ...       0.000000e+00  1.000000e+00
75%          1.073900e+04  5.000000e+00  ...       0.000000e+00  1.000000e+00
max          5.556150e+05  1.943136e+06  ...       6.360000e+02  1.000000e+00

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
clock_time_between    206071
clock_freq              9999
lifetime_freq          42605
obj_size_relative        348
wasted                     2
dtype: int64

🚫 Subset: wasted == 0
------------------------------------------------------------
       clock_time_between    clock_freq  ...  obj_size_relative       wasted
count        1.010350e+08  1.010350e+08  ...       1.010350e+08  101034986.0
mean         1.192942e+04  1.225454e+01  ...       7.991453e-01          0.0
std          2.120536e+04  6.870674e+02  ...       2.970616e+00          0.0
min          0.000000e+00  1.000000e+00  ...       0.000000e+00          0.0
25%          5.180000e+02  2.000000e+00  ...       0.000000e+00          0.0
50%          2.648000e+03  4.000000e+00  ...       0.000000e+00          0.0
75%          1.114500e+04  7.000000e+00  ...       0.000000e+00          0.0
max          5.556150e+05  1.943136e+06  ...       6.360000e+02          0.0

[8 rows x 5 columns]

✅ Subset: wasted == 1
------------------------------------------------------------
       clock_time_between    clock_freq  ...  obj_size_relative       wasted
count        1.228750e+08  1.228750e+08  ...       1.228750e+08  122874988.0
mean         1.144751e+04  3.941962e+00  ...       8.869682e-01          1.0
std          2.176690e+04  7.504490e+01  ...       4.050932e+00          0.0
min          0.000000e+00  1.000000e+00  ...       0.000000e+00          1.0
25%          6.000000e+00  2.000000e+00  ...       0.000000e+00          1.0
50%          8.900000e+02  3.000000e+00  ...       0.000000e+00          1.0
75%          1.009800e+04  4.000000e+00  ...       0.000000e+00          1.0
max          3.142830e+05  7.299890e+05  ...       6.360000e+02          1.0

[8 rows x 5 columns]
#### Model
[1 1 1 ... 1 1 1]
Classification Report:
              precision    recall  f1-score   support

           0       0.65      0.46      0.54  25258747
           1       0.64      0.80      0.71  30718747

    accuracy                           0.65  55977494
   macro avg       0.65      0.63      0.63  55977494
weighted avg       0.65      0.65      0.63  55977494

Accuracy: 0.6456410678191489
Confusion Matrix:
[[11693483 13565264]
 [ 6270861 24447886]]
Confusion Matrix (%):
[[20.88961503 24.23342495]
 [11.20246826 43.67449175]]
