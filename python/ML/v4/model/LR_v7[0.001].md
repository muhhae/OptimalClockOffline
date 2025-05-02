#### Datasets

🧾 Basic Info:
------------------------------------------------------------
<class 'pandas.core.frame.DataFrame'>
Index: 186191784 entries, 185502581 to 155768186
Data columns (total 5 columns):
 #   Column                         Dtype  
---  ------                         -----  
 0   clock_time_between             int64  
 1   clock_freq                     int64  
 2   clock_time_between_normalized  float64
 3   clock_freq_normalized          float64
 4   wasted                         int64  
dtypes: float64(2), int64(3)
memory usage: 8.3 GB
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
clock_time_between               10901
clock_freq                        5694
clock_time_between_normalized    10901
clock_freq_normalized             5694
wasted                               2
dtype: int64

📊 Column-wise Summary Statistics:
------------------------------------------------------------

🔹 Column: clock_time_between
----------------------------------------
Type: int64
Missing: 0
Unique: 10901
count    1.861918e+08
mean     4.345585e+01
std      5.645290e+02
min      0.000000e+00
25%      0.000000e+00
50%      1.000000e+00
75%      2.700000e+01
max      4.152700e+04
Name: clock_time_between, dtype: float64

🔹 Column: clock_freq
----------------------------------------
Type: int64
Missing: 0
Unique: 5694
count    1.861918e+08
mean     7.331200e+00
std      8.889060e+01
min      1.000000e+00
25%      2.000000e+00
50%      3.000000e+00
75%      5.000000e+00
max      7.299890e+05
Name: clock_freq, dtype: float64

🔹 Column: clock_time_between_normalized
----------------------------------------
Type: float64
Missing: 0
Unique: 10901
count    1.861918e+08
mean     1.046448e-03
std      1.359426e-02
min      0.000000e+00
25%      0.000000e+00
50%      2.408072e-05
75%      6.501794e-04
max      1.000000e+00
Name: clock_time_between_normalized, dtype: float64

🔹 Column: clock_freq_normalized
----------------------------------------
Type: float64
Missing: 0
Unique: 5694
count    1.861918e+08
mean     1.004289e-05
std      1.217698e-04
min      1.369884e-06
25%      2.739767e-06
50%      4.109651e-06
75%      6.849418e-06
max      1.000000e+00
Name: clock_freq_normalized, dtype: float64

🔹 Column: wasted
----------------------------------------
Type: int64
Missing: 0
Unique: 2
count    1.861918e+08
mean     8.099467e-01
std      3.923430e-01
min      0.000000e+00
25%      1.000000e+00
50%      1.000000e+00
75%      1.000000e+00
max      1.000000e+00
Name: wasted, dtype: float64

🚫 Subset: wasted == 0
------------------------------------------------------------

🔹 Column: clock_time_between
----------------------------------------
count    3.538636e+07
mean     8.508719e+01
std      7.308552e+02
min      0.000000e+00
25%      5.000000e+00
50%      3.000000e+01
75%      7.600000e+01
max      4.152700e+04
Name: clock_time_between, dtype: float64

🔹 Column: clock_freq
----------------------------------------
count    3.538636e+07
mean     9.587501e+00
std      5.321495e+01
min      1.000000e+00
25%      2.000000e+00
50%      4.000000e+00
75%      7.000000e+00
max      4.425800e+04
Name: clock_freq, dtype: float64

🔹 Column: clock_time_between_normalized
----------------------------------------
count    3.538636e+07
mean     2.048961e-03
std      1.759952e-02
min      0.000000e+00
25%      1.204036e-04
50%      7.224216e-04
75%      1.830135e-03
max      1.000000e+00
Name: clock_time_between_normalized, dtype: float64

🔹 Column: clock_freq_normalized
----------------------------------------
count    3.538636e+07
mean     1.313376e-05
std      7.289829e-05
min      1.369884e-06
25%      2.739767e-06
50%      5.479535e-06
75%      9.589186e-06
max      6.062831e-02
Name: clock_freq_normalized, dtype: float64

🔹 Column: wasted
----------------------------------------
count    35386364.0
mean            0.0
std             0.0
min             0.0
25%             0.0
50%             0.0
75%             0.0
max             0.0
Name: wasted, dtype: float64

✅ Subset: wasted == 1
------------------------------------------------------------

🔹 Column: clock_time_between
----------------------------------------
count    1.508054e+08
mean     3.368709e+01
std      5.173338e+02
min      0.000000e+00
25%      0.000000e+00
50%      1.000000e+00
75%      9.000000e+00
max      4.151600e+04
Name: clock_time_between, dtype: float64

🔹 Column: clock_freq
----------------------------------------
count    1.508054e+08
mean     6.801761e+00
std      9.533975e+01
min      1.000000e+00
25%      2.000000e+00
50%      3.000000e+00
75%      5.000000e+00
max      7.299890e+05
Name: clock_freq, dtype: float64

🔹 Column: clock_time_between_normalized
----------------------------------------
count    1.508054e+08
mean     8.112094e-04
std      1.245777e-02
min      0.000000e+00
25%      0.000000e+00
50%      2.408072e-05
75%      2.167265e-04
max      9.997351e-01
Name: clock_time_between_normalized, dtype: float64

🔹 Column: clock_freq_normalized
----------------------------------------
count    1.508054e+08
mean     9.317621e-06
std      1.306044e-04
min      1.369884e-06
25%      2.739767e-06
50%      4.109651e-06
75%      6.849418e-06
max      1.000000e+00
Name: clock_freq_normalized, dtype: float64

🔹 Column: wasted
----------------------------------------
count    150805420.0
mean             1.0
std              0.0
min              1.0
25%              1.0
50%              1.0
75%              1.0
max              1.0
Name: wasted, dtype: float64
#### Model
[1 1 1 ... 1 1 0]
Classification Report:
              precision    recall  f1-score   support

           0       0.39      0.42      0.41   8846591
           1       0.86      0.85      0.86  37701355

    accuracy                           0.77  46547946
   macro avg       0.63      0.63      0.63  46547946
weighted avg       0.77      0.77      0.77  46547946

Accuracy: 0.7670498500621273
Confusion Matrix:
[[ 3722427  5124164]
 [ 5719187 31982168]]
Confusion Matrix (%):
[[ 7.9969737  11.00835685]
 [12.28665815 68.70801131]]
