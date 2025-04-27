#### Datasets

🧾 Basic Info:
------------------------------------------------------------
<class 'pandas.core.frame.DataFrame'>
Index: 126803407 entries, 138474002 to 105057964
Data columns (total 7 columns):
 #   Column              Dtype
---  ------              -----
 0   clock_time          int64
 1   clock_time_between  int64
 2   cache_size          int64
 3   obj_size            int64
 4   clock_freq          int64
 5   lifetime_freq       int64
 6   wasted              int64
dtypes: int64(7)
memory usage: 7.6 GB
None

📊 Summary Statistics (Numerical Columns):
------------------------------------------------------------
         clock_time  clock_time_between  ...  lifetime_freq        wasted
count  1.268034e+08        1.268034e+08  ...   1.268034e+08  1.268034e+08
mean   2.525792e+08        6.990087e+04  ...   4.341141e+01  4.155460e-01
std    5.759846e+08        1.050110e+05  ...   3.038302e+03  4.928159e-01
min    1.000000e+00        0.000000e+00  ...   2.000000e+00  0.000000e+00
25%    4.254580e+05        2.960000e+02  ...   3.000000e+00  0.000000e+00
50%    1.232877e+06        1.632700e+04  ...   6.000000e+00  0.000000e+00
75%    3.089178e+06        9.465200e+04  ...   1.900000e+01  1.000000e+00
max    1.702922e+09        9.204590e+05  ...   1.410327e+07  1.000000e+00

[8 rows x 7 columns]

📌 Missing Values:
------------------------------------------------------------
clock_time            0
clock_time_between    0
cache_size            0
obj_size              0
clock_freq            0
lifetime_freq         0
wasted                0
dtype: int64

🆔 Unique Values per Column:
------------------------------------------------------------
clock_time            3965193
clock_time_between     682487
cache_size                 11
obj_size                    1
clock_freq              11745
lifetime_freq           20266
wasted                      2
dtype: int64

🚫 Subset: wasted == 0
------------------------------------------------------------
         clock_time  clock_time_between  ...  lifetime_freq      wasted
count  7.411076e+07        7.411076e+07  ...   7.411076e+07  74110764.0
mean   3.023160e+08        6.758166e+04  ...   6.623311e+01         0.0
std    6.162866e+08        1.009057e+05  ...   3.852437e+03         0.0
min    1.000000e+00        0.000000e+00  ...   2.000000e+00         0.0
25%    4.740510e+05        8.600000e+02  ...   5.000000e+00         0.0
50%    1.348708e+06        1.600200e+04  ...   1.100000e+01         0.0
75%    2.166320e+06        8.651500e+04  ...   3.600000e+01         0.0
max    1.702922e+09        9.115880e+05  ...   1.410327e+07         0.0

[8 rows x 7 columns]

✅ Subset: wasted == 1
------------------------------------------------------------
         clock_time  clock_time_between  ...  lifetime_freq      wasted
count  5.269264e+07        5.269264e+07  ...   5.269264e+07  52692643.0
mean   1.826256e+08        7.316279e+04  ...   1.131332e+01         1.0
std    5.057699e+08        1.104448e+05  ...   1.157249e+03         0.0
min    1.000000e+00        0.000000e+00  ...   2.000000e+00         1.0
25%    3.145120e+05        4.200000e+01  ...   2.000000e+00         1.0
50%    1.052421e+06        1.694900e+04  ...   3.000000e+00         1.0
75%    3.103456e+06        1.075930e+05  ...   7.000000e+00         1.0
max    1.702919e+09        9.204590e+05  ...   1.959682e+06         1.0

[8 rows x 7 columns]
#### Model
[0 1 0 ... 1 1 1]
Classification Report:
              precision    recall  f1-score   support

           0       0.70      0.78      0.74  18527691
           1       0.63      0.54      0.58  13173161

    accuracy                           0.68  31700852
   macro avg       0.67      0.66      0.66  31700852
weighted avg       0.67      0.68      0.67  31700852

Accuracy: 0.678852196149176
Confusion Matrix:
[[14453048  4074643]
 [ 6106016  7067145]]
Confusion Matrix (%):
[[45.59198598 12.85341795]
 [19.26136244 22.29323363]]
