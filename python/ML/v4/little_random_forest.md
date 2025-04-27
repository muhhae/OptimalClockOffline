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
==> model/little_random_forest[0.001,ignore_obj_size].md <==
              precision    recall  f1-score   support

           0       0.78      0.48      0.59  10011394
           1       0.88      0.96      0.92  39243713

    accuracy                           0.87  49255107
   macro avg       0.83      0.72      0.76  49255107
weighted avg       0.86      0.87      0.85  49255107

Accuracy: 0.8661169896555092
Confusion Matrix:
[[ 4797521  5213873]
 [ 1380549 37863164]]
Confusion Matrix (%):
[[ 9.74014938 10.5854465 ]
 [ 2.80285453 76.87154958]]

==> model/little_random_forest[0.001].md <==
              precision    recall  f1-score   support

           0       0.78      0.36      0.50   7980566
           1       0.88      0.98      0.93  38532772

    accuracy                           0.87  46513338
   macro avg       0.83      0.67      0.71  46513338
weighted avg       0.86      0.87      0.85  46513338

Accuracy: 0.8734724435386684
Confusion Matrix:
[[ 2905241  5075325]
 [  809894 37722878]]
Confusion Matrix (%):
[[ 6.2460385  10.91154757]
 [ 1.74120808 81.10120585]]

==> model/little_random_forest[0.01,ignore_obj_size].md <==
              precision    recall  f1-score   support

           0       0.81      0.18      0.29  22636409
           1       0.74      0.98      0.84  52716324

    accuracy                           0.74  75352733
   macro avg       0.77      0.58      0.57  75352733
weighted avg       0.76      0.74      0.68  75352733

Accuracy: 0.7404915890708303
Confusion Matrix:
[[ 3993041 18643368]
 [  911300 51805024]]
Confusion Matrix (%):
[[ 5.29913228 24.74146226]
 [ 1.20937883 68.75002662]]

==> model/little_random_forest[0.01].md <==
              precision    recall  f1-score   support

           0       0.82      0.30      0.44  27778376
           1       0.72      0.97      0.83  52861330

    accuracy                           0.74  80639706
   macro avg       0.77      0.63      0.63  80639706
weighted avg       0.76      0.74      0.69  80639706

Accuracy: 0.7370291503790949
Confusion Matrix:
[[ 8378657 19399719]
 [ 1806173 51055157]]
Confusion Matrix (%):
[[10.39023753 24.05727893]
 [ 2.23980603 63.3126775 ]]

==> model/little_random_forest[0.1,ignore_obj_size].md <==
              precision    recall  f1-score   support

           0       0.74      0.60      0.66  22673616
           1       0.76      0.86      0.80  33744431

    accuracy                           0.75  56418047
   macro avg       0.75      0.73      0.73  56418047
weighted avg       0.75      0.75      0.75  56418047

Accuracy: 0.7516559727776468
Confusion Matrix:
[[13527822  9145794]
 [ 4865291 28879140]]
Confusion Matrix (%):
[[23.97782752 16.21075965]
 [ 8.62364307 51.18776976]]

==> model/little_random_forest[0.1].md <==
              precision    recall  f1-score   support

           0       0.69      0.70      0.69  25258747
           1       0.75      0.74      0.74  30718747

    accuracy                           0.72  55977494
   macro avg       0.72      0.72      0.72  55977494
weighted avg       0.72      0.72      0.72  55977494

Accuracy: 0.7212527234606108
Confusion Matrix:
[[17776306  7482441]
 [ 8121133 22597614]]
Confusion Matrix (%):
[[31.75616615 13.36687384]
 [14.50785382 40.3691062 ]]

==> model/little_random_forest[0.2,ignore_obj_size].md <==
              precision    recall  f1-score   support

           0       0.75      0.75      0.75  27849041
           1       0.73      0.73      0.73  26157259

    accuracy                           0.74  54006300
   macro avg       0.74      0.74      0.74  54006300
weighted avg       0.74      0.74      0.74  54006300

Accuracy: 0.7382918844653309
Confusion Matrix:
[[20789122  7059919]
 [ 7073968 19083291]]
Confusion Matrix (%):
[[38.49388312 13.07239896]
 [13.09841259 35.33530533]]

==> model/little_random_forest[0.2].md <==
              precision    recall  f1-score   support

           0       0.77      0.81      0.79  25205693
           1       0.75      0.70      0.72  20399591

    accuracy                           0.76  45605284
   macro avg       0.76      0.76      0.76  45605284
weighted avg       0.76      0.76      0.76  45605284

Accuracy: 0.7608522073889508
Confusion Matrix:
[[20422152  4783541]
 [ 6122862 14276729]]
Confusion Matrix (%):
[[44.78023205 10.48900605]
 [13.42577321 31.30498869]]

==> model/little_random_forest[0.4,ignore_obj_size].md <==
              precision    recall  f1-score   support

           0       0.80      0.84      0.82  18527691
           1       0.75      0.70      0.73  13173161

    accuracy                           0.78  31700852
   macro avg       0.78      0.77      0.77  31700852
weighted avg       0.78      0.78      0.78  31700852

Accuracy: 0.7805145741824226
Confusion Matrix:
[[15500268  3027423]
 [ 3930452  9242709]]
Confusion Matrix (%):
[[48.89543032  9.54997361]
 [12.39856897 29.1560271 ]]

==> model/little_random_forest[0.4].md <==
              precision    recall  f1-score   support

           0       0.79      0.85      0.82  17414266
           1       0.75      0.67      0.71  11850092

    accuracy                           0.78  29264358
   macro avg       0.77      0.76      0.76  29264358
weighted avg       0.78      0.78      0.78  29264358

Accuracy: 0.7779534408374856
Confusion Matrix:
[[14822678  2591588]
 [ 3906462  7943630]]
Confusion Matrix (%):
[[50.6509591   8.85578286]
 [13.34887306 27.14438499]]

==> model/little_random_forest[All,ignore_obj_size].md <==

==> model/little_random_forest[All].md <==
