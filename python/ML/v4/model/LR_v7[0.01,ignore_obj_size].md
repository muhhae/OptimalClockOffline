#### Datasets

🧾 Basic Info:
------------------------------------------------------------
<class 'pandas.core.frame.DataFrame'>
Index: 302965548 entries, 291503067 to 215269799
Data columns (total 5 columns):
 #   Column                         Dtype  
---  ------                         -----  
 0   clock_time_between             int64  
 1   clock_freq                     int64  
 2   clock_time_between_normalized  float64
 3   clock_freq_normalized          float64
 4   wasted                         int64  
dtypes: float64(2), int64(3)
memory usage: 13.5 GB
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
clock_time_between               30265
clock_freq                        6687
clock_time_between_normalized    30265
clock_freq_normalized             6687
wasted                               2
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

           0       0.47      0.29      0.36  26581015
           1       0.68      0.82      0.75  49160373

    accuracy                           0.64  75741388
   macro avg       0.57      0.56      0.55  75741388
weighted avg       0.61      0.64      0.61  75741388

Accuracy: 0.6354612355400723
Confusion Matrix:
[[ 7599202 18981813]
 [ 8628859 40531514]]
Confusion Matrix (%):
[[10.03309049 25.06134823]
 [11.39252822 53.51303306]]
