#### Datasets

🧾 Basic Info:
------------------------------------------------------------
<class 'pandas.core.frame.DataFrame'>
Index: 227078018 entries, 146270207 to 62523096
Data columns (total 4 columns):
 #   Column                         Dtype  
---  ------                         -----  
 0   clock_time_between_normalized  float64
 1   clock_freq_normalized          float64
 2   lifetime_freq_normalized       float64
 3   wasted                         int64  
dtypes: float64(3), int64(1)
memory usage: 8.5 GB
None

📌 Missing Values:
------------------------------------------------------------
clock_time_between_normalized    0
clock_freq_normalized            0
lifetime_freq_normalized         0
wasted                           0
dtype: int64

🆔 Unique Values per Column:
------------------------------------------------------------
clock_time_between_normalized    5600911
clock_freq_normalized             333812
lifetime_freq_normalized         4489423
wasted                                 2
dtype: int64

📊 Column-wise Summary Statistics:
------------------------------------------------------------

🔹 Column: clock_time_between_normalized
----------------------------------------
Type: float64
Missing: 0
Unique: 5600911
count    2.270780e+08
mean     2.337393e-02
std      6.872556e-02
min      0.000000e+00
25%      3.445250e-07
50%      7.470660e-04
75%      1.360120e-02
max      9.982540e-01
Name: clock_time_between_normalized, dtype: float64

🔹 Column: clock_freq_normalized
----------------------------------------
Type: float64
Missing: 0
Unique: 333812
count    2.270780e+08
mean     5.385036e-03
std      1.582542e-02
min      7.799440e-07
25%      4.270220e-05
50%      1.440510e-04
75%      1.733100e-03
max      1.000000e+00
Name: clock_freq_normalized, dtype: float64

🔹 Column: lifetime_freq_normalized
----------------------------------------
Type: float64
Missing: 0
Unique: 4489423
count    2.270780e+08
mean     5.861329e-03
std      1.993546e-02
min      1.312050e-07
25%      2.730170e-05
50%      1.166350e-04
75%      2.055150e-03
max      1.000000e+00
Name: lifetime_freq_normalized, dtype: float64

🔹 Column: wasted
----------------------------------------
Type: int64
Missing: 0
Unique: 2
count    2.270780e+08
mean     5.569662e-01
std      4.967443e-01
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
count    1.006032e+08
mean     2.820950e-02
std      7.372545e-02
min      0.000000e+00
25%      4.632450e-06
50%      3.121090e-03
75%      2.191470e-02
max      9.982540e-01
Name: clock_time_between_normalized, dtype: float64

🔹 Column: clock_freq_normalized
----------------------------------------
count    1.006032e+08
mean     6.365092e-03
std      1.861096e-02
min      7.799440e-07
25%      5.370860e-05
50%      1.443900e-04
75%      1.937000e-03
max      1.000000e+00
Name: clock_freq_normalized, dtype: float64

🔹 Column: lifetime_freq_normalized
----------------------------------------
count    1.006032e+08
mean     9.467859e-03
std      2.774936e-02
min      1.312050e-07
25%      4.553220e-05
50%      1.915560e-04
75%      3.443440e-03
max      1.000000e+00
Name: lifetime_freq_normalized, dtype: float64

🔹 Column: wasted
----------------------------------------
count    100603234.0
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
count    1.264748e+08
mean     1.952752e-02
std      6.421264e-02
min      0.000000e+00
25%      1.000970e-07
50%      4.456730e-05
75%      7.663450e-03
max      9.954290e-01
Name: clock_time_between_normalized, dtype: float64

🔹 Column: clock_freq_normalized
----------------------------------------
count    1.264748e+08
mean     4.605459e-03
std      1.314422e-02
min      7.799440e-07
25%      4.028140e-05
50%      1.440510e-04
75%      1.733100e-03
max      1.000000e+00
Name: clock_freq_normalized, dtype: float64

🔹 Column: lifetime_freq_normalized
----------------------------------------
count    1.264748e+08
mean     2.992548e-03
std      9.080806e-03
min      1.344090e-07
25%      1.771220e-05
50%      7.332920e-05
75%      1.304300e-03
max      1.000000e+00
Name: lifetime_freq_normalized, dtype: float64

🔹 Column: wasted
----------------------------------------
count    126474784.0
mean             1.0
std              0.0
min              1.0
25%              1.0
50%              1.0
75%              1.0
max              1.0
Name: wasted, dtype: float64
#### Model
[1 0 1 ... 1 1 1]
Classification Report:
              precision    recall  f1-score   support

           0       0.57      0.28      0.37  25150809
           1       0.59      0.83      0.69  31618696

    accuracy                           0.59  56769505
   macro avg       0.58      0.55      0.53  56769505
weighted avg       0.58      0.59      0.55  56769505

Accuracy: 0.5863534832653552
Confusion Matrix:
[[ 6931868 18218941]
 [ 5263567 26355129]]
Confusion Matrix (%):
[[12.2105486  32.09283047]
 [ 9.2718212  46.42479972]]
