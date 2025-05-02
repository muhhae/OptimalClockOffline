#### Datasets

🧾 Basic Info:
------------------------------------------------------------
<class 'pandas.core.frame.DataFrame'>
Index: 219372328 entries, 78523004 to 202637383
Data columns (total 5 columns):
 #   Column                         Dtype  
---  ------                         -----  
 0   clock_time_between             int64  
 1   clock_freq                     float64
 2   clock_time_between_normalized  float64
 3   clock_freq_normalized          float64
 4   wasted                         int64  
dtypes: float64(3), int64(2)
memory usage: 9.8 GB
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
clock_time_between               294917
clock_freq                        10908
clock_time_between_normalized    294917
clock_freq_normalized             10908
wasted                                2
dtype: int64

📊 Column-wise Summary Statistics:
------------------------------------------------------------

🔹 Column: clock_time_between
----------------------------------------
Type: int64
Missing: 0
Unique: 294917
count    2.193723e+08
mean     3.006160e+04
std      4.310727e+04
min      0.000000e+00
25%      1.860000e+02
50%      3.604000e+03
75%      6.448600e+04
max      5.373010e+05
Name: clock_time_between, dtype: float64

🔹 Column: clock_freq
----------------------------------------
Type: float64
Missing: 0
Unique: 10908
count    2.193723e+08
mean     7.952357e+00
std      4.993927e+02
min      1.000000e+00
25%      2.000000e+00
50%      3.000000e+00
75%      5.000000e+00
max      3.338380e+06
Name: clock_freq, dtype: float64

🔹 Column: clock_time_between_normalized
----------------------------------------
Type: float64
Missing: 0
Unique: 294917
count    2.193723e+08
mean     5.594928e-02
std      8.022927e-02
min      0.000000e+00
25%      3.461747e-04
50%      6.707600e-03
75%      1.200184e-01
max      1.000000e+00
Name: clock_time_between_normalized, dtype: float64

🔹 Column: clock_freq_normalized
----------------------------------------
Type: float64
Missing: 0
Unique: 10908
count    2.193723e+08
mean     2.382101e-06
std      1.495913e-04
min      2.995465e-07
25%      5.990930e-07
50%      8.986395e-07
75%      1.497732e-06
max      1.000000e+00
Name: clock_freq_normalized, dtype: float64

🔹 Column: wasted
----------------------------------------
Type: int64
Missing: 0
Unique: 2
count    2.193723e+08
mean     4.478346e-01
std      4.972713e-01
min      0.000000e+00
25%      0.000000e+00
50%      0.000000e+00
75%      1.000000e+00
max      1.000000e+00
Name: wasted, dtype: float64

🚫 Subset: wasted == 0
------------------------------------------------------------

🔹 Column: clock_time_between
----------------------------------------
count    1.211298e+08
mean     3.786386e+04
std      4.504385e+04
min      0.000000e+00
25%      1.048000e+03
50%      1.103800e+04
75%      8.611000e+04
max      5.373010e+05
Name: clock_time_between, dtype: float64

🔹 Column: clock_freq
----------------------------------------
count    1.211298e+08
mean     1.113472e+01
std      6.713523e+02
min      1.000000e+00
25%      2.000000e+00
50%      3.000000e+00
75%      5.000000e+00
max      3.338380e+06
Name: clock_freq, dtype: float64

🔹 Column: clock_time_between_normalized
----------------------------------------
count    1.211298e+08
mean     7.047048e-02
std      8.383354e-02
min      0.000000e+00
25%      1.950490e-03
50%      2.054342e-02
75%      1.602640e-01
max      1.000000e+00
Name: clock_time_between_normalized, dtype: float64

🔹 Column: clock_freq_normalized
----------------------------------------
count    1.211298e+08
mean     3.335366e-06
std      2.011012e-04
min      2.995465e-07
25%      5.990930e-07
50%      8.986395e-07
75%      1.497732e-06
max      1.000000e+00
Name: clock_freq_normalized, dtype: float64

🔹 Column: wasted
----------------------------------------
count    121129812.0
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
count    9.824252e+07
mean     2.044168e+04
std      3.847278e+04
min      0.000000e+00
25%      1.000000e+01
50%      7.820000e+02
75%      1.791100e+04
max      3.925900e+05
Name: clock_time_between, dtype: float64

🔹 Column: clock_freq
----------------------------------------
count    9.824252e+07
mean     4.028609e+00
std      3.381080e+01
min      1.000000e+00
25%      2.000000e+00
50%      2.000000e+00
75%      4.000000e+00
max      1.880670e+05
Name: clock_freq, dtype: float64

🔹 Column: clock_time_between_normalized
----------------------------------------
count    9.824252e+07
mean     3.804512e-02
std      7.160377e-02
min      0.000000e+00
25%      1.861154e-05
50%      1.455423e-03
75%      3.333513e-02
max      7.306705e-01
Name: clock_time_between_normalized, dtype: float64

🔹 Column: clock_freq_normalized
----------------------------------------
count    9.824252e+07
mean     1.206756e-06
std      1.012791e-05
min      2.995465e-07
25%      5.990930e-07
50%      5.990930e-07
75%      1.198186e-06
max      5.633481e-02
Name: clock_freq_normalized, dtype: float64

🔹 Column: wasted
----------------------------------------
count    98242516.0
mean            1.0
std             0.0
min             1.0
25%             1.0
50%             1.0
75%             1.0
max             1.0
Name: wasted, dtype: float64
#### Model
[1 1 1 ... 1 0 0]
Classification Report:
              precision    recall  f1-score   support

           0       0.73      0.52      0.61  30282453
           1       0.56      0.76      0.65  24560629

    accuracy                           0.63  54843082
   macro avg       0.64      0.64      0.63  54843082
weighted avg       0.65      0.63      0.63  54843082

Accuracy: 0.6282605160665479
Confusion Matrix:
[[15858189 14424264]
 [ 5963075 18597554]]
Confusion Matrix (%):
[[28.9155686  26.30097266]
 [10.87297574 33.910483  ]]
