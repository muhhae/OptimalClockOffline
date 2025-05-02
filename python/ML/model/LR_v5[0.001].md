#### Datasets

🧾 Basic Info:
------------------------------------------------------------
<class 'pandas.core.frame.DataFrame'>
Index: 186191784 entries, 185502581 to 155768186
Data columns (total 3 columns):
 #   Column                         Dtype  
---  ------                         -----  
 0   clock_time_between_normalized  float64
 1   clock_freq_normalized          float64
 2   wasted                         int64  
dtypes: float64(2), int64(1)
memory usage: 5.5 GB
None

📌 Missing Values:
------------------------------------------------------------
clock_time_between_normalized    0
clock_freq_normalized            0
wasted                           0
dtype: int64

🆔 Unique Values per Column:
------------------------------------------------------------
clock_time_between_normalized    3730193
clock_freq_normalized             502287
wasted                                 2
dtype: int64

📊 Column-wise Summary Statistics:
------------------------------------------------------------

🔹 Column: clock_time_between_normalized
----------------------------------------
Type: float64
Missing: 0
Unique: 3730193
count    1.861918e+08
mean     1.906744e-04
std      3.828105e-03
min      0.000000e+00
25%      0.000000e+00
50%      5.701750e-08
75%      3.253800e-05
max      9.727270e-01
Name: clock_time_between_normalized, dtype: float64

🔹 Column: clock_freq_normalized
----------------------------------------
Type: float64
Missing: 0
Unique: 502287
count    1.861918e+08
mean     8.283615e-03
std      3.334057e-02
min      1.369880e-06
25%      1.961550e-04
50%      1.103750e-03
75%      2.619520e-03
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

🔹 Column: clock_time_between_normalized
----------------------------------------
count    3.538636e+07
mean     3.685534e-04
std      5.203735e-03
min      0.000000e+00
25%      1.900990e-08
50%      2.024250e-05
75%      1.115900e-04
max      9.666670e-01
Name: clock_time_between_normalized, dtype: float64

🔹 Column: clock_freq_normalized
----------------------------------------
count    3.538636e+07
mean     4.618194e-03
std      2.709610e-02
min      1.369880e-06
25%      1.500860e-04
50%      6.835270e-04
75%      2.290080e-03
max      1.000000e+00
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

🔹 Column: clock_time_between_normalized
----------------------------------------
count    1.508054e+08
mean     1.489352e-04
std      3.424884e-03
min      0.000000e+00
25%      0.000000e+00
50%      6.327620e-10
75%      1.667580e-05
max      9.727270e-01
Name: clock_time_between_normalized, dtype: float64

🔹 Column: clock_freq_normalized
----------------------------------------
count    1.508054e+08
mean     9.143703e-03
std      3.458695e-02
min      1.369880e-06
25%      2.270660e-04
50%      1.103750e-03
75%      2.699060e-03
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
[0 0 0 ... 0 0 0]
Classification Report:
              precision    recall  f1-score   support

           0       0.20      0.92      0.34   8846591
           1       0.90      0.16      0.27  37701355

    accuracy                           0.30  46547946
   macro avg       0.55      0.54      0.30  46547946
weighted avg       0.77      0.30      0.28  46547946

Accuracy: 0.30274790213084807
Confusion Matrix:
[[ 8179322   667269]
 [31788384  5912971]]
Confusion Matrix (%):
[[17.57182154  1.43350901]
 [68.29170078 12.70296868]]
