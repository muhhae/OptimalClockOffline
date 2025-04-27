#### Datasets

🧾 Basic Info:
------------------------------------------------------------
<class 'pandas.core.frame.DataFrame'>
Index: 186053350 entries, 4154098 to 53189435
Data columns (total 5 columns):
 #   Column              Dtype
---  ------              -----
 0   clock_time_between  int64
 1   clock_freq          int64
 2   lifetime_freq       int64
 3   obj_size_relative   int64
 4   wasted              int64
dtypes: int64(5)
memory usage: 8.3 GB
==> model/logistic_regression_v3[0.001,ignore_obj_size].md <==
              precision    recall  f1-score   support

           0       0.87      0.02      0.04  10011394
           1       0.80      1.00      0.89  39243713

    accuracy                           0.80  49255107
   macro avg       0.84      0.51      0.47  49255107
weighted avg       0.82      0.80      0.72  49255107

Accuracy: 0.8007136194019434
Confusion Matrix:
[[  228155  9783239]
 [   32633 39211080]]
Confusion Matrix (%):
[[4.63210850e-01 1.98623850e+01]
 [6.62530283e-02 7.96081511e+01]]

==> model/logistic_regression_v3[0.001].md <==
              precision    recall  f1-score   support

           0       0.71      0.01      0.01   7980566
           1       0.83      1.00      0.91  38532772

    accuracy                           0.83  46513338
   macro avg       0.77      0.50      0.46  46513338
weighted avg       0.81      0.83      0.75  46513338

Accuracy: 0.8289977382401581
Confusion Matrix:
[[   44748  7935818]
 [   18068 38514704]]
Confusion Matrix (%):
[[9.62046628e-02 1.70613814e+01]
 [3.88447718e-02 8.28035692e+01]]

==> model/logistic_regression_v3[0.01,ignore_obj_size].md <==

==> model/logistic_regression_v3[0.01].md <==
              precision    recall  f1-score   support

           0       0.80      0.20      0.32  27778376
           1       0.70      0.97      0.81  52861330

    accuracy                           0.71  80639706
   macro avg       0.75      0.59      0.57  80639706
weighted avg       0.73      0.71      0.64  80639706

Accuracy: 0.7069765234511147
Confusion Matrix:
[[ 5582718 22195658]
 [ 1433669 51427661]]
Confusion Matrix (%):
[[ 6.92303863 27.52447783]
 [ 1.77786983 63.77461371]]

==> model/logistic_regression_v3[0.1,ignore_obj_size].md <==
              precision    recall  f1-score   support

           0       0.79      0.27      0.40  22673616
           1       0.66      0.95      0.78  33744431

    accuracy                           0.68  56418047
   macro avg       0.72      0.61      0.59  56418047
weighted avg       0.71      0.68      0.63  56418047

Accuracy: 0.6780035650649162
Confusion Matrix:
[[ 6176572 16497044]
 [ 1669366 32075065]]
Confusion Matrix (%):
[[10.94786567 29.2407215 ]
 [ 2.95892199 56.85249084]]

==> model/logistic_regression_v3[0.1].md <==
              precision    recall  f1-score   support

           0       0.71      0.30      0.43  25258747
           1       0.61      0.90      0.73  30718747

    accuracy                           0.63  55977494
   macro avg       0.66      0.60      0.58  55977494
weighted avg       0.66      0.63      0.59  55977494

Accuracy: 0.6300318660210119
Confusion Matrix:
[[ 7690528 17568219]
 [ 3141670 27577077]]
Confusion Matrix (%):
[[13.73860716 31.38443282]
 [ 5.61238058 49.26457944]]

==> model/logistic_regression_v3[0.2,ignore_obj_size].md <==
              precision    recall  f1-score   support

           0       0.69      0.57      0.62  27849041
           1       0.61      0.73      0.66  26157259

    accuracy                           0.65  54006300
   macro avg       0.65      0.65      0.64  54006300
weighted avg       0.65      0.65      0.64  54006300

Accuracy: 0.6452766436508334
Confusion Matrix:
[[15874422 11974619]
 [ 7182677 18974582]]
Confusion Matrix (%):
[[29.39364852 22.17263356]
 [13.29970207 35.13401585]]

==> model/logistic_regression_v3[0.2].md <==
              precision    recall  f1-score   support

           0       0.70      0.75      0.73  25205693
           1       0.66      0.61      0.64  20399591

    accuracy                           0.69  45605284
   macro avg       0.68      0.68      0.68  45605284
weighted avg       0.69      0.69      0.69  45605284

Accuracy: 0.6866941120243873
Confusion Matrix:
[[18880678  6325015]
 [ 7963389 12436202]]
Confusion Matrix (%):
[[41.40019828 13.86903982]
 [17.46154897 27.26921293]]

==> model/logistic_regression_v3[0.4,ignore_obj_size].md <==
              precision    recall  f1-score   support

           0       0.71      0.82      0.76  18527691
           1       0.67      0.53      0.59  13173161

    accuracy                           0.70  31700852
   macro avg       0.69      0.67      0.68  31700852
weighted avg       0.69      0.70      0.69  31700852

Accuracy: 0.6972042265614817
Confusion Matrix:
[[15184966  3342725]
 [ 6256159  6917002]]
Confusion Matrix (%):
[[47.90081352 10.54459041]
 [19.73498693 21.81960914]]

==> model/logistic_regression_v3[0.4].md <==
              precision    recall  f1-score   support

           0       0.60      0.99      0.75  17414266
           1       0.64      0.04      0.07  11850092

    accuracy                           0.60  29264358
   macro avg       0.62      0.51      0.41  29264358
weighted avg       0.62      0.60      0.47  29264358

Accuracy: 0.6016103958268963
Confusion Matrix:
[[17174650   239616]
 [11419000   431092]]
Confusion Matrix (%):
[[58.68794388  0.81879808]
 [39.02016234  1.4730957 ]]

==> model/logistic_regression_v3[All,ignore_obj_size].md <==
              precision    recall  f1-score   support

           0       0.62      0.13      0.22 101698151
           1       0.64      0.95      0.76 165034887

    accuracy                           0.64 266733038
   macro avg       0.63      0.54      0.49 266733038
weighted avg       0.63      0.64      0.56 266733038

Accuracy: 0.6379917623852805
Confusion Matrix:
[[ 13354365  88343786]
 [  8215771 156819116]]
Confusion Matrix (%):
[[ 5.00664076 33.12067626]
 [ 3.0801475  58.79253548]]

==> model/logistic_regression_v3[All].md <==
              precision    recall  f1-score   support

           0       0.64      0.16      0.26 103637647
           1       0.62      0.94      0.75 154362531

    accuracy                           0.63 258000178
   macro avg       0.63      0.55      0.50 258000178
weighted avg       0.63      0.63      0.55 258000178

Accuracy: 0.6263382849294004
Confusion Matrix:
[[ 16549023  87088624]
 [  9316165 145046366]]
Confusion Matrix (%):
[[ 6.41434557 33.75525733]
 [ 3.61091418 56.21948292]]
