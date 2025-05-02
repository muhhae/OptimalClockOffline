#### Datasets

🧾 Basic Info:
------------------------------------------------------------
<class 'pandas.core.frame.DataFrame'>
Index: 226285960 entries, 31282783 to 97384499
Data columns (total 7 columns):
 #   Column                         Dtype  
---  ------                         -----  
 0   clock_time_between             int64  
 1   clock_freq                     float64
 2   lifetime_freq                  float64
 3   clock_time_between_normalized  float64
 4   clock_freq_normalized          float64
 5   lifetime_freq_normalized       float64
 6   wasted                         int64  
dtypes: float64(5), int64(2)
memory usage: 13.5 GB
None

📌 Missing Values:
------------------------------------------------------------
clock_time_between               0
clock_freq                       0
lifetime_freq                    0
clock_time_between_normalized    0
clock_freq_normalized            0
lifetime_freq_normalized         0
wasted                           0
dtype: int64

🆔 Unique Values per Column:
------------------------------------------------------------
clock_time_between               205856
clock_freq                        10024
lifetime_freq                     42687
clock_time_between_normalized    205856
clock_freq_normalized             10024
lifetime_freq_normalized          42687
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

🔹 Column: lifetime_freq
----------------------------------------
Type: float64
Missing: 0
Unique: 42687
count    2.262860e+08
mean     1.050490e+02
std      4.451750e+03
min      2.000000e+00
25%      6.000000e+00
50%      2.100000e+01
75%      7.600000e+01
max      1.496890e+07
Name: lifetime_freq, dtype: float64

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

🔹 Column: lifetime_freq_normalized
----------------------------------------
Type: float64
Missing: 0
Unique: 42687
count    2.262860e+08
mean     7.017818e-06
std      2.973999e-04
min      1.336104e-07
25%      4.008311e-07
50%      1.402909e-06
75%      5.077193e-06
max      1.000000e+00
Name: lifetime_freq_normalized, dtype: float64

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

🔹 Column: lifetime_freq
----------------------------------------
count    1.097522e+08
mean     1.718331e+02
std      6.308086e+03
min      2.000000e+00
25%      1.400000e+01
50%      4.400000e+01
75%      1.180000e+02
max      1.496890e+07
Name: lifetime_freq, dtype: float64

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

🔹 Column: lifetime_freq_normalized
----------------------------------------
count    1.097522e+08
mean     1.147934e-05
std      4.214128e-04
min      1.336104e-07
25%      9.352725e-07
50%      2.939428e-06
75%      7.883011e-06
max      1.000000e+00
Name: lifetime_freq_normalized, dtype: float64

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

🔹 Column: lifetime_freq
----------------------------------------
count    1.165337e+08
mean     4.215132e+01
std      9.991927e+02
min      2.000000e+00
25%      3.000000e+00
50%      1.000000e+01
75%      3.600000e+01
max      2.223400e+06
Name: lifetime_freq, dtype: float64

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

🔹 Column: lifetime_freq_normalized
----------------------------------------
count    1.165337e+08
mean     2.815926e-06
std      6.675125e-05
min      1.336104e-07
25%      2.004155e-07
50%      6.680518e-07
75%      2.404986e-06
max      1.485346e-01
Name: lifetime_freq_normalized, dtype: float64

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
[1 1 1 ... 0 0 1]
Classification Report:
              precision    recall  f1-score   support

           0       0.66      0.49      0.56  27438061
           1       0.61      0.77      0.68  29133429

    accuracy                           0.63  56571490
   macro avg       0.64      0.63      0.62  56571490
weighted avg       0.64      0.63      0.62  56571490

Accuracy: 0.6302637777438777
Confusion Matrix:
[[13349377 14088684]
 [ 6827845 22305584]]
Confusion Matrix (%):
[[23.59735796 24.90421235]
 [12.06940987 39.42901981]]
