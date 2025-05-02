#### Datasets

🧾 Basic Info:
------------------------------------------------------------
<class 'pandas.core.frame.DataFrame'>
Index: 1036455761 entries, 15812354 to 490073092
Data columns (total 3 columns):
 #   Column                         Dtype  
---  ------                         -----  
 0   clock_time_between_normalized  float64
 1   clock_freq_normalized          float64
 2   wasted                         int64  
dtypes: float64(2), int64(1)
memory usage: 30.9 GB
None

📌 Missing Values:
------------------------------------------------------------
clock_time_between_normalized    0
clock_freq_normalized            0
wasted                           0
dtype: int64

🆔 Unique Values per Column:
------------------------------------------------------------
clock_time_between_normalized    6153822
clock_freq_normalized            1300916
wasted                                 2
dtype: int64

📊 Column-wise Summary Statistics:
------------------------------------------------------------

🔹 Column: clock_time_between_normalized
----------------------------------------
Type: float64
Missing: 0
Unique: 6153822
count    1.036456e+09
mean     2.452642e-02
std      7.741393e-02
min      0.000000e+00
25%      1.936860e-07
50%      1.467340e-04
75%      5.812600e-03
max      1.000000e+00
Name: clock_time_between_normalized, dtype: float64

🔹 Column: clock_freq_normalized
----------------------------------------
Type: float64
Missing: 0
Unique: 1300916
count    1.036456e+09
mean     4.162272e-03
std      1.718120e-02
min      1.624140e-07
25%      4.613610e-05
50%      2.559730e-04
75%      2.759380e-03
max      1.000000e+00
Name: clock_freq_normalized, dtype: float64

🔹 Column: wasted
----------------------------------------
Type: int64
Missing: 0
Unique: 2
count    1.036456e+09
mean     5.636888e-01
std      4.959271e-01
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
count    4.522173e+08
mean     3.573321e-02
std      9.264541e-02
min      0.000000e+00
25%      1.003280e-05
50%      9.023230e-04
75%      2.619180e-02
max      1.000000e+00
Name: clock_time_between_normalized, dtype: float64

🔹 Column: clock_freq_normalized
----------------------------------------
count    4.522173e+08
mean     3.380708e-03
std      1.293624e-02
min      1.624140e-07
25%      3.886700e-05
50%      1.544400e-04
75%      2.902760e-03
max      1.000000e+00
Name: clock_freq_normalized, dtype: float64

🔹 Column: wasted
----------------------------------------
count    452217261.0
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
count    5.842385e+08
mean     1.585204e-02
std      6.176995e-02
min      0.000000e+00
25%      0.000000e+00
50%      2.013840e-05
75%      1.263100e-03
max      9.987730e-01
Name: clock_time_between_normalized, dtype: float64

🔹 Column: clock_freq_normalized
----------------------------------------
count    5.842385e+08
mean     4.767225e-03
std      1.983211e-02
min      1.624140e-07
25%      5.688280e-05
50%      3.909300e-04
75%      2.713700e-03
max      1.000000e+00
Name: clock_freq_normalized, dtype: float64

🔹 Column: wasted
----------------------------------------
count    584238500.0
mean             1.0
std              0.0
min              1.0
25%              1.0
50%              1.0
75%              1.0
max              1.0
Name: wasted, dtype: float64
#### Model
[0 1 1 ... 1 1 1]
Classification Report:
              precision    recall  f1-score   support

           0       0.62      0.27      0.37 113054316
           1       0.61      0.87      0.72 146059625

    accuracy                           0.61 259113941
   macro avg       0.61      0.57      0.55 259113941
weighted avg       0.61      0.61      0.57 259113941

Accuracy: 0.6094397830952677
Confusion Matrix:
[[ 30322011  82732305]
 [ 18467292 127592333]]
Confusion Matrix (%):
[[11.70219205 31.92892852]
 [ 7.12709317 49.24178626]]
