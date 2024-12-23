#!/usr/bin/python3
# -*- coding: utf-8 -*- 
import os, sys
import requests
import base64
import gzip
import json
import time

http_headers = {
    'xweb_xhr': '1',
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36 MicroMessenger/7.0.20.1781(0x6700143B) NetType/WIFI MiniProgramEnv/Windows WindowsWechat/WMPF WindowsWechat(0x63090c10)XWEB/8518',
    'Content-Type': 'application/x-www-form-urlencoded',
    'Accept-Language': '*',
    'Referer': 'https://servicewechat.com/wx1dcf48f85b0b793f/6/page-frame.html'
}

user_token = 'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJzdWIiOjM3ODEzMzIsImNobCI6Ind4Z2FtZSIsImRhdGUiOiIyMDI0LTEyLTIzIiwidGltZSI6MTczNDkzMTg4OC41MDg5NX0.6g4LsIdDpLPJ16OeRr0guqahAcdqfLt-1vfqxRraftE'
file_config = 'H4sIAAAAAAAAA8VZXXPauhb9K3f8TM%2Bwt%2FyZNwK05Z58DZA2nU6HcUEBnxibYxvS3Ez%2B%2B5W0Dayk6Zy2LycP0afXkpekZWnz6E1002TF8jwt0qWuvJNHL902Zb%2FMcz1vsrLwTqjjlTtd5enmv9vFUo%2BKfrreeCfdjlfp%2BbaqTafJQ9GsdJPNoXGjm7fZTvfL9aastavK6tOy2NaXO0tkyvOyuM2q9XXbvMqWq7dVujYleup4vcGsdzGYTd73xsPZoDftucEtLrZr74R9izbWazOy3sI93VRZmk%2Bz9Z5qsirvp5mMxbDUTdvv9PrTrN8bC1i%2FaLwTg1Wv0kq7gu1d6UO%2B3m501U%2FrlVSYYfXTata7nl7O%2Bmej%2Fp8Aw78Mc359Nh1dDb9DCn4JafL%2B8mp2fWUUGgKG%2BhEGvTqa3ng2%2FDC8mAJC%2FEuj6A0Gs%2FPLi%2BEnQKBfQnjb%2B3A5fl3a7m8A%2FUjcX8Myi7B%2FPR4PL%2FqfZg73t5GGN8NxfzQZ%2FjbA9Hp8Me2dng1%2FRuFXZtlAXJ31Pg3Hs9HF20sLUs%2FLSrbLssxldyyydF0Wki%2By%2Bd2F247ex5sNr97dBMW5Z%2FapTk0Hz%2BRq%2FU12mymrKCalzCZI5%2FNyaym98nxyfhPdvP%2B4u%2Fo2%2FGu9uhnefPzzTTLfPTS%2Bebop77Txl2Kb56Zgdm7dOPOgSPlJEPi%2BXYHpTsumbmuD0GzXvFxmxSB9KLbrr9ZLyHrRMqsbXb1eCxDUTfy427UOlT6sddHMzBtvW%2F2MM9UH09vowr7YP71GXs7TfPLqOO3oB3qXza2G999mH4f9973p7F3vfDhz%2FRQlZixEnh3N%2FO7Dnt7b%2FYf%2B6P5B%2Fox94m5CgeljJvC8N7o4eKF5z9qmgfjlrU6bbaVN1ecv5k2yhTY27l7s0bQap650MX%2BwD5B5%2FS6Zp7ruj7q%2BcRxXYO8kOfy1deqVOh%2FrDHqhvzVjPbffiUHaoNRhmNhllT44TZfZrR2Px0pGEJo2l2fIK8j7kA8gH0I%2BgnwM%2BeSYpy7kgZeAl4CXgJeAl4CXgJeAl4CXgZeBl4GXgZeBl4GXgZeBl4GXgVcBrwJeBbwKeBXwKuBVwKuAVwGvAl4feH3g9YHXB14feH3g9YHXB14feH3gDYA3AN4AeAPgDYA3AN4AeAPgDYA3AN4QeEPgDYE3BN4QeEPgDYE3BN4QeEPgjYA3At4IeCPgjYA3At4IeCPgjYA3At4YeGPgjYE3Bt4YeGPgjYE3Bt4YeGPgTYA3Ad4EeBPgTYA3Ad4EeBPgTYA3OfIar4M8QZ4hryDvQz6AfAj5CPIx5IEX%2FIrArwj8isCvCPyKwK8I%2FIrArwj8isCvCPyKwK8I%2FIrArwj8isCvCPyKwK8I%2FIrArwj8isCvCPyKwK8I%2FIrArwj8isCvCPyKwK8I%2FIrArwj8isCvCPyKwK8I%2FIrArwj8isCvCPyKwK8I%2FIrArwj8isCvCPyKwK8I%2FIrArwj8isCvCPyKwK8I%2FIrArwj8isCvCPyKwK8I%2FIrArwj8isCvCPyKwK8I%2FIrArwj8isCvCPyKwK8I%2FIrArwj8isCvCPyKwK8I%2FIrArwj8isCvCPyKwK8I%2FIrArwj8isCvCPyKxK%2Be3Lm8ar6aU%2BC5uRdX7qTH7Unv0dsW5px6Zw%2BHHBorizouiSVJXMJdSUgSlkRJ4ktPaSNpI2kjaeNAklASYWBhYGFQwqAERQmKEhQlKEpQlKAoQVGCogTFFxRfUHxB8QXFFxRfUHxB8QXFFxRfUAJBCQQlEJRAfbGH2fu9TqZshOX2aPxcRRYVWVRkUZFFRRYVWVRkUZFFRRYVWVRkUZFFRRb5WORjkY9FPhb5WORjkY9FPhb5WORjkY9FPhb5WORjkY9FPhb5WORjkY9FPhb5WORjkY9FPhb5WORjkc8kghIISiAogaAEghIISiAooaCEghIyqu%2FKe%2FXVS%2FWVqK9EfSXqK1FfifpK1FeivhL1laivRH0l6itRX8kaVjIJSiZBySQomQQlk6BkEpRMgpJJUDIJSiZBySQomQQlk2CSBN%2FRlZ%2Fs1dxeIEfFbWnf092W2J62Ot691nemEIfm6mVu5s3K3KNIrsv%2FKwt9eXtba3OlesNx7C5zBspdL%2FeXxKrM9XMnyPVO5%2FbyFx7uY%2Bahv98dsrfpzjuJ%2Fa67JNsecrG1TbpYTHRt76jtNVOmxN3t5nmarc8EvGuLZbOyt1Eme%2BdysGU1WrhA2fO7aibvbamrTNvoA9krY6NN7jbNa%2F1sD%2F4b42ccP%2F32%2BNW%2FNX6F41e%2FM%2F75thqbpeTmz02FXPrf7kGDjltqNeK4NS6d5fUlocO4x2VpQxifzV7qqEOtXvT3Y%2F%2FcLh6XsCSq086IS6SSpVJJpZJKZSFbGa4yPXeD8wTqOK2C%2BbzML9r5Rbt60a4O7XYrz1epC3LkWW3Sz48uPOZN%2Bp40jaQ0s0GfrFi4ENpTp%2B3VO8VevdMZv9br7OYGu5nirPtav8HkE%2FYzxef9vtjQeJHVxlQ%2B2yF1PVOT3qfVQhbGQufWih7tW%2BlvuppntTOTrv23S%2FOt3seBDEsbdmzcYn1jI1L0c934Z7qZfumiD0Es0%2BM83RzCWewW%2FT44ZW2weRbzC%2Fip3QL9PLM75tFLy2Z7tnPPrbd5k9m820emfR9Q1WtdLfeURw91w5ORCo1Z%2FmbnFY3bUc%2Fs6ue6qp%2Fo6taWXc5ZsXTjtxPl1rQ7t9oYnj2z%2Br75AClbCN37uAMrR6H1G3dg9WNzJ3O9E%2BlgT6sqilQY2YJ5QRWYD7thqw2b84usMANKrQpxOzd%2B%2B6tKG2ZdtEorc1x3kzVN67tB2qQuztykS20rbKExaX1YRHaZcmC3se3VbGuZgkPEOqtHRSYk%2B5VquzuK0967%2FWfOxtfTqmiFWbS8cPB1X52tXb3czrBR2i6pI5%2F92sKaURybM45E1KW%2FmSiCCTG25HeSDnXI%2Boz91axdQMfFtF%2FcLaFdlW6il1W53dhl7SKj03aNG3o7tSM7pxIU31SZcy0ppfO%2Ft5mTWspf02qZFYffB3z3udfrNCtO0zxvN1eAGlCrQfegQVc0sM%2BH2NPu%2FnRhQ7rWC4yUkeyvWJLEJTZaYBOSRLag9Uqb%2BJIEkoSSCAoLCguKEhQljyt5PJDn7D3WrAN3QFqVG5xcbkPIcgvaGwC3QVQ%2BxjnoGObgY8QALpd8vFvS8QppxSuL%2FMF9hdzV%2Bcsxju0WTGB6SLT7MCq0%2F8NAX3MNBxT8yCiet770hrbVcr27Hg2OZz3ZUWLuRwPGCn5Z4b%2BsCL%2FD%2BB71OxQr84ua5HnN09P%2FAQq7wtxrHgAA'

