
import pandas as pd
import sqlite3
import os
import time
import gc
import logging
logging.basicConfig(level=logging.INFO,
                    filename='logs.log',
                    format='%(asctime)s - %(levelname)s - %(message)s',
                    filemode='a')
print("Ready ✓")






data_path="C:\\Vendor project\\Data"
def load_data_fast(data_path="C:\\Vendor project\\Data", db_path="data1.db"):
    
    # Direct SQLite — 10x faster than SQLAlchemy
    conn = sqlite3.connect(db_path)
    
    files = [f for f in os.listdir(data_path) if f.endswith(".csv")]
    print(f"Found {len(files)} CSV files\n")

    for file in files:
        full_path = os.path.join(data_path, file)
        table_name = file[:-5].replace(" ", "_")
        file_size = os.path.getsize(full_path) / (1024**2)  # MB
        print(f"📂 {file} ({file_size:.1f} MB)")

        start = time.time()
        first_chunk = True
        rows_loaded = 0

        try:
            for chunk in pd.read_excel(
                full_path,
                chunksize=5000,         # bigger chunks = faster
                low_memory=True,
                on_bad_lines='skip',
                encoding='utf-8',
                encoding_errors='replace'
            ):
                chunk.to_sql(
                    table_name,
                    conn,
                    if_exists='replace' if first_chunk else 'append',
                    index=False,
                    method='multi'      # batch insert = much faster
                )
                rows_loaded += len(chunk)
                first_chunk = False
                del chunk
                gc.collect()
                print(f"   {rows_loaded:,} rows...", end="\r")

            elapsed = time.time() - start
            print(f"   ✅ {rows_loaded:,} rows in {elapsed:.1f}s          ")

        except Exception as e:
            print(f"   ❌ Failed: {e}")

    conn.commit()
    conn.close()
    print("\n🎉 All files loaded!")

print("Function ready ✓")
load_data_fast(data_path="C:\\Vendor project\\Data", db_path="data1.db")