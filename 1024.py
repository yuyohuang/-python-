import urllib.request
import csv

url = 'https://rate.bot.com.tw/xrt/flcsv/0/day' # 設定要抓取匯率資料的網址
webpage = urllib.request.urlopen(url)  #開啟網頁
data = csv.reader(webpage.read().decode('utf-8').splitlines()) #讀取資料到data陣列中

list_m = {'NTW': 1.0}
for i in data:  #讀取串列的每個項目
    print('幣別:', i[0], '匯率:', i[12]) # 顯示幣別及其匯率
    list_m[i[0]] = i[12]   # 將幣別及其匯率存入字典 list_m

def Convert_currency(money, currency):
    return money * float(currency)

# main
while True:   # 進入無窮迴圈，直到選擇退出
    try:
        money = float(input("輸入金額: "))
    except ValueError:   #如果轉換失敗
        print('輸入無效，請輸入有效的數字。') #顯示錯誤訊息
        continue

    currency_t = input("輸入幣別: ")  #輸入轉換的幣別
    
    if currency_t not in list_m:  # 檢查輸入的幣別是否存在於字典中
        print(f"無效的幣別。可用的幣別: {', '.join(list_m.keys())}") #顯示可用的幣別
        continue #重新循環
    
    converted_amount = Convert_currency(money, list_m[currency_t])
    print(f"轉換結果: {converted_amount:.1f}")  # 輸出轉換結果，保留1位小數
    print()

    exit_prompt = input("要退出嗎？(y/n): ") #詢問是否要退出程序
    if exit_prompt.lower() == 'y':      #如果輸入"y"
        break      #表示退出
