#### Datasets

🧾 Basic Info:
------------------------------------------------------------
<class 'pandas.core.frame.DataFrame'>
Index: 226285960 entries, 31282783 to 97384499
Data columns (total 3 columns):
 #   Column                         Dtype  
---  ------                         -----  
 0   clock_time_between_normalized  float64
 1   clock_freq_normalized          float64
 2   wasted                         int64  
dtypes: float64(2), int64(1)
memory usage: 6.7 GB
None

📌 Missing Values:
------------------------------------------------------------
clock_time_between_normalized    0
clock_freq_normalized            0
wasted                           0
dtype: int64

🆔 Unique Values per Column:
------------------------------------------------------------
clock_time_between_normalized    5597198
clock_freq_normalized             364062
wasted                                 2
dtype: int64

📊 Column-wise Summary Statistics:
------------------------------------------------------------

🔹 Column: clock_time_between_normalized
----------------------------------------
Type: float64
Missing: 0
Unique: 5597198
count    2.262860e+08
mean     2.411623e-02
std      7.058921e-02
min      0.000000e+00
25%      1.292690e-06
50%      8.300600e-04
75%      1.392830e-02
max      9.980670e-01
Name: clock_time_between_normalized, dtype: float64

🔹 Column: clock_freq_normalized
----------------------------------------
Type: float64
Missing: 0
Unique: 364062
count    2.262860e+08
mean     3.037225e-03
std      1.044732e-02
min      5.038120e-07
25%      3.137440e-05
50%      1.461700e-04
75%      1.980980e-03
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

🔹 Column: clock_time_between_normalized
----------------------------------------
count    1.097522e+08
mean     2.715262e-02
std      7.515549e-02
min      0.000000e+00
25%      2.005220e-06
50%      1.978230e-03
75%      1.827620e-02
max      9.978890e-01
Name: clock_time_between_normalized, dtype: float64

🔹 Column: clock_freq_normalized
----------------------------------------
count    1.097522e+08
mean     3.813105e-03
std      1.315527e-02
min      5.038120e-07
25%      3.792190e-05
50%      1.565800e-04
75%      2.902760e-03
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

🔹 Column: clock_time_between_normalized
----------------------------------------
count    1.165337e+08
mean     2.125654e-02
std      6.587254e-02
min      0.000000e+00
25%      6.558470e-07
50%      1.695350e-04
75%      1.001670e-02
max      9.980670e-01
Name: clock_time_between_normalized, dtype: float64

🔹 Column: clock_freq_normalized
----------------------------------------
count    1.165337e+08
mean     2.306495e-03
std      6.917391e-03
min      5.038120e-07
25%      2.008780e-05
50%      1.449280e-04
75%      1.752850e-03
max      1.000000e+00
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
[1 1 0 ... 0 0 1]
Classification Report:
              precision    recall  f1-score   support

           0       0.55      0.29      0.38  27438061
           1       0.54      0.78      0.64  29133429

    accuracy                           0.54  56571490
   macro avg       0.55      0.54      0.51  56571490
weighted avg       0.55      0.54      0.51  56571490

Accuracy: 0.5429015215968326
Confusion Matrix:
[[ 8087625 19350436]
 [ 6508306 22625123]]
Confusion Matrix (%):
[[14.29629129 34.20527902]
 [11.50456882 39.99386087]]
