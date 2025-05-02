#### Datasets

🧾 Basic Info:
------------------------------------------------------------
<class 'pandas.core.frame.DataFrame'>
Index: 1036455761 entries, 15812354 to 490073092
Data columns (total 4 columns):
 #   Column                         Dtype  
---  ------                         -----  
 0   clock_time_between_normalized  float64
 1   clock_freq_normalized          float64
 2   lifetime_freq_normalized       float64
 3   wasted                         int64  
dtypes: float64(3), int64(1)
memory usage: 38.6 GB
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
clock_time_between_normalized    6153822
clock_freq_normalized            1300916
lifetime_freq_normalized         5094725
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

🔹 Column: lifetime_freq_normalized
----------------------------------------
Type: float64
Missing: 0
Unique: 5094725
count    1.036456e+09
mean     7.765838e-03
std      3.240250e-02
min      1.312050e-07
25%      3.156370e-05
50%      1.968700e-04
75%      4.357800e-03
max      1.000000e+00
Name: lifetime_freq_normalized, dtype: float64

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

🔹 Column: lifetime_freq_normalized
----------------------------------------
count    4.522173e+08
mean     8.662648e-03
std      3.874676e-02
min      1.312050e-07
25%      4.408260e-05
50%      2.194510e-04
75%      4.412580e-03
max      1.000000e+00
Name: lifetime_freq_normalized, dtype: float64

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

🔹 Column: lifetime_freq_normalized
----------------------------------------
count    5.842385e+08
mean     7.071681e-03
std      2.644672e-02
min      1.312050e-07
25%      2.206680e-05
50%      1.862940e-04
75%      4.317230e-03
max      1.000000e+00
Name: lifetime_freq_normalized, dtype: float64

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

           0       0.58      0.30      0.40 113054316
           1       0.61      0.83      0.70 146059625

    accuracy                           0.60 259113941
   macro avg       0.59      0.57      0.55 259113941
weighted avg       0.60      0.60      0.57 259113941

Accuracy: 0.6012650048806135
Confusion Matrix:
[[ 34101898  78952418]
 [ 24365378 121694247]]
Confusion Matrix (%):
[[13.16096612 30.47015444]
 [ 9.40334507 46.96553436]]
