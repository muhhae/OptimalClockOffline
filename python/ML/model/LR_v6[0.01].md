#### Datasets

🧾 Basic Info:
------------------------------------------------------------
<class 'pandas.core.frame.DataFrame'>
Index: 321914325 entries, 227745590 to 136587840
Data columns (total 4 columns):
 #   Column                         Dtype  
---  ------                         -----  
 0   clock_time_between_normalized  float64
 1   clock_freq_normalized          float64
 2   lifetime_freq_normalized       float64
 3   wasted                         int64  
dtypes: float64(3), int64(1)
memory usage: 12.0 GB
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
clock_time_between_normalized    4917682
clock_freq_normalized             162967
lifetime_freq_normalized         4687607
wasted                                 2
dtype: int64

📊 Column-wise Summary Statistics:
------------------------------------------------------------

🔹 Column: clock_time_between_normalized
----------------------------------------
Type: float64
Missing: 0
Unique: 4917682
count    3.219143e+08
mean     2.135940e-03
std      1.447465e-02
min      0.000000e+00
25%      4.940350e-08
50%      1.437560e-04
75%      7.931480e-04
max      1.000000e+00
Name: clock_time_between_normalized, dtype: float64

🔹 Column: clock_freq_normalized
----------------------------------------
Type: float64
Missing: 0
Unique: 162967
count    3.219143e+08
mean     5.349632e-03
std      1.307972e-02
min      1.369880e-06
25%      2.316600e-04
50%      2.512560e-03
75%      6.250000e-03
max      1.000000e+00
Name: clock_freq_normalized, dtype: float64

🔹 Column: lifetime_freq_normalized
----------------------------------------
Type: float64
Missing: 0
Unique: 4687607
count    3.219143e+08
mean     1.273765e-02
std      3.501481e-02
min      1.312050e-07
25%      1.482250e-04
50%      2.021460e-03
75%      6.581780e-03
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

🔹 Column: clock_time_between_normalized
----------------------------------------
count    1.280199e+08
mean     2.380142e-03
std      1.395668e-02
min      0.000000e+00
25%      2.244440e-05
50%      3.629870e-04
75%      1.126560e-03
max      1.000000e+00
Name: clock_time_between_normalized, dtype: float64

🔹 Column: clock_freq_normalized
----------------------------------------
count    1.280199e+08
mean     5.484683e-03
std      1.218904e-02
min      1.369880e-06
25%      2.316600e-04
50%      2.512560e-03
75%      7.537690e-03
max      1.000000e+00
Name: clock_freq_normalized, dtype: float64

🔹 Column: lifetime_freq_normalized
----------------------------------------
count    1.280199e+08
mean     1.698607e-02
std      4.699784e-02
min      1.312050e-07
25%      6.410730e-04
50%      3.289980e-03
75%      6.967200e-03
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

🔹 Column: clock_time_between_normalized
----------------------------------------
count    1.938944e+08
mean     1.974705e-03
std      1.480451e-02
min      0.000000e+00
25%      1.364880e-08
50%      4.333450e-05
75%      5.750840e-04
max      9.949020e-01
Name: clock_time_between_normalized, dtype: float64

🔹 Column: clock_freq_normalized
----------------------------------------
count    1.938944e+08
mean     5.260464e-03
std      1.363521e-02
min      1.369880e-06
25%      2.316600e-04
50%      2.212390e-03
75%      5.025130e-03
max      1.000000e+00
Name: clock_freq_normalized, dtype: float64

🔹 Column: lifetime_freq_normalized
----------------------------------------
count    1.938944e+08
mean     9.932611e-03
std      2.360888e-02
min      1.313130e-07
25%      5.429470e-05
50%      9.535920e-04
75%      6.288530e-03
max      1.000000e+00
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
[0 0 1 ... 1 1 1]
Classification Report:
              precision    recall  f1-score   support

           0       0.42      0.17      0.24  32004985
           1       0.61      0.84      0.70  48473597

    accuracy                           0.58  80478582
   macro avg       0.51      0.51      0.47  80478582
weighted avg       0.53      0.58      0.52  80478582

Accuracy: 0.575178312659634
Confusion Matrix:
[[ 5444816 26560169]
 [ 7628878 40844719]]
Confusion Matrix (%):
[[ 6.76554664 33.00277955]
 [ 9.47938919 50.75228463]]
