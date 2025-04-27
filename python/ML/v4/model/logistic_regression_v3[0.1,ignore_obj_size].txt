#### Datasets

🧾 Basic Info:
------------------------------------------------------------
<class 'pandas.core.frame.DataFrame'>
Index: 225672187 entries, 270584384 to 202669305
Data columns (total 5 columns):
 #   Column              Dtype
---  ------              -----
 0   clock_time_between  int64
 1   clock_freq          int64
 2   lifetime_freq       int64
 3   obj_size_relative   int64
 4   wasted              int64
dtypes: int64(5)
memory usage: 10.1 GB
None

📊 Summary Statistics (Numerical Columns):
------------------------------------------------------------
       clock_time_between    clock_freq  ...  obj_size_relative        wasted
count        2.256722e+08  2.256722e+08  ...       2.256722e+08  2.256722e+08
mean         1.049025e+04  7.661967e+00  ...       1.364605e+00  5.981141e-01
std          1.944156e+04  3.727946e+02  ...       2.447787e+00  4.902791e-01
min          0.000000e+00  1.000000e+00  ...       0.000000e+00  0.000000e+00
25%          5.400000e+01  2.000000e+00  ...       0.000000e+00  0.000000e+00
50%          1.198000e+03  3.000000e+00  ...       0.000000e+00  1.000000e+00
75%          9.849000e+03  5.000000e+00  ...       2.000000e+00  1.000000e+00
max          2.029590e+05  1.313592e+06  ...       2.500000e+01  1.000000e+00

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
clock_time_between    135740
clock_freq             11064
lifetime_freq          50955
obj_size_relative          6
wasted                     2
dtype: int64

🚫 Subset: wasted == 0
------------------------------------------------------------
       clock_time_between    clock_freq  ...  obj_size_relative      wasted
count        9.069446e+07  9.069446e+07  ...       9.069446e+07  90694465.0
mean         1.140952e+04  1.305273e+01  ...       1.296488e+00         0.0
std          1.886404e+04  5.821267e+02  ...       2.839958e+00         0.0
min          0.000000e+00  1.000000e+00  ...       0.000000e+00         0.0
25%          2.090000e+02  2.000000e+00  ...       0.000000e+00         0.0
50%          3.022000e+03  4.000000e+00  ...       0.000000e+00         0.0
75%          1.117000e+04  7.000000e+00  ...       2.000000e+00         0.0
max          2.029590e+05  1.313592e+06  ...       2.500000e+01         0.0

[8 rows x 5 columns]

✅ Subset: wasted == 1
------------------------------------------------------------
       clock_time_between    clock_freq  ...  obj_size_relative       wasted
count        1.349777e+08  1.349777e+08  ...       1.349777e+08  134977722.0
mean         9.872569e+03  4.039798e+00  ...       1.410374e+00          1.0
std          1.979620e+04  6.803541e+01  ...       2.143149e+00          0.0
min          0.000000e+00  1.000000e+00  ...       0.000000e+00          1.0
25%          9.000000e+00  2.000000e+00  ...       0.000000e+00          1.0
50%          5.190000e+02  3.000000e+00  ...       0.000000e+00          1.0
75%          7.896000e+03  4.000000e+00  ...       2.000000e+00          1.0
max          1.725990e+05  7.299890e+05  ...       2.500000e+01          1.0

[8 rows x 5 columns]
#### Model
Classification Report:
              precision    recall  f1-score   support

           0       0.79      0.27      0.40  22673616
           1       0.66      0.95      0.78  33744431

    accuracy                           0.68  56418047
   macro avg       0.72      0.61      0.59  56418047
weighted avg       0.71      0.68      0.63  56418047

Accuracy: 0.6780035650649162
Confusion Matrix:
[[ 6176572 16497044]
 [ 1669366 32075065]]
Confusion Matrix (%):
[[10.94786567 29.2407215 ]
 [ 2.95892199 56.85249084]]
