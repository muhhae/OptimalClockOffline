#### Datasets

🧾 Basic Info:
------------------------------------------------------------
<class 'pandas.core.frame.DataFrame'>
Index: 301410930 entries, 88985620 to 333159863
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
memory usage: 15.7 GB
None

📊 Summary Statistics (Numerical Columns):
------------------------------------------------------------
       clock_time_between    clock_freq  ...  obj_size_relative        wasted
count        3.014109e+08  3.014109e+08  ...       3.014109e+08  3.014109e+08
mean         5.187065e+02  5.089636e+00  ...       2.678567e+01  6.995941e-01
std          2.512572e+03  7.085640e+01  ...       5.796288e+01  4.584345e-01
min          0.000000e+00  1.000000e+00  ...       0.000000e+00  0.000000e+00
25%          1.000000e+00  2.000000e+00  ...       5.000000e+00  0.000000e+00
50%          8.500000e+01  3.000000e+00  ...       6.000000e+00  1.000000e+00
75%          5.830000e+02  4.000000e+00  ...       2.000000e+01  1.000000e+00
max          1.051850e+05  1.313280e+05  ...       2.560000e+02  1.000000e+00

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
clock_time_between      30217
clock_freq               6677
lifetime_freq          207667
time_since            4352461
obj_size_relative          10
wasted                      2
dtype: int64

🚫 Subset: wasted == 0
------------------------------------------------------------
       clock_time_between    clock_freq  ...  obj_size_relative      wasted
count        9.054564e+07  9.054564e+07  ...       9.054564e+07  90545636.0
mean         5.286403e+02  7.331226e+00  ...       1.926536e+01         0.0
std          1.663018e+03  1.182810e+02  ...       4.528180e+01         0.0
min          0.000000e+00  1.000000e+00  ...       0.000000e+00         0.0
25%          3.700000e+01  2.000000e+00  ...       5.000000e+00         0.0
50%          2.290000e+02  3.000000e+00  ...       6.000000e+00         0.0
75%          6.030000e+02  5.000000e+00  ...       6.000000e+00         0.0
max          8.723900e+04  9.868400e+04  ...       2.560000e+02         0.0

[8 rows x 6 columns]

✅ Subset: wasted == 1
------------------------------------------------------------
       clock_time_between    clock_freq  ...  obj_size_relative       wasted
count        2.108653e+08  2.108653e+08  ...       2.108653e+08  210865294.0
mean         5.144409e+02  4.127097e+00  ...       3.001489e+01          1.0
std          2.799322e+03  3.414562e+01  ...       6.234723e+01          0.0
min          0.000000e+00  1.000000e+00  ...       0.000000e+00          1.0
25%          1.000000e+00  2.000000e+00  ...       5.000000e+00          1.0
50%          4.800000e+01  3.000000e+00  ...       6.000000e+00          1.0
75%          5.280000e+02  4.000000e+00  ...       3.700000e+01          1.0
max          1.051850e+05  1.313280e+05  ...       2.560000e+02          1.0

[8 rows x 6 columns]
#### Model
Classification Report:
              precision    recall  f1-score   support

           0       0.31      0.05      0.08  22636409
           1       0.70      0.96      0.81  52716324

    accuracy                           0.68  75352733
   macro avg       0.50      0.50      0.44  75352733
weighted avg       0.58      0.68      0.59  75352733

Accuracy: 0.6827022451859842
Confusion Matrix:
[[ 1034784 21601625]
 [ 2307628 50408696]]
Confusion Matrix (%):
[[ 1.37325344 28.6673411 ]
 [ 3.06243438 66.89697108]]
