#### Datasets

🧾 Basic Info:
------------------------------------------------------------
<class 'pandas.core.frame.DataFrame'>
Index: 322558820 entries, 77401861 to 53643052
Data columns (total 6 columns):
 #   Column              Dtype
---  ------              -----
 0   clock_time_between  int64
 1   clock_freq          int64
 2   lifetime_freq       int64
 3   time_since          int64
 4   obj_size_relative   int64
 5   wasted              int64
dtypes: int64(6)
memory usage: 16.8 GB
None

📊 Summary Statistics (Numerical Columns):
------------------------------------------------------------
       clock_time_between    clock_freq  ...  obj_size_relative        wasted
count        3.225588e+08  3.225588e+08  ...       3.225588e+08  3.225588e+08
mean         6.749270e+02  4.988609e+00  ...       1.536287e+01  6.555248e-01
std          3.390020e+03  9.187708e+01  ...       6.077122e+01  4.751968e-01
min          0.000000e+00  1.000000e+00  ...       0.000000e+00  0.000000e+00
25%          1.000000e+01  2.000000e+00  ...       0.000000e+00  0.000000e+00
50%          8.600000e+01  3.000000e+00  ...       6.000000e+00  1.000000e+00
75%          5.860000e+02  4.000000e+00  ...       6.000000e+00  1.000000e+00
max          1.016680e+05  7.299890e+05  ...       6.361000e+03  1.000000e+00

[8 rows x 6 columns]

📌 Missing Values:
------------------------------------------------------------
clock_time_between    0
clock_freq            0
lifetime_freq         0
time_since            0
obj_size_relative     0
wasted                0
dtype: int64

🆔 Unique Values per Column:
------------------------------------------------------------
clock_time_between      43851
clock_freq              10557
lifetime_freq          139272
time_since            4371930
obj_size_relative        2967
wasted                      2
dtype: int64

🚫 Subset: wasted == 0
------------------------------------------------------------
       clock_time_between    clock_freq  ...  obj_size_relative       wasted
count        1.111135e+08  1.111135e+08  ...       1.111135e+08  111113501.0
mean         4.947648e+02  7.116031e+00  ...       2.474985e+01          0.0
std          1.891631e+03  1.393370e+02  ...       8.659617e+01          0.0
min          0.000000e+00  1.000000e+00  ...       0.000000e+00          0.0
25%          4.700000e+01  2.000000e+00  ...       3.000000e+00          0.0
50%          1.100000e+02  3.000000e+00  ...       6.000000e+00          0.0
75%          5.860000e+02  5.000000e+00  ...       1.600000e+01          0.0
max          9.146000e+04  1.140220e+05  ...       6.361000e+03          0.0

[8 rows x 6 columns]

✅ Subset: wasted == 1
------------------------------------------------------------
       clock_time_between    clock_freq  ...  obj_size_relative       wasted
count        2.114453e+08  2.114453e+08  ...       2.114453e+08  211445319.0
mean         7.696014e+02  3.870659e+00  ...       1.043006e+01          1.0
std          3.952843e+03  5.168461e+01  ...       4.028149e+01          0.0
min          0.000000e+00  1.000000e+00  ...       0.000000e+00          1.0
25%          1.000000e+00  2.000000e+00  ...       0.000000e+00          1.0
50%          7.600000e+01  3.000000e+00  ...       5.000000e+00          1.0
75%          5.860000e+02  4.000000e+00  ...       6.000000e+00          1.0
max          1.016680e+05  7.299890e+05  ...       6.361000e+03          1.0

[8 rows x 6 columns]
#### Model
Classification Report:
              precision    recall  f1-score   support

           0       0.41      0.58      0.48  27778376
           1       0.71      0.55      0.62  52861330

    accuracy                           0.56  80639706
   macro avg       0.56      0.57      0.55  80639706
weighted avg       0.61      0.56      0.57  80639706

Accuracy: 0.5627948097925853
Confusion Matrix:
[[16076272 11702104]
 [23553994 29307336]]
Confusion Matrix (%):
[[19.93592586 14.51159061]
 [29.20892842 36.34355512]]
