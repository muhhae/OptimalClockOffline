#### Datasets

🧾 Basic Info:
------------------------------------------------------------
<class 'pandas.core.frame.DataFrame'>
Index: 302965548 entries, 291503067 to 215269799
Data columns (total 3 columns):
 #   Column                         Dtype  
---  ------                         -----  
 0   clock_time_between_normalized  float64
 1   clock_freq_normalized          float64
 2   wasted                         int64  
dtypes: float64(2), int64(1)
memory usage: 9.0 GB
None

📌 Missing Values:
------------------------------------------------------------
clock_time_between_normalized    0
clock_freq_normalized            0
wasted                           0
dtype: int64

🆔 Unique Values per Column:
------------------------------------------------------------
clock_time_between_normalized    4894821
clock_freq_normalized             352180
wasted                                 2
dtype: int64

📊 Column-wise Summary Statistics:
------------------------------------------------------------

🔹 Column: clock_time_between_normalized
----------------------------------------
Type: float64
Missing: 0
Unique: 4894821
count    3.029655e+08
mean     1.921959e-03
std      1.285088e-02
min      0.000000e+00
25%      1.689940e-08
50%      1.621950e-04
75%      8.194520e-04
max      9.980480e-01
Name: clock_time_between_normalized, dtype: float64

🔹 Column: clock_freq_normalized
----------------------------------------
Type: float64
Missing: 0
Unique: 352180
count    3.029655e+08
mean     4.956366e-03
std      1.258190e-02
min      1.369880e-06
25%      3.102700e-04
50%      2.512560e-03
75%      6.756760e-03
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

🔹 Column: clock_time_between_normalized
----------------------------------------
count    1.063241e+08
mean     2.501549e-03
std      1.378406e-02
min      0.000000e+00
25%      6.661590e-05
50%      4.663750e-04
75%      1.334640e-03
max      9.970030e-01
Name: clock_time_between_normalized, dtype: float64

🔹 Column: clock_freq_normalized
----------------------------------------
count    1.063241e+08
mean     5.515869e-03
std      1.405546e-02
min      1.369880e-06
25%      3.770030e-04
50%      2.717390e-03
75%      7.537690e-03
max      1.000000e+00
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

🔹 Column: clock_time_between_normalized
----------------------------------------
count    1.966415e+08
mean     1.608574e-03
std      1.230553e-02
min      0.000000e+00
25%      0.000000e+00
50%      3.343600e-05
75%      5.433860e-04
max      9.980480e-01
Name: clock_time_between_normalized, dtype: float64

🔹 Column: clock_freq_normalized
----------------------------------------
count    1.966415e+08
mean     4.653842e-03
std      1.169701e-02
min      1.369880e-06
25%      2.880600e-04
50%      1.805050e-03
75%      5.484460e-03
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
[1 1 1 ... 1 1 1]
Classification Report:
              precision    recall  f1-score   support

           0       0.45      0.37      0.41  26581015
           1       0.69      0.75      0.72  49160373

    accuracy                           0.62  75741388
   macro avg       0.57      0.56      0.56  75741388
weighted avg       0.60      0.62      0.61  75741388

Accuracy: 0.6176431702043802
Confusion Matrix:
[[ 9952697 16628318]
 [12331919 36828454]]
Confusion Matrix (%):
[[13.14036785 21.95407087]
 [16.28161211 48.62394917]]