# json字符串压缩并URL编码 
def encrypt_data(jv_str):
    bytes_obj = gzip.compress(jv_str.encode('utf-8'))
    b64_data = base64.b64encode(bytes_obj)
    b64_str = b64_data.decode('utf-8').replace('+', '%2B').replace('/', '%2F')
    return b64_str

# 解码数据转成json字符串 
def decrypt_data(data):
    b64_data = data.replace('%2B', '+').replace('%2F', '/').encode('utf-8')
    b64_data = base64.b64decode(b64_data) 
    json_data = gzip.decompress(b64_data)
    json_str = json_data.decode('utf-8')
    return json_str

# 发送数据 
def post_file(file_data):
    post_url = 'https://goddess.gzqidong.cn/api/user/file'
    data = 'api_token=' + user_token
    data = data + '&file=' + file_data
    data = data + '&loginTime=' + str(int(time.time()))
    r = requests.post(post_url, data=data, headers=http_headers)
    print(r.text)

if __name__ == '__main__':
    en_str = file_config
    jv_str = decrypt_data(en_str)
    jv_data = json.loads(jv_str)
    if 'MAIN_DATA' in jv_data:
        jv_data['MAIN_DATA']['nums']['5'] = 1 
        # 货币量99.99亿 
        jv_data['MAIN_DATA']['currency']['100001'] = 9999999999
        # 不知道啥 
        jv_data['MAIN_DATA']['currency']['100002'] = 9999999999
        # 体力值99.99亿 
        jv_data['MAIN_DATA']['currency']['100003'] = 9999999999
        # 不知道啥 
        jv_data['MAIN_DATA']['currency']['100004'] = 9999999999
        # 背包内道具 
        jv_data['MAIN_DATA']['gift'] = {}
        for i in range(230001, 230200):
            jv_data['MAIN_DATA']['gift'][str(i)] = 60

        video_list1 = []
        # 1号女生, OL风, 心动时刻 (200001) 
        for i in range(261017, 261017+8):
            video_list1.append(i)
        # 约会 
        for i in range(261011, 261011+4):
            video_list1.append(i)
        # 照片 
        for i in range(261025, 261053+1):
            video_list1.append(i)
        # video_list1 += [261025, 261026, 261037, 261039, 261043, 261033, 261044, 261045, 261046, 261047, 261049, 261050, 261052, 261053]
        jv_data['MAIN_DATA']['heartbeatMemory']['200001'] = {}
        jv_data['MAIN_DATA']['heartbeatMemory']['200001']['unlocks'] = video_list1
        jv_data['MAIN_DATA']['heartbeatMemory']['200001']['news'] = [video_list1[-1]]

        video_list2 = []
        # 2号女生, 双马尾可爱风, 心动时刻 (200002) 
        for i in range(262017, 262017+8):
            video_list2.append(i)
        # 约会
        for i in range(262011, 262011+4):
            video_list2.append(i)
        # 照片 
        for i in range(262026, 262062+1):
            video_list2.append(i)
        jv_data['MAIN_DATA']['heartbeatMemory']['200002'] = {}
        jv_data['MAIN_DATA']['heartbeatMemory']['200002']['unlocks'] = video_list2
        jv_data['MAIN_DATA']['heartbeatMemory']['200002']['news'] = [video_list2[-1]]

        video_list3 = []
        # 3号, 瑜伽女, 心动时刻(200003) 
        for i in range(263017, 263017+8):
            video_list3.append(i)
        # 约会
        for i in range(263011, 263011+4):
            video_list3.append(i)
        # 照片 
        for i in range(263025, 263039+1):
            video_list3.append(i)
        jv_data['MAIN_DATA']['heartbeatMemory']['200003'] = {}
        jv_data['MAIN_DATA']['heartbeatMemory']['200003']['unlocks'] = video_list3
        jv_data['MAIN_DATA']['heartbeatMemory']['200003']['news'] = [video_list3[-1]]

    if 'GAME_DATA' in jv_data:
        jv_data['GAME_DATA']['role']['200001']['level'] = 106  # 好感度,不要超过106,程序会黑屏 
        jv_data['GAME_DATA']['role']['200001']['fav'] = 840000  # 好感值 
        jv_data['GAME_DATA']['role']['200001']['unlock'] = 1   # 解锁 
        jv_data['GAME_DATA']['role']['200001']['favorId'] = 2  # 住第2楼(不同人要住不同楼层，否则公寓里面会显示不出来) 
        jv_data['GAME_DATA']['role']['200001']['friend'] = 1 
        jv_data['GAME_DATA']['role']['200001']['dated'] = False
        jv_data['GAME_DATA']['role']['200002']['level'] = 106
        jv_data['GAME_DATA']['role']['200002']['fav'] = 840000
        jv_data['GAME_DATA']['role']['200002']['unlock'] = 1
        jv_data['GAME_DATA']['role']['200002']['favorId'] = 1  # 住第顶楼 
        jv_data['GAME_DATA']['role']['200002']['friend'] = 1
        jv_data['GAME_DATA']['role']['200002']['dated'] = False
        jv_data['GAME_DATA']['role']['200003']['level'] = 106
        jv_data['GAME_DATA']['role']['200003']['fav'] = 840000
        jv_data['GAME_DATA']['role']['200003']['unlock'] = 1
        jv_data['GAME_DATA']['role']['200003']['favorId'] = 3 # 住第1楼 
        jv_data['GAME_DATA']['role']['200003']['friend'] = 1
        jv_data['GAME_DATA']['role']['200003']['dated'] = False
        jv_data['GAME_DATA']['role']['unlockRooms'] = [1,2,3]
        jv_data['GAME_DATA']['role']['nextFavorId'] = 5
        jv_data['GAME_DATA']['role']['friends'] = [200002, 200003, 200001]
        # 衣柜换装 
        jv_data['GAME_DATA']['role']['unlockedClothes'] = [210011, 210012, 210013, 210021, 210022, 210023, 210031, 210032, 210033]
        jv_data['GAME_DATA']['role']['clothesPieces'] = {'210012': 210021, '210013': 210021, '210022': 210021, '210023': 210021, '210032': 210021, '210033': 210021}
        # 智力、体力、形象 
        jv_data['GAME_DATA']['exercise']['0']['value'] = 999999
        jv_data['GAME_DATA']['exercise']['1']['value'] = 999999
        jv_data['GAME_DATA']['exercise']['2']['value'] = 999999
        # 以下好像没什么用 
        jv_data['GAME_DATA']['favorClick']['emergency'] = {}
        jv_data['GAME_DATA']['favorClick']['emergency']['200001'] = {}
        jv_data['GAME_DATA']['favorClick']['emergency']['200001']['cnt'] = 9999
        jv_data['GAME_DATA']['favorClick']['emergency']['200001']['time'] = 5
        jv_data['GAME_DATA']['favorClick']['emergency']['200001']['events'] = []
        jv_data['GAME_DATA']['favorClick']['emergency']['200002'] = {}
        jv_data['GAME_DATA']['favorClick']['emergency']['200002']['cnt'] = 9999
        jv_data['GAME_DATA']['favorClick']['emergency']['200002']['time'] = 5
        jv_data['GAME_DATA']['favorClick']['emergency']['200002']['events'] = []
        jv_data['GAME_DATA']['favorClick']['emergency']['200003'] = {}
        jv_data['GAME_DATA']['favorClick']['emergency']['200003']['cnt'] = 9999
        jv_data['GAME_DATA']['favorClick']['emergency']['200003']['time'] = 5
        jv_data['GAME_DATA']['favorClick']['emergency']['200003']['events'] = []
    # 解锁所有车辆 
    if 'Earning' in jv_data:
        jv_data['Earning']['data']['1']['unlock'] = 5 # 解锁5辆车(默认有一辆车，编号0)  
        jv_data['Earning']['data']['1']['use'] = 0 # 使用第0辆 
        jv_data['Earning']['data']['1']['click'] = 8
        jv_data['Earning']['data']['1']['cnt'] = 80
        # 自动驾驶  
        jv_data['Earning']['data']['1']['freeClick'] = 2001
        jv_data['Earning']['data']['1']['autoLv'] = 99
        # 多重点击倍数  
        jv_data['Earning']['data']['1']['multiLv'] = 99
    # 好像也没用(聊天相关) 
    jv_data['chat']['data'] = {}
    jv_data['chat']['data']['200001'] = {}
    jv_data['chat']['data']['200001']['cnt'] = 9999
    jv_data['chat']['data']['200001']['day'] = 5
    jv_data['chat']['data']['200002'] = {}
    jv_data['chat']['data']['200002']['cnt'] = 9999
    jv_data['chat']['data']['200002']['day'] = 5
    jv_data['chat']['data']['200003'] = {}
    jv_data['chat']['data']['200003']['cnt'] = 9999
    jv_data['chat']['data']['200003']['day'] = 5
    ren_str = encrypt_data(json.dumps(jv_data))
    post_file(ren_str)