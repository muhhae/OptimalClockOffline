#### Datasets

🧾 Basic Info:
------------------------------------------------------------
<class 'pandas.core.frame.DataFrame'>
Index: 219372328 entries, 78523004 to 202637383
Data columns (total 4 columns):
 #   Column                         Dtype  
---  ------                         -----  
 0   clock_time_between_normalized  float64
 1   clock_freq_normalized          float64
 2   lifetime_freq_normalized       float64
 3   wasted                         int64  
dtypes: float64(3), int64(1)
memory usage: 8.2 GB
None

📌 Missing Values:
------------------------------------------------------------
clock_time_between_normalized    0
clock_freq_normalized            0
lifetime_freq_normalized         0
wasted                           0
dtype: int64

🆔 Unique Values per Column:
------------------------------------------------------------
clock_time_between_normalized    5734662
clock_freq_normalized             557642
lifetime_freq_normalized         4227207
wasted                                 2
dtype: int64

📊 Column-wise Summary Statistics:
------------------------------------------------------------

🔹 Column: clock_time_between_normalized
----------------------------------------
Type: float64
Missing: 0
Unique: 5734662
count    2.193723e+08
mean     4.670061e-02
std      1.006286e-01
min      0.000000e+00
25%      9.138750e-07
50%      1.898110e-03
75%      5.090050e-02
max      9.989520e-01
Name: clock_time_between_normalized, dtype: float64

🔹 Column: clock_freq_normalized
----------------------------------------
Type: float64
Missing: 0
Unique: 557642
count    2.193723e+08
mean     2.746180e-03
std      9.583279e-03
min      2.995460e-07
25%      2.580050e-05
50%      7.740140e-05
75%      8.853470e-04
max      1.000000e+00
Name: clock_freq_normalized, dtype: float64

🔹 Column: lifetime_freq_normalized
----------------------------------------
Type: float64
Missing: 0
Unique: 4227207
count    2.193723e+08
mean     3.150865e-03
std      1.249715e-02
min      1.312050e-07
25%      2.193620e-05
50%      6.115620e-05
75%      1.100730e-03
max      1.000000e+00
Name: lifetime_freq_normalized, dtype: float64

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

🔹 Column: clock_time_between_normalized
----------------------------------------
count    1.211298e+08
mean     5.889685e-02
std      1.137847e-01
min      0.000000e+00
25%      4.249907e-06
50%      1.008860e-02
75%      6.408190e-02
max      9.983090e-01
Name: clock_time_between_normalized, dtype: float64

🔹 Column: clock_freq_normalized
----------------------------------------
count    1.211298e+08
mean     3.305961e-03
std      1.194905e-02
min      2.995460e-07
25%      2.580050e-05
50%      6.450110e-05
75%      5.309510e-04
max      1.000000e+00
Name: clock_freq_normalized, dtype: float64

🔹 Column: lifetime_freq_normalized
----------------------------------------
count    1.211298e+08
mean     3.956398e-03
std      1.571076e-02
min      1.312050e-07
25%      3.349720e-05
50%      6.689500e-05
75%      5.816580e-04
max      1.000000e+00
Name: lifetime_freq_normalized, dtype: float64

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

🔹 Column: clock_time_between_normalized
----------------------------------------
count    9.824252e+07
mean     3.166305e-02
std      7.898470e-02
min      0.000000e+00
25%      2.795030e-07
50%      3.836050e-05
75%      2.407920e-02
max      9.989520e-01
Name: clock_time_between_normalized, dtype: float64

🔹 Column: clock_freq_normalized
----------------------------------------
count    9.824252e+07
mean     2.055989e-03
std      5.307387e-03
min      2.995460e-07
25%      1.930450e-05
50%      7.780080e-05
75%      1.286590e-03
max      1.000000e+00
Name: clock_freq_normalized, dtype: float64

🔹 Column: lifetime_freq_normalized
----------------------------------------
count    9.824252e+07
mean     2.157669e-03
std      6.528738e-03
min      1.389410e-07
25%      1.220220e-05
50%      4.959430e-05
75%      1.867410e-03
max      1.000000e+00
Name: lifetime_freq_normalized, dtype: float64

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
[1 1 1 ... 1 0 1]
Classification Report:
              precision    recall  f1-score   support

           0       0.66      0.35      0.46  30282453
           1       0.49      0.78      0.60  24560629

    accuracy                           0.54  54843082
   macro avg       0.58      0.56      0.53  54843082
weighted avg       0.59      0.54      0.52  54843082

Accuracy: 0.5424156687620145
Confusion Matrix:
[[10578686 19703767]
 [ 5391568 19169061]]
Confusion Matrix (%):
[[19.28900713 35.92753412]
 [ 9.830899   34.95255974]]
