import requests
import json

API_KEY = "RUN8puBkDXJDkQxg8HPtXbspGEiVxNic"
url = "https://financialmodelingprep.com/stable/insider-trading/latest"
params = {
    "page": 0,
    "limit": 50,
    "apikey": API_KEY
}

response = requests.get(url, params=params)
print(response.json())

with open('insider_trades.json', 'w', encoding='utf-8') as f:
    json.dump(
        response.json(), 
        f, 
        ensure_ascii=False,   # 保留 Unicode 字元而不轉成 \uXXXX
        indent=4              # 縮排 4 個空格，方便閱讀
    )
  
print("已把資料寫入 insider_trades.json")