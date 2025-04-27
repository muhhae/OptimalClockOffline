#### Datasets

🧾 Basic Info:
------------------------------------------------------------
<class 'pandas.core.frame.DataFrame'>
Index: 186053350 entries, 4154098 to 53189435
Data columns (total 7 columns):
 #   Column              Dtype
---  ------              -----
 0   clock_time          int64
 1   clock_time_between  int64
 2   cache_size          int64
 3   obj_size            int64
 4   clock_freq          int64
 5   lifetime_freq       int64
 6   wasted              int64
==> model/logistic_regression[0.001,ignore_obj_size].md <==
              precision    recall  f1-score   support

           0       0.06      0.02      0.03  10011394
           1       0.79      0.93      0.85  39243713

    accuracy                           0.74  49255107
   macro avg       0.42      0.47      0.44  49255107
weighted avg       0.64      0.74      0.68  49255107

Accuracy: 0.743873239378
Confusion Matrix:
[[  173074  9838320]
 [ 2777231 36466482]]
Confusion Matrix (%):
[[ 0.35138285 19.97421303]
 [ 5.63846303 74.03594109]]

==> model/logistic_regression[0.001].md <==
              precision    recall  f1-score   support

           0       0.00      0.00      0.00   7980566
           1       0.83      1.00      0.91  38532772

    accuracy                           0.83  46513338
   macro avg       0.41      0.50      0.45  46513338
weighted avg       0.69      0.83      0.75  46513338

Accuracy: 0.8284241393296693
Confusion Matrix:
[[       0  7980566]
 [       0 38532772]]
Confusion Matrix (%):
[[ 0.         17.15758607]
 [ 0.         82.84241393]]

==> model/logistic_regression[0.01,ignore_obj_size].md <==
              precision    recall  f1-score   support

           0       0.20      0.02      0.03  22636409
           1       0.70      0.97      0.81  52716324

    accuracy                           0.68  75352733
   macro avg       0.45      0.49      0.42  75352733
weighted avg       0.55      0.68      0.58  75352733

Accuracy: 0.6841690400267234
Confusion Matrix:
[[  402465 22233944]
 [ 1564782 51151542]]
Confusion Matrix (%):
[[ 0.53410803 29.50648651]
 [ 2.07660948 67.88279597]]

==> model/logistic_regression[0.01].md <==
              precision    recall  f1-score   support

           0       0.00      0.00      0.00  27778376
           1       0.66      1.00      0.79  52861330

    accuracy                           0.66  80639706
   macro avg       0.33      0.50      0.40  80639706
weighted avg       0.43      0.66      0.52  80639706

Accuracy: 0.6555248353708035
Confusion Matrix:
[[       0 27778376]
 [       0 52861330]]
Confusion Matrix (%):
[[ 0.         34.44751646]
 [ 0.         65.55248354]]

==> model/logistic_regression[0.1,ignore_obj_size].md <==
              precision    recall  f1-score   support

           0       0.61      0.36      0.46  22673616
           1       0.66      0.84      0.74  33744431

    accuracy                           0.65  56418047
   macro avg       0.63      0.60      0.60  56418047
weighted avg       0.64      0.65      0.63  56418047

Accuracy: 0.6494531794055189
Confusion Matrix:
[[ 8260366 14413250]
 [ 5363917 28380514]]
Confusion Matrix (%):
[[14.64135403 25.54723314]
 [ 9.50744892 50.30396391]]

==> model/logistic_regression[0.1].md <==
              precision    recall  f1-score   support

           0       0.53      0.28      0.37  25258747
           1       0.57      0.79      0.67  30718747

    accuracy                           0.56  55977494
   macro avg       0.55      0.54      0.52  55977494
weighted avg       0.55      0.56      0.53  55977494

Accuracy: 0.5618147000292654
Confusion Matrix:
[[ 7078216 18180531]
 [ 6347984 24370763]]
Confusion Matrix (%):
[[12.64475326 32.47828672]
 [11.34024328 43.53671674]]

==> model/logistic_regression[0.2,ignore_obj_size].md <==
              precision    recall  f1-score   support

           0       0.63      0.68      0.65  27849041
           1       0.63      0.58      0.60  26157259

    accuracy                           0.63  54006300
   macro avg       0.63      0.63      0.63  54006300
weighted avg       0.63      0.63      0.63  54006300

Accuracy: 0.6298834395246481
Confusion Matrix:
[[18800398  9048643]
 [10939983 15217276]]
Confusion Matrix (%):
[[34.81149051 16.75479157]
 [20.25686448 28.17685344]]

==> model/logistic_regression[0.2].md <==
              precision    recall  f1-score   support

           0       0.51      0.34      0.40  25205693
           1       0.42      0.60      0.49  20399591

    accuracy                           0.45  45605284
   macro avg       0.46      0.47      0.45  45605284
weighted avg       0.47      0.45      0.44  45605284

Accuracy: 0.45233453649800753
Confusion Matrix:
[[ 8479648 16726045]
 [ 8250394 12149197]]
Confusion Matrix (%):
[[18.59356473 36.67567337]
 [18.09087298 26.63988892]]

==> model/logistic_regression[0.4,ignore_obj_size].md <==
              precision    recall  f1-score   support

           0       0.70      0.78      0.74  18527691
           1       0.63      0.54      0.58  13173161

    accuracy                           0.68  31700852
   macro avg       0.67      0.66      0.66  31700852
weighted avg       0.67      0.68      0.67  31700852

Accuracy: 0.678852196149176
Confusion Matrix:
[[14453048  4074643]
 [ 6106016  7067145]]
Confusion Matrix (%):
[[45.59198598 12.85341795]
 [19.26136244 22.29323363]]

==> model/logistic_regression[0.4].md <==
              precision    recall  f1-score   support

           0       0.58      0.55      0.57  17414266
           1       0.39      0.42      0.41  11850092

    accuracy                           0.50  29264358
   macro avg       0.49      0.49      0.49  29264358
weighted avg       0.50      0.50      0.50  29264358

Accuracy: 0.4980537416880972
Confusion Matrix:
[[9557377 7856889]
 [6832246 5017846]]
Confusion Matrix (%):
[[32.6587619  26.84798006]
 [23.34664577 17.14661227]]

==> model/logistic_regression[All,ignore_obj_size].md <==

==> model/logistic_regression[All].md <==
