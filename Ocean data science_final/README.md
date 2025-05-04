### Project Title
---
Identifying abnormal sea states and
grouping similar sea states by clustering  
~ Application to hazard maps ~

### Files
---
- downloading_ERA5_data.py
    - CDSAPIを使用してERA5データをダウンロードするスクリプト
- preprocessing_ERA5_data.mlx
    - 波浪と風に関するERA5データを1つのcsvとして出力するスクリプト
- preprocessing_data.py
    - 波浪と風のデータに対して事故データでラベリングするスクリプト
- tsunami_REN.ipynb
    - クラスタリング及び主成分分析を行うスクリプト
- mapping_test_data.mlx
    - テストデータを使用してハザードマップを作成するスクリプト