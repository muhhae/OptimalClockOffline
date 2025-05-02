#### Datasets

🧾 Basic Info:
------------------------------------------------------------
<class 'pandas.core.frame.DataFrame'>
Index: 321914325 entries, 227745590 to 136587840
Data columns (total 7 columns):
 #   Column                         Dtype  
---  ------                         -----  
 0   clock_time_between             int64  
 1   clock_freq                     int64  
 2   lifetime_freq                  float64
 3   clock_time_between_normalized  float64
 4   clock_freq_normalized          float64
 5   lifetime_freq_normalized       float64
 6   wasted                         int64  
dtypes: float64(4), int64(3)
memory usage: 19.2 GB
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
clock_time_between                43799
clock_freq                        10494
lifetime_freq                    140044
clock_time_between_normalized     43799
clock_freq_normalized             10494
lifetime_freq_normalized         140044
wasted                                2
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

🔹 Column: lifetime_freq
----------------------------------------
Type: float64
Missing: 0
Unique: 140044
count    3.219143e+08
mean     1.078241e+03
std      2.796553e+04
min      2.000000e+00
25%      2.200000e+01
50%      1.360000e+02
75%      4.910000e+02
max      1.521720e+07
Name: lifetime_freq, dtype: float64

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

🔹 Column: lifetime_freq_normalized
----------------------------------------
Type: float64
Missing: 0
Unique: 140044
count    3.219143e+08
mean     7.085673e-05
std      1.837758e-03
min      1.314302e-07
25%      1.445732e-06
50%      8.937255e-06
75%      3.226612e-05
max      1.000000e+00
Name: lifetime_freq_normalized, dtype: float64

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

🔹 Column: lifetime_freq
----------------------------------------
count    1.280199e+08
mean     2.289174e+03
std      4.425284e+04
min      2.000000e+00
25%      9.500000e+01
50%      3.510000e+02
75%      9.430000e+02
max      1.521720e+07
Name: lifetime_freq, dtype: float64

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

🔹 Column: lifetime_freq_normalized
----------------------------------------
count    1.280199e+08
mean     1.504333e-04
std      2.908080e-03
min      1.314302e-07
25%      6.242936e-06
50%      2.306600e-05
75%      6.196935e-05
max      1.000000e+00
Name: lifetime_freq_normalized, dtype: float64

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

🔹 Column: lifetime_freq
----------------------------------------
count    1.938944e+08
mean     2.787154e+02
std      1.959952e+03
min      2.000000e+00
25%      1.000000e+01
50%      6.300000e+01
75%      2.760000e+02
max      6.555200e+06
Name: lifetime_freq, dtype: float64

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

🔹 Column: lifetime_freq_normalized
----------------------------------------
count    1.938944e+08
mean     1.831581e-05
std      1.287985e-04
min      1.314302e-07
25%      6.571511e-07
50%      4.140052e-06
75%      1.813737e-05
max      4.307757e-01
Name: lifetime_freq_normalized, dtype: float64

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
[1 1 1 ... 0 1 1]
Classification Report:
              precision    recall  f1-score   support

           0       0.67      0.38      0.49  32004985
           1       0.68      0.87      0.77  48473597

    accuracy                           0.68  80478582
   macro avg       0.67      0.63      0.63  80478582
weighted avg       0.68      0.68      0.65  80478582

Accuracy: 0.6780983790196502
Confusion Matrix:
[[12245154 19759831]
 [ 6146355 42327242]]
Confusion Matrix (%):
[[15.21541968 24.55290651]
 [ 7.63725559 52.59441823]]
