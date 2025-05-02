#### Datasets

🧾 Basic Info:
------------------------------------------------------------
<class 'pandas.core.frame.DataFrame'>
Index: 226285960 entries, 31282783 to 97384499
Data columns (total 5 columns):
 #   Column                         Dtype  
---  ------                         -----  
 0   clock_time_between             int64  
 1   clock_freq                     float64
 2   clock_time_between_normalized  float64
 3   clock_freq_normalized          float64
 4   wasted                         int64  
dtypes: float64(3), int64(2)
memory usage: 10.1 GB
None

📌 Missing Values:
------------------------------------------------------------
clock_time_between               0
clock_freq                       0
clock_time_between_normalized    0
clock_freq_normalized            0
wasted                           0
dtype: int64

🆔 Unique Values per Column:
------------------------------------------------------------
clock_time_between               205856
clock_freq                        10024
clock_time_between_normalized    205856
clock_freq_normalized             10024
wasted                                2
dtype: int64

📊 Column-wise Summary Statistics:
------------------------------------------------------------

🔹 Column: clock_time_between
----------------------------------------
Type: int64
Missing: 0
Unique: 205856
count    2.262860e+08
mean     1.161516e+04
std      2.145172e+04
min      0.000000e+00
25%      8.400000e+01
50%      1.688000e+03
75%      1.072400e+04
max      5.556150e+05
Name: clock_time_between, dtype: float64

🔹 Column: clock_freq
----------------------------------------
Type: float64
Missing: 0
Unique: 10024
count    2.262860e+08
mean     7.617712e+00
std      4.622272e+02
min      1.000000e+00
25%      2.000000e+00
50%      3.000000e+00
75%      5.000000e+00
max      1.984870e+06
Name: clock_freq, dtype: float64

🔹 Column: clock_time_between_normalized
----------------------------------------
Type: float64
Missing: 0
Unique: 205856
count    2.262860e+08
mean     2.090505e-02
std      3.860896e-02
min      0.000000e+00
25%      1.511838e-04
50%      3.038075e-03
75%      1.930113e-02
max      1.000000e+00
Name: clock_time_between_normalized, dtype: float64

🔹 Column: clock_freq_normalized
----------------------------------------
Type: float64
Missing: 0
Unique: 10024
count    2.262860e+08
mean     3.837890e-06
std      2.328753e-04
min      5.038113e-07
25%      1.007623e-06
50%      1.511434e-06
75%      2.519057e-06
max      1.000000e+00
Name: clock_freq_normalized, dtype: float64

🔹 Column: wasted
----------------------------------------
Type: int64
Missing: 0
Unique: 2
count    2.262860e+08
mean     5.149843e-01
std      4.997754e-01
min      0.000000e+00
25%      0.000000e+00
50%      1.000000e+00
75%      1.000000e+00
max      1.000000e+00
Name: wasted, dtype: float64

🚫 Subset: wasted == 0
------------------------------------------------------------

🔹 Column: clock_time_between
----------------------------------------
count    1.097522e+08
mean     1.313444e+04
std      2.225217e+04
min      0.000000e+00
25%      5.740000e+02
50%      2.953000e+03
75%      1.292600e+04
max      5.556150e+05
Name: clock_time_between, dtype: float64

🔹 Column: clock_freq
----------------------------------------
count    1.097522e+08
mean     1.152213e+01
std      6.593369e+02
min      1.000000e+00
25%      2.000000e+00
50%      3.000000e+00
75%      6.000000e+00
max      1.984870e+06
Name: clock_freq, dtype: float64

🔹 Column: clock_time_between_normalized
----------------------------------------
count    1.097522e+08
mean     2.363945e-02
std      4.004962e-02
min      0.000000e+00
25%      1.033089e-03
50%      5.314831e-03
75%      2.326431e-02
max      1.000000e+00
Name: clock_time_between_normalized, dtype: float64

🔹 Column: clock_freq_normalized
----------------------------------------
count    1.097522e+08
mean     5.804982e-06
std      3.321814e-04
min      5.038113e-07
25%      1.007623e-06
50%      1.511434e-06
75%      3.022868e-06
max      1.000000e+00
Name: clock_freq_normalized, dtype: float64

🔹 Column: wasted
----------------------------------------
count    109752244.0
mean             0.0
std              0.0
min              0.0
25%              0.0
50%              0.0
75%              0.0
max              0.0
Name: wasted, dtype: float64

✅ Subset: wasted == 1
------------------------------------------------------------

🔹 Column: clock_time_between
----------------------------------------
count    1.165337e+08
mean     1.018430e+04
std      2.056715e+04
min      0.000000e+00
25%      3.000000e+00
50%      6.710000e+02
75%      8.289000e+03
max      3.084180e+05
Name: clock_time_between, dtype: float64

🔹 Column: clock_freq
----------------------------------------
count    1.165337e+08
mean     3.940501e+00
std      7.361885e+01
min      1.000000e+00
25%      2.000000e+00
50%      3.000000e+00
75%      4.000000e+00
max      7.299890e+05
Name: clock_freq, dtype: float64

🔹 Column: clock_time_between_normalized
----------------------------------------
count    1.165337e+08
mean     1.832977e-02
std      3.701691e-02
min      0.000000e+00
25%      5.399422e-06
50%      1.207671e-03
75%      1.491860e-02
max      5.550930e-01
Name: clock_time_between_normalized, dtype: float64

🔹 Column: clock_freq_normalized
----------------------------------------
count    1.165337e+08
mean     1.985269e-06
std      3.709001e-05
min      5.038113e-07
25%      1.007623e-06
50%      1.511434e-06
75%      2.015245e-06
max      3.677767e-01
Name: clock_freq_normalized, dtype: float64

🔹 Column: wasted
----------------------------------------
count    116533716.0
mean             1.0
std              0.0
min              1.0
25%              1.0
50%              1.0
75%              1.0
max              1.0
Name: wasted, dtype: float64
#### Model
[1 0 1 ... 0 1 1]
Classification Report:
              precision    recall  f1-score   support

           0       0.64      0.41      0.50  27438061
           1       0.58      0.78      0.67  29133429

    accuracy                           0.60  56571490
   macro avg       0.61      0.60      0.58  56571490
weighted avg       0.61      0.60      0.59  56571490

Accuracy: 0.6005831912859286
Confusion Matrix:
[[11230731 16207330]
 [ 6388274 22745155]]
Confusion Matrix (%):
[[19.85228072 28.6492896 ]
 [11.29239127 40.20603841]]
