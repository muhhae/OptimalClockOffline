#### Datasets

🧾 Basic Info:
------------------------------------------------------------
<class 'pandas.core.frame.DataFrame'>
Index: 1066932149 entries, 1206026114 to 1274848070
Data columns (total 5 columns):
 #   Column              Dtype
---  ------              -----
 0   clock_time_between  int64
 1   clock_freq          int64
 2   lifetime_freq       int64
 3   obj_size_relative   int64
 4   wasted              int64
dtypes: int64(5)
memory usage: 47.7 GB
None

📊 Summary Statistics (Numerical Columns):
------------------------------------------------------------
       clock_time_between    clock_freq  ...  obj_size_relative        wasted
count        1.066932e+09  1.066932e+09  ...       1.066932e+09  1.066932e+09
mean         1.679599e+04  7.573496e+00  ...       7.448014e+01  6.187268e-01
std          4.773598e+04  5.655714e+02  ...       3.380104e+02  4.856994e-01
min          0.000000e+00  1.000000e+00  ...       0.000000e+00  0.000000e+00
25%          1.000000e+00  2.000000e+00  ...       0.000000e+00  0.000000e+00
50%          1.980000e+02  3.000000e+00  ...       2.000000e+00  1.000000e+00
75%          4.223000e+03  5.000000e+00  ...       1.600000e+01  1.000000e+00
max          9.204590e+05  6.046901e+06  ...       2.564000e+03  1.000000e+00

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
clock_time_between    682390
clock_freq             20829
lifetime_freq         861333
obj_size_relative         24
wasted                     2
dtype: int64

🚫 Subset: wasted == 0
------------------------------------------------------------
       clock_time_between    clock_freq  ...  obj_size_relative       wasted
count        4.067926e+08  4.067926e+08  ...       4.067926e+08  406792603.0
mean         2.508733e+04  1.226574e+01  ...       2.010542e+01          0.0
std          5.534679e+04  9.112606e+02  ...       1.067077e+02          0.0
min          0.000000e+00  1.000000e+00  ...       0.000000e+00          0.0
25%          7.000000e+01  2.000000e+00  ...       0.000000e+00          0.0
50%          1.082000e+03  3.000000e+00  ...       0.000000e+00          0.0
75%          1.869200e+04  6.000000e+00  ...       6.000000e+00          0.0
max          9.188250e+05  6.046901e+06  ...       2.564000e+03          0.0

[8 rows x 5 columns]

✅ Subset: wasted == 1
------------------------------------------------------------
       clock_time_between    clock_freq  ...  obj_size_relative       wasted
count        6.601395e+08  6.601395e+08  ...       6.601395e+08  660139546.0
mean         1.168669e+04  4.682034e+00  ...       1.079870e+02          1.0
std          4.155482e+04  7.247343e+01  ...       4.179638e+02          0.0
min          0.000000e+00  1.000000e+00  ...       0.000000e+00          1.0
25%          0.000000e+00  2.000000e+00  ...       0.000000e+00          1.0
50%          5.700000e+01  3.000000e+00  ...       5.000000e+00          1.0
75%          1.012000e+03  4.000000e+00  ...       3.700000e+01          1.0
max          9.204590e+05  7.299890e+05  ...       2.564000e+03          1.0

[8 rows x 5 columns]
#### Model
Classification Report:
              precision    recall  f1-score   support

           0       0.62      0.13      0.22 101698151
           1       0.64      0.95      0.76 165034887

    accuracy                           0.64 266733038
   macro avg       0.63      0.54      0.49 266733038
weighted avg       0.63      0.64      0.56 266733038

Accuracy: 0.6379917623852805
Confusion Matrix:
[[ 13354365  88343786]
 [  8215771 156819116]]
Confusion Matrix (%):
[[ 5.00664076 33.12067626]
 [ 3.0801475  58.79253548]]
