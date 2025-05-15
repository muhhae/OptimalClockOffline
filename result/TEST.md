# RESULT AGAINST TEST DATA
# [Train Data](./README.md)
# [Box Plot](./overall/README.md)
# [Box Plot (obj_size_ignored)](./overall/README_obj_size_ignored.md)
# Line Plot
# Model Summaries  
|Model|Better Than Base (%)|Mean Miss Ratio Reduced (%)|Median Miss Ratio Reduced (%)|Mean Promotion Reduced (%)|Median Promotion Reduced (%)|  
|---|---|---|---|---|---|  
|LR_1_spec|12.857142857142856|-0.03774838739969144|-4.791913923859484e-05|31.504071072404145|5.988833172584343|  
|LR_1_All|3.571428571428571|-0.025807746278498498|0.0|13.743827857605654|0.0|  
|LR_1_log_spec|17.142857142857142|-0.024136272934038826|-9.315611464586344e-05|30.262976924909847|11.009006376595313|  
|LR_1_log_All|9.285714285714286|-0.040439592771876955|-0.017380774105176983|48.2558462388842|52.9957821551605|  
|LR_1_mean_spec|17.142857142857142|-0.041429737630018476|-3.513990319261423e-06|30.283349268671405|2.6359511269154092|  
|LR_1_mean_All|10.0|-0.15380500579223175|-0.040828229450330274|58.76728068710144|72.40602691144706|  
|LR_v5_spec|5.714285714285714|-0.15805933113512255|-0.12139863922672642|80.01424976288017|99.99999125773157|  
|LR_v5_All|5.714285714285714|-0.166526046156917|-0.12186122032818807|99.99999883069638|100.0|  
|LR_v6_spec|5.714285714285714|-0.16649746993884643|-0.12186012935641584|99.9242944328451|99.99985703711181|  
|LR_v6_All|5.714285714285714|-0.16649790485911967|-0.12186012935641584|99.92427149193281|99.99989235333611|  
|logistic_regression_v2_spec|8.571428571428571|-0.018376391363078247|-0.0016176674879658987|35.74119964891261|6.30771400014299|  
|logistic_regression_v2_All|31.428571428571427|-0.025194026880002152|0.0|32.27505384504198|13.848591581184955|  
|logistic_regression_v3_spec|22.857142857142858|-0.04746244077130976|-0.02550564885234547|73.01044279954334|85.41809330039021|  
|logistic_regression_v3_All|7.142857142857142|-0.12763558265744318|-0.1003360996742261|90.49194602601649|94.88229612515515|  
|logistic_regression_v4_spec|18.571428571428573|-0.05032400126273785|-0.024428310379282073|64.05042131003862|70.59708418008083|  
|logistic_regression_v4_All|15.714285714285714|-0.062263128951266684|-0.042027174577580276|70.27056002621465|76.97631367868148|  
## 10 https://ftp.pdl.cmu.edu/pub/datasets/twemcacheWorkload/cacheDatasets/twitter/cluster10.oracleGeneral.zst
> ![graph](./graph/10[0.001,TEST].png)  
> **Trace Path**: 10.oracleGeneral.zst  
> **Desc**: ['0.001', 'TEST', {}]  
> **Cache Size**: 82  
> **Total Request**: 2,756,726,994  
> **Best Model**: LR_1_All,LR_v5_spec => 0.999568  
> **Better Than Base**: False  
> ![graph](./graph/10[0.001,ignore_obj_size,TEST].png)  
> **Trace Path**: 10.oracleGeneral.zst  
> **Desc**: ['0.001', 'ignore_obj_size', 'TEST', {}]  
> **Cache Size**: 7360  
> **Total Request**: 2,756,726,994  
> **Best Model**: LR_1_All,LR_v5_spec => 0.999575  
> **Better Than Base**: False  
> ![graph](./graph/10[0.01,TEST].png)  
> **Trace Path**: 10.oracleGeneral.zst  
> **Desc**: ['0.01', 'TEST', {}]  
> **Cache Size**: 826  
> **Total Request**: 2,756,726,994  
> **Best Model**: LR_v5_spec,LR_v5_All,LR_v6_spec,LR_v6_All => 0.890473  
> **Better Than Base**: True  
> ![graph](./graph/10[0.01,ignore_obj_size,TEST].png)  
> **Trace Path**: 10.oracleGeneral.zst  
> **Desc**: ['0.01', 'ignore_obj_size', 'TEST', {}]  
> **Cache Size**: 73601  
> **Total Request**: 2,756,726,994  
> **Best Model**: LR_1_mean_All => 0.994365  
> **Better Than Base**: True  
> ![graph](./graph/10[0.1,TEST].png)  
> **Trace Path**: 10.oracleGeneral.zst  
> **Desc**: ['0.1', 'TEST', {}]  
> **Cache Size**: 8269  
> **Total Request**: 2,756,726,994  
> **Best Model**: logistic_regression_v4_spec => 0.0346106  
> **Better Than Base**: True  
> ![graph](./graph/10[0.1,ignore_obj_size,TEST].png)  
> **Trace Path**: 10.oracleGeneral.zst  
> **Desc**: ['0.1', 'ignore_obj_size', 'TEST', {}]  
> **Cache Size**: 736017  
> **Total Request**: 2,756,726,994  
> **Best Model**: logistic_regression_v4_spec => 0.062645  
> **Better Than Base**: True  
> ![graph](./graph/10[0.2,TEST].png)  
> **Trace Path**: 10.oracleGeneral.zst  
> **Desc**: ['0.2', 'TEST', {}]  
> **Cache Size**: 16539  
> **Total Request**: 2,756,726,994  
> **Best Model**: logistic_regression_v3_spec => 0.0342232  
> **Better Than Base**: True  
> ![graph](./graph/10[0.2,ignore_obj_size,TEST].png)  
> **Trace Path**: 10.oracleGeneral.zst  
> **Desc**: ['0.2', 'ignore_obj_size', 'TEST', {}]  
> **Cache Size**: 1472034  
> **Total Request**: 2,756,726,994  
> **Best Model**: LR_v5_spec,LR_v5_All,LR_v6_spec,LR_v6_All => 0.0342699  
> **Better Than Base**: True  
> ![graph](./graph/10[0.4,TEST].png)  
> **Trace Path**: 10.oracleGeneral.zst  
> **Desc**: ['0.4', 'TEST', {}]  
> **Cache Size**: 33078  
> **Total Request**: 2,756,726,994  
> **Best Model**: logistic_regression_v4_spec => 0.0336914  
> **Better Than Base**: True  
> ![graph](./graph/10[0.4,ignore_obj_size,TEST].png)  
> **Trace Path**: 10.oracleGeneral.zst  
> **Desc**: ['0.4', 'ignore_obj_size', 'TEST', {}]  
> **Cache Size**: 2944069  
> **Total Request**: 2,756,726,994  
> **Best Model**: LR_1_log_spec => 0.034033  
> **Better Than Base**: True  
## 2016_LUN6 https://ftp.pdl.cmu.edu/pub/datasets/twemcacheWorkload/cacheDatasets/systor/2016_LUN6.oracleGeneral.zst
> ![graph](./graph/2016_LUN6[0.001,TEST].png)  
> **Trace Path**: 2016_LUN6.oracleGeneral.zst  
> **Desc**: ['0.001', 'TEST', {}]  
> **Cache Size**: 2476  
> **Total Request**: 655,119,703  
> **Best Model**: LR_1_All,LR_v5_spec => 0.830016  
> **Better Than Base**: False  
> ![graph](./graph/2016_LUN6[0.001,ignore_obj_size,TEST].png)  
> **Trace Path**: 2016_LUN6.oracleGeneral.zst  
> **Desc**: ['0.001', 'ignore_obj_size', 'TEST', {}]  
> **Cache Size**: 72393  
> **Total Request**: 655,119,703  
> **Best Model**: LR_1_All,LR_v5_spec => 0.836408  
> **Better Than Base**: False  
> ![graph](./graph/2016_LUN6[0.01,TEST].png)  
> **Trace Path**: 2016_LUN6.oracleGeneral.zst  
> **Desc**: ['0.01', 'TEST', {}]  
> **Cache Size**: 24761  
> **Total Request**: 655,119,703  
> **Best Model**: LR_1_All => 0.699474  
> **Better Than Base**: False  
> ![graph](./graph/2016_LUN6[0.01,ignore_obj_size,TEST].png)  
> **Trace Path**: 2016_LUN6.oracleGeneral.zst  
> **Desc**: ['0.01', 'ignore_obj_size', 'TEST', {}]  
> **Cache Size**: 723935  
> **Total Request**: 655,119,703  
> **Best Model**: LR_1_All => 0.733029  
> **Better Than Base**: False  
> ![graph](./graph/2016_LUN6[0.1,TEST].png)  
> **Trace Path**: 2016_LUN6.oracleGeneral.zst  
> **Desc**: ['0.1', 'TEST', {}]  
> **Cache Size**: 247614  
> **Total Request**: 655,119,703  
> **Best Model**: logistic_regression_v2_All => 0.383723  
> **Better Than Base**: False  
> ![graph](./graph/2016_LUN6[0.1,ignore_obj_size,TEST].png)  
> **Trace Path**: 2016_LUN6.oracleGeneral.zst  
> **Desc**: ['0.1', 'ignore_obj_size', 'TEST', {}]  
> **Cache Size**: 7239357  
> **Total Request**: 655,119,703  
> **Best Model**: logistic_regression_v2_All => 0.403522  
> **Better Than Base**: False  
> ![graph](./graph/2016_LUN6[0.2,TEST].png)  
> **Trace Path**: 2016_LUN6.oracleGeneral.zst  
> **Desc**: ['0.2', 'TEST', {}]  
> **Cache Size**: 495229  
> **Total Request**: 655,119,703  
> **Best Model**: logistic_regression_v2_spec => 0.198792  
> **Better Than Base**: False  
> ![graph](./graph/2016_LUN6[0.2,ignore_obj_size,TEST].png)  
> **Trace Path**: 2016_LUN6.oracleGeneral.zst  
> **Desc**: ['0.2', 'ignore_obj_size', 'TEST', {}]  
> **Cache Size**: 14478714  
> **Total Request**: 655,119,703  
> **Best Model**: logistic_regression_v2_All => 0.214693  
> **Better Than Base**: False  
> ![graph](./graph/2016_LUN6[0.4,TEST].png)  
> **Trace Path**: 2016_LUN6.oracleGeneral.zst  
> **Desc**: ['0.4', 'TEST', {}]  
> **Cache Size**: 990459  
> **Total Request**: 655,119,703  
> **Best Model**: logistic_regression_v2_spec => 0.143264  
> **Better Than Base**: False  
> ![graph](./graph/2016_LUN6[0.4,ignore_obj_size,TEST].png)  
> **Trace Path**: 2016_LUN6.oracleGeneral.zst  
> **Desc**: ['0.4', 'ignore_obj_size', 'TEST', {}]  
> **Cache Size**: 28957428  
> **Total Request**: 655,119,703  
> **Best Model**: logistic_regression_v2_spec,logistic_regression_v2_All => 0.147587  
> **Better Than Base**: False  
## 202206_kv_traces_all.csv https://ftp.pdl.cmu.edu/pub/datasets/twemcacheWorkload/cacheDatasets/metaKV/202206_kv_traces_all.csv.oracleGeneral.zst
> ![graph](./graph/202206_kv_traces_all.csv[0.001,TEST].png)  
> **Trace Path**: 202206_kv_traces_all.csv.oracleGeneral.zst  
> **Desc**: ['0.001', 'TEST', {}]  
> **Cache Size**: 60  
> **Total Request**: 1,665,685,869  
> **Best Model**: logistic_regression_v2_All => 0.211619  
> **Better Than Base**: True  
> ![graph](./graph/202206_kv_traces_all.csv[0.001,ignore_obj_size,TEST].png)  
> **Trace Path**: 202206_kv_traces_all.csv.oracleGeneral.zst  
> **Desc**: ['0.001', 'ignore_obj_size', 'TEST', {}]  
> **Cache Size**: 52429  
> **Total Request**: 1,644,762,386  
> **Best Model**: LR_1_All => 0.242686  
> **Better Than Base**: True  
> ![graph](./graph/202206_kv_traces_all.csv[0.01,TEST].png)  
> **Trace Path**: 202206_kv_traces_all.csv.oracleGeneral.zst  
> **Desc**: ['0.01', 'TEST', {}]  
> **Cache Size**: 605  
> **Total Request**: 1,665,685,869  
> **Best Model**: logistic_regression_v2_All => 0.100321  
> **Better Than Base**: True  
> ![graph](./graph/202206_kv_traces_all.csv[0.01,ignore_obj_size,TEST].png)  
> **Trace Path**: 202206_kv_traces_all.csv.oracleGeneral.zst  
> **Desc**: ['0.01', 'ignore_obj_size', 'TEST', {}]  
> **Cache Size**: 524291  
> **Total Request**: 1,644,762,386  
> **Best Model**: LR_1_log_spec,LR_1_mean_spec => 0.115557  
> **Better Than Base**: True  
> ![graph](./graph/202206_kv_traces_all.csv[0.1,TEST].png)  
> **Trace Path**: 202206_kv_traces_all.csv.oracleGeneral.zst  
> **Desc**: ['0.1', 'TEST', {}]  
> **Cache Size**: 6055  
> **Total Request**: 1,665,685,869  
> **Best Model**: logistic_regression_v2_All => 0.0499373  
> **Better Than Base**: True  
> ![graph](./graph/202206_kv_traces_all.csv[0.1,ignore_obj_size,TEST].png)  
> **Trace Path**: 202206_kv_traces_all.csv.oracleGeneral.zst  
> **Desc**: ['0.1', 'ignore_obj_size', 'TEST', {}]  
> **Cache Size**: 5242910  
> **Total Request**: 1,644,762,386  
> **Best Model**: logistic_regression_v2_spec,logistic_regression_v2_All => 0.0552932  
> **Better Than Base**: False  
> ![graph](./graph/202206_kv_traces_all.csv[0.2,TEST].png)  
> **Trace Path**: 202206_kv_traces_all.csv.oracleGeneral.zst  
> **Desc**: ['0.2', 'TEST', {}]  
> **Cache Size**: 12110  
> **Total Request**: 1,665,685,869  
> **Best Model**: logistic_regression_v2_All => 0.0411439  
> **Better Than Base**: True  
> ![graph](./graph/202206_kv_traces_all.csv[0.2,ignore_obj_size,TEST].png)  
> **Trace Path**: 202206_kv_traces_all.csv.oracleGeneral.zst  
> **Desc**: ['0.2', 'ignore_obj_size', 'TEST', {}]  
> **Cache Size**: 10485820  
> **Total Request**: 1,644,762,386  
> **Best Model**: logistic_regression_v2_spec,logistic_regression_v2_All => 0.0451591  
> **Better Than Base**: False  
> ![graph](./graph/202206_kv_traces_all.csv[0.4,TEST].png)  
> **Trace Path**: 202206_kv_traces_all.csv.oracleGeneral.zst  
> **Desc**: ['0.4', 'TEST', {}]  
> **Cache Size**: 24221  
> **Total Request**: 1,665,685,869  
> **Best Model**: logistic_regression_v3_spec => 0.0338314  
> **Better Than Base**: True  
> ![graph](./graph/202206_kv_traces_all.csv[0.4,ignore_obj_size,TEST].png)  
> **Trace Path**: 202206_kv_traces_all.csv.oracleGeneral.zst  
> **Desc**: ['0.4', 'ignore_obj_size', 'TEST', {}]  
> **Cache Size**: 20971640  
> **Total Request**: 1,644,762,386  
> **Best Model**: logistic_regression_v2_spec,logistic_regression_v2_All => 0.0351843  
> **Better Than Base**: False  
## 8610 https://ftp.pdl.cmu.edu/pub/datasets/twemcacheWorkload/cacheDatasets/tencentBlock/v2/traces/8610.oracleGeneral.zst
> ![graph](./graph/8610[0.001,TEST].png)  
> **Trace Path**: 8610.oracleGeneral.zst  
> **Desc**: ['0.001', 'TEST', {}]  
> **Cache Size**: 16  
> **Total Request**: 188,982,398  
> **Best Model**: LR_1_spec => 0.9037  
> **Better Than Base**: True  
> ![graph](./graph/8610[0.001,ignore_obj_size,TEST].png)  
> **Trace Path**: 8610.oracleGeneral.zst  
> **Desc**: ['0.001', 'ignore_obj_size', 'TEST', {}]  
> **Cache Size**: 1033  
> **Total Request**: 188,982,398  
> **Best Model**: LR_1_spec => 0.89831  
> **Better Than Base**: True  
> ![graph](./graph/8610[0.01,TEST].png)  
> **Trace Path**: 8610.oracleGeneral.zst  
> **Desc**: ['0.01', 'TEST', {}]  
> **Cache Size**: 166  
> **Total Request**: 188,982,398  
> **Best Model**: logistic_regression_v2_All => 0.79176  
> **Better Than Base**: True  
> ![graph](./graph/8610[0.01,ignore_obj_size,TEST].png)  
> **Trace Path**: 8610.oracleGeneral.zst  
> **Desc**: ['0.01', 'ignore_obj_size', 'TEST', {}]  
> **Cache Size**: 10330  
> **Total Request**: 188,982,398  
> **Best Model**: LR_1_spec,LR_1_All => 0.763691  
> **Better Than Base**: False  
> ![graph](./graph/8610[0.1,TEST].png)  
> **Trace Path**: 8610.oracleGeneral.zst  
> **Desc**: ['0.1', 'TEST', {}]  
> **Cache Size**: 1669  
> **Total Request**: 188,982,398  
> **Best Model**: logistic_regression_v4_spec => 0.176032  
> **Better Than Base**: True  
> ![graph](./graph/8610[0.1,ignore_obj_size,TEST].png)  
> **Trace Path**: 8610.oracleGeneral.zst  
> **Desc**: ['0.1', 'ignore_obj_size', 'TEST', {}]  
> **Cache Size**: 103301  
> **Total Request**: 188,982,398  
> **Best Model**: LR_1_log_spec => 0.164029  
> **Better Than Base**: True  
> ![graph](./graph/8610[0.2,TEST].png)  
> **Trace Path**: 8610.oracleGeneral.zst  
> **Desc**: ['0.2', 'TEST', {}]  
> **Cache Size**: 3339  
> **Total Request**: 188,982,398  
> **Best Model**: logistic_regression_v3_spec => 0.0491772  
> **Better Than Base**: True  
> ![graph](./graph/8610[0.2,ignore_obj_size,TEST].png)  
> **Trace Path**: 8610.oracleGeneral.zst  
> **Desc**: ['0.2', 'ignore_obj_size', 'TEST', {}]  
> **Cache Size**: 206602  
> **Total Request**: 188,982,398  
> **Best Model**: LR_1_mean_spec => 0.0521634  
> **Better Than Base**: True  
> ![graph](./graph/8610[0.4,TEST].png)  
> **Trace Path**: 8610.oracleGeneral.zst  
> **Desc**: ['0.4', 'TEST', {}]  
> **Cache Size**: 6679  
> **Total Request**: 188,982,398  
> **Best Model**: logistic_regression_v3_spec => 0.00992362  
> **Better Than Base**: True  
> ![graph](./graph/8610[0.4,ignore_obj_size,TEST].png)  
> **Trace Path**: 8610.oracleGeneral.zst  
> **Desc**: ['0.4', 'ignore_obj_size', 'TEST', {}]  
> **Cache Size**: 413204  
> **Total Request**: 188,982,398  
> **Best Model**: LR_1_log_spec => 0.0126434  
> **Better Than Base**: True  
## cluster53 https://ftp.pdl.cmu.edu/pub/datasets/twemcacheWorkload/cacheDatasets/twitter/cluster53.oracleGeneral.zst
> ![graph](./graph/cluster53[0.001,TEST].png)  
> **Trace Path**: cluster53.oracleGeneral.zst  
> **Desc**: ['0.001', 'TEST', {}]  
> **Cache Size**: 10  
> **Total Request**: 246,508,262  
> **Best Model**: logistic_regression_v2_All => 0.636095  
> **Better Than Base**: True  
> ![graph](./graph/cluster53[0.001,ignore_obj_size,TEST].png)  
> **Trace Path**: cluster53.oracleGeneral.zst  
> **Desc**: ['0.001', 'ignore_obj_size', 'TEST', {}]  
> **Cache Size**: 7243  
> **Total Request**: 246,508,262  
> **Best Model**: LR_1_log_spec => 0.456887  
> **Better Than Base**: True  
> ![graph](./graph/cluster53[0.01,TEST].png)  
> **Trace Path**: cluster53.oracleGeneral.zst  
> **Desc**: ['0.01', 'TEST', {}]  
> **Cache Size**: 103  
> **Total Request**: 246,508,262  
> **Best Model**: logistic_regression_v2_All => 0.313188  
> **Better Than Base**: True  
> ![graph](./graph/cluster53[0.01,ignore_obj_size,TEST].png)  
> **Trace Path**: cluster53.oracleGeneral.zst  
> **Desc**: ['0.01', 'ignore_obj_size', 'TEST', {}]  
> **Cache Size**: 72439  
> **Total Request**: 246,508,262  
> **Best Model**: LR_1_log_spec => 0.1583  
> **Better Than Base**: True  
> ![graph](./graph/cluster53[0.1,TEST].png)  
> **Trace Path**: cluster53.oracleGeneral.zst  
> **Desc**: ['0.1', 'TEST', {}]  
> **Cache Size**: 1033  
> **Total Request**: 246,508,262  
> **Best Model**: logistic_regression_v2_All => 0.108301  
> **Better Than Base**: True  
> ![graph](./graph/cluster53[0.1,ignore_obj_size,TEST].png)  
> **Trace Path**: cluster53.oracleGeneral.zst  
> **Desc**: ['0.1', 'ignore_obj_size', 'TEST', {}]  
> **Cache Size**: 724391  
> **Total Request**: 246,508,262  
> **Best Model**: LR_1_All => 0.0570364  
> **Better Than Base**: True  
> ![graph](./graph/cluster53[0.2,TEST].png)  
> **Trace Path**: cluster53.oracleGeneral.zst  
> **Desc**: ['0.2', 'TEST', {}]  
> **Cache Size**: 2066  
> **Total Request**: 246,508,262  
> **Best Model**: logistic_regression_v2_All => 0.0763369  
> **Better Than Base**: True  
> ![graph](./graph/cluster53[0.2,ignore_obj_size,TEST].png)  
> **Trace Path**: cluster53.oracleGeneral.zst  
> **Desc**: ['0.2', 'ignore_obj_size', 'TEST', {}]  
> **Cache Size**: 1448783  
> **Total Request**: 246,508,262  
> **Best Model**: logistic_regression_v2_spec => 0.0422154  
> **Better Than Base**: True  
> ![graph](./graph/cluster53[0.4,TEST].png)  
> **Trace Path**: cluster53.oracleGeneral.zst  
> **Desc**: ['0.4', 'TEST', {}]  
> **Cache Size**: 4132  
> **Total Request**: 246,508,262  
> **Best Model**: logistic_regression_v3_spec => 0.0537166  
> **Better Than Base**: True  
> ![graph](./graph/cluster53[0.4,ignore_obj_size,TEST].png)  
> **Trace Path**: cluster53.oracleGeneral.zst  
> **Desc**: ['0.4', 'ignore_obj_size', 'TEST', {}]  
> **Cache Size**: 2897567  
> **Total Request**: 246,508,262  
> **Best Model**: LR_1_log_All => 0.0327878  
> **Better Than Base**: True  
## meta_rprn https://ftp.pdl.cmu.edu/pub/datasets/twemcacheWorkload/cacheDatasets/metaCDN/meta_rprn.oracleGeneral.zst
> ![graph](./graph/meta_rprn[0.001,TEST].png)  
> **Trace Path**: meta_rprn.oracleGeneral.zst  
> **Desc**: ['0.001', 'TEST', {}]  
> **Cache Size**: 698675  
> **Total Request**: 88,470,732  
> **Best Model**: logistic_regression_v2_All => 0.586703  
> **Better Than Base**: True  
> ![graph](./graph/meta_rprn[0.001,ignore_obj_size,TEST].png)  
> **Trace Path**: meta_rprn.oracleGeneral.zst  
> **Desc**: ['0.001', 'ignore_obj_size', 'TEST', {}]  
> **Cache Size**: 29030  
> **Total Request**: 88,470,732  
> **Best Model**: LR_1_All => 0.59364  
> **Better Than Base**: False  
> ![graph](./graph/meta_rprn[0.01,TEST].png)  
> **Trace Path**: meta_rprn.oracleGeneral.zst  
> **Desc**: ['0.01', 'TEST', {}]  
> **Cache Size**: 6986759  
> **Total Request**: 88,470,732  
> **Best Model**: logistic_regression_v2_All => 0.520473  
> **Better Than Base**: True  
> ![graph](./graph/meta_rprn[0.01,ignore_obj_size,TEST].png)  
> **Trace Path**: meta_rprn.oracleGeneral.zst  
> **Desc**: ['0.01', 'ignore_obj_size', 'TEST', {}]  
> **Cache Size**: 290302  
> **Total Request**: 88,470,732  
> **Best Model**: LR_1_All,logistic_regression_v4_spec => 0.527533  
> **Better Than Base**: False  
> ![graph](./graph/meta_rprn[0.1,TEST].png)  
> **Trace Path**: meta_rprn.oracleGeneral.zst  
> **Desc**: ['0.1', 'TEST', {}]  
> **Cache Size**: 69867592  
> **Total Request**: 88,470,732  
> **Best Model**: logistic_regression_v2_All => 0.429722  
> **Better Than Base**: True  
> ![graph](./graph/meta_rprn[0.1,ignore_obj_size,TEST].png)  
> **Trace Path**: meta_rprn.oracleGeneral.zst  
> **Desc**: ['0.1', 'ignore_obj_size', 'TEST', {}]  
> **Cache Size**: 2903028  
> **Total Request**: 88,470,732  
> **Best Model**: LR_1_All,logistic_regression_v2_All => 0.437969  
> **Better Than Base**: False  
> ![graph](./graph/meta_rprn[0.2,TEST].png)  
> **Trace Path**: meta_rprn.oracleGeneral.zst  
> **Desc**: ['0.2', 'TEST', {}]  
> **Cache Size**: 139735184  
> **Total Request**: 88,470,732  
> **Best Model**: logistic_regression_v2_All => 0.389006  
> **Better Than Base**: True  
> ![graph](./graph/meta_rprn[0.2,ignore_obj_size,TEST].png)  
> **Trace Path**: meta_rprn.oracleGeneral.zst  
> **Desc**: ['0.2', 'ignore_obj_size', 'TEST', {}]  
> **Cache Size**: 5806056  
> **Total Request**: 88,470,732  
> **Best Model**: logistic_regression_v2_spec => 0.394803  
> **Better Than Base**: True  
> ![graph](./graph/meta_rprn[0.4,TEST].png)  
> **Trace Path**: meta_rprn.oracleGeneral.zst  
> **Desc**: ['0.4', 'TEST', {}]  
> **Cache Size**: 279470368  
> **Total Request**: 88,470,732  
> **Best Model**: logistic_regression_v3_spec => 0.346304  
> **Better Than Base**: True  
> ![graph](./graph/meta_rprn[0.4,ignore_obj_size,TEST].png)  
> **Trace Path**: meta_rprn.oracleGeneral.zst  
> **Desc**: ['0.4', 'ignore_obj_size', 'TEST', {}]  
> **Cache Size**: 11612113  
> **Total Request**: 88,470,732  
> **Best Model**: logistic_regression_v4_All => 0.355398  
> **Better Than Base**: True  
## wiki_2019u https://ftp.pdl.cmu.edu/pub/datasets/twemcacheWorkload/cacheDatasets/wiki/wiki_2019u.oracleGeneral.zst
> ![graph](./graph/wiki_2019u[0.001,TEST].png)  
> **Trace Path**: wiki_2019u.oracleGeneral.zst  
> **Desc**: ['0.001', 'TEST', {}]  
> **Cache Size**: 8016  
> **Total Request**: 2,655,612,611  
> **Best Model**: logistic_regression_v2_All => 0.6071  
> **Better Than Base**: True  
> ![graph](./graph/wiki_2019u[0.001,ignore_obj_size,TEST].png)  
> **Trace Path**: wiki_2019u.oracleGeneral.zst  
> **Desc**: ['0.001', 'ignore_obj_size', 'TEST', {}]  
> **Cache Size**: 49619  
> **Total Request**: 2,655,612,611  
> **Best Model**: LR_1_All,LR_v5_spec => 0.728852  
> **Better Than Base**: False  
> ![graph](./graph/wiki_2019u[0.01,TEST].png)  
> **Trace Path**: wiki_2019u.oracleGeneral.zst  
> **Desc**: ['0.01', 'TEST', {}]  
> **Cache Size**: 80166  
> **Total Request**: 2,655,612,611  
> **Best Model**: logistic_regression_v2_All => 0.290395  
> **Better Than Base**: True  
> ![graph](./graph/wiki_2019u[0.01,ignore_obj_size,TEST].png)  
> **Trace Path**: wiki_2019u.oracleGeneral.zst  
> **Desc**: ['0.01', 'ignore_obj_size', 'TEST', {}]  
> **Cache Size**: 496199  
> **Total Request**: 2,655,612,611  
> **Best Model**: LR_1_All,logistic_regression_v4_spec => 0.458307  
> **Better Than Base**: False  
> ![graph](./graph/wiki_2019u[0.1,TEST].png)  
> **Trace Path**: wiki_2019u.oracleGeneral.zst  
> **Desc**: ['0.1', 'TEST', {}]  
> **Cache Size**: 801664  
> **Total Request**: 2,655,612,611  
> **Best Model**: logistic_regression_v2_All => 0.0668907  
> **Better Than Base**: False  
> ![graph](./graph/wiki_2019u[0.1,ignore_obj_size,TEST].png)  
> **Trace Path**: wiki_2019u.oracleGeneral.zst  
> **Desc**: ['0.1', 'ignore_obj_size', 'TEST', {}]  
> **Cache Size**: 4961999  
> **Total Request**: 2,655,612,611  
> **Best Model**: logistic_regression_v2_All => 0.117294  
> **Better Than Base**: False  
> ![graph](./graph/wiki_2019u[0.2,TEST].png)  
> **Trace Path**: wiki_2019u.oracleGeneral.zst  
> **Desc**: ['0.2', 'TEST', {}]  
> **Cache Size**: 1603329  
> **Total Request**: 2,655,612,611  
> **Best Model**: logistic_regression_v2_spec => 0.0386781  
> **Better Than Base**: False  
> ![graph](./graph/wiki_2019u[0.2,ignore_obj_size,TEST].png)  
> **Trace Path**: wiki_2019u.oracleGeneral.zst  
> **Desc**: ['0.2', 'ignore_obj_size', 'TEST', {}]  
> **Cache Size**: 9923998  
> **Total Request**: 2,655,612,611  
> **Best Model**: logistic_regression_v2_All => 0.0595329  
> **Better Than Base**: False  
> ![graph](./graph/wiki_2019u[0.4,TEST].png)  
> **Trace Path**: wiki_2019u.oracleGeneral.zst  
> **Desc**: ['0.4', 'TEST', {}]  
> **Cache Size**: 3206658  
> **Total Request**: 2,655,612,611  
> **Best Model**: logistic_regression_v3_spec => 0.0239131  
> **Better Than Base**: True  
> ![graph](./graph/wiki_2019u[0.4,ignore_obj_size,TEST].png)  
> **Trace Path**: wiki_2019u.oracleGeneral.zst  
> **Desc**: ['0.4', 'ignore_obj_size', 'TEST', {}]  
> **Cache Size**: 19847996  
> **Total Request**: 2,655,612,611  
> **Best Model**: logistic_regression_v2_spec,logistic_regression_v2_All => 0.0295192  
> **Better Than Base**: False  
## zipf_0.3 
> ![graph](./graph/zipf_0.3[0.001,TEST].png)  
> **Trace Path**: zipf_0.3.oracleGeneral  
> **Desc**: ['0.001', 'TEST', {}]  
> **Cache Size**: 3  
> **Total Request**: 100,000,000  
> **Best Model**: LR_1_mean_All => 0.998778  
> **Better Than Base**: True  
> ![graph](./graph/zipf_0.3[0.001,ignore_obj_size,TEST].png)  
> **Trace Path**: zipf_0.3.oracleGeneral  
> **Desc**: ['0.001', 'ignore_obj_size', 'TEST', {}]  
> **Cache Size**: 1000  
> **Total Request**: 100,000,000  
> **Best Model**: LR_1_mean_All => 0.998778  
> **Better Than Base**: True  
> ![graph](./graph/zipf_0.3[0.01,TEST].png)  
> **Trace Path**: zipf_0.3.oracleGeneral  
> **Desc**: ['0.01', 'TEST', {}]  
> **Cache Size**: 38  
> **Total Request**: 100,000,000  
> **Best Model**: LR_1_mean_All => 0.987792  
> **Better Than Base**: True  
> ![graph](./graph/zipf_0.3[0.01,ignore_obj_size,TEST].png)  
> **Trace Path**: zipf_0.3.oracleGeneral  
> **Desc**: ['0.01', 'ignore_obj_size', 'TEST', {}]  
> **Cache Size**: 10000  
> **Total Request**: 100,000,000  
> **Best Model**: LR_1_mean_All => 0.9878  
> **Better Than Base**: True  
> ![graph](./graph/zipf_0.3[0.1,TEST].png)  
> **Trace Path**: zipf_0.3.oracleGeneral  
> **Desc**: ['0.1', 'TEST', {}]  
> **Cache Size**: 381  
> **Total Request**: 100,000,000  
> **Best Model**: LR_1_mean_All => 0.879949  
> **Better Than Base**: True  
> ![graph](./graph/zipf_0.3[0.1,ignore_obj_size,TEST].png)  
> **Trace Path**: zipf_0.3.oracleGeneral  
> **Desc**: ['0.1', 'ignore_obj_size', 'TEST', {}]  
> **Cache Size**: 100001  
> **Total Request**: 100,000,000  
> **Best Model**: LR_1_mean_All => 0.880255  
> **Better Than Base**: True  
> ![graph](./graph/zipf_0.3[0.2,TEST].png)  
> **Trace Path**: zipf_0.3.oracleGeneral  
> **Desc**: ['0.2', 'TEST', {}]  
> **Cache Size**: 762  
> **Total Request**: 100,000,000  
> **Best Model**: LR_1_mean_All => 0.765574  
> **Better Than Base**: True  
> ![graph](./graph/zipf_0.3[0.2,ignore_obj_size,TEST].png)  
> **Trace Path**: zipf_0.3.oracleGeneral  
> **Desc**: ['0.2', 'ignore_obj_size', 'TEST', {}]  
> **Cache Size**: 200002  
> **Total Request**: 100,000,000  
> **Best Model**: LR_1_mean_All => 0.766415  
> **Better Than Base**: True  
> ![graph](./graph/zipf_0.3[0.4,TEST].png)  
> **Trace Path**: zipf_0.3.oracleGeneral  
> **Desc**: ['0.4', 'TEST', {}]  
> **Cache Size**: 1525  
> **Total Request**: 100,000,000  
> **Best Model**: LR_1_mean_All => 0.552575  
> **Better Than Base**: True  
> ![graph](./graph/zipf_0.3[0.4,ignore_obj_size,TEST].png)  
> **Trace Path**: zipf_0.3.oracleGeneral  
> **Desc**: ['0.4', 'ignore_obj_size', 'TEST', {}]  
> **Cache Size**: 400004  
> **Total Request**: 100,000,000  
> **Best Model**: LR_1_mean_All => 0.553504  
> **Better Than Base**: True  
## zipf_0.7 
> ![graph](./graph/zipf_0.7[0.001,TEST].png)  
> **Trace Path**: zipf_0.7.oracleGeneral  
> **Desc**: ['0.001', 'TEST', {}]  
> **Cache Size**: 3  
> **Total Request**: 100,000,000  
> **Best Model**: LR_1_spec,LR_1_mean_spec => 0.961411  
> **Better Than Base**: False  
> ![graph](./graph/zipf_0.7[0.001,ignore_obj_size,TEST].png)  
> **Trace Path**: zipf_0.7.oracleGeneral  
> **Desc**: ['0.001', 'ignore_obj_size', 'TEST', {}]  
> **Cache Size**: 1000  
> **Total Request**: 100,000,000  
> **Best Model**: LR_1_spec => 0.961405  
> **Better Than Base**: True  
> ![graph](./graph/zipf_0.7[0.01,TEST].png)  
> **Trace Path**: zipf_0.7.oracleGeneral  
> **Desc**: ['0.01', 'TEST', {}]  
> **Cache Size**: 38  
> **Total Request**: 100,000,000  
> **Best Model**: LR_1_spec,LR_1_All,LR_1_mean_spec => 0.872851  
> **Better Than Base**: False  
> ![graph](./graph/zipf_0.7[0.01,ignore_obj_size,TEST].png)  
> **Trace Path**: zipf_0.7.oracleGeneral  
> **Desc**: ['0.01', 'ignore_obj_size', 'TEST', {}]  
> **Cache Size**: 10000  
> **Total Request**: 100,000,000  
> **Best Model**: LR_1_spec,LR_1_All,LR_1_mean_spec => 0.872851  
> **Better Than Base**: False  
> ![graph](./graph/zipf_0.7[0.1,TEST].png)  
> **Trace Path**: zipf_0.7.oracleGeneral  
> **Desc**: ['0.1', 'TEST', {}]  
> **Cache Size**: 381  
> **Total Request**: 100,000,000  
> **Best Model**: LR_1_spec,LR_1_All,LR_1_log_spec,LR_1_mean_spec => 0.632252  
> **Better Than Base**: False  
> ![graph](./graph/zipf_0.7[0.1,ignore_obj_size,TEST].png)  
> **Trace Path**: zipf_0.7.oracleGeneral  
> **Desc**: ['0.1', 'ignore_obj_size', 'TEST', {}]  
> **Cache Size**: 100001  
> **Total Request**: 100,000,000  
> **Best Model**: LR_1_spec,LR_1_All,LR_1_mean_spec => 0.632252  
> **Better Than Base**: False  
> ![graph](./graph/zipf_0.7[0.2,TEST].png)  
> **Trace Path**: zipf_0.7.oracleGeneral  
> **Desc**: ['0.2', 'TEST', {}]  
> **Cache Size**: 762  
> **Total Request**: 100,000,000  
> **Best Model**: LR_1_spec,LR_1_All,LR_1_log_spec,LR_1_mean_spec => 0.499366  
> **Better Than Base**: False  
> ![graph](./graph/zipf_0.7[0.2,ignore_obj_size,TEST].png)  
> **Trace Path**: zipf_0.7.oracleGeneral  
> **Desc**: ['0.2', 'ignore_obj_size', 'TEST', {}]  
> **Cache Size**: 200002  
> **Total Request**: 100,000,000  
> **Best Model**: LR_1_spec,LR_1_All,LR_1_log_spec,LR_1_mean_spec => 0.499366  
> **Better Than Base**: False  
> ![graph](./graph/zipf_0.7[0.4,TEST].png)  
> **Trace Path**: zipf_0.7.oracleGeneral  
> **Desc**: ['0.4', 'TEST', {}]  
> **Cache Size**: 1525  
> **Total Request**: 100,000,000  
> **Best Model**: LR_1_spec,LR_1_All,LR_1_log_spec,LR_1_mean_spec => 0.321945  
> **Better Than Base**: False  
> ![graph](./graph/zipf_0.7[0.4,ignore_obj_size,TEST].png)  
> **Trace Path**: zipf_0.7.oracleGeneral  
> **Desc**: ['0.4', 'ignore_obj_size', 'TEST', {}]  
> **Cache Size**: 400004  
> **Total Request**: 100,000,000  
> **Best Model**: LR_1_spec,LR_1_All,LR_1_log_spec,LR_1_mean_spec => 0.321945  
> **Better Than Base**: False  
## zipf_0 
> ![graph](./graph/zipf_0[0.001,TEST].png)  
> **Trace Path**: zipf_0.oracleGeneral  
> **Desc**: ['0.001', 'TEST', {}]  
> **Cache Size**: 3  
> **Total Request**: 100,000,000  
> **Best Model**: LR_1_spec,LR_1_All,LR_1_log_spec,LR_1_log_All,LR_1_mean_spec,LR_1_mean_All => 0.998997  
> **Better Than Base**: False  
> ![graph](./graph/zipf_0[0.001,ignore_obj_size,TEST].png)  
> **Trace Path**: zipf_0.oracleGeneral  
> **Desc**: ['0.001', 'ignore_obj_size', 'TEST', {}]  
> **Cache Size**: 1000  
> **Total Request**: 100,000,000  
> **Best Model**: LR_1_spec,LR_1_All,LR_1_log_spec,LR_1_log_All,LR_1_mean_spec,LR_1_mean_All => 0.998997  
> **Better Than Base**: False  
> ![graph](./graph/zipf_0[0.01,TEST].png)  
> **Trace Path**: zipf_0.oracleGeneral  
> **Desc**: ['0.01', 'TEST', {}]  
> **Cache Size**: 38  
> **Total Request**: 100,000,000  
> **Best Model**: LR_1_spec,LR_1_All,LR_1_log_spec,LR_1_mean_spec => 0.990002  
> **Better Than Base**: False  
> ![graph](./graph/zipf_0[0.01,ignore_obj_size,TEST].png)  
> **Trace Path**: zipf_0.oracleGeneral  
> **Desc**: ['0.01', 'ignore_obj_size', 'TEST', {}]  
> **Cache Size**: 10000  
> **Total Request**: 100,000,000  
> **Best Model**: LR_1_spec,LR_1_All,LR_1_log_spec,LR_1_mean_spec => 0.990002  
> **Better Than Base**: False  
> ![graph](./graph/zipf_0[0.1,TEST].png)  
> **Trace Path**: zipf_0.oracleGeneral  
> **Desc**: ['0.1', 'TEST', {}]  
> **Cache Size**: 381  
> **Total Request**: 100,000,000  
> **Best Model**: LR_1_log_All => 0.900073  
> **Better Than Base**: True  
> ![graph](./graph/zipf_0[0.1,ignore_obj_size,TEST].png)  
> **Trace Path**: zipf_0.oracleGeneral  
> **Desc**: ['0.1', 'ignore_obj_size', 'TEST', {}]  
> **Cache Size**: 100001  
> **Total Request**: 100,000,000  
> **Best Model**: LR_1_log_All => 0.90007  
> **Better Than Base**: True  
> ![graph](./graph/zipf_0[0.2,TEST].png)  
> **Trace Path**: zipf_0.oracleGeneral  
> **Desc**: ['0.2', 'TEST', {}]  
> **Cache Size**: 762  
> **Total Request**: 100,000,000  
> **Best Model**: LR_1_mean_spec => 0.800232  
> **Better Than Base**: True  
> ![graph](./graph/zipf_0[0.2,ignore_obj_size,TEST].png)  
> **Trace Path**: zipf_0.oracleGeneral  
> **Desc**: ['0.2', 'ignore_obj_size', 'TEST', {}]  
> **Cache Size**: 200002  
> **Total Request**: 100,000,000  
> **Best Model**: LR_1_mean_spec => 0.800232  
> **Better Than Base**: True  
> ![graph](./graph/zipf_0[0.4,TEST].png)  
> **Trace Path**: zipf_0.oracleGeneral  
> **Desc**: ['0.4', 'TEST', {}]  
> **Cache Size**: 1525  
> **Total Request**: 100,000,000  
> **Best Model**: LR_1_mean_spec => 0.600966  
> **Better Than Base**: True  
> ![graph](./graph/zipf_0[0.4,ignore_obj_size,TEST].png)  
> **Trace Path**: zipf_0.oracleGeneral  
> **Desc**: ['0.4', 'ignore_obj_size', 'TEST', {}]  
> **Cache Size**: 400004  
> **Total Request**: 100,000,000  
> **Best Model**: LR_1_spec,LR_1_All,LR_1_log_spec,LR_1_mean_spec => 0.600968  
> **Better Than Base**: False  
## zipf_1.3 
> ![graph](./graph/zipf_1.3[0.001,TEST].png)  
> **Trace Path**: zipf_1.3.oracleGeneral  
> **Desc**: ['0.001', 'TEST', {}]  
> **Cache Size**: 2  
> **Total Request**: 100,000,000  
> **Best Model**: LR_1_spec,LR_1_mean_spec => 0.145437  
> **Better Than Base**: False  
> ![graph](./graph/zipf_1.3[0.001,ignore_obj_size,TEST].png)  
> **Trace Path**: zipf_1.3.oracleGeneral  
> **Desc**: ['0.001', 'ignore_obj_size', 'TEST', {}]  
> **Cache Size**: 669  
> **Total Request**: 100,000,000  
> **Best Model**: LR_1_spec => 0.145431  
> **Better Than Base**: True  
> ![graph](./graph/zipf_1.3[0.01,TEST].png)  
> **Trace Path**: zipf_1.3.oracleGeneral  
> **Desc**: ['0.01', 'TEST', {}]  
> **Cache Size**: 25  
> **Total Request**: 100,000,000  
> **Best Model**: LR_1_spec,LR_1_All => 0.0645036  
> **Better Than Base**: False  
> ![graph](./graph/zipf_1.3[0.01,ignore_obj_size,TEST].png)  
> **Trace Path**: zipf_1.3.oracleGeneral  
> **Desc**: ['0.01', 'ignore_obj_size', 'TEST', {}]  
> **Cache Size**: 6695  
> **Total Request**: 100,000,000  
> **Best Model**: LR_1_spec,LR_1_All => 0.0645036  
> **Better Than Base**: False  
> ![graph](./graph/zipf_1.3[0.1,TEST].png)  
> **Trace Path**: zipf_1.3.oracleGeneral  
> **Desc**: ['0.1', 'TEST', {}]  
> **Cache Size**: 255  
> **Total Request**: 100,000,000  
> **Best Model**: LR_1_All => 0.0239022  
> **Better Than Base**: False  
> ![graph](./graph/zipf_1.3[0.1,ignore_obj_size,TEST].png)  
> **Trace Path**: zipf_1.3.oracleGeneral  
> **Desc**: ['0.1', 'ignore_obj_size', 'TEST', {}]  
> **Cache Size**: 66952  
> **Total Request**: 100,000,000  
> **Best Model**: LR_1_All => 0.0239022  
> **Better Than Base**: False  
> ![graph](./graph/zipf_1.3[0.2,TEST].png)  
> **Trace Path**: zipf_1.3.oracleGeneral  
> **Desc**: ['0.2', 'TEST', {}]  
> **Cache Size**: 510  
> **Total Request**: 100,000,000  
> **Best Model**: LR_1_All => 0.0163646  
> **Better Than Base**: False  
> ![graph](./graph/zipf_1.3[0.2,ignore_obj_size,TEST].png)  
> **Trace Path**: zipf_1.3.oracleGeneral  
> **Desc**: ['0.2', 'ignore_obj_size', 'TEST', {}]  
> **Cache Size**: 133905  
> **Total Request**: 100,000,000  
> **Best Model**: LR_1_All => 0.0163646  
> **Better Than Base**: False  
> ![graph](./graph/zipf_1.3[0.4,TEST].png)  
> **Trace Path**: zipf_1.3.oracleGeneral  
> **Desc**: ['0.4', 'TEST', {}]  
> **Cache Size**: 1021  
> **Total Request**: 100,000,000  
> **Best Model**: LR_1_mean_spec => 0.0105821  
> **Better Than Base**: False  
> ![graph](./graph/zipf_1.3[0.4,ignore_obj_size,TEST].png)  
> **Trace Path**: zipf_1.3.oracleGeneral  
> **Desc**: ['0.4', 'ignore_obj_size', 'TEST', {}]  
> **Cache Size**: 267810  
> **Total Request**: 100,000,000  
> **Best Model**: LR_1_mean_spec => 0.010594  
> **Better Than Base**: False  
## zipf_1.7 
> ![graph](./graph/zipf_1.7[0.001,TEST].png)  
> **Trace Path**: zipf_1.7.oracleGeneral  
> **Desc**: ['0.001', 'TEST', {}]  
> **Cache Size**: 0  
> **Total Request**: 100,000,000  
> **Best Model**: LR_1_mean_spec => 0.0520027  
> **Better Than Base**: True  
> ![graph](./graph/zipf_1.7[0.001,ignore_obj_size,TEST].png)  
> **Trace Path**: zipf_1.7.oracleGeneral  
> **Desc**: ['0.001', 'ignore_obj_size', 'TEST', {}]  
> **Cache Size**: 68  
> **Total Request**: 100,000,000  
> **Best Model**: LR_1_spec => 0.0519973  
> **Better Than Base**: True  
> ![graph](./graph/zipf_1.7[0.01,TEST].png)  
> **Trace Path**: zipf_1.7.oracleGeneral  
> **Desc**: ['0.01', 'TEST', {}]  
> **Cache Size**: 2  
> **Total Request**: 100,000,000  
> **Best Model**: LR_1_spec,LR_1_All,LR_1_mean_spec => 0.0103631  
> **Better Than Base**: False  
> ![graph](./graph/zipf_1.7[0.01,ignore_obj_size,TEST].png)  
> **Trace Path**: zipf_1.7.oracleGeneral  
> **Desc**: ['0.01', 'ignore_obj_size', 'TEST', {}]  
> **Cache Size**: 680  
> **Total Request**: 100,000,000  
> **Best Model**: LR_1_spec,LR_1_All => 0.0103631  
> **Better Than Base**: False  
> ![graph](./graph/zipf_1.7[0.1,TEST].png)  
> **Trace Path**: zipf_1.7.oracleGeneral  
> **Desc**: ['0.1', 'TEST', {}]  
> **Cache Size**: 25  
> **Total Request**: 100,000,000  
> **Best Model**: LR_1_All => 0.00205443  
> **Better Than Base**: False  
> ![graph](./graph/zipf_1.7[0.1,ignore_obj_size,TEST].png)  
> **Trace Path**: zipf_1.7.oracleGeneral  
> **Desc**: ['0.1', 'ignore_obj_size', 'TEST', {}]  
> **Cache Size**: 6807  
> **Total Request**: 100,000,000  
> **Best Model**: LR_1_All => 0.00205443  
> **Better Than Base**: False  
> ![graph](./graph/zipf_1.7[0.2,TEST].png)  
> **Trace Path**: zipf_1.7.oracleGeneral  
> **Desc**: ['0.2', 'TEST', {}]  
> **Cache Size**: 51  
> **Total Request**: 100,000,000  
> **Best Model**: LR_1_All => 0.00128691  
> **Better Than Base**: False  
> ![graph](./graph/zipf_1.7[0.2,ignore_obj_size,TEST].png)  
> **Trace Path**: zipf_1.7.oracleGeneral  
> **Desc**: ['0.2', 'ignore_obj_size', 'TEST', {}]  
> **Cache Size**: 13615  
> **Total Request**: 100,000,000  
> **Best Model**: LR_1_All => 0.00128691  
> **Better Than Base**: False  
> ![graph](./graph/zipf_1.7[0.4,TEST].png)  
> **Trace Path**: zipf_1.7.oracleGeneral  
> **Desc**: ['0.4', 'TEST', {}]  
> **Cache Size**: 103  
> **Total Request**: 100,000,000  
> **Best Model**: LR_1_mean_spec => 0.00085977  
> **Better Than Base**: False  
> ![graph](./graph/zipf_1.7[0.4,ignore_obj_size,TEST].png)  
> **Trace Path**: zipf_1.7.oracleGeneral  
> **Desc**: ['0.4', 'ignore_obj_size', 'TEST', {}]  
> **Cache Size**: 27231  
> **Total Request**: 100,000,000  
> **Best Model**: LR_1_All => 0.00087406  
> **Better Than Base**: False  
## zipf_1 
> ![graph](./graph/zipf_1[0.001,TEST].png)  
> **Trace Path**: zipf_1.oracleGeneral  
> **Desc**: ['0.001', 'TEST', {}]  
> **Cache Size**: 3  
> **Total Request**: 100,000,000  
> **Best Model**: LR_1_mean_spec => 0.586261  
> **Better Than Base**: True  
> ![graph](./graph/zipf_1[0.001,ignore_obj_size,TEST].png)  
> **Trace Path**: zipf_1.oracleGeneral  
> **Desc**: ['0.001', 'ignore_obj_size', 'TEST', {}]  
> **Cache Size**: 999  
> **Total Request**: 100,000,000  
> **Best Model**: LR_1_spec => 0.586254  
> **Better Than Base**: True  
> ![graph](./graph/zipf_1[0.01,TEST].png)  
> **Trace Path**: zipf_1.oracleGeneral  
> **Desc**: ['0.01', 'TEST', {}]  
> **Cache Size**: 38  
> **Total Request**: 100,000,000  
> **Best Model**: LR_1_spec,LR_1_All,LR_1_mean_spec => 0.405233  
> **Better Than Base**: False  
> ![graph](./graph/zipf_1[0.01,ignore_obj_size,TEST].png)  
> **Trace Path**: zipf_1.oracleGeneral  
> **Desc**: ['0.01', 'ignore_obj_size', 'TEST', {}]  
> **Cache Size**: 9999  
> **Total Request**: 100,000,000  
> **Best Model**: LR_1_spec,LR_1_All => 0.405233  
> **Better Than Base**: False  
> ![graph](./graph/zipf_1[0.1,TEST].png)  
> **Trace Path**: zipf_1.oracleGeneral  
> **Desc**: ['0.1', 'TEST', {}]  
> **Cache Size**: 381  
> **Total Request**: 100,000,000  
> **Best Model**: LR_1_spec,LR_1_All,LR_1_mean_spec => 0.213886  
> **Better Than Base**: False  
> ![graph](./graph/zipf_1[0.1,ignore_obj_size,TEST].png)  
> **Trace Path**: zipf_1.oracleGeneral  
> **Desc**: ['0.1', 'ignore_obj_size', 'TEST', {}]  
> **Cache Size**: 99994  
> **Total Request**: 100,000,000  
> **Best Model**: LR_1_spec,LR_1_All,LR_1_mean_spec => 0.213886  
> **Better Than Base**: False  
> ![graph](./graph/zipf_1[0.2,TEST].png)  
> **Trace Path**: zipf_1.oracleGeneral  
> **Desc**: ['0.2', 'TEST', {}]  
> **Cache Size**: 762  
> **Total Request**: 100,000,000  
> **Best Model**: LR_1_spec,LR_1_All,LR_1_log_spec,LR_1_mean_spec => 0.152787  
> **Better Than Base**: False  
> ![graph](./graph/zipf_1[0.2,ignore_obj_size,TEST].png)  
> **Trace Path**: zipf_1.oracleGeneral  
> **Desc**: ['0.2', 'ignore_obj_size', 'TEST', {}]  
> **Cache Size**: 199988  
> **Total Request**: 100,000,000  
> **Best Model**: LR_1_spec,LR_1_All,LR_1_log_spec,LR_1_mean_spec => 0.152787  
> **Better Than Base**: False  
> ![graph](./graph/zipf_1[0.4,TEST].png)  
> **Trace Path**: zipf_1.oracleGeneral  
> **Desc**: ['0.4', 'TEST', {}]  
> **Cache Size**: 1525  
> **Total Request**: 100,000,000  
> **Best Model**: LR_1_All,LR_1_log_spec,LR_1_mean_spec => 0.0897345  
> **Better Than Base**: False  
> ![graph](./graph/zipf_1[0.4,ignore_obj_size,TEST].png)  
> **Trace Path**: zipf_1.oracleGeneral  
> **Desc**: ['0.4', 'ignore_obj_size', 'TEST', {}]  
> **Cache Size**: 399977  
> **Total Request**: 100,000,000  
> **Best Model**: LR_1_All,LR_1_log_spec,LR_1_mean_spec => 0.0897345  
> **Better Than Base**: False  
## zipf_2 
> ![graph](./graph/zipf_2[0.001,TEST].png)  
> **Trace Path**: zipf_2.oracleGeneral  
> **Desc**: ['0.001', 'TEST', {}]  
> **Cache Size**: 0  
> **Total Request**: 100,000,000  
> **Best Model**: LR_1_mean_spec => 0.0677591  
> **Better Than Base**: True  
> ![graph](./graph/zipf_2[0.001,ignore_obj_size,TEST].png)  
> **Trace Path**: zipf_2.oracleGeneral  
> **Desc**: ['0.001', 'ignore_obj_size', 'TEST', {}]  
> **Cache Size**: 13  
> **Total Request**: 100,000,000  
> **Best Model**: LR_1_spec => 0.0677552  
> **Better Than Base**: True  
> ![graph](./graph/zipf_2[0.01,TEST].png)  
> **Trace Path**: zipf_2.oracleGeneral  
> **Desc**: ['0.01', 'TEST', {}]  
> **Cache Size**: 0  
> **Total Request**: 100,000,000  
> **Best Model**: LR_1_spec,LR_1_All,LR_1_mean_spec => 0.00656036  
> **Better Than Base**: False  
> ![graph](./graph/zipf_2[0.01,ignore_obj_size,TEST].png)  
> **Trace Path**: zipf_2.oracleGeneral  
> **Desc**: ['0.01', 'ignore_obj_size', 'TEST', {}]  
> **Cache Size**: 137  
> **Total Request**: 100,000,000  
> **Best Model**: LR_1_spec,LR_1_All => 0.00656036  
> **Better Than Base**: False  
> ![graph](./graph/zipf_2[0.1,TEST].png)  
> **Trace Path**: zipf_2.oracleGeneral  
> **Desc**: ['0.1', 'TEST', {}]  
> **Cache Size**: 5  
> **Total Request**: 100,000,000  
> **Best Model**: LR_1_All,LR_1_mean_spec => 0.00065771  
> **Better Than Base**: False  
> ![graph](./graph/zipf_2[0.1,ignore_obj_size,TEST].png)  
> **Trace Path**: zipf_2.oracleGeneral  
> **Desc**: ['0.1', 'ignore_obj_size', 'TEST', {}]  
> **Cache Size**: 1379  
> **Total Request**: 100,000,000  
> **Best Model**: LR_1_All => 0.00065771  
> **Better Than Base**: False  
> ![graph](./graph/zipf_2[0.2,TEST].png)  
> **Trace Path**: zipf_2.oracleGeneral  
> **Desc**: ['0.2', 'TEST', {}]  
> **Cache Size**: 10  
> **Total Request**: 100,000,000  
> **Best Model**: LR_1_All => 0.00034185  
> **Better Than Base**: False  
> ![graph](./graph/zipf_2[0.2,ignore_obj_size,TEST].png)  
> **Trace Path**: zipf_2.oracleGeneral  
> **Desc**: ['0.2', 'ignore_obj_size', 'TEST', {}]  
> **Cache Size**: 2758  
> **Total Request**: 100,000,000  
> **Best Model**: LR_1_All => 0.00034185  
> **Better Than Base**: False  
> ![graph](./graph/zipf_2[0.4,TEST].png)  
> **Trace Path**: zipf_2.oracleGeneral  
> **Desc**: ['0.4', 'TEST', {}]  
> **Cache Size**: 21  
> **Total Request**: 100,000,000  
> **Best Model**: LR_1_mean_spec => 0.00019375  
> **Better Than Base**: False  
> ![graph](./graph/zipf_2[0.4,ignore_obj_size,TEST].png)  
> **Trace Path**: zipf_2.oracleGeneral  
> **Desc**: ['0.4', 'ignore_obj_size', 'TEST', {}]  
> **Cache Size**: 5517  
> **Total Request**: 100,000,000  
> **Best Model**: LR_1_mean_spec => 0.00019568  
> **Better Than Base**: False  
