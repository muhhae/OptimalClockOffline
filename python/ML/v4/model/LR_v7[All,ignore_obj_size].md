#### Datasets

🧾 Basic Info:
------------------------------------------------------------
<class 'pandas.core.frame.DataFrame'>
Index: 1074429246 entries, 761403510 to 73388452
Data columns (total 5 columns):
 #   Column                         Dtype  
---  ------                         -----  
 0   clock_time_between             int64  
 1   clock_freq                     float64
 2   clock_time_between_normalized  float64
 3   clock_freq_normalized          float64
 4   wasted                         int64  
dtypes: float64(3), int64(2)
memory usage: 48.0 GB
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
clock_time_between               683142
clock_freq                        20689
clock_time_between_normalized    683142
clock_freq_normalized             20689
wasted                                2
dtype: int64

📊 Column-wise Summary Statistics:
------------------------------------------------------------

🔹 Column: clock_time_between
----------------------------------------
Type: int64
Missing: 0
Unique: 683142
count    1.074429e+09
mean     1.671107e+04
std      4.742552e+04
min      0.000000e+00
25%      2.000000e+00
50%      2.000000e+02
75%      4.257000e+03
max      9.204590e+05
Name: clock_time_between, dtype: float64

🔹 Column: clock_freq
----------------------------------------
Type: float64
Missing: 0
Unique: 20689
count    1.074429e+09
mean     7.497953e+00
std      5.414287e+02
min      1.000000e+00
25%      2.000000e+00
50%      3.000000e+00
75%      5.000000e+00
max      6.046900e+06
Name: clock_freq, dtype: float64

🔹 Column: clock_time_between_normalized
----------------------------------------
Type: float64
Missing: 0
Unique: 683142
count    1.074429e+09
mean     1.815515e-02
std      5.152378e-02
min      0.000000e+00
25%      2.172829e-06
50%      2.172829e-04
75%      4.624867e-03
max      1.000000e+00
Name: clock_time_between_normalized, dtype: float64

🔹 Column: clock_freq_normalized
----------------------------------------
Type: float64
Missing: 0
Unique: 20689
count    1.074429e+09
mean     1.239966e-06
std      8.953823e-05
min      1.653740e-07
25%      3.307480e-07
50%      4.961220e-07
75%      8.268700e-07
max      1.000000e+00
Name: clock_freq_normalized, dtype: float64

🔹 Column: wasted
----------------------------------------
Type: int64
Missing: 0
Unique: 2
count    1.074429e+09
mean     5.807153e-01
std      4.934420e-01
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
count    4.504918e+08
mean     2.545537e+04
std      5.624474e+04
min      0.000000e+00
25%      8.000000e+01
50%      1.080000e+03
75%      1.922900e+04
max      9.188250e+05
Name: clock_time_between, dtype: float64

🔹 Column: clock_freq
----------------------------------------
count    4.504918e+08
mean     1.139964e+01
std      8.313770e+02
min      1.000000e+00
25%      2.000000e+00
50%      3.000000e+00
75%      6.000000e+00
max      6.046900e+06
Name: clock_freq, dtype: float64

🔹 Column: clock_time_between_normalized
----------------------------------------
count    4.504918e+08
mean     2.765508e-02
std      6.110510e-02
min      0.000000e+00
25%      8.691316e-05
50%      1.173328e-03
75%      2.089066e-02
max      9.982248e-01
Name: clock_time_between_normalized, dtype: float64

🔹 Column: clock_freq_normalized
----------------------------------------
count    4.504918e+08
mean     1.885204e-06
std      1.374881e-04
min      1.653740e-07
25%      3.307480e-07
50%      4.961220e-07
75%      9.922440e-07
max      1.000000e+00
Name: clock_freq_normalized, dtype: float64

🔹 Column: wasted
----------------------------------------
count    450491784.0
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
count    6.239375e+08
mean     1.039756e+04
std      3.865206e+04
min      0.000000e+00
25%      0.000000e+00
50%      3.900000e+01
75%      7.570000e+02
max      9.204590e+05
Name: clock_time_between, dtype: float64

🔹 Column: clock_freq
----------------------------------------
count    6.239375e+08
mean     4.680877e+00
std      7.572044e+01
min      1.000000e+00
25%      2.000000e+00
50%      3.000000e+00
75%      4.000000e+00
max      7.299890e+05
Name: clock_freq, dtype: float64

🔹 Column: clock_time_between_normalized
----------------------------------------
count    6.239375e+08
mean     1.129606e-02
std      4.199216e-02
min      0.000000e+00
25%      0.000000e+00
50%      4.237017e-05
75%      8.224158e-04
max      1.000000e+00
Name: clock_time_between_normalized, dtype: float64

🔹 Column: clock_freq_normalized
----------------------------------------
count    6.239375e+08
mean     7.740954e-07
std      1.252219e-05
min      1.653740e-07
25%      3.307480e-07
50%      4.961220e-07
75%      6.614960e-07
max      1.207212e-01
Name: clock_freq_normalized, dtype: float64

🔹 Column: wasted
----------------------------------------
count    623937462.0
mean             1.0
std              0.0
min              1.0
25%              1.0
50%              1.0
75%              1.0
max              1.0
Name: wasted, dtype: float64
#### Model
[1 1 0 ... 0 1 1]
Classification Report:
              precision    recall  f1-score   support

           0       0.64      0.37      0.47 112622946
           1       0.65      0.85      0.74 155984366

    accuracy                           0.65 268607312
   macro avg       0.64      0.61      0.60 268607312
weighted avg       0.64      0.65      0.62 268607312

Accuracy: 0.6468556373476534
Confusion Matrix:
[[ 41765821  70857125]
 [ 24000033 131984333]]
Confusion Matrix (%):
[[15.54902608 26.37944756]
 [ 8.93498871 49.13653765]]
