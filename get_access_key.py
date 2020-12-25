import requests
import hashlib
import json
import time

appkey = "4409e2ce8ffd12b8"
appsec = "59b43e04ad6965f34319062b478f83dd"

auth_code = ""
QRcodeURL = ""


def CalcSign(appkey, appsec, body):
    bodys = f"{body}{appsec}"
    sign = hashlib.md5(bodys.encode(encoding="utf-8")).hexdigest()
    #body_result = f"appkey={appkey}&{body}&sign={sign}"
    body_result = f"{body}&sign={sign}"
    return body_result


def getQRcodeURLandAuth_code():
    url = "http://passport.bilibili.com/x/passport-tv-login/qrcode/auth_code"
    ts = int(time.time())
    body = f"local_id=0&ts={ts}"
    body_result = CalcSign(appkey, appsec, body)
    url = url + "?" + body_result
    res = json.loads(requests.post(url).text)
    global QRcodeURL, auth_code
    QRcodeURL = res["data"]["url"]
    auth_code = res["data"]["auth_code"]
    print("------ QRcodeURL BEGIN ------")
    print(QRcodeURL)
    print("------ QRcodeURL END ------")
    print("[auth_code]", auth_code)

def LoginQRcode():
    url = "http://passport.bilibili.com/x/passport-tv-login/qrcode/poll"
    ts = int(time.time())
    body = f"auth_code={auth_code}&local_id=0&ts={ts}"
    body_result = CalcSign(appkey, appsec, body)
    url = url + "?" + body_result
    res = json.loads(requests.post(url).text)
    if res["code"]==0:
        uid = res["data"]["mid"]
        access_key = res["data"]["access_token"]
        refresh_token = res["data"]["refresh_token"]
        print("[uid]", uid)
        print("[access_key]", access_key)
        print("[refresh_token]", refresh_token)
    else:
        print(res)

def main():
    getQRcodeURLandAuth_code()
    input("Are you scan finished?[Enter]")
    LoginQRcode()

def test():
    #url = "https://app.bilibili.com/x/playurl"
    url = "https://1735831202235667.cn-hongkong.fc.aliyuncs.com/2016-08-15/proxy/bililimit/removelimit/"
    ts = int(time.time())
    #body = f"aid=669904231&access_key=35f17e127a90ef4a3067df5a66b278c1&cid=243833780&device=android&fnval=0&fnver=0&mobi_app=android&npcybs=0&otype=json&platform=android&qn=80&ts={ts}"
    
    # 测试中 忧国的莫里亚蒂（限定） 第一集-魔改（失败）
    #body = f"access_key=3a4d835fac7cc6cc12b98325b53020c1&aid=627455788&appkey=iVGUTjsxvpLeuDCf&build=5370000&buvid=XY412F34F7C09E5D417D5BDACC727A3258263&cid=253193011&device=android&expire=1597289802&fnval=0&fnver=0&force_host=0&mid=688418886&mobi_app=android&npcybs=0&otype=json&platform=android&qn=80&ts={ts}"
    
    # 测试中 忧国的莫里亚蒂（限定） 第一集-类似改（失败）
    #body = "access_key=c336c3669686a5c264ed64e651c63c71&aid=627455788&appkey=iVGUTjsxvpLeuDCf&build=5370000&buvid=XXD9E43D7A1EBB6669597650E3EE417D9E7F5&cid=253193011&device=android&expire=1597289802&fnval=0&fnver=0&force_host=0&mid=688418886&mobi_app=android&npcybs=0&otype=json&platform=android&qn=112&ts=1594974158"
    # 测试中 在魔王城说晚安（限定） 第十一集-类似改（失败）有可能是body不对
    #body = "access_key=c336c3669686a5c264ed64e651c63c71&aid=330714489&appkey=iVGUTjsxvpLeuDCf&build=5370000&buvid=XXD9E43D7A1EBB6669597650E3EE417D9E7F5&cid=266547816&device=android&expire=1597289802&fnval=0&fnver=0&force_host=0&mid=688418886&mobi_app=android&npcybs=0&otype=json&platform=android&qn=112&ts=1594974158"
    #res = {'code': -404, 'message': '啥都木有', 'ttl': 1, 'data': None}(有可能是国家不对)

    # succeed 原始
    #body = "access_key=c336c3669686a5c264ed64e651c63c71&aid=99999999&appkey=iVGUTjsxvpLeuDCf&build=5370000&buvid=XXD9E43D7A1EBB6669597650E3EE417D9E7F5&cid=171776208&device=android&expire=1597289802&fnval=0&fnver=0&force_host=0&mid=174438027&mobi_app=android&npcybs=0&otype=json&platform=android&qn=112&ts=1594974158"
    
    # succeed oneroom第三季第一集(国内)
    #body = "access_key=c336c3669686a5c264ed64e651c63c71&aid=884840446&appkey=iVGUTjsxvpLeuDCf&build=5370000&buvid=XXD9E43D7A1EBB6669597650E3EE417D9E7F5&cid=244951054&device=android&expire=1597289802&fnval=0&fnver=0&force_host=0&mid=928123&mobi_app=android&npcybs=0&otype=json&platform=android&qn=112&ts=1594974158"
    #res = {'code': -404, 'message': '啥都木有', 'ttl': 1, 'data': None} (国外网址)
    #res = {xxx}（国内网址，可以正常解析）

    # 出租女友（香港可以） av456273732  md: 28229298
    #body = "access_key=c336c3669686a5c264ed64e651c63c71&aid=456273732&appkey=iVGUTjsxvpLeuDCf&build=5370000&buvid=XXD9E43D7A1EBB6669597650E3EE417D9E7F5&cid=222747655&device=android&expire=1597289802&fnval=0&fnver=0&force_host=0&mid=11783021&mobi_app=android&npcybs=0&otype=json&platform=android&qn=112&ts=1594974158"
    # 香港ali实验成功！！！！

    body_result = CalcSign("iVGUTjsxvpLeuDCf", "aHRmhWMLkdeMuILqORnYZocwMBpMEOdt", body)
    url = url + "?" + body_result
    res = json.loads(requests.get(url).text)
    print(url)
    print(res)

if __name__ == '__main__':
    main()
    test()


'''

{'code': 0, 'message': '0', 'ttl': 1, 'data': {'mid': 498766638, 'access_token': '3fcfe9399476d65b1b5ec7c771b15ac1', 'refresh_token': '1b585317b88cd15f99696a96600db2c1', 'expires_in': 2592000}}

[uid] 498766638
[access_key] 35f17e127a90ef4a3067df5a66b278c1
[refresh_token] 88dde9fe38ec42ef34d2150f38b305c1


'''