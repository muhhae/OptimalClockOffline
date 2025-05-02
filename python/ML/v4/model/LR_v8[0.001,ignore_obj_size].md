#### Datasets

🧾 Basic Info:
------------------------------------------------------------
<class 'pandas.core.frame.DataFrame'>
Index: 197016992 entries, 77198350 to 159165060
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
memory usage: 11.7 GB
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
clock_time_between                 8942
clock_freq                         6003
lifetime_freq                    671929
clock_time_between_normalized      8942
clock_freq_normalized              6003
lifetime_freq_normalized         671929
wasted                                2
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

🔹 Column: lifetime_freq
----------------------------------------
Type: float64
Missing: 0
Unique: 671929
count    1.970170e+08
mean     1.159899e+04
std      1.815417e+05
min      2.000000e+00
25%      1.400000e+01
50%      1.490000e+02
75%      1.835000e+03
max      1.524330e+07
Name: lifetime_freq, dtype: float64

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

🔹 Column: lifetime_freq_normalized
----------------------------------------
Type: float64
Missing: 0
Unique: 671929
count    1.970170e+08
mean     7.609240e-04
std      1.190960e-02
min      1.312052e-07
25%      9.184363e-07
50%      9.774786e-06
75%      1.203808e-04
max      1.000000e+00
Name: lifetime_freq_normalized, dtype: float64

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

🔹 Column: lifetime_freq
----------------------------------------
count    4.405794e+07
mean     3.719956e+04
std      3.414929e+05
min      2.000000e+00
25%      2.710000e+02
50%      2.181000e+03
75%      1.193200e+04
max      8.801870e+06
Name: lifetime_freq, dtype: float64

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

🔹 Column: lifetime_freq_normalized
----------------------------------------
count    4.405794e+07
mean     2.440388e-03
std      2.240282e-02
min      1.312052e-07
25%      1.777830e-05
50%      1.430793e-04
75%      7.827701e-04
max      5.774255e-01
Name: lifetime_freq_normalized, dtype: float64

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

🔹 Column: lifetime_freq
----------------------------------------
count    1.529590e+08
mean     4.225071e+03
std      9.282775e+04
min      2.000000e+00
25%      9.000000e+00
50%      8.000000e+01
75%      6.100000e+02
max      1.524330e+07
Name: lifetime_freq, dtype: float64

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

🔹 Column: lifetime_freq_normalized
----------------------------------------
count    1.529590e+08
mean     2.771756e-04
std      6.089741e-03
min      1.312052e-07
25%      5.904233e-07
50%      5.248207e-06
75%      4.001758e-05
max      1.000000e+00
Name: lifetime_freq_normalized, dtype: float64

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

           0       0.44      0.53      0.48  11014486
           1       0.86      0.81      0.83  38239762

    accuracy                           0.75  49254248
   macro avg       0.65      0.67      0.66  49254248
weighted avg       0.76      0.75      0.75  49254248

Accuracy: 0.7467477729027555
Confusion Matrix:
[[ 5809486  5205000]
 [ 7268748 30971014]]
Confusion Matrix (%):
[[11.79489331 10.56761642]
 [14.75760629 62.87988398]]
