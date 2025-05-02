#### Datasets

🧾 Basic Info:
------------------------------------------------------------
<class 'pandas.core.frame.DataFrame'>
Index: 302965548 entries, 291503067 to 215269799
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
memory usage: 18.1 GB
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
clock_time_between                30265
clock_freq                         6687
lifetime_freq                    202240
clock_time_between_normalized     30265
clock_freq_normalized              6687
lifetime_freq_normalized         202240
wasted                                2
dtype: int64

📊 Column-wise Summary Statistics:
------------------------------------------------------------

🔹 Column: clock_time_between
----------------------------------------
Type: int64
Missing: 0
Unique: 30265
count    3.029655e+08
mean     5.141763e+02
std      2.494768e+03
min      0.000000e+00
25%      1.000000e+00
50%      8.500000e+01
75%      5.810000e+02
max      1.051850e+05
Name: clock_time_between, dtype: float64

🔹 Column: clock_freq
----------------------------------------
Type: int64
Missing: 0
Unique: 6687
count    3.029655e+08
mean     5.068077e+00
std      8.278760e+01
min      1.000000e+00
25%      2.000000e+00
50%      3.000000e+00
75%      4.000000e+00
max      7.299890e+05
Name: clock_freq, dtype: float64

🔹 Column: lifetime_freq
----------------------------------------
Type: float64
Missing: 0
Unique: 202240
count    3.029655e+08
mean     2.175074e+03
std      6.473963e+04
min      2.000000e+00
25%      2.100000e+01
50%      1.420000e+02
75%      4.960000e+02
max      1.523120e+07
Name: lifetime_freq, dtype: float64

🔹 Column: clock_time_between_normalized
----------------------------------------
Type: float64
Missing: 0
Unique: 30265
count    3.029655e+08
mean     4.888304e-03
std      2.371791e-02
min      0.000000e+00
25%      9.507059e-06
50%      8.081000e-04
75%      5.523601e-03
max      1.000000e+00
Name: clock_time_between_normalized, dtype: float64

🔹 Column: clock_freq_normalized
----------------------------------------
Type: float64
Missing: 0
Unique: 6687
count    3.029655e+08
mean     6.942675e-06
std      1.134094e-04
min      1.369884e-06
25%      2.739767e-06
50%      4.109651e-06
75%      5.479535e-06
max      1.000000e+00
Name: clock_freq_normalized, dtype: float64

🔹 Column: lifetime_freq_normalized
----------------------------------------
Type: float64
Missing: 0
Unique: 202240
count    3.029655e+08
mean     1.428038e-04
std      4.250462e-03
min      1.313094e-07
25%      1.378749e-06
50%      9.322969e-06
75%      3.256474e-05
max      1.000000e+00
Name: lifetime_freq_normalized, dtype: float64

🔹 Column: wasted
----------------------------------------
Type: int64
Missing: 0
Unique: 2
count    3.029655e+08
mean     6.490556e-01
std      4.772656e-01
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
count    1.063241e+08
mean     6.284067e+02
std      2.278205e+03
min      0.000000e+00
25%      4.500000e+01
50%      3.110000e+02
75%      6.310000e+02
max      7.317500e+04
Name: clock_time_between, dtype: float64

🔹 Column: clock_freq
----------------------------------------
count    1.063241e+08
mean     6.903835e+00
std      1.111919e+02
min      1.000000e+00
25%      2.000000e+00
50%      3.000000e+00
75%      5.000000e+00
max      9.814900e+04
Name: clock_freq, dtype: float64

🔹 Column: lifetime_freq
----------------------------------------
count    1.063241e+08
mean     3.834069e+03
std      1.082892e+05
min      2.000000e+00
25%      8.800000e+01
50%      3.050000e+02
75%      6.860000e+02
max      1.523120e+07
Name: lifetime_freq, dtype: float64

🔹 Column: clock_time_between_normalized
----------------------------------------
count    1.063241e+08
mean     5.974300e-03
std      2.165903e-02
min      0.000000e+00
25%      4.278177e-04
50%      2.956695e-03
75%      5.998954e-03
max      6.956790e-01
Name: clock_time_between_normalized, dtype: float64

🔹 Column: clock_freq_normalized
----------------------------------------
count    1.063241e+08
mean     9.457451e-06
std      1.523200e-04
min      1.369884e-06
25%      2.739767e-06
50%      4.109651e-06
75%      6.849418e-06
max      1.344527e-01
Name: clock_freq_normalized, dtype: float64

🔹 Column: lifetime_freq_normalized
----------------------------------------
count    1.063241e+08
mean     2.517247e-04
std      7.109694e-03
min      1.313094e-07
25%      5.777614e-06
50%      2.002469e-05
75%      4.503913e-05
max      1.000000e+00
Name: lifetime_freq_normalized, dtype: float64

🔹 Column: wasted
----------------------------------------
count    106324058.0
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
count    1.966415e+08
mean     4.524119e+02
std      2.602286e+03
min      0.000000e+00
25%      0.000000e+00
50%      3.300000e+01
75%      4.400000e+02
max      1.051850e+05
Name: clock_time_between, dtype: float64

🔹 Column: clock_freq
----------------------------------------
count    1.966415e+08
mean     4.075482e+00
std      6.222377e+01
min      1.000000e+00
25%      2.000000e+00
50%      3.000000e+00
75%      4.000000e+00
max      7.299890e+05
Name: clock_freq, dtype: float64

🔹 Column: lifetime_freq
----------------------------------------
count    1.966415e+08
mean     1.278055e+03
std      1.070404e+04
min      2.000000e+00
25%      1.000000e+01
50%      7.700000e+01
75%      3.660000e+02
max      8.746610e+06
Name: lifetime_freq, dtype: float64

🔹 Column: clock_time_between_normalized
----------------------------------------
count    1.966415e+08
mean     4.301106e-03
std      2.474009e-02
min      0.000000e+00
25%      0.000000e+00
50%      3.137329e-04
75%      4.183106e-03
max      1.000000e+00
Name: clock_time_between_normalized, dtype: float64

🔹 Column: clock_freq_normalized
----------------------------------------
count    1.966415e+08
mean     5.582936e-06
std      8.523933e-05
min      1.369884e-06
25%      2.739767e-06
50%      4.109651e-06
75%      5.479535e-06
max      1.000000e+00
Name: clock_freq_normalized, dtype: float64

🔹 Column: lifetime_freq_normalized
----------------------------------------
count    1.966415e+08
mean     8.391033e-05
std      7.027705e-04
min      1.313094e-07
25%      6.565471e-07
50%      5.055413e-06
75%      2.402962e-05
max      5.742561e-01
Name: lifetime_freq_normalized, dtype: float64

🔹 Column: wasted
----------------------------------------
count    196641490.0
mean             1.0
std              0.0
min              1.0
25%              1.0
50%              1.0
75%              1.0
max              1.0
Name: wasted, dtype: float64
#### Model
[1 1 1 ... 0 0 1]
Classification Report:
              precision    recall  f1-score   support

           0       0.43      0.28      0.34  26581015
           1       0.67      0.79      0.73  49160373

    accuracy                           0.62  75741388
   macro avg       0.55      0.54      0.54  75741388
weighted avg       0.59      0.62      0.59  75741388

Accuracy: 0.6157447761585779
Confusion Matrix:
[[ 7565755 19015260]
 [10088764 39071609]]
Confusion Matrix (%):
[[ 9.98893102 25.1055077 ]
 [13.32001468 51.5855466 ]]
