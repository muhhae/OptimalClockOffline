#### Datasets

🧾 Basic Info:
------------------------------------------------------------
<class 'pandas.core.frame.DataFrame'>
Index: 118046137 entries, 115656551 to 108006826
Data columns (total 4 columns):
 #   Column                         Dtype  
---  ------                         -----  
 0   clock_time_between_normalized  float64
 1   clock_freq_normalized          float64
 2   lifetime_freq_normalized       float64
 3   wasted                         int64  
dtypes: float64(3), int64(1)
memory usage: 4.4 GB
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
clock_time_between_normalized    5237151
clock_freq_normalized             459179
lifetime_freq_normalized         2915546
wasted                                 2
dtype: int64

📊 Column-wise Summary Statistics:
------------------------------------------------------------

🔹 Column: clock_time_between_normalized
----------------------------------------
Type: float64
Missing: 0
Unique: 5237151
count    1.180461e+08
mean     7.450096e-02
std      1.264329e-01
min      0.000000e+00
25%      5.054190e-05
50%      1.978480e-02
75%      8.941970e-02
max      9.992860e-01
Name: clock_time_between_normalized, dtype: float64

🔹 Column: clock_freq_normalized
----------------------------------------
Type: float64
Missing: 0
Unique: 459179
count    1.180461e+08
mean     8.710048e-04
std      5.113963e-03
min      1.624140e-07
25%      1.526070e-05
50%      4.240880e-05
75%      1.043350e-04
max      1.000000e+00
Name: clock_freq_normalized, dtype: float64

🔹 Column: lifetime_freq_normalized
----------------------------------------
Type: float64
Missing: 0
Unique: 2915546
count    1.180461e+08
mean     1.357695e-03
std      7.123644e-03
min      1.312050e-07
25%      1.109970e-05
50%      3.990960e-05
75%      9.446290e-05
max      1.000000e+00
Name: lifetime_freq_normalized, dtype: float64

🔹 Column: wasted
----------------------------------------
Type: int64
Missing: 0
Unique: 2
count    1.180461e+08
mean     3.857351e-01
std      4.867685e-01
min      0.000000e+00
25%      0.000000e+00
50%      0.000000e+00
75%      1.000000e+00
max      1.000000e+00
Name: wasted, dtype: float64

🚫 Subset: wasted == 0
------------------------------------------------------------

🔹 Column: clock_time_between_normalized
----------------------------------------
count    7.251160e+07
mean     7.756680e-02
std      1.238956e-01
min      0.000000e+00
25%      1.435640e-04
50%      2.597740e-02
75%      9.674070e-02
max      9.992860e-01
Name: clock_time_between_normalized, dtype: float64

🔹 Column: clock_freq_normalized
----------------------------------------
count    7.251160e+07
mean     1.002627e-03
std      6.044551e-03
min      1.624140e-07
25%      1.554680e-05
50%      4.664030e-05
75%      1.043350e-04
max      1.000000e+00
Name: clock_freq_normalized, dtype: float64

🔹 Column: lifetime_freq_normalized
----------------------------------------
count    7.251160e+07
mean     1.516519e-03
std      8.041211e-03
min      1.312050e-07
25%      1.428490e-05
50%      4.295550e-05
75%      9.739660e-05
max      1.000000e+00
Name: lifetime_freq_normalized, dtype: float64

🔹 Column: wasted
----------------------------------------
count    72511602.0
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
count    4.553454e+07
mean     6.961874e-02
std      1.302227e-01
min      0.000000e+00
25%      1.264710e-05
50%      9.644840e-03
75%      6.628810e-02
max      9.987730e-01
Name: clock_time_between_normalized, dtype: float64

🔹 Column: clock_freq_normalized
----------------------------------------
count    4.553454e+07
mean     6.614033e-04
std      3.089514e-03
min      1.624140e-07
25%      7.773390e-06
50%      4.011930e-05
75%      1.010540e-04
max      1.000000e+00
Name: clock_freq_normalized, dtype: float64

🔹 Column: lifetime_freq_normalized
----------------------------------------
count    4.553454e+07
mean     1.104776e-03
std      5.336998e-03
min      1.494760e-07
25%      7.152030e-06
50%      3.192750e-05
75%      8.879420e-05
max      1.000000e+00
Name: lifetime_freq_normalized, dtype: float64

🔹 Column: wasted
----------------------------------------
count    45534535.0
mean            1.0
std             0.0
min             1.0
25%             1.0
50%             1.0
75%             1.0
max             1.0
Name: wasted, dtype: float64
#### Model
[1 1 1 ... 1 0 1]
Classification Report:
              precision    recall  f1-score   support

           0       0.66      0.32      0.43  18127901
           1       0.40      0.73      0.52  11383634

    accuracy                           0.48  29511535
   macro avg       0.53      0.53      0.48  29511535
weighted avg       0.56      0.48      0.47  29511535

Accuracy: 0.4805064528158227
Confusion Matrix:
[[ 5833238 12294663]
 [ 3036389  8347245]]
Confusion Matrix (%):
[[19.76595931 41.66053375]
 [10.28882096 28.28468597]]
