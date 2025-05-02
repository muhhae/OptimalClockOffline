#### Datasets

🧾 Basic Info:
------------------------------------------------------------
<class 'pandas.core.frame.DataFrame'>
Index: 321914325 entries, 227745590 to 136587840
Data columns (total 5 columns):
 #   Column                         Dtype  
---  ------                         -----  
 0   clock_time_between             int64  
 1   clock_freq                     int64  
 2   clock_time_between_normalized  float64
 3   clock_freq_normalized          float64
 4   wasted                         int64  
dtypes: float64(2), int64(3)
memory usage: 14.4 GB
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
clock_time_between               43799
clock_freq                       10494
clock_time_between_normalized    43799
clock_freq_normalized            10494
wasted                               2
dtype: int64

📊 Column-wise Summary Statistics:
------------------------------------------------------------

🔹 Column: clock_time_between
----------------------------------------
Type: int64
Missing: 0
Unique: 43799
count    3.219143e+08
mean     6.714856e+02
std      3.383158e+03
min      0.000000e+00
25%      9.000000e+00
50%      8.700000e+01
75%      5.840000e+02
max      1.020300e+05
Name: clock_time_between, dtype: float64

🔹 Column: clock_freq
----------------------------------------
Type: int64
Missing: 0
Unique: 10494
count    3.219143e+08
mean     4.989603e+00
std      8.107542e+01
min      1.000000e+00
25%      2.000000e+00
50%      3.000000e+00
75%      4.000000e+00
max      1.313280e+05
Name: clock_freq, dtype: float64

🔹 Column: clock_time_between_normalized
----------------------------------------
Type: float64
Missing: 0
Unique: 43799
count    3.219143e+08
mean     6.581257e-03
std      3.315847e-02
min      0.000000e+00
25%      8.820935e-05
50%      8.526904e-04
75%      5.723807e-03
max      1.000000e+00
Name: clock_time_between_normalized, dtype: float64

🔹 Column: clock_freq_normalized
----------------------------------------
Type: float64
Missing: 0
Unique: 10494
count    3.219143e+08
mean     3.799344e-05
std      6.173506e-04
min      7.614522e-06
25%      1.522904e-05
50%      2.284357e-05
75%      3.045809e-05
max      1.000000e+00
Name: clock_freq_normalized, dtype: float64

🔹 Column: wasted
----------------------------------------
Type: int64
Missing: 0
Unique: 2
count    3.219143e+08
mean     6.023167e-01
std      4.894193e-01
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
count    1.280199e+08
mean     6.094780e+02
std      2.320227e+03
min      0.000000e+00
25%      5.400000e+01
50%      1.430000e+02
75%      6.020000e+02
max      9.778800e+04
Name: clock_time_between, dtype: float64

🔹 Column: clock_freq
----------------------------------------
count    1.280199e+08
mean     6.733508e+00
std      1.275623e+02
min      1.000000e+00
25%      2.000000e+00
50%      3.000000e+00
75%      5.000000e+00
max      1.056880e+05
Name: clock_freq, dtype: float64

🔹 Column: clock_time_between_normalized
----------------------------------------
count    1.280199e+08
mean     5.973518e-03
std      2.274063e-02
min      0.000000e+00
25%      5.292561e-04
50%      1.401549e-03
75%      5.900225e-03
max      9.584240e-01
Name: clock_time_between_normalized, dtype: float64

🔹 Column: clock_freq_normalized
----------------------------------------
count    1.280199e+08
mean     5.127244e-05
std      9.713262e-04
min      7.614522e-06
25%      1.522904e-05
50%      2.284357e-05
75%      3.807261e-05
max      8.047636e-01
Name: clock_freq_normalized, dtype: float64

🔹 Column: wasted
----------------------------------------
count    128019938.0
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
count    1.938944e+08
mean     7.124265e+02
std      3.929914e+03
min      0.000000e+00
25%      1.000000e+00
50%      6.500000e+01
75%      5.210000e+02
max      1.020300e+05
Name: clock_time_between, dtype: float64

🔹 Column: clock_freq
----------------------------------------
count    1.938944e+08
mean     3.838180e+00
std      1.288865e+01
min      1.000000e+00
25%      2.000000e+00
50%      2.000000e+00
75%      4.000000e+00
max      1.313280e+05
Name: clock_freq, dtype: float64

🔹 Column: clock_time_between_normalized
----------------------------------------
count    1.938944e+08
mean     6.982520e-03
std      3.851724e-02
min      0.000000e+00
25%      9.801039e-06
50%      6.370675e-04
75%      5.106341e-03
max      1.000000e+00
Name: clock_time_between_normalized, dtype: float64

🔹 Column: clock_freq_normalized
----------------------------------------
count    1.938944e+08
mean     2.922590e-05
std      9.814089e-05
min      7.614522e-06
25%      1.522904e-05
50%      1.522904e-05
75%      3.045809e-05
max      1.000000e+00
Name: clock_freq_normalized, dtype: float64

🔹 Column: wasted
----------------------------------------
count    193894387.0
mean             1.0
std              0.0
min              1.0
25%              1.0
50%              1.0
75%              1.0
max              1.0
Name: wasted, dtype: float64
#### Model
[1 1 0 ... 0 1 1]
Classification Report:
              precision    recall  f1-score   support

           0       0.46      0.25      0.33  32004985
           1       0.62      0.81      0.70  48473597

    accuracy                           0.59  80478582
   macro avg       0.54      0.53      0.51  80478582
weighted avg       0.56      0.59      0.55  80478582

Accuracy: 0.5866565715583806
Confusion Matrix:
[[ 8124337 23880648]
 [ 9384645 39088952]]
Confusion Matrix (%):
[[10.09503    29.67329618]
 [11.66104666 48.57062715]]
