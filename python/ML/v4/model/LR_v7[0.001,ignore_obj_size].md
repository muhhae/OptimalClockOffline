#### Datasets

🧾 Basic Info:
------------------------------------------------------------
<class 'pandas.core.frame.DataFrame'>
Index: 197016992 entries, 77198350 to 159165060
Data columns (total 5 columns):
 #   Column                         Dtype  
---  ------                         -----  
 0   clock_time_between             int64  
 1   clock_freq                     int64  
 2   clock_time_between_normalized  float64
 3   clock_freq_normalized          float64
 4   wasted                         int64  
dtypes: float64(2), int64(3)
memory usage: 8.8 GB
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
clock_time_between               8942
clock_freq                       6003
clock_time_between_normalized    8942
clock_freq_normalized            6003
wasted                              2
dtype: int64

📊 Column-wise Summary Statistics:
------------------------------------------------------------

🔹 Column: clock_time_between
----------------------------------------
Type: int64
Missing: 0
Unique: 8942
count    1.970170e+08
mean     3.764037e+01
std      4.434605e+02
min      0.000000e+00
25%      0.000000e+00
50%      1.000000e+00
75%      3.000000e+01
max      7.242200e+04
Name: clock_time_between, dtype: float64

🔹 Column: clock_freq
----------------------------------------
Type: int64
Missing: 0
Unique: 6003
count    1.970170e+08
mean     6.811036e+00
std      8.588845e+01
min      1.000000e+00
25%      2.000000e+00
50%      3.000000e+00
75%      5.000000e+00
max      7.299890e+05
Name: clock_freq, dtype: float64

🔹 Column: clock_time_between_normalized
----------------------------------------
Type: float64
Missing: 0
Unique: 8942
count    1.970170e+08
mean     5.197367e-04
std      6.123284e-03
min      0.000000e+00
25%      0.000000e+00
50%      1.380796e-05
75%      4.142388e-04
max      1.000000e+00
Name: clock_time_between_normalized, dtype: float64

🔹 Column: clock_freq_normalized
----------------------------------------
Type: float64
Missing: 0
Unique: 6003
count    1.970170e+08
mean     9.330327e-06
std      1.176572e-04
min      1.369884e-06
25%      2.739767e-06
50%      4.109651e-06
75%      6.849418e-06
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

🔹 Column: clock_time_between
----------------------------------------
count    4.405794e+07
mean     6.639167e+01
std      5.926931e+02
min      0.000000e+00
25%      1.000000e+01
50%      3.000000e+01
75%      6.000000e+01
max      4.837000e+04
Name: clock_time_between, dtype: float64

🔹 Column: clock_freq
----------------------------------------
count    4.405794e+07
mean     8.008811e+00
std      5.660127e+01
min      1.000000e+00
25%      2.000000e+00
50%      3.000000e+00
75%      5.000000e+00
max      2.139700e+04
Name: clock_freq, dtype: float64

🔹 Column: clock_time_between_normalized
----------------------------------------
count    4.405794e+07
mean     9.167334e-04
std      8.183881e-03
min      0.000000e+00
25%      1.380796e-04
50%      4.142388e-04
75%      8.284775e-04
max      6.678910e-01
Name: clock_time_between_normalized, dtype: float64

🔹 Column: clock_freq_normalized
----------------------------------------
count    4.405794e+07
mean     1.097114e-05
std      7.753715e-05
min      1.369884e-06
25%      2.739767e-06
50%      4.109651e-06
75%      6.849418e-06
max      2.931140e-02
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

🔹 Column: clock_time_between
----------------------------------------
count    1.529590e+08
mean     2.935892e+01
std      3.896305e+02
min      0.000000e+00
25%      0.000000e+00
50%      0.000000e+00
75%      9.000000e+00
max      7.242200e+04
Name: clock_time_between, dtype: float64

🔹 Column: clock_freq
----------------------------------------
count    1.529590e+08
mean     6.466032e+00
std      9.261916e+01
min      1.000000e+00
25%      2.000000e+00
50%      3.000000e+00
75%      5.000000e+00
max      7.299890e+05
Name: clock_freq, dtype: float64

🔹 Column: clock_time_between_normalized
----------------------------------------
count    1.529590e+08
mean     4.053867e-04
std      5.380001e-03
min      0.000000e+00
25%      0.000000e+00
50%      0.000000e+00
75%      1.242716e-04
max      1.000000e+00
Name: clock_time_between_normalized, dtype: float64

🔹 Column: clock_freq_normalized
----------------------------------------
count    1.529590e+08
mean     8.857711e-06
std      1.268775e-04
min      1.369884e-06
25%      2.739767e-06
50%      4.109651e-06
75%      6.849418e-06
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
[1 1 1 ... 1 1 1]
Classification Report:
              precision    recall  f1-score   support

           0       0.42      0.40      0.41  11014486
           1       0.83      0.84      0.83  38239762

    accuracy                           0.74  49254248
   macro avg       0.62      0.62      0.62  49254248
weighted avg       0.74      0.74      0.74  49254248

Accuracy: 0.7410236168868115
Confusion Matrix:
[[ 4368837  6645649]
 [ 6110038 32129724]]
Confusion Matrix (%):
[[ 8.86996996 13.49253977]
 [12.40509854 65.23239173]]
