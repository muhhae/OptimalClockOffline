#### Datasets

🧾 Basic Info:
------------------------------------------------------------
<class 'pandas.core.frame.DataFrame'>
Index: 197020424 entries, 87104649 to 64871190
Data columns (total 6 columns):
 #   Column              Dtype
---  ------              -----
 0   clock_time_between  int64
 1   clock_freq          int64
 2   lifetime_freq       int64
 3   time_since          int64
 4   obj_size_relative   int64
 5   wasted              int64
dtypes: int64(6)
==> model/logistic_regression_v2[0.001,ignore_obj_size].md <==
              precision    recall  f1-score   support

           0       0.71      0.17      0.28  10011394
           1       0.82      0.98      0.90  39243713

    accuracy                           0.82  49255107
   macro avg       0.77      0.58      0.59  49255107
weighted avg       0.80      0.82      0.77  49255107

Accuracy: 0.8179185358383243
Confusion Matrix:
[[ 1743015  8268379]
 [  700063 38543650]]
Confusion Matrix (%):
[[ 3.5387498  16.78684608]
 [ 1.42130033 78.25310378]]

==> model/logistic_regression_v2[0.001].md <==
              precision    recall  f1-score   support

           0       0.64      0.04      0.07   7980566
           1       0.83      1.00      0.91  38532772

    accuracy                           0.83  46513338
   macro avg       0.73      0.52      0.49  46513338
weighted avg       0.80      0.83      0.76  46513338

Accuracy: 0.8312464050634251
Confusion Matrix:
[[  306168  7674398]
 [  174895 38357877]]
Confusion Matrix (%):
[[ 0.658237   16.49934907]
 [ 0.37601043 82.46640351]]

==> model/logistic_regression_v2[0.01,ignore_obj_size].md <==
              precision    recall  f1-score   support

           0       0.31      0.05      0.08  22636409
           1       0.70      0.96      0.81  52716324

    accuracy                           0.68  75352733
   macro avg       0.50      0.50      0.44  75352733
weighted avg       0.58      0.68      0.59  75352733

Accuracy: 0.6827022451859842
Confusion Matrix:
[[ 1034784 21601625]
 [ 2307628 50408696]]
Confusion Matrix (%):
[[ 1.37325344 28.6673411 ]
 [ 3.06243438 66.89697108]]

==> model/logistic_regression_v2[0.01].md <==
              precision    recall  f1-score   support

           0       0.41      0.58      0.48  27778376
           1       0.71      0.55      0.62  52861330

    accuracy                           0.56  80639706
   macro avg       0.56      0.57      0.55  80639706
weighted avg       0.61      0.56      0.57  80639706

Accuracy: 0.5627948097925853
Confusion Matrix:
[[16076272 11702104]
 [23553994 29307336]]
Confusion Matrix (%):
[[19.93592586 14.51159061]
 [29.20892842 36.34355512]]

==> model/logistic_regression_v2[0.1,ignore_obj_size].md <==
              precision    recall  f1-score   support

           0       0.47      0.63      0.54  22673616
           1       0.68      0.52      0.59  33744431

    accuracy                           0.57  56418047
   macro avg       0.57      0.58      0.57  56418047
weighted avg       0.59      0.57      0.57  56418047

Accuracy: 0.5667942564548539
Confusion Matrix:
[[14275473  8398143]
 [16042479 17701952]]
Confusion Matrix (%):
[[25.30302582 14.88556135]
 [28.435013   31.37639982]]

==> model/logistic_regression_v2[0.1].md <==
              precision    recall  f1-score   support

           0       0.48      0.68      0.56  25258747
           1       0.60      0.39      0.47  30718747

    accuracy                           0.52  55977494
   macro avg       0.54      0.54      0.52  55977494
weighted avg       0.55      0.52      0.51  55977494

Accuracy: 0.5230630545911898
Confusion Matrix:
[[17279338  7979409]
 [18718326 12000421]]
Confusion Matrix (%):
[[30.86836649 14.25467349]
 [33.43902105 21.43793897]]

==> model/logistic_regression_v2[0.2,ignore_obj_size].md <==
              precision    recall  f1-score   support

           0       0.59      0.71      0.64  27849041
           1       0.60      0.47      0.53  26157259

    accuracy                           0.59  54006300
   macro avg       0.59      0.59      0.58  54006300
weighted avg       0.59      0.59      0.59  54006300

Accuracy: 0.5925705889868405
Confusion Matrix:
[[19753542  8095499]
 [13908256 12249003]]
Confusion Matrix (%):
[[36.57636609 14.98991599]
 [25.75302511 22.68069281]]

==> model/logistic_regression_v2[0.2].md <==
              precision    recall  f1-score   support

           0       0.55      1.00      0.71  25205693
           1       0.00      0.00      0.00  20399591

    accuracy                           0.55  45605284
   macro avg       0.28      0.50      0.36  45605284
weighted avg       0.31      0.55      0.39  45605284

Accuracy: 0.5526923809969038
Confusion Matrix:
[[25205693        0]
 [20399591        0]]
Confusion Matrix (%):
[[55.2692381  0.       ]
 [44.7307619  0.       ]]

==> model/logistic_regression_v2[0.4,ignore_obj_size].md <==
              precision    recall  f1-score   support

           0       0.58      1.00      0.74  18527691
           1       0.00      0.00      0.00  13173161

    accuracy                           0.58  31700852
   macro avg       0.29      0.50      0.37  31700852
weighted avg       0.34      0.58      0.43  31700852

Accuracy: 0.5844540392794491
Confusion Matrix:
[[18527691        0]
 [13173161        0]]
Confusion Matrix (%):
[[58.44540393  0.        ]
 [41.55459607  0.        ]]

==> model/logistic_regression_v2[0.4].md <==
              precision    recall  f1-score   support

           0       0.60      1.00      0.75  17414266
           1       0.00      0.00      0.00  11850092

    accuracy                           0.60  29264358
   macro avg       0.30      0.50      0.37  29264358
weighted avg       0.35      0.60      0.44  29264358

Accuracy: 0.5950674195552146
Confusion Matrix:
[[17414266        0]
 [11850092        0]]
Confusion Matrix (%):
[[59.50674196  0.        ]
 [40.49325804  0.        ]]

==> model/logistic_regression_v2[All,ignore_obj_size].md <==
              precision    recall  f1-score   support

           0       0.52      0.54      0.53 101698151
           1       0.71      0.69      0.70 165034887

    accuracy                           0.63 266733038
   macro avg       0.61      0.61      0.61 266733038
weighted avg       0.64      0.63      0.63 266733038

Accuracy: 0.632507559862157
Confusion Matrix:
[[ 54755127  46943024]
 [ 51079351 113955536]]
Confusion Matrix (%):
[[20.52806334 17.59925368]
 [19.14999034 42.72269264]]

==> model/logistic_regression_v2[All].md <==
              precision    recall  f1-score   support

           0       0.47      0.75      0.58 103637647
           1       0.72      0.43      0.54 154362531

    accuracy                           0.56 258000178
   macro avg       0.59      0.59      0.56 258000178
weighted avg       0.62      0.56      0.55 258000178

Accuracy: 0.5579543011012962
Confusion Matrix:
[[77786269 25851378]
 [88196491 66166040]]
Confusion Matrix (%):
[[30.14969587 10.01990704]
 [34.18466285 25.64573424]]
