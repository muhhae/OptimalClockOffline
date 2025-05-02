#### Datasets

🧾 Basic Info:
------------------------------------------------------------
<class 'pandas.core.frame.DataFrame'>
Index: 184017554 entries, 186239329 to 143761731
Data columns (total 7 columns):
 #   Column                         Dtype  
---  ------                         -----  
 0   clock_time_between             int64  
 1   clock_freq                     float64
 2   lifetime_freq                  float64
 3   clock_time_between_normalized  float64
 4   clock_freq_normalized          float64
 5   lifetime_freq_normalized       float64
 6   wasted                         int64  
dtypes: float64(5), int64(2)
memory usage: 11.0 GB
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
clock_time_between               309668
clock_freq                        10840
lifetime_freq                     28897
clock_time_between_normalized    309668
clock_freq_normalized             10840
lifetime_freq_normalized          28897
wasted                                2
dtype: int64

📊 Column-wise Summary Statistics:
------------------------------------------------------------

🔹 Column: clock_time_between
----------------------------------------
Type: int64
Missing: 0
Unique: 309668
count    1.840176e+08
mean     3.639508e+04
std      4.658171e+04
min      0.000000e+00
25%      2.320000e+02
50%      8.691000e+03
75%      8.381100e+04
max      7.376410e+05
Name: clock_time_between, dtype: float64

🔹 Column: clock_freq
----------------------------------------
Type: float64
Missing: 0
Unique: 10840
count    1.840176e+08
mean     9.536043e+00
std      7.671092e+02
min      1.000000e+00
25%      2.000000e+00
50%      3.000000e+00
75%      6.000000e+00
max      3.312520e+06
Name: clock_freq, dtype: float64

🔹 Column: lifetime_freq
----------------------------------------
Type: float64
Missing: 0
Unique: 28897
count    1.840176e+08
mean     5.591540e+01
std      3.104041e+03
min      2.000000e+00
25%      4.000000e+00
50%      1.000000e+01
75%      2.900000e+01
max      1.293440e+07
Name: lifetime_freq, dtype: float64

🔹 Column: clock_time_between_normalized
----------------------------------------
Type: float64
Missing: 0
Unique: 309668
count    1.840176e+08
mean     4.933982e-02
std      6.314957e-02
min      0.000000e+00
25%      3.145161e-04
50%      1.178215e-02
75%      1.136203e-01
max      1.000000e+00
Name: clock_time_between_normalized, dtype: float64

🔹 Column: clock_freq_normalized
----------------------------------------
Type: float64
Missing: 0
Unique: 10840
count    1.840176e+08
mean     2.878788e-06
std      2.315787e-04
min      3.018850e-07
25%      6.037699e-07
50%      9.056549e-07
75%      1.811310e-06
max      1.000000e+00
Name: clock_freq_normalized, dtype: float64

🔹 Column: lifetime_freq_normalized
----------------------------------------
Type: float64
Missing: 0
Unique: 28897
count    1.840176e+08
mean     4.322999e-06
std      2.399834e-04
min      1.546264e-07
25%      3.092528e-07
50%      7.731321e-07
75%      2.242083e-06
max      1.000000e+00
Name: lifetime_freq_normalized, dtype: float64

🔹 Column: wasted
----------------------------------------
Type: int64
Missing: 0
Unique: 2
count    1.840176e+08
mean     4.209948e-01
std      4.937187e-01
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
count    1.065471e+08
mean     4.291579e+04
std      4.688278e+04
min      0.000000e+00
25%      1.579000e+03
50%      1.747100e+04
75%      8.635600e+04
max      7.376410e+05
Name: clock_time_between, dtype: float64

🔹 Column: clock_freq
----------------------------------------
count    1.065471e+08
mean     1.328914e+01
std      1.006599e+03
min      1.000000e+00
25%      2.000000e+00
50%      3.000000e+00
75%      8.000000e+00
max      3.312520e+06
Name: clock_freq, dtype: float64

