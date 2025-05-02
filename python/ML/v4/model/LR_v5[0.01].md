#### Datasets

🧾 Basic Info:
------------------------------------------------------------
<class 'pandas.core.frame.DataFrame'>
Index: 321914325 entries, 227745590 to 136587840
Data columns (total 3 columns):
 #   Column                         Dtype  
---  ------                         -----  
 0   clock_time_between_normalized  float64
 1   clock_freq_normalized          float64
 2   wasted                         int64  
dtypes: float64(2), int64(1)
memory usage: 9.6 GB
None

📌 Missing Values:
------------------------------------------------------------
clock_time_between_normalized    0
clock_freq_normalized            0
wasted                           0
dtype: int64

🆔 Unique Values per Column:
------------------------------------------------------------
clock_time_between_normalized    4917682
clock_freq_normalized             162967
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

           0       0.47      0.27      0.34  32004985
           1       0.62      0.80      0.70  48473597

    accuracy                           0.59  80478582
   macro avg       0.54      0.53      0.52  80478582
weighted avg       0.56      0.59      0.56  80478582

Accuracy: 0.5863844370418952
Confusion Matrix:
[[ 8644324 23360661]
 [ 9926533 38547064]]
Confusion Matrix (%):
[[10.7411485  29.02717769]
 [12.33437861 47.89729521]]
