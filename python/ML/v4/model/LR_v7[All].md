#### Datasets

🧾 Basic Info:
------------------------------------------------------------
<class 'pandas.core.frame.DataFrame'>
Index: 1036455761 entries, 15812354 to 490073092
Data columns (total 5 columns):
 #   Column                         Dtype  
---  ------                         -----  
 0   clock_time_between             float64
 1   clock_freq                     float64
 2   clock_time_between_normalized  float64
 3   clock_freq_normalized          float64
 4   wasted                         int64  
dtypes: float64(4), int64(1)
memory usage: 46.3 GB
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
clock_time_between               693415
clock_freq                        21150
clock_time_between_normalized    693415
clock_freq_normalized             21150
wasted                                2
dtype: int64

📊 Column-wise Summary Statistics:
------------------------------------------------------------

🔹 Column: clock_time_between
----------------------------------------
Type: float64
Missing: 0
Unique: 693415
count    1.036456e+09
mean     1.752578e+04
std      4.873857e+04
min      0.000000e+00
25%      2.000000e+00
50%      2.240000e+02
75%      4.567000e+03
max      1.122030e+06
Name: clock_time_between, dtype: float64

🔹 Column: clock_freq
----------------------------------------
Type: float64
Missing: 0
Unique: 21150
count    1.036456e+09
mean     7.848518e+00
std      5.576205e+02
min      1.000000e+00
25%      2.000000e+00
50%      3.000000e+00
75%      5.000000e+00
max      5.709380e+06
Name: clock_freq, dtype: float64

🔹 Column: clock_time_between_normalized
----------------------------------------
Type: float64
Missing: 0
Unique: 693415
count    1.036456e+09
mean     1.561971e-02
std      4.343785e-02
min      0.000000e+00
25%      1.782484e-06
50%      1.996382e-04
75%      4.070301e-03
max      1.000000e+00
Name: clock_time_between_normalized, dtype: float64

🔹 Column: clock_freq_normalized
----------------------------------------
Type: float64
Missing: 0
Unique: 21150
count    1.036456e+09
mean     1.374671e-06
std      9.766744e-05
min      1.751504e-07
25%      3.503007e-07
50%      5.254511e-07
75%      8.757518e-07
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

🔹 Column: clock_time_between
----------------------------------------
count    4.522173e+08
mean     2.565060e+04
std      5.641848e+04
min      0.000000e+00
25%      7.200000e+01
50%      1.082000e+03
75%      1.982300e+04
max      1.122030e+06
Name: clock_time_between, dtype: float64

🔹 Column: clock_freq
----------------------------------------
count    4.522173e+08
mean     1.182009e+01
std      8.371433e+02
min      1.000000e+00
25%      2.000000e+00
50%      3.000000e+00
75%      6.000000e+00
max      5.709380e+06
Name: clock_freq, dtype: float64

🔹 Column: clock_time_between_normalized
----------------------------------------
count    4.522173e+08
mean     2.286089e-02
std      5.028250e-02
min      0.000000e+00
25%      6.416941e-05
50%      9.643236e-04
75%      1.766709e-02
max      1.000000e+00
Name: clock_time_between_normalized, dtype: float64

🔹 Column: clock_freq_normalized
----------------------------------------
count    4.522173e+08
mean     2.070293e-06
std      1.466260e-04
min      1.751504e-07
25%      3.503007e-07
50%      5.254511e-07
75%      1.050902e-06
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

🔹 Column: clock_time_between
----------------------------------------
count    5.842385e+08
mean     1.123693e+04
std      4.073941e+04
min      0.000000e+00
25%      0.000000e+00
50%      4.800000e+01
75%      9.000000e+02
max      9.229410e+05
Name: clock_time_between, dtype: float64

🔹 Column: clock_freq
----------------------------------------
count    5.842385e+08
mean     4.774407e+00
std      9.565478e+01
min      1.000000e+00
25%      2.000000e+00
50%      3.000000e+00
75%      4.000000e+00
max      7.299890e+05
Name: clock_freq, dtype: float64

🔹 Column: clock_time_between_normalized
----------------------------------------
count    5.842385e+08
mean     1.001482e-02
std      3.630867e-02
min      0.000000e+00
25%      0.000000e+00
50%      4.277960e-05
75%      8.021176e-04
max      8.225636e-01
Name: clock_time_between_normalized, dtype: float64

🔹 Column: clock_freq_normalized
----------------------------------------
count    5.842385e+08
mean     8.362392e-07
std      1.675397e-05
min      1.751504e-07
25%      3.503007e-07
50%      5.254511e-07
75%      7.006015e-07
max      1.278578e-01
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

           0       0.64      0.38      0.48 113054316
           1       0.64      0.84      0.72 146059625

    accuracy                           0.64 259113941
   macro avg       0.64      0.61      0.60 259113941
weighted avg       0.64      0.64      0.61 259113941

Accuracy: 0.6369057618555537
Confusion Matrix:
[[ 42863536  70190780]
 [ 23891999 122167626]]
Confusion Matrix (%):
[[16.54235038 27.08877019]
 [ 9.22065363 47.14822581]]