🔹 Column: lifetime_freq
----------------------------------------
count    1.065471e+08
mean     7.960059e+01
std      3.960120e+03
min      2.000000e+00
25%      7.000000e+00
50%      1.700000e+01
75%      4.800000e+01
max      1.293440e+07
Name: lifetime_freq, dtype: float64

🔹 Column: clock_time_between_normalized
----------------------------------------
count    1.065471e+08
mean     5.817978e-02
std      6.355772e-02
min      0.000000e+00
25%      2.140608e-03
50%      2.368496e-02
75%      1.170705e-01
max      1.000000e+00
Name: clock_time_between_normalized, dtype: float64

🔹 Column: clock_freq_normalized
----------------------------------------
count    1.065471e+08
mean     4.011791e-06
std      3.038770e-04
min      3.018850e-07
25%      6.037699e-07
50%      9.056549e-07
75%      2.415080e-06
max      1.000000e+00
Name: clock_freq_normalized, dtype: float64

🔹 Column: lifetime_freq_normalized
----------------------------------------
count    1.065471e+08
mean     6.154177e-06
std      3.061696e-04
min      1.546264e-07
25%      5.411925e-07
50%      1.314325e-06
75%      3.711034e-06
max      1.000000e+00
Name: lifetime_freq_normalized, dtype: float64

🔹 Column: wasted
----------------------------------------
count    106547113.0
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
count    7.747044e+07
mean     2.742697e+04
std      4.463462e+04
min      0.000000e+00
25%      5.000000e+00
50%      1.289000e+03
75%      4.749900e+04
max      4.694240e+05
Name: clock_time_between, dtype: float64

🔹 Column: clock_freq
----------------------------------------
count    7.747044e+07
mean     4.374315e+00
std      6.475699e+01
min      1.000000e+00
25%      2.000000e+00
50%      3.000000e+00
75%      4.000000e+00
max      2.272820e+05
Name: clock_freq, dtype: float64

🔹 Column: lifetime_freq
----------------------------------------
count    7.747044e+07
mean     2.334055e+01
std      1.147166e+03
min      2.000000e+00
25%      3.000000e+00
50%      5.000000e+00
75%      1.300000e+01
max      1.959680e+06
Name: lifetime_freq, dtype: float64

🔹 Column: clock_time_between_normalized
----------------------------------------
count    7.747044e+07
mean     3.718201e-02
std      6.050995e-02
min      0.000000e+00
25%      6.778365e-06
50%      1.747463e-03
75%      6.439311e-02
max      6.363855e-01
Name: clock_time_between_normalized, dtype: float64

🔹 Column: clock_freq_normalized
----------------------------------------
count    7.747044e+07
mean     1.320540e-06
std      1.954916e-05
min      3.018850e-07
25%      6.037699e-07
50%      9.056549e-07
75%      1.207540e-06
max      6.861302e-02
Name: clock_freq_normalized, dtype: float64

🔹 Column: lifetime_freq_normalized
----------------------------------------
count    7.747044e+07
mean     1.804533e-06
std      8.869110e-05
min      1.546264e-07
25%      2.319396e-07
50%      3.865661e-07
75%      1.005072e-06
max      1.515092e-01
Name: lifetime_freq_normalized, dtype: float64

🔹 Column: wasted
----------------------------------------
count    77470441.0
mean            1.0
std             0.0
min             1.0
25%             1.0
50%             1.0
75%             1.0
max             1.0
Name: wasted, dtype: float64
#### Model
[1 0 0 ... 1 1 0]
Classification Report:
              precision    recall  f1-score   support

           0       0.74      0.61      0.67  26636778
           1       0.57      0.71      0.63  19367611

    accuracy                           0.65  46004389
   macro avg       0.66      0.66      0.65  46004389
weighted avg       0.67      0.65      0.66  46004389

Accuracy: 0.6532690826520922
Confusion Matrix:
[[16310539 10326239]
 [ 5624905 13742706]]
Confusion Matrix (%):
[[35.45431067 22.44620399]
 [12.22688774 29.87259759]]
