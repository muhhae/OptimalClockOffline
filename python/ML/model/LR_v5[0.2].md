#### Datasets

🧾 Basic Info:
------------------------------------------------------------
<class 'pandas.core.frame.DataFrame'>
Index: 184017554 entries, 186239329 to 143761731
Data columns (total 3 columns):
 #   Column                         Dtype  
---  ------                         -----  
 0   clock_time_between_normalized  float64
 1   clock_freq_normalized          float64
 2   wasted                         int64  
dtypes: float64(2), int64(1)
memory usage: 5.5 GB
None

📌 Missing Values:
------------------------------------------------------------
clock_time_between_normalized    0
clock_freq_normalized            0
wasted                           0
dtype: int64

🆔 Unique Values per Column:
------------------------------------------------------------
clock_time_between_normalized    5608654
clock_freq_normalized             444706
wasted                                 2
dtype: int64

📊 Column-wise Summary Statistics:
------------------------------------------------------------

🔹 Column: clock_time_between_normalized
----------------------------------------
Type: float64
Missing: 0
Unique: 5608654
count    1.840176e+08
mean     5.675613e-02
std      1.134463e-01
min      0.000000e+00
25%      1.461743e-05
50%      8.044460e-03
75%      6.147390e-02
max      9.988970e-01
Name: clock_time_between_normalized, dtype: float64

🔹 Column: clock_freq_normalized
----------------------------------------
Type: float64
Missing: 0
Unique: 444706
count    1.840176e+08
mean     1.407717e-03
std      7.192045e-03
min      3.018850e-07
25%      2.057870e-05
50%      6.090130e-05
75%      1.967920e-04
max      1.000000e+00
Name: clock_freq_normalized, dtype: float64

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

🔹 Column: clock_time_between_normalized
----------------------------------------
count    1.065471e+08
mean     6.790178e-02
std      1.259386e-01
min      0.000000e+00
25%      1.245590e-04
50%      2.205220e-02
75%      7.478380e-02
max      9.988970e-01
Name: clock_time_between_normalized, dtype: float64

🔹 Column: clock_freq_normalized
----------------------------------------
count    1.065471e+08
mean     1.615927e-03
std      8.507759e-03
min      3.018850e-07
25%      2.950900e-05
50%      6.090130e-05
75%      2.044990e-04
max      1.000000e+00
Name: clock_freq_normalized, dtype: float64

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

🔹 Column: clock_time_between_normalized
----------------------------------------
count    7.747044e+07
mean     4.142722e-02
std      9.138594e-02
min      0.000000e+00
25%      3.669360e-06
50%      1.353180e-03
75%      4.489340e-02
max      9.977460e-01
Name: clock_time_between_normalized, dtype: float64

🔹 Column: clock_freq_normalized
----------------------------------------
count    7.747044e+07
mean     1.121359e-03
std      4.813996e-03
min      3.018850e-07
25%      1.475450e-05
50%      5.901790e-05
75%      1.967920e-04
max      1.000000e+00
Name: clock_freq_normalized, dtype: float64

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
[1 0 0 ... 1 1 1]
Classification Report:
              precision    recall  f1-score   support

           0       0.65      0.32      0.43  26636778
           1       0.45      0.76      0.57  19367611

    accuracy                           0.51  46004389
   macro avg       0.55      0.54      0.50  46004389
weighted avg       0.57      0.51      0.49  46004389

Accuracy: 0.5066142276120654
Confusion Matrix:
[[ 8513704 18123074]
 [ 4574837 14792774]]
Confusion Matrix (%):
[[18.50628643 39.39422823]
 [ 9.94434901 32.15513633]]
