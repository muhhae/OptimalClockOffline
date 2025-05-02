#### Datasets

🧾 Basic Info:
------------------------------------------------------------
<class 'pandas.core.frame.DataFrame'>
Index: 197020424 entries, 87104649 to 64871190
Data columns (total 5 columns):
 #   Column              Dtype
---  ------              -----
 0   clock_time_between  int64
 1   clock_freq          int64
 2   lifetime_freq       int64
 3   obj_size_relative   int64
 4   wasted              int64
dtypes: int64(5)
memory usage: 8.8 GB
None

📊 Summary Statistics (Numerical Columns):
------------------------------------------------------------
       clock_time_between    clock_freq  ...  obj_size_relative        wasted
count        1.970204e+08  1.970204e+08  ...       1.970204e+08  1.970204e+08
mean         3.776541e+01  6.814789e+00  ...       3.600108e+02  7.967440e-01
std          4.444025e+02  8.608672e+01  ...       7.161504e+02  4.024214e-01
min          0.000000e+00  1.000000e+00  ...       8.000000e+00  0.000000e+00
25%          0.000000e+00  2.000000e+00  ...       2.800000e+01  1.000000e+00
50%          1.000000e+00  3.000000e+00  ...       5.800000e+01  1.000000e+00
75%          3.000000e+01  5.000000e+00  ...       3.750000e+02  1.000000e+00
max          7.242200e+04  7.299890e+05  ...       2.564000e+03  1.000000e+00

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
clock_time_between      8897
clock_freq              6020
lifetime_freq         812909
obj_size_relative         11
wasted                     2
dtype: int64

🚫 Subset: wasted == 0
------------------------------------------------------------
       clock_time_between    clock_freq  ...  obj_size_relative      wasted
count        4.004558e+07  4.004558e+07  ...       4.004558e+07  40045575.0
mean         6.154703e+01  8.101919e+00  ...       1.558827e+02         0.0
std          5.645872e+02  5.842987e+01  ...       3.000038e+02         0.0
min          0.000000e+00  1.000000e+00  ...       8.000000e+00         0.0
25%          1.000000e+01  2.000000e+00  ...       1.600000e+01         0.0
50%          3.000000e+01  3.000000e+00  ...       5.800000e+01         0.0
75%          6.000000e+01  5.000000e+00  ...       2.070000e+02         0.0
max          4.776800e+04  2.523900e+04  ...       2.564000e+03         0.0

[8 rows x 5 columns]

✅ Subset: wasted == 1
------------------------------------------------------------
       clock_time_between    clock_freq  ...  obj_size_relative       wasted
count        1.569748e+08  1.569748e+08  ...       1.569748e+08  156974849.0
mean         3.169852e+01  6.486432e+00  ...       4.120856e+02          1.0
std          4.078930e+02  9.181519e+01  ...       7.793632e+02          0.0
min          0.000000e+00  1.000000e+00  ...       8.000000e+00          1.0
25%          0.000000e+00  2.000000e+00  ...       5.400000e+01          1.0
50%          1.000000e+00  3.000000e+00  ...       6.700000e+01          1.0
75%          1.200000e+01  5.000000e+00  ...       3.750000e+02          1.0
max          7.242200e+04  7.299890e+05  ...       2.564000e+03          1.0

[8 rows x 5 columns]
#### Model
Classification Report:
              precision    recall  f1-score   support

           0       0.87      0.02      0.04  10011394
           1       0.80      1.00      0.89  39243713

    accuracy                           0.80  49255107
   macro avg       0.84      0.51      0.47  49255107
weighted avg       0.82      0.80      0.72  49255107

Accuracy: 0.8007136194019434
Confusion Matrix:
[[  228155  9783239]
 [   32633 39211080]]
Confusion Matrix (%):
[[4.63210850e-01 1.98623850e+01]
 [6.62530283e-02 7.96081511e+01]]
