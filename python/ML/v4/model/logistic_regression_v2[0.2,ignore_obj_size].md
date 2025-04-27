#### Datasets

🧾 Basic Info:
------------------------------------------------------------
<class 'pandas.core.frame.DataFrame'>
Index: 216025200 entries, 141712864 to 110418635
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
memory usage: 11.3 GB
None

📊 Summary Statistics (Numerical Columns):
------------------------------------------------------------
       clock_time_between    clock_freq  ...  obj_size_relative        wasted
count        2.160252e+08  2.160252e+08  ...       2.160252e+08  2.160252e+08
mean         3.020862e+04  8.179216e+00  ...       6.655322e-01  4.843372e-01
std          4.331737e+04  6.371305e+02  ...       1.147313e+00  4.997546e-01
min          0.000000e+00  1.000000e+00  ...       0.000000e+00  0.000000e+00
25%          1.860000e+02  2.000000e+00  ...       0.000000e+00  0.000000e+00
50%          3.601000e+03  3.000000e+00  ...       0.000000e+00  0.000000e+00
75%          6.464000e+04  5.000000e+00  ...       1.000000e+00  1.000000e+00
max          5.373010e+05  3.338681e+06  ...       1.200000e+01  1.000000e+00

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
clock_time_between     293922
clock_freq              10960
lifetime_freq           32806
time_since            4336142
obj_size_relative           4
wasted                      2
dtype: int64

🚫 Subset: wasted == 0
------------------------------------------------------------
       clock_time_between    clock_freq  ...  obj_size_relative       wasted
count        1.113962e+08  1.113962e+08  ...       1.113962e+08  111396163.0
mean         3.691358e+04  1.208916e+01  ...       5.994228e-01          0.0
std          4.374384e+04  8.839459e+02  ...       1.165900e+00          0.0
min          0.000000e+00  1.000000e+00  ...       0.000000e+00          0.0
25%          1.009000e+03  2.000000e+00  ...       0.000000e+00          0.0
50%          1.079900e+04  3.000000e+00  ...       0.000000e+00          0.0
75%          8.601000e+04  6.000000e+00  ...       1.000000e+00          0.0
max          5.373010e+05  3.338681e+06  ...       1.200000e+01          0.0

[8 rows x 6 columns]

✅ Subset: wasted == 1
------------------------------------------------------------
       clock_time_between    clock_freq  ...  obj_size_relative       wasted
count        1.046290e+08  1.046290e+08  ...       1.046290e+08  104629037.0
mean         2.307001e+04  4.016390e+00  ...       7.359174e-01          1.0
std          4.168981e+04  7.870824e+01  ...       1.122917e+00          0.0
min          0.000000e+00  1.000000e+00  ...       0.000000e+00          1.0
25%          1.700000e+01  2.000000e+00  ...       0.000000e+00          1.0
50%          1.000000e+03  2.000000e+00  ...       0.000000e+00          1.0
75%          2.428300e+04  4.000000e+00  ...       1.000000e+00          1.0
max          3.976120e+05  7.299890e+05  ...       1.200000e+01          1.0

[8 rows x 6 columns]
#### Model
Classification Report:
              precision    recall  f1-score   support

           0       0.59      0.71      0.64  27849041
           1       0.60      0.47      0.53  26157259

    accuracy                           0.59  54006300
   macro avg       0.59      0.59      0.58  54006300
weighted avg       0.59      0.59      0.59  54006300

Accuracy: 0.5925705889868405
Confusion Matrix:
[[19753542  8095499]
 [13908256 12249003]]
Confusion Matrix (%):
[[36.57636609 14.98991599]
 [25.75302511 22.68069281]]
