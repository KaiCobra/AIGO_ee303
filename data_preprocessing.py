import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler

import os
import sys
import psutil  # 新增記憶體監控

def print_memory_usage():
    """即時打印記憶體使用情況"""
    process = psutil.Process(os.getpid())
    print(f"當前記憶體使用：{process.memory_info().rss / 1024**3:.2f} GB", flush=True)

def main():
    try:
        print("=== 大型檔案分塊處理開始 ===", flush=True)
        
        # 設定分塊大小（根據記憶體調整，例如每塊 100,000 行）
        chunksize = 100000
        data_path = "Datasets/training.csv"
        
        # 初始化 StandardScaler 和數據容器
        scaler = StandardScaler()
        processed_X = []
        processed_y = []
        
        # 第一次循環：擬合 scaler（僅統計均值和方差）
        print("=== 第一階段：擬合標準化參數 ===", flush=True)
        for i, chunk in enumerate(pd.read_csv(data_path, chunksize=chunksize)):
            print(f"擬合第 {i+1} 塊...", flush=True)
            chunk = chunk.dropna()  # 刪除缺失值（或改用填充）
            X_chunk = chunk.drop(columns=["ID", "飆股"]).astype('float32')  # 指定數據類型
            scaler.partial_fit(X_chunk)  # 增量計算均值和方差
            print_memory_usage()
        
        # 第二次循環：轉換數據
        print("\n=== 第二階段：標準化數據 ===", flush=True)
        for i, chunk in enumerate(pd.read_csv(data_path, chunksize=chunksize)):
            print(f"處理第 {i+1} 塊...", flush=True)
            chunk = chunk.dropna()
            X_chunk = chunk.drop(columns=["ID", "飆股"]).astype('float32')
            y_chunk = chunk["飆股"].astype('int8')  # 節省記憶體
            
            # 標準化並收集數據
            X_scaled = scaler.transform(X_chunk)
            processed_X.append(X_scaled)
            processed_y.append(y_chunk)
            
            # 釋放記憶體（關鍵！）
            del X_chunk, y_chunk, X_scaled
            print_memory_usage()
        
        # 合併所有塊（若後續需要完整數據）
        X_full = np.concatenate(processed_X)
        y_full = pd.concat(processed_y)
        
        print("\n=== 最終數據形狀 ===", flush=True)
        print(f"X: {X_full.shape}", flush=True)
        print(f"y: {y_full.shape}", flush=True)
        print("=== 處理完成 ===", flush=True)
        
    except Exception as e:
        print(f"發生錯誤：{e}", flush=True)
        sys.exit(1)

if __name__ == "__main__":
    main()