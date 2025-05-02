#### Datasets

🧾 Basic Info:
------------------------------------------------------------
<class 'pandas.core.frame.DataFrame'>
Index: 182421133 entries, 109609189 to 207259788
Data columns (total 5 columns):
 #   Column              Dtype
---  ------              -----
 0   clock_time_between  int64
 1   clock_freq          int64
 2   lifetime_freq       int64
 3   obj_size_relative   int64
 4   wasted              int64
dtypes: int64(5)
memory usage: 8.2 GB
None

📊 Summary Statistics (Numerical Columns):
------------------------------------------------------------
       clock_time_between    clock_freq  ...  obj_size_relative        wasted
count        1.824211e+08  1.824211e+08  ...       1.824211e+08  1.824211e+08
mean         3.657296e+04  9.692801e+00  ...       2.829067e-01  4.473076e-01
std          4.673440e+04  8.244145e+02  ...       1.723237e+00  4.972158e-01
min          0.000000e+00  1.000000e+00  ...       0.000000e+00  0.000000e+00
25%          2.260000e+02  2.000000e+00  ...       0.000000e+00  0.000000e+00
50%          8.729000e+03  3.000000e+00  ...       0.000000e+00  0.000000e+00
75%          8.397000e+04  6.000000e+00  ...       0.000000e+00  1.000000e+00
max          6.492780e+05  3.312519e+06  ...       3.180000e+02  1.000000e+00

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
clock_time_between    308070
clock_freq             10907
lifetime_freq          28579
obj_size_relative        184
wasted                     2
dtype: int64

🚫 Subset: wasted == 0
------------------------------------------------------------
       clock_time_between    clock_freq  ...  obj_size_relative       wasted
count        1.008228e+08  1.008228e+08  ...       1.008228e+08  100822770.0
mean         4.119993e+04  1.400418e+01  ...       2.110332e-01          0.0
std          4.515594e+04  1.105632e+03  ...       1.291176e+00          0.0
min          0.000000e+00  1.000000e+00  ...       0.000000e+00          0.0
25%          1.395000e+03  2.000000e+00  ...       0.000000e+00          0.0
50%          1.566700e+04  4.000000e+00  ...       0.000000e+00          0.0
75%          8.628000e+04  8.000000e+00  ...       0.000000e+00          0.0
max          6.492780e+05  3.312519e+06  ...       3.180000e+02          0.0

[8 rows x 5 columns]

✅ Subset: wasted == 1
------------------------------------------------------------
       clock_time_between    clock_freq  ...  obj_size_relative      wasted
count        8.159836e+07  8.159836e+07  ...       8.159836e+07  81598363.0
mean         3.085589e+04  4.365675e+00  ...       3.717135e-01         1.0
std          4.800192e+04  9.471993e+01  ...       2.136477e+00         0.0
min          0.000000e+00  1.000000e+00  ...       0.000000e+00         1.0
25%          1.000000e+01  2.000000e+00  ...       0.000000e+00         1.0
50%          1.893000e+03  2.000000e+00  ...       0.000000e+00         1.0
75%          5.783400e+04  4.000000e+00  ...       0.000000e+00         1.0
max          4.695840e+05  7.299890e+05  ...       3.180000e+02         1.0

[8 rows x 5 columns]
#### Model
Classification Report:
              precision    recall  f1-score   support

           0       0.70      0.75      0.73  25205693
           1       0.66      0.61      0.64  20399591

    accuracy                           0.69  45605284
   macro avg       0.68      0.68      0.68  45605284
weighted avg       0.69      0.69      0.69  45605284

Accuracy: 0.6866941120243873
Confusion Matrix:
[[18880678  6325015]
 [ 7963389 12436202]]
Confusion Matrix (%):
[[41.40019828 13.86903982]
 [17.46154897 27.26921293]]
