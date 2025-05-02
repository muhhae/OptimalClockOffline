#### Datasets

🧾 Basic Info:
------------------------------------------------------------
<class 'pandas.core.frame.DataFrame'>
Index: 186053350 entries, 4154098 to 53189435
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
memory usage: 9.7 GB
None

📊 Summary Statistics (Numerical Columns):
------------------------------------------------------------
       clock_time_between    clock_freq  ...  obj_size_relative        wasted
count        1.860534e+08  1.860534e+08  ...       1.860534e+08  1.860534e+08
mean         4.349716e+01  7.341430e+00  ...       1.980018e+02  8.284241e-01
std          5.650675e+02  8.921871e+01  ...       9.117192e+02  3.770114e-01
min          0.000000e+00  1.000000e+00  ...       0.000000e+00  0.000000e+00
25%          0.000000e+00  2.000000e+00  ...       1.000000e+00  1.000000e+00
50%          1.000000e+00  3.000000e+00  ...       1.100000e+01  1.000000e+00
75%          2.700000e+01  5.000000e+00  ...       6.700000e+01  1.000000e+00
max          7.242200e+04  7.299890e+05  ...       6.361800e+04  1.000000e+00

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
clock_time_between      10872
clock_freq               5723
lifetime_freq          486157
time_since            4328346
obj_size_relative       14450
wasted                      2
dtype: int64

🚫 Subset: wasted == 0
------------------------------------------------------------
       clock_time_between    clock_freq  ...  obj_size_relative      wasted
count        3.192226e+07  3.192226e+07  ...       3.192226e+07  31922262.0
mean         7.874402e+01  9.744762e+00  ...       7.266914e+01         0.0
std          7.287130e+02  5.270778e+01  ...       5.031262e+02         0.0
min          0.000000e+00  1.000000e+00  ...       0.000000e+00         0.0
25%          4.000000e+00  2.000000e+00  ...       2.000000e+00         0.0
50%          3.000000e+01  4.000000e+00  ...       1.100000e+01         0.0
75%          6.600000e+01  6.000000e+00  ...       5.900000e+01         0.0
max          4.152700e+04  3.742700e+04  ...       6.361800e+04         0.0

[8 rows x 6 columns]

✅ Subset: wasted == 1
------------------------------------------------------------
       clock_time_between    clock_freq  ...  obj_size_relative       wasted
count        1.541311e+08  1.541311e+08  ...       1.541311e+08  154131088.0
mean         3.619715e+01  6.843674e+00  ...       2.239596e+02          1.0
std          5.245387e+02  9.503556e+01  ...       9.731571e+02          0.0
min          0.000000e+00  1.000000e+00  ...       0.000000e+00          1.0
25%          0.000000e+00  2.000000e+00  ...       1.000000e+00          1.0
50%          1.000000e+00  3.000000e+00  ...       1.100000e+01          1.0
75%          1.100000e+01  5.000000e+00  ...       6.700000e+01          1.0
max          7.242200e+04  7.299890e+05  ...       6.361800e+04          1.0

[8 rows x 6 columns]
#### Model
Classification Report:
              precision    recall  f1-score   support

           0       0.64      0.04      0.07   7980566
           1       0.83      1.00      0.91  38532772

    accuracy                           0.83  46513338
   macro avg       0.73      0.52      0.49  46513338
weighted avg       0.80      0.83      0.76  46513338

Accuracy: 0.8312464050634251
Confusion Matrix:
[[  306168  7674398]
 [  174895 38357877]]
Confusion Matrix (%):
[[ 0.658237   16.49934907]
 [ 0.37601043 82.46640351]]
