#### Datasets

🧾 Basic Info:
------------------------------------------------------------
<class 'pandas.core.frame.DataFrame'>
Index: 126803407 entries, 138474002 to 105057964
Data columns (total 5 columns):
 #   Column              Dtype
---  ------              -----
 0   clock_time_between  int64
 1   clock_freq          int64
 2   lifetime_freq       int64
 3   obj_size_relative   int64
 4   wasted              int64
dtypes: int64(5)
memory usage: 5.7 GB
None

📊 Summary Statistics (Numerical Columns):
------------------------------------------------------------
       clock_time_between    clock_freq  ...  obj_size_relative        wasted
count        1.268034e+08  1.268034e+08  ...       1.268034e+08  1.268034e+08
mean         6.990087e+04  1.349666e+01  ...       7.433103e-02  4.155460e-01
std          1.050110e+05  1.311836e+03  ...       3.065823e-01  4.928159e-01
min          0.000000e+00  1.000000e+00  ...       0.000000e+00  0.000000e+00
25%          2.960000e+02  2.000000e+00  ...       0.000000e+00  0.000000e+00
50%          1.632700e+04  4.000000e+00  ...       0.000000e+00  0.000000e+00
75%          9.465200e+04  7.000000e+00  ...       0.000000e+00  1.000000e+00
max          9.204590e+05  6.046901e+06  ...       6.000000e+00  1.000000e+00

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
clock_time_between    682487
clock_freq             11745
lifetime_freq          20266
obj_size_relative          3
wasted                     2
dtype: int64

🚫 Subset: wasted == 0
------------------------------------------------------------
       clock_time_between    clock_freq  ...  obj_size_relative      wasted
count        7.411076e+07  7.411076e+07  ...       7.411076e+07  74110764.0
mean         6.758166e+04  1.987887e+01  ...       1.096705e-01         0.0
std          1.009057e+05  1.709952e+03  ...       3.613745e-01         0.0
min          0.000000e+00  1.000000e+00  ...       0.000000e+00         0.0
25%          8.600000e+02  3.000000e+00  ...       0.000000e+00         0.0
50%          1.600200e+04  5.000000e+00  ...       0.000000e+00         0.0
75%          8.651500e+04  1.100000e+01  ...       0.000000e+00         0.0
max          9.115880e+05  6.046901e+06  ...       6.000000e+00         0.0

[8 rows x 5 columns]

✅ Subset: wasted == 1
------------------------------------------------------------
       clock_time_between    clock_freq  ...  obj_size_relative      wasted
count        5.269264e+07  5.269264e+07  ...       5.269264e+07  52692643.0
mean         7.316279e+04  4.520273e+00  ...       2.462702e-02         1.0
std          1.104448e+05  1.695802e+02  ...       1.956795e-01         0.0
min          0.000000e+00  1.000000e+00  ...       0.000000e+00         1.0
25%          4.200000e+01  2.000000e+00  ...       0.000000e+00         1.0
50%          1.694900e+04  2.000000e+00  ...       0.000000e+00         1.0
75%          1.075930e+05  4.000000e+00  ...       0.000000e+00         1.0
max          9.204590e+05  7.299890e+05  ...       6.000000e+00         1.0

[8 rows x 5 columns]
#### Model
Classification Report:
              precision    recall  f1-score   support

           0       0.71      0.82      0.76  18527691
           1       0.67      0.53      0.59  13173161

    accuracy                           0.70  31700852
   macro avg       0.69      0.67      0.68  31700852
weighted avg       0.69      0.70      0.69  31700852

Accuracy: 0.6972042265614817
Confusion Matrix:
[[15184966  3342725]
 [ 6256159  6917002]]
Confusion Matrix (%):
[[47.90081352 10.54459041]
 [19.73498693 21.81960914]]
