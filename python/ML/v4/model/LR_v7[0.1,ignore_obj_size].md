#### Datasets

🧾 Basic Info:
------------------------------------------------------------
<class 'pandas.core.frame.DataFrame'>
Index: 227078018 entries, 146270207 to 62523096
Data columns (total 5 columns):
 #   Column                         Dtype  
---  ------                         -----  
 0   clock_time_between             int64  
 1   clock_freq                     float64
 2   clock_time_between_normalized  float64
 3   clock_freq_normalized          float64
 4   wasted                         int64  
dtypes: float64(3), int64(2)
memory usage: 10.2 GB
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
clock_time_between               135911
clock_freq                        11027
clock_time_between_normalized    135911
clock_freq_normalized             11027
wasted                                2
dtype: int64

📊 Column-wise Summary Statistics:
------------------------------------------------------------

🔹 Column: clock_time_between
----------------------------------------
Type: int64
Missing: 0
Unique: 135911
count    2.270780e+08
mean     1.042869e+04
std      1.937334e+04
min      0.000000e+00
25%      5.400000e+01
50%      1.200000e+03
75%      9.756000e+03
max      2.029590e+05
Name: clock_time_between, dtype: float64

🔹 Column: clock_freq
----------------------------------------
Type: float64
Missing: 0
Unique: 11027
count    2.270780e+08
mean     7.580599e+00
std      3.670617e+02
min      1.000000e+00
25%      2.000000e+00
50%      3.000000e+00
75%      5.000000e+00
max      1.282140e+06
Name: clock_freq, dtype: float64

🔹 Column: clock_time_between_normalized
----------------------------------------
Type: float64
Missing: 0
Unique: 135911
count    2.270780e+08
mean     5.138325e-02
std      9.545446e-02
min      0.000000e+00
25%      2.660636e-04
50%      5.912524e-03
75%      4.806882e-02
max      1.000000e+00
Name: clock_time_between_normalized, dtype: float64

🔹 Column: clock_freq_normalized
----------------------------------------
Type: float64
Missing: 0
Unique: 11027
count    2.270780e+08
mean     5.912458e-06
std      2.862883e-04
min      7.799460e-07
25%      1.559892e-06
50%      2.339838e-06
75%      3.899730e-06
max      1.000000e+00
Name: clock_freq_normalized, dtype: float64

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

🔹 Column: clock_time_between
----------------------------------------
count    1.006032e+08
mean     1.263899e+04
std      2.030927e+04
min      0.000000e+00
25%      2.680000e+02
50%      3.459000e+03
75%      1.255000e+04
max      2.029590e+05
Name: clock_time_between, dtype: float64

🔹 Column: clock_freq
----------------------------------------
count    1.006032e+08
mean     1.204686e+01
std      5.463172e+02
min      1.000000e+00
25%      2.000000e+00
50%      4.000000e+00
75%      7.000000e+00
max      1.282140e+06
Name: clock_freq, dtype: float64

🔹 Column: clock_time_between_normalized
----------------------------------------
count    1.006032e+08
mean     6.227360e-02
std      1.000659e-01
min      0.000000e+00
25%      1.320464e-03
50%      1.704285e-02
75%      6.183515e-02
max      1.000000e+00
Name: clock_time_between_normalized, dtype: float64

🔹 Column: clock_freq_normalized
----------------------------------------
count    1.006032e+08
mean     9.395898e-06
std      4.260979e-04
min      7.799460e-07
25%      1.559892e-06
50%      3.119784e-06
75%      5.459622e-06
max      1.000000e+00
Name: clock_freq_normalized, dtype: float64

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

🔹 Column: clock_time_between
----------------------------------------
count    1.264748e+08
mean     8.670534e+03
std      1.840669e+04
min      0.000000e+00
25%      5.000000e+00
50%      3.870000e+02
75%      6.097000e+03
max      1.673230e+05
Name: clock_time_between, dtype: float64

🔹 Column: clock_freq
----------------------------------------
count    1.264748e+08
mean     4.027953e+00
std      6.685553e+01
min      1.000000e+00
25%      2.000000e+00
50%      3.000000e+00
75%      4.000000e+00
max      7.299890e+05
Name: clock_freq, dtype: float64

🔹 Column: clock_time_between_normalized
----------------------------------------
count    1.264748e+08
mean     4.272062e-02
std      9.069167e-02
min      0.000000e+00
25%      2.463552e-05
50%      1.906789e-03
75%      3.004055e-02
max      8.244177e-01
Name: clock_time_between_normalized, dtype: float64

🔹 Column: clock_freq_normalized
----------------------------------------
count    1.264748e+08
mean     3.141586e-06
std      5.214371e-05
min      7.799460e-07
25%      1.559892e-06
50%      2.339838e-06
75%      3.119784e-06
max      5.693520e-01
Name: clock_freq_normalized, dtype: float64

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

           0       0.61      0.41      0.49  25150809
           1       0.63      0.79      0.70  31618696

    accuracy                           0.62  56769505
   macro avg       0.62      0.60      0.60  56769505
weighted avg       0.62      0.62      0.61  56769505

Accuracy: 0.6243615124000113
Confusion Matrix:
[[10434519 14716290]
 [ 6608521 25010175]]
Confusion Matrix (%):
[[18.38050024 25.92287884]
 [11.64096992 44.055651  ]]
