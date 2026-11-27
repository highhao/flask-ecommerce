import hashlib
import hmac
import urllib.parse
from copy import deepcopy
from flask import current_app

# 主要函數: 檢查碼排序
def generate_check_mac(order_data):

    # 1. 排序參數
    sorted_params = sort_params(order_data)
    # print('1')
    # print(sorted_params)
    # 2. 加入 HashKey 和 HashIV
    hashed_params = add_hash_key_and_iv(sorted_params)
    # print('2')
    # print(hashed_params)
    # 3. 進行 URL 編碼
    url_encoded_params = url_encode_params(hashed_params)
    # print('3')
    # print(url_encoded_params)

    # 4.符號編碼表 (反向)
    decoded_string  = dotnet_url_decode(url_encoded_params)
    # print('4')
    # print(decoded_string)

    # 5. 轉為小寫
    lowercased_params = decoded_string.lower()
    # print('5')
    # print(lowercased_params)
    # 6. 使用 SHA256 加密
    check_mac_value = calculate_sha256(lowercased_params)
    # print('6')
    # print(check_mac_value)
    # 7. 轉為大寫
    check_mac_value = check_mac_value.upper()
    # print('7')
    # print(check_mac_value)
    # 在這裡可以驗證 CheckMacValue 是否正確，然後進行其他邏輯處理
    return check_mac_value

# 輔助函數: 驗證 CheckMacValue
def verify_check_mac(received_data):
    # 從 received_data 中取得 CheckMacValue
    received_check_mac = received_data.get('CheckMacValue', '')

    # 使用深層拷貝創建 del_received_check_mac，以避免修改原始數據
    del_received_check_mac = deepcopy(received_data)
    del_received_check_mac.pop("CheckMacValue", None)

    # 使用 generate_check_mac 函數計算出期望的 CheckMacValue
    expected_check_mac = generate_check_mac(del_received_check_mac)

    # 檢查計算出的 CheckMacValue 與接收到的 CheckMacValue 是否相符
    return hmac.compare_digest(expected_check_mac, received_check_mac)

# 輔助函數: 將參數排序
def sort_params(params):
    # 將參數按照字母順序排序
    sorted_params = sorted(params.items())
    return '&'.join(['{}={}'.format(key, value) for key, value in sorted_params])

# 輔助函數: 加入 HashKey 和 HashIV
def add_hash_key_and_iv(params):
    # 加入 HashKey 和 HashIV
    hash_key = current_app.config['EC_PAY_HASH_KEY']  # 替換成你的 HashKey
    hash_iv = current_app.config['EC_PAY_HASH_IV']  # 替換成你的 HashIV
    return 'HashKey={}&{}&HashIV={}'.format(hash_key, params, hash_iv)

# 輔助函數: 將字串進行 URL 編碼
def url_encode_params(params):
    # 進行 URL 編碼
    return urllib.parse.quote(params)

def dotnet_url_decode(encoded_value):
    replacements = {
        '%2d': '-', '%5f': '_', '%2e': '.', '%21': '!',
        '%2a': '*', '%28': '(', '%29': ')','%20':'+','/':'%2f'
    }

    # 將編碼根據反向編碼表替換
    decoded_value = encoded_value
    for pattern, replacement in replacements.items():
        decoded_value = decoded_value.replace(pattern, replacement)

    return decoded_value

# 輔助函數: 計算 SHA256 雜湊值
def calculate_sha256(data):
    # 使用 SHA256 加密方式生成雜湊值
    sha256 = hashlib.sha256()
    sha256.update(data.encode('utf-8'))
    return sha256.hexdigest()
