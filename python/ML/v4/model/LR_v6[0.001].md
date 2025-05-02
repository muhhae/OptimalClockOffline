#### Datasets

🧾 Basic Info:
------------------------------------------------------------
<class 'pandas.core.frame.DataFrame'>
Index: 186191784 entries, 185502581 to 155768186
Data columns (total 4 columns):
 #   Column                         Dtype  
---  ------                         -----  
 0   clock_time_between_normalized  float64
 1   clock_freq_normalized          float64
 2   lifetime_freq_normalized       float64
 3   wasted                         int64  
dtypes: float64(3), int64(1)
memory usage: 6.9 GB
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
clock_time_between_normalized    3730193
clock_freq_normalized             502287
lifetime_freq_normalized         4810434
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

🔹 Column: lifetime_freq_normalized
----------------------------------------
Type: float64
Missing: 0
Unique: 4810434
count    1.861918e+08
mean     1.337510e-02
std      5.674398e-02
min      1.312050e-07
25%      7.500840e-05
50%      7.933110e-04
75%      5.490300e-03
max      1.000000e+00
Name: lifetime_freq_normalized, dtype: float64

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

🔹 Column: lifetime_freq_normalized
----------------------------------------
count    3.538636e+07
mean     2.337943e-02
std      9.524708e-02
min      1.312050e-07
25%      2.252750e-04
50%      1.267240e-03
75%      9.803240e-03
max      1.000000e+00
Name: lifetime_freq_normalized, dtype: float64

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

🔹 Column: lifetime_freq_normalized
----------------------------------------
count    1.508054e+08
mean     1.102759e-02
std      4.263434e-02
min      1.312050e-07
25%      5.278480e-05
50%      6.285330e-04
75%      5.311560e-03
max      1.000000e+00
Name: lifetime_freq_normalized, dtype: float64

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
[1 1 1 ... 0 1 1]
Classification Report:
              precision    recall  f1-score   support

           0       0.23      0.32      0.27   8846591
           1       0.83      0.75      0.79  37701355

    accuracy                           0.67  46547946
   macro avg       0.53      0.54      0.53  46547946
weighted avg       0.71      0.67      0.69  46547946

Accuracy: 0.671658294009364
Confusion Matrix:
[[ 2824232  6022359]
 [ 9261273 28440082]]
Confusion Matrix (%):
[[ 6.06736117 12.93796938]
 [19.89620122 61.09846823]]
