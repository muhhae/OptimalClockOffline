#### Datasets

🧾 Basic Info:
------------------------------------------------------------
<class 'pandas.core.frame.DataFrame'>
Index: 127996359 entries, 110837847 to 380700
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
memory usage: 7.6 GB
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
clock_time_between               683169
clock_freq                        11536
lifetime_freq                     20051
clock_time_between_normalized    683169
clock_freq_normalized             11536
lifetime_freq_normalized          20051
wasted                                2
dtype: int64

📊 Column-wise Summary Statistics:
------------------------------------------------------------

🔹 Column: clock_time_between
----------------------------------------
Type: int64
Missing: 0
Unique: 683169
count    1.279964e+08
mean     6.898576e+04
std      1.042122e+05
min      0.000000e+00
25%      2.880000e+02
50%      1.549600e+04
75%      9.209900e+04
max      9.196890e+05
Name: clock_time_between, dtype: float64

🔹 Column: clock_freq
----------------------------------------
Type: float64
Missing: 0
Unique: 11536
count    1.279964e+08
mean     1.324335e+01
std      1.171840e+03
min      1.000000e+00
25%      2.000000e+00
50%      4.000000e+00
75%      7.000000e+00
max      6.046900e+06
Name: clock_freq, dtype: float64

🔹 Column: lifetime_freq
----------------------------------------
Type: float64
Missing: 0
Unique: 20051
count    1.279964e+08
mean     4.397525e+01
std      2.977912e+03
min      2.000000e+00
25%      3.000000e+00
50%      6.000000e+00
75%      1.900000e+01
max      1.393560e+07
Name: lifetime_freq, dtype: float64

🔹 Column: clock_time_between_normalized
----------------------------------------
Type: float64
Missing: 0
Unique: 683169
count    1.279964e+08
mean     7.500988e-02
std      1.133125e-01
min      0.000000e+00
25%      3.131493e-04
50%      1.684917e-02
75%      1.001415e-01
max      1.000000e+00
Name: clock_time_between_normalized, dtype: float64

🔹 Column: clock_freq_normalized
----------------------------------------
Type: float64
Missing: 0
Unique: 11536
count    1.279964e+08
mean     2.190105e-06
std      1.937918e-04
min      1.653740e-07
25%      3.307480e-07
50%      6.614960e-07
75%      1.157618e-06
max      1.000000e+00
Name: clock_freq_normalized, dtype: float64

🔹 Column: lifetime_freq_normalized
----------------------------------------
Type: float64
Missing: 0
Unique: 20051
count    1.279964e+08
mean     3.155605e-06
std      2.136910e-04
min      1.435173e-07
25%      2.152760e-07
50%      4.305520e-07
75%      1.363415e-06
max      1.000000e+00
Name: lifetime_freq_normalized, dtype: float64

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

🔹 Column: clock_time_between
----------------------------------------
count    7.837674e+07
mean     7.068734e+04
std      1.040234e+05
min      0.000000e+00
25%      9.390000e+02
50%      1.827700e+04
75%      8.666000e+04
max      9.130580e+05
Name: clock_time_between, dtype: float64

🔹 Column: clock_freq
----------------------------------------
count    7.837674e+07
mean     1.875459e+01
std      1.492076e+03
min      1.000000e+00
25%      3.000000e+00
50%      5.000000e+00
75%      1.000000e+01
max      6.046900e+06
Name: clock_freq, dtype: float64

🔹 Column: lifetime_freq
----------------------------------------
count    7.837674e+07
mean     6.446100e+01
std      3.668681e+03
min      2.000000e+00
25%      4.000000e+00
50%      1.100000e+01
75%      3.400000e+01
max      1.393560e+07
Name: lifetime_freq, dtype: float64

🔹 Column: clock_time_between_normalized
----------------------------------------
count    7.837674e+07
mean     7.686004e-02
std      1.131071e-01
min      0.000000e+00
25%      1.020997e-03
50%      1.987302e-02
75%      9.422751e-02
max      9.927900e-01
Name: clock_time_between_normalized, dtype: float64

🔹 Column: clock_freq_normalized
----------------------------------------
count    7.837674e+07
mean     3.101521e-06
std      2.467505e-04
min      1.653740e-07
25%      4.961220e-07
50%      8.268700e-07
75%      1.653740e-06
max      1.000000e+00
Name: clock_freq_normalized, dtype: float64

🔹 Column: lifetime_freq_normalized
----------------------------------------
count    7.837674e+07
mean     4.625635e-06
std      2.632596e-04
min      1.435173e-07
25%      2.870346e-07
50%      7.893453e-07
75%      2.439794e-06
max      1.000000e+00
Name: lifetime_freq_normalized, dtype: float64

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

🔹 Column: clock_time_between
----------------------------------------
count    4.961962e+07
mean     6.629804e+04
std      1.044534e+05
min      0.000000e+00
25%      2.900000e+01
50%      1.086800e+04
75%      1.037210e+05
max      9.196890e+05
Name: clock_time_between, dtype: float64

🔹 Column: clock_freq
----------------------------------------
count    4.961962e+07
mean     4.538058e+00
std      1.599935e+02
min      1.000000e+00
25%      2.000000e+00
50%      2.000000e+00
75%      4.000000e+00
max      7.299890e+05
Name: clock_freq, dtype: float64

🔹 Column: lifetime_freq
----------------------------------------
count    4.961962e+07
mean     1.161696e+01
std      1.270482e+03
min      2.000000e+00
25%      2.000000e+00
50%      3.000000e+00
75%      7.000000e+00
max      1.959680e+06
Name: lifetime_freq, dtype: float64

🔹 Column: clock_time_between_normalized
----------------------------------------
count    4.961962e+07
mean     7.208745e-02
std      1.135747e-01
min      0.000000e+00
25%      3.153240e-05
50%      1.181704e-02
75%      1.127783e-01
max      1.000000e+00
Name: clock_time_between_normalized, dtype: float64

🔹 Column: clock_freq_normalized
----------------------------------------
count    4.961962e+07
mean     7.504768e-07
std      2.645876e-05
min      1.653740e-07
25%      3.307480e-07
50%      3.307480e-07
75%      6.614960e-07
max      1.207212e-01
Name: clock_freq_normalized, dtype: float64

🔹 Column: lifetime_freq_normalized
----------------------------------------
count    4.961962e+07
mean     8.336177e-07
std      9.116808e-05
min      1.435173e-07
25%      1.435173e-07
50%      2.152760e-07
75%      5.023106e-07
max      1.406240e-01
Name: lifetime_freq_normalized, dtype: float64

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
[0 0 0 ... 1 0 1]
Classification Report:
              precision    recall  f1-score   support

           0       0.83      0.48      0.61  19594184
           1       0.51      0.84      0.63  12404906

    accuracy                           0.62  31999090
   macro avg       0.67      0.66      0.62  31999090
weighted avg       0.71      0.62      0.62  31999090

Accuracy: 0.6235113873550779
Confusion Matrix:
[[ 9481428 10112756]
 [ 1934537 10470369]]
Confusion Matrix (%):
[[29.63030511 31.60326122]
 [ 6.04560005 32.72083362]]
