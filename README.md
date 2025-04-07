# <AIGO_ee303>
2025永豐AI GO競賽：股神對決 -- 專題生\
**永豐AIGO的競賽連結**
> https://tbrain.trendmicro.com.tw/Competitions/Details/38\


| 日期       | Sun    | Mon              | Tue              | Wed           | Thu         | Fri         | Sat         |
|------------|--------|------------------|------------------|---------------|-------------|-------------|-------------|
| 3/23~3/29  |        |                  |                  | ~~隊伍問題~~      | 資料分析    | 資料分析    | 資料分析    |
| 3/30~4/5   | 模型架構 | 模型架構         | 模型架構         | 模型架構圖    | coding      | coding      | coding      |
| 4/6~4/12   | coding | training pipeline<br>loss | training pipeline<br>loss | 訓練&微調    | 訓練&微調   | 訓練&微調   | 訓練&微調   |
| 4/13~4/14  | 訓練&微調 | 訓練&微調       |                  |               |             |             |             |



## 請先建立環境 (這裡面安裝的套件就不會和其他環境衝突)
```bash
conda create --name aigo python==3.10
```

### 每次要跑這個專案，就要先開環境，才會跑得動
```bash
conda activate aigo
```


### 然後git clone 這個專案
```bash
git clone https://github.com/KaiCobra/AIGO_ee303.git
```


# <進度條>
### 3/26~3/29任務
 - 請先幫我使用pandas套件分析資料集的資料型態
 - 週六做一份簡報，解釋一下這份資料，確保不會有太怪的數字

※ 你如果要安裝pandas，請記得先開你的環境，然後跑
```bash
pip install pandas
```

> TIPS:\
> 下載好之後，新建資料夾(dataset)，接著解壓縮放到 dataset 資料夾。\
> 然後就可以分析了