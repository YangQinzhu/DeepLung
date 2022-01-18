# Detection 
 This is a refine version of DeepLung repo with dependecies:
 * python 3.7
 * pytorch 1.10
 
 Reference: 
 > https://github.com/wentaozhu/DeepLung.git
 
 > https://github.com/uci-cbcl/DeepLung.git
 
 ## Preprare data
 1. Download the luna16 data and put all them in folder `luna16`
 2. change `path` variable in file `config_training.py` and `config_training9.py` to your data folder. (change `f` variable in `run_training.sh` to choose another config file)
 3. run `prepare.py` to preproess all data.

## Start running detection
1. use the cmd
```
sh run_training.sh 
```
## Done
- [x] torch version problem
- [x] data path
- [x] numpy version problem (1.21.5 with problem of np.asarray(metrics))

# Classification 
- [x]  fix the error loading file with xlrd  : /data/yangqinzhu/ctLung/DeepLung-master/nodcls/data/list3.2.csv

## PrepareData
1. change `.dcm` file name, such as `1-001.dcm` to `0000001.dcm`
2. run `./nodcls/data/extclsshpinfo.py`
3. run `/data/yangqinzhu/ctLung/DeepLung-master/nodcls/data/dataconverter.py` to get file `annotationdetclsconv_v3.csv`
4. run `/data/yangqinzhu/ctLung/DeepLung-master/nodcls/data/nodclsgbt.py` to generate folder `/luna16/cls/crop_v3/`
5. run `main_nodcls.py`

___you can change the path as you need, I have listed them it front of the function in each python file___