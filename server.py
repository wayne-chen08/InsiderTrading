from http.server import HTTPServer, SimpleHTTPRequestHandler
import json

class Handler(SimpleHTTPRequestHandler):
    def do_GET(self):
        if self.path == '/data':
            # 讀取 JSON 資料
            with open('insider_trades.json', 'r', encoding='utf-8') as f:
                data = json.load(f)
            
            # 設定回應標頭
            self.send_response(200)
            self.send_header('Content-type', 'application/json')
            self.send_header('Access-Control-Allow-Origin', '*')
            self.end_headers()
            
            # 傳送 JSON 資料
            self.wfile.write(json.dumps(data).encode())
        else:
            # 處理其他一般的 HTTP 請求
            try:
                super().do_GET()
            except Exception as e:
                self.send_error(404, f"File not found: {self.path}")
# 啟動伺服器
PORT = 8080
# 設定目前目錄為伺服器根目錄
import os
os.chdir(os.path.dirname(os.path.abspath(__file__)))
print(f"啟動伺服器在 http://localhost:{PORT}")
print("請在瀏覽器中開啟上述網址")
print("按 Ctrl+C 可以關閉伺服器")

HTTPServer(("", PORT), Handler).serve_forever()
