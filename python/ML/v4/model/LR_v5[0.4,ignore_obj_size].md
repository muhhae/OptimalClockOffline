#### Datasets

🧾 Basic Info:
------------------------------------------------------------
<class 'pandas.core.frame.DataFrame'>
Index: 127996359 entries, 110837847 to 380700
Data columns (total 3 columns):
 #   Column                         Dtype  
---  ------                         -----  
 0   clock_time_between_normalized  float64
 1   clock_freq_normalized          float64
 2   wasted                         int64  
dtypes: float64(2), int64(1)
memory usage: 3.8 GB
None

📌 Missing Values:
------------------------------------------------------------
clock_time_between_normalized    0
clock_freq_normalized            0
wasted                           0
dtype: int64

🆔 Unique Values per Column:
------------------------------------------------------------
clock_time_between_normalized    5586048
clock_freq_normalized             618437
wasted                                 2
dtype: int64

📊 Column-wise Summary Statistics:
------------------------------------------------------------

🔹 Column: clock_time_between_normalized
----------------------------------------
Type: float64
Missing: 0
Unique: 5586048
count    1.279964e+08
mean     7.132776e-02
std      1.244919e-01
min      0.000000e+00
25%      1.113130e-05
50%      1.321810e-02
75%      8.551670e-02
max      9.991010e-01
Name: clock_time_between_normalized, dtype: float64

🔹 Column: clock_freq_normalized
----------------------------------------
Type: float64
Missing: 0
Unique: 618437
count    1.279964e+08
mean     1.003968e-03
std      5.630590e-03
min      1.653740e-07
25%      1.172590e-05
50%      4.347830e-05
75%      1.159420e-04
max      1.000000e+00
Name: clock_freq_normalized, dtype: float64

🔹 Column: wasted
----------------------------------------
Type: int64
Missing: 0
Unique: 2
count    1.279964e+08
mean     3.876643e-01
std      4.872173e-01
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
count    7.837674e+07
mean     7.619661e-02
std      1.258954e-01
min      0.000000e+00
25%      1.350720e-05
50%      1.744310e-02
75%      9.648720e-02
max      9.991010e-01
Name: clock_time_between_normalized, dtype: float64

🔹 Column: clock_freq_normalized
----------------------------------------
count    7.837674e+07
mean     1.341789e-03
std      6.890315e-03
min      1.653740e-07
25%      1.485820e-05
50%      4.457450e-05
75%      1.407110e-04
max      1.000000e+00
Name: clock_freq_normalized, dtype: float64

🔹 Column: wasted
----------------------------------------
count    78376736.0
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
count    4.961962e+07
mean     6.363717e-02
std      1.218465e-01
min      0.000000e+00
25%      8.970140e-06
50%      8.535600e-03
75%      5.494070e-02
max      9.983620e-01
Name: clock_time_between_normalized, dtype: float64

🔹 Column: clock_freq_normalized
----------------------------------------
count    4.961962e+07
mean     4.703630e-04
std      2.514847e-03
min      1.653740e-07
25%      7.817260e-06
50%      4.222750e-05
75%      8.205800e-05
max      1.000000e+00
Name: clock_freq_normalized, dtype: float64

🔹 Column: wasted
----------------------------------------
count    49619623.0
mean            1.0
std             0.0
min             1.0
25%             1.0
50%             1.0
75%             1.0
max             1.0
Name: wasted, dtype: float64
#### Model
[1 1 0 ... 1 0 0]
Classification Report:
              precision    recall  f1-score   support

           0       0.71      0.36      0.48  19594184
           1       0.43      0.77      0.55  12404906

    accuracy                           0.52  31999090
   macro avg       0.57      0.57      0.52  31999090
weighted avg       0.60      0.52      0.51  31999090

Accuracy: 0.5194167084126455
Confusion Matrix:
[[ 7072720 12521464]
 [ 2856764  9548142]]
Confusion Matrix (%):
[[22.10287855 39.13068778]
 [ 8.92764138 29.83879229]]
