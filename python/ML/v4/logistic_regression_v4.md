#### Datasets

🧾 Basic Info:
------------------------------------------------------------
<class 'pandas.core.frame.DataFrame'>
Index: 197020424 entries, 87104649 to 64871190
Data columns (total 5 columns):
 #   Column              Dtype
---  ------              -----
 0   clock_time_between  int64
 1   clock_freq          int64
 2   lifetime_freq       int64
 3   obj_size_relative   int64
 4   wasted              int64
dtypes: int64(5)
memory usage: 8.8 GB
==> model/logistic_regression_v4[0.001,ignore_obj_size].md <==
              precision    recall  f1-score   support

           0       0.47      0.68      0.55  10011394
           1       0.91      0.80      0.85  39243713

    accuracy                           0.78  49255107
   macro avg       0.69      0.74      0.70  49255107
weighted avg       0.82      0.78      0.79  49255107

Accuracy: 0.7777990412242938
Confusion Matrix:
[[ 6816905  3194489]
 [ 7750043 31493670]]
Confusion Matrix (%):
[[13.83999633  6.48559955]
 [15.73449632 63.93990779]]

==> model/logistic_regression_v4[0.001].md <==
              precision    recall  f1-score   support

           0       0.40      0.58      0.48   7980566
           1       0.90      0.82      0.86  38532772

    accuracy                           0.78  46513338
   macro avg       0.65      0.70      0.67  46513338
weighted avg       0.82      0.78      0.80  46513338

Accuracy: 0.7811674578160784
Confusion Matrix:
[[ 4607798  3372768]
 [ 6805864 31726908]]
Confusion Matrix (%):
[[ 9.90640147  7.2511846 ]
 [14.63206962 68.21034431]]

==> model/logistic_regression_v4[0.01,ignore_obj_size].md <==
              precision    recall  f1-score   support

           0       0.35      0.86      0.50  22636409
           1       0.84      0.32      0.46  52716324

    accuracy                           0.48  75352733
   macro avg       0.59      0.59      0.48  75352733
weighted avg       0.69      0.48      0.47  75352733

Accuracy: 0.4798589720694006
Confusion Matrix:
[[19366543  3269866]
 [35924182 16792142]]
Confusion Matrix (%):
[[25.70118193  4.33941261]
 [47.67469018 22.28471527]]

==> model/logistic_regression_v4[0.01].md <==
              precision    recall  f1-score   support

           0       0.64      0.37      0.47  27778376
           1       0.73      0.89      0.80  52861330

    accuracy                           0.71  80639706
   macro avg       0.68      0.63      0.64  80639706
weighted avg       0.70      0.71      0.69  80639706

Accuracy: 0.7105820301477785
Confusion Matrix:
[[10344920 17433456]
 [ 5905124 46956206]]
Confusion Matrix (%):
[[12.8285686  21.61894787]
 [ 7.32284912 58.22963442]]

==> model/logistic_regression_v4[0.1,ignore_obj_size].md <==
              precision    recall  f1-score   support

           0       0.65      0.50      0.57  22673616
           1       0.71      0.81      0.76  33744431

    accuracy                           0.69  56418047
   macro avg       0.68      0.66      0.66  56418047
weighted avg       0.68      0.69      0.68  56418047

Accuracy: 0.6897602641225776
Confusion Matrix:
[[11430369 11243247]
 [ 6259873 27484558]]
Confusion Matrix (%):
[[20.26012882 19.92845835]
 [11.09551523 48.71589759]]

==> model/logistic_regression_v4[0.1].md <==
              precision    recall  f1-score   support

           0       0.65      0.46      0.54  25258747
           1       0.64      0.80      0.71  30718747

    accuracy                           0.65  55977494
   macro avg       0.65      0.63      0.63  55977494
weighted avg       0.65      0.65      0.63  55977494

Accuracy: 0.6456410678191489
Confusion Matrix:
[[11693483 13565264]
 [ 6270861 24447886]]
Confusion Matrix (%):
[[20.88961503 24.23342495]
 [11.20246826 43.67449175]]

==> model/logistic_regression_v4[0.2,ignore_obj_size].md <==
              precision    recall  f1-score   support

           0       0.69      0.54      0.61  27849041
           1       0.60      0.74      0.67  26157259

    accuracy                           0.64  54006300
   macro avg       0.65      0.64      0.64  54006300
weighted avg       0.65      0.64      0.64  54006300

Accuracy: 0.6390327054436241
Confusion Matrix:
[[15100171 12748870]
 [ 6745638 19411621]]
Confusion Matrix (%):
[[27.96001763 23.60626445]
 [12.490465   35.94325292]]

==> model/logistic_regression_v4[0.2].md <==
              precision    recall  f1-score   support

           0       0.72      0.63      0.67  25205693
           1       0.60      0.70      0.65  20399591

    accuracy                           0.66  45605284
   macro avg       0.66      0.66      0.66  45605284
weighted avg       0.67      0.66      0.66  45605284

Accuracy: 0.6583525277465655
Confusion Matrix:
[[15839137  9366556]
 [ 6214374 14185217]]
Confusion Matrix (%):
[[34.73092504 20.53831306]
 [13.62643416 31.10432774]]

==> model/logistic_regression_v4[0.4,ignore_obj_size].md <==

==> model/logistic_regression_v4[0.4].md <==
              precision    recall  f1-score   support

           0       0.77      0.40      0.53  17414266
           1       0.48      0.83      0.61  11850092

    accuracy                           0.57  29264358
   macro avg       0.63      0.61      0.57  29264358
weighted avg       0.66      0.57      0.56  29264358

Accuracy: 0.5733519935752562
Confusion Matrix:
[[ 6973790 10440476]
 [ 2045104  9804988]]
Confusion Matrix (%):
[[23.83031946 35.67642249]
 [ 6.98837815 33.5048799 ]]

==> model/logistic_regression_v4[All,ignore_obj_size].md <==

==> model/logistic_regression_v4[All].md <==
