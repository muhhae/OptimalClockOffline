#### Datasets

🧾 Basic Info:
------------------------------------------------------------
<class 'pandas.core.frame.DataFrame'>
Index: 118046137 entries, 115656551 to 108006826
Data columns (total 5 columns):
 #   Column                         Dtype  
---  ------                         -----  
 0   clock_time_between             float64
 1   clock_freq                     float64
 2   clock_time_between_normalized  float64
 3   clock_freq_normalized          float64
 4   wasted                         int64  
dtypes: float64(4), int64(1)
memory usage: 5.3 GB
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
clock_time_between               693339
clock_freq                        12061
clock_time_between_normalized    693339
clock_freq_normalized             12061
wasted                                2
dtype: int64

📊 Column-wise Summary Statistics:
------------------------------------------------------------

🔹 Column: clock_time_between
----------------------------------------
Type: float64
Missing: 0
Unique: 693339
count    1.180461e+08
mean     7.297320e+04
std      1.077239e+05
min      0.000000e+00
25%      2.790000e+02
50%      2.096700e+04
75%      9.533200e+04
max      1.122030e+06
Name: clock_time_between, dtype: float64

🔹 Column: clock_freq
----------------------------------------
Type: float64
Missing: 0
Unique: 12061
count    1.180461e+08
mean     1.435431e+01
std      1.370227e+03
min      1.000000e+00
25%      2.000000e+00
50%      4.000000e+00
75%      7.000000e+00
max      5.709380e+06
Name: clock_freq, dtype: float64

🔹 Column: clock_time_between_normalized
----------------------------------------
Type: float64
Missing: 0
Unique: 693339
count    1.180461e+08
mean     6.503676e-02
std      9.600807e-02
min      0.000000e+00
25%      2.486565e-04
50%      1.868667e-02
75%      8.496386e-02
max      1.000000e+00
Name: clock_time_between_normalized, dtype: float64

🔹 Column: clock_freq_normalized
----------------------------------------
Type: float64
Missing: 0
Unique: 12061
count    1.180461e+08
mean     2.514162e-06
std      2.399957e-04
min      1.751504e-07
25%      3.503007e-07
50%      7.006015e-07
75%      1.226053e-06
max      1.000000e+00
Name: clock_freq_normalized, dtype: float64

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

🔹 Column: clock_time_between
----------------------------------------
count    7.251160e+07
mean     7.589646e+04
std      1.059796e+05
min      0.000000e+00
25%      9.470000e+02
50%      3.112700e+04
75%      8.723100e+04
max      1.122030e+06
Name: clock_time_between, dtype: float64

🔹 Column: clock_freq
----------------------------------------
count    7.251160e+07
mean     2.032949e+01
std      1.740272e+03
min      1.000000e+00
25%      2.000000e+00
50%      5.000000e+00
75%      1.000000e+01
max      5.709380e+06
Name: clock_freq, dtype: float64

🔹 Column: clock_time_between_normalized
----------------------------------------
count    7.251160e+07
mean     6.764209e-02
std      9.445345e-02
min      0.000000e+00
25%      8.440060e-04
50%      2.774168e-02
75%      7.774391e-02
max      1.000000e+00
Name: clock_time_between_normalized, dtype: float64

🔹 Column: clock_freq_normalized
----------------------------------------
count    7.251160e+07
mean     3.560717e-06
std      3.048092e-04
min      1.751504e-07
25%      3.503007e-07
50%      8.757518e-07
75%      1.751504e-06
max      1.000000e+00
Name: clock_freq_normalized, dtype: float64

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

🔹 Column: clock_time_between
----------------------------------------
count    4.553454e+07
mean     6.831804e+04
std      1.102850e+05
min      0.000000e+00
25%      3.000000e+01
50%      9.687000e+03
75%      1.036140e+05
max      9.229410e+05
Name: clock_time_between, dtype: float64

🔹 Column: clock_freq
----------------------------------------
count    4.553454e+07
mean     4.839115e+00
std      2.107623e+02
min      1.000000e+00
25%      2.000000e+00
50%      2.000000e+00
75%      4.000000e+00
max      4.729750e+05
Name: clock_freq, dtype: float64

🔹 Column: clock_time_between_normalized
----------------------------------------
count    4.553454e+07
mean     6.088789e-02
std      9.829062e-02
min      0.000000e+00
25%      2.673725e-05
50%      8.633459e-03
75%      9.234512e-02
max      8.225636e-01
Name: clock_time_between_normalized, dtype: float64

🔹 Column: clock_freq_normalized
----------------------------------------
count    4.553454e+07
mean     8.475728e-07
std      3.691510e-05
min      1.751504e-07
25%      3.503007e-07
50%      3.503007e-07
75%      7.006015e-07
max      8.284174e-02
Name: clock_freq_normalized, dtype: float64

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

           0       0.79      0.43      0.55  18127901
           1       0.47      0.82      0.60  11383634

    accuracy                           0.58  29511535
   macro avg       0.63      0.62      0.58  29511535
weighted avg       0.67      0.58      0.57  29511535

Accuracy: 0.5771849888526639
Confusion Matrix:
[[ 7704378 10423523]
 [ 2054397  9329237]]
Confusion Matrix (%):
[[26.10632758 35.32016549]
 [ 6.96133563 31.61217131]]
