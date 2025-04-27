#### Datasets

🧾 Basic Info:
------------------------------------------------------------
<class 'pandas.core.frame.DataFrame'>
Index: 117057432 entries, 107913913 to 77681622
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
memory usage: 7.0 GB
None

📊 Summary Statistics (Numerical Columns):
------------------------------------------------------------
         clock_time  clock_time_between  ...  lifetime_freq        wasted
count  1.170574e+08        1.170574e+08  ...   1.170574e+08  1.170574e+08
mean   1.622438e+08        7.363177e+04  ...   3.641810e+01  4.049326e-01
std    4.787544e+08        1.084552e+05  ...   2.796186e+03  4.908790e-01
min    0.000000e+00        0.000000e+00  ...   2.000000e+00  0.000000e+00
25%    3.823640e+05        2.790000e+02  ...   3.000000e+00  0.000000e+00
50%    1.046417e+06        2.113400e+04  ...   6.000000e+00  0.000000e+00
75%    2.025594e+06        9.586000e+04  ...   1.600000e+01  1.000000e+00
max    1.702922e+09        1.024021e+06  ...   1.437958e+07  1.000000e+00

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
clock_time            3666571
clock_time_between     691218
cache_size                 11
obj_size              1321137
clock_freq              11961
lifetime_freq           18816
wasted                      2
dtype: int64

🚫 Subset: wasted == 0
------------------------------------------------------------
         clock_time  clock_time_between  ...  lifetime_freq      wasted
count  6.965707e+07        6.965707e+07  ...   6.965707e+07  69657066.0
mean   1.831375e+08        7.348413e+04  ...   5.181044e+01         0.0
std    5.034458e+08        1.027650e+05  ...   3.538521e+03         0.0
min    1.000000e+00        0.000000e+00  ...   2.000000e+00         0.0
25%    4.735520e+05        8.640000e+02  ...   4.000000e+00         0.0
50%    1.314035e+06        2.964100e+04  ...   9.000000e+00         0.0
75%    1.933211e+06        8.679600e+04  ...   2.400000e+01         0.0
max    1.702922e+09        1.024021e+06  ...   1.437958e+07         0.0

[8 rows x 7 columns]

✅ Subset: wasted == 1
------------------------------------------------------------
         clock_time  clock_time_between  ...  lifetime_freq      wasted
count  4.740037e+07        4.740037e+07  ...   4.740037e+07  47400366.0
mean   1.315395e+08        7.384873e+04  ...   1.379833e+01         1.0
std    4.381576e+08        1.163129e+05  ...   9.525173e+02         0.0
min    0.000000e+00        0.000000e+00  ...   2.000000e+00         1.0
25%    2.350980e+05        3.900000e+01  ...   2.000000e+00         1.0
50%    7.933560e+05        1.177300e+04  ...   3.000000e+00         1.0
75%    3.070362e+06        1.051190e+05  ...   7.000000e+00         1.0
max    1.702921e+09        9.229410e+05  ...   1.917032e+06         1.0

[8 rows x 7 columns]
#### Model
[0 0 0 ... 1 0 0]
Classification Report:
              precision    recall  f1-score   support

           0       0.79      0.85      0.82  17414266
           1       0.75      0.67      0.71  11850092

    accuracy                           0.78  29264358
   macro avg       0.77      0.76      0.76  29264358
weighted avg       0.78      0.78      0.78  29264358

Accuracy: 0.7779534408374856
Confusion Matrix:
[[14822678  2591588]
 [ 3906462  7943630]]
Confusion Matrix (%):
[[50.6509591   8.85578286]
 [13.34887306 27.14438499]]
