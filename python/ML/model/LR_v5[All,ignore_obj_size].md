#### Datasets

🧾 Basic Info:
------------------------------------------------------------
<class 'pandas.core.frame.DataFrame'>
Index: 1074429246 entries, 761403510 to 73388452
Data columns (total 3 columns):
 #   Column                         Dtype  
---  ------                         -----  
 0   clock_time_between_normalized  float64
 1   clock_freq_normalized          float64
 2   wasted                         int64  
dtypes: float64(2), int64(1)
memory usage: 32.0 GB
None

📌 Missing Values:
------------------------------------------------------------
clock_time_between_normalized    0
clock_freq_normalized            0
wasted                           0
dtype: int64

🆔 Unique Values per Column:
------------------------------------------------------------
clock_time_between_normalized    6159668
clock_freq_normalized            1395980
wasted                                 2
dtype: int64

📊 Column-wise Summary Statistics:
------------------------------------------------------------

🔹 Column: clock_time_between_normalized
----------------------------------------
Type: float64
Missing: 0
Unique: 6159668
count    1.074429e+09
mean     2.354400e-02
std      7.466174e-02
min      0.000000e+00
25%      4.119150e-08
50%      8.986030e-05
75%      4.960460e-03
max      9.995020e-01
Name: clock_time_between_normalized, dtype: float64

🔹 Column: clock_freq_normalized
----------------------------------------
Type: float64
Missing: 0
Unique: 1395980
count    1.074429e+09
mean     4.766020e-03
std      1.820252e-02
min      1.653740e-07
25%      5.094300e-05
50%      2.727700e-04
75%      3.538120e-03
max      1.000000e+00
Name: clock_freq_normalized, dtype: float64

🔹 Column: wasted
----------------------------------------
Type: int64
Missing: 0
Unique: 2
count    1.074429e+09
mean     5.807153e-01
std      4.934420e-01
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
count    4.504918e+08
mean     3.601033e-02
std      9.124369e-02
min      0.000000e+00
25%      4.422570e-06
50%      8.591410e-04
75%      2.761100e-02
max      9.991010e-01
Name: clock_time_between_normalized, dtype: float64

🔹 Column: clock_freq_normalized
----------------------------------------
count    4.504918e+08
mean     4.403587e-03
std      1.643847e-02
min      1.653740e-07
25%      3.870070e-05
50%      1.641160e-04
75%      3.521310e-03
max      1.000000e+00
Name: clock_freq_normalized, dtype: float64

🔹 Column: wasted
----------------------------------------
count    450491784.0
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
count    6.239375e+08
mean     1.454312e-02
std      5.826546e-02
min      0.000000e+00
25%      0.000000e+00
50%      1.006330e-05
75%      9.777310e-04
max      9.995020e-01
Name: clock_time_between_normalized, dtype: float64

🔹 Column: clock_freq_normalized
----------------------------------------
count    6.239375e+08
mean     5.027702e-03
std      1.937239e-02
min      1.653740e-07
25%      6.137230e-05
50%      3.928500e-04
75%      3.546100e-03
max      1.000000e+00
Name: clock_freq_normalized, dtype: float64

🔹 Column: wasted
----------------------------------------
count    623937462.0
mean             1.0
std              0.0
min              1.0
25%              1.0
50%              1.0
75%              1.0
max              1.0
Name: wasted, dtype: float64
#### Model
[1 1 0 ... 1 1 1]
Classification Report:
              precision    recall  f1-score   support

           0       0.63      0.26      0.37 112622946
           1       0.63      0.89      0.73 155984366

    accuracy                           0.63 268607312
   macro avg       0.63      0.57      0.55 268607312
weighted avg       0.63      0.63      0.58 268607312

Accuracy: 0.6251424644761718
Confusion Matrix:
[[ 29692761  82930185]
 [ 17759290 138225076]]
Confusion Matrix (%):
[[11.05433831 30.87413533]
 [ 6.61161823 51.45990814]]
