#### Datasets

🧾 Basic Info:
------------------------------------------------------------
<class 'pandas.core.frame.DataFrame'>
Index: 197016992 entries, 77198350 to 159165060
Data columns (total 3 columns):
 #   Column                         Dtype  
---  ------                         -----  
 0   clock_time_between_normalized  float64
 1   clock_freq_normalized          float64
 2   wasted                         int64  
dtypes: float64(2), int64(1)
memory usage: 5.9 GB
None

📌 Missing Values:
------------------------------------------------------------
clock_time_between_normalized    0
clock_freq_normalized            0
wasted                           0
dtype: int64

🆔 Unique Values per Column:
------------------------------------------------------------
clock_time_between_normalized    3696268
clock_freq_normalized             332627
wasted                                 2
dtype: int64

📊 Column-wise Summary Statistics:
------------------------------------------------------------

🔹 Column: clock_time_between_normalized
----------------------------------------
Type: float64
Missing: 0
Unique: 3696268
count    1.970170e+08
mean     1.663705e-04
std      3.473015e-03
min      0.000000e+00
25%      0.000000e+00
50%      1.964650e-08
75%      2.999260e-05
max      9.812500e-01
Name: clock_time_between_normalized, dtype: float64

🔹 Column: clock_freq_normalized
----------------------------------------
Type: float64
Missing: 0
Unique: 332627
count    1.970170e+08
mean     8.453294e-03
std      3.353485e-02
min      1.369880e-06
25%      1.544280e-04
50%      1.102540e-03
75%      3.333330e-03
max      1.000000e+00
Name: clock_freq_normalized, dtype: float64

🔹 Column: wasted
----------------------------------------
Type: int64
Missing: 0
Unique: 2
count    1.970170e+08
mean     7.763749e-01
std      4.166736e-01
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
count    4.405794e+07
mean     2.663457e-04
std      4.369205e-03
min      0.000000e+00
25%      1.899550e-08
50%      7.652420e-06
75%      8.160730e-05
max      9.723440e-01
Name: clock_time_between_normalized, dtype: float64

🔹 Column: clock_freq_normalized
----------------------------------------
count    4.405794e+07
mean     5.705494e-03
std      3.136986e-02
min      1.369880e-06
25%      1.250720e-04
50%      8.130080e-04
75%      2.604170e-03
max      1.000000e+00
Name: clock_freq_normalized, dtype: float64

🔹 Column: wasted
----------------------------------------
count    44057943.0
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
count    1.529590e+08
mean     1.375739e-04
std      3.167611e-03
min      0.000000e+00
25%      0.000000e+00
50%      0.000000e+00
75%      1.593620e-05
max      9.812500e-01
Name: clock_time_between_normalized, dtype: float64

🔹 Column: clock_freq_normalized
----------------------------------------
count    1.529590e+08
mean     9.244764e-03
std      3.409192e-02
min      1.369880e-06
25%      1.751010e-04
50%      1.103750e-03
75%      3.731340e-03
max      1.000000e+00
Name: clock_freq_normalized, dtype: float64

🔹 Column: wasted
----------------------------------------
count    152959049.0
mean             1.0
std              0.0
min              1.0
25%              1.0
50%              1.0
75%              1.0
max              1.0
Name: wasted, dtype: float64
#### Model
[1 0 0 ... 0 0 0]
Classification Report:
              precision    recall  f1-score   support

           0       0.24      0.92      0.38  11014486
           1       0.87      0.15      0.26  38239762

    accuracy                           0.32  49254248
   macro avg       0.55      0.54      0.32  49254248
weighted avg       0.73      0.32      0.28  49254248

Accuracy: 0.32247182009559866
Confusion Matrix:
[[10135594   878892]
 [32492249  5747513]]
Confusion Matrix (%):
[[20.57811135  1.78439837]
 [65.96841962 11.66907066]]
