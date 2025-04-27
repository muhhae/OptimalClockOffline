#### Datasets

🧾 Basic Info:
------------------------------------------------------------
<class 'pandas.core.frame.DataFrame'>
Index: 117057432 entries, 107913913 to 77681622
Data columns (total 5 columns):
 #   Column              Dtype
---  ------              -----
 0   clock_time_between  int64
 1   clock_freq          int64
 2   lifetime_freq       int64
 3   obj_size_relative   int64
 4   wasted              int64
dtypes: int64(5)
memory usage: 5.2 GB
None

📊 Summary Statistics (Numerical Columns):
------------------------------------------------------------
       clock_time_between    clock_freq  ...  obj_size_relative        wasted
count        1.170574e+08  1.170574e+08  ...       1.170574e+08  1.170574e+08
mean         7.363177e+04  1.436455e+01  ...       1.163323e-01  4.049326e-01
std          1.084552e+05  1.359346e+03  ...       8.839776e-01  4.908790e-01
min          0.000000e+00  1.000000e+00  ...       0.000000e+00  0.000000e+00
25%          2.790000e+02  2.000000e+00  ...       0.000000e+00  0.000000e+00
50%          2.113400e+04  4.000000e+00  ...       0.000000e+00  0.000000e+00
75%          9.586000e+04  7.000000e+00  ...       0.000000e+00  1.000000e+00
max          1.024021e+06  5.709376e+06  ...       1.590000e+02  1.000000e+00

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
clock_time_between    691218
clock_freq             11961
lifetime_freq          18816
obj_size_relative        105
wasted                     2
dtype: int64

🚫 Subset: wasted == 0
------------------------------------------------------------
       clock_time_between    clock_freq  ...  obj_size_relative      wasted
count        6.965707e+07  6.965707e+07  ...       6.965707e+07  69657066.0
mean         7.348413e+04  2.089248e+01  ...       1.010946e-01         0.0
std          1.027650e+05  1.754422e+03  ...       8.013563e-01         0.0
min          0.000000e+00  1.000000e+00  ...       0.000000e+00         0.0
25%          8.640000e+02  3.000000e+00  ...       0.000000e+00         0.0
50%          2.964100e+04  5.000000e+00  ...       0.000000e+00         0.0
75%          8.679600e+04  1.000000e+01  ...       0.000000e+00         0.0
max          1.024021e+06  5.709376e+06  ...       1.590000e+02         0.0

[8 rows x 5 columns]

✅ Subset: wasted == 1
------------------------------------------------------------
       clock_time_between    clock_freq  ...  obj_size_relative      wasted
count        4.740037e+07  4.740037e+07  ...       4.740037e+07  47400366.0
mean         7.384873e+04  4.771441e+00  ...       1.387249e-01         1.0
std          1.163129e+05  1.996725e+02  ...       9.925725e-01         0.0
min          0.000000e+00  1.000000e+00  ...       0.000000e+00         1.0
25%          3.900000e+01  2.000000e+00  ...       0.000000e+00         1.0
50%          1.177300e+04  2.000000e+00  ...       0.000000e+00         1.0
75%          1.051190e+05  4.000000e+00  ...       0.000000e+00         1.0
max          9.229410e+05  7.299890e+05  ...       1.590000e+02         1.0

[8 rows x 5 columns]
#### Model
Classification Report:
              precision    recall  f1-score   support

           0       0.77      0.40      0.53  17414266
           1       0.48      0.83      0.61  11850092

    accuracy                           0.57  29264358
   macro avg       0.63      0.61      0.57  29264358
weighted avg       0.66      0.57      0.56  29264358

Accuracy: 0.5733519252327354
Confusion Matrix:
[[ 6973788 10440478]
 [ 2045104  9804988]]
Confusion Matrix (%):
[[23.83031263 35.67642933]
 [ 6.98837815 33.5048799 ]]
