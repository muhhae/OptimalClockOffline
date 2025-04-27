#### Datasets

🧾 Basic Info:
------------------------------------------------------------
<class 'pandas.core.frame.DataFrame'>
Index: 186053350 entries, 4154098 to 53189435
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
memory usage: 11.1 GB
None

📊 Summary Statistics (Numerical Columns):
------------------------------------------------------------
         clock_time  clock_time_between  ...  lifetime_freq        wasted
count  1.860534e+08        1.860534e+08  ...   1.860534e+08  1.860534e+08
mean   1.922247e+08        4.349716e+01  ...   6.945396e+03  8.284241e-01
std    5.170466e+08        5.650675e+02  ...   1.260950e+05  3.770114e-01
min    0.000000e+00        0.000000e+00  ...   2.000000e+00  0.000000e+00
25%    1.174490e+05        0.000000e+00  ...   1.200000e+01  1.000000e+00
50%    4.884820e+05        1.000000e+00  ...   1.200000e+02  1.000000e+00
75%    1.594812e+06        2.700000e+01  ...   1.176000e+03  1.000000e+00
max    1.702944e+09        7.242200e+04  ...   1.524333e+07  1.000000e+00

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
clock_time            4328346
clock_time_between      10872
cache_size                 11
obj_size              1573963
clock_freq               5723
lifetime_freq          486157
wasted                      2
dtype: int64

🚫 Subset: wasted == 0
------------------------------------------------------------
         clock_time  clock_time_between  ...  lifetime_freq      wasted
count  3.192226e+07        3.192226e+07  ...   3.192226e+07  31922262.0
mean   3.449767e+08        7.874402e+01  ...   2.147613e+04         0.0
std    6.514540e+08        7.287130e+02  ...   2.387593e+05         0.0
min    0.000000e+00        0.000000e+00  ...   2.000000e+00         0.0
25%    8.384400e+04        4.000000e+00  ...   2.160000e+02         0.0
50%    9.934740e+05        3.000000e+01  ...   1.560000e+03         0.0
75%    3.166010e+06        6.600000e+01  ...   7.643000e+03         0.0
max    1.702944e+09        4.152700e+04  ...   8.801897e+06         0.0

[8 rows x 7 columns]

✅ Subset: wasted == 1
------------------------------------------------------------
         clock_time  clock_time_between  ...  lifetime_freq       wasted
count  1.541311e+08        1.541311e+08  ...   1.541311e+08  154131088.0
mean   1.605881e+08        3.619715e+01  ...   3.935919e+03          1.0
std    4.785143e+08        5.245387e+02  ...   8.563663e+04          0.0
min    0.000000e+00        0.000000e+00  ...   2.000000e+00          1.0
25%    1.236600e+05        0.000000e+00  ...   9.000000e+00          1.0
50%    4.589270e+05        1.000000e+00  ...   7.600000e+01          1.0
75%    1.473716e+06        1.100000e+01  ...   5.750000e+02          1.0
max    1.702944e+09        7.242200e+04  ...   1.524333e+07          1.0

[8 rows x 7 columns]
#### Model
[1 1 1 ... 1 0 0]
Classification Report:
              precision    recall  f1-score   support

           0       0.78      0.36      0.50   7980566
           1       0.88      0.98      0.93  38532772

    accuracy                           0.87  46513338
   macro avg       0.83      0.67      0.71  46513338
weighted avg       0.86      0.87      0.85  46513338

Accuracy: 0.8734724435386684
Confusion Matrix:
[[ 2905241  5075325]
 [  809894 37722878]]
Confusion Matrix (%):
[[ 6.2460385  10.91154757]
 [ 1.74120808 81.10120585]]
