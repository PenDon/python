from selenium import webdriver
import time
import requests
import execjs

s = ["GET", "https://www.douyin.com/aweme/v1/web/user/profile/other/?device_platform=webapp&aid=6383&channel=channel_pc_web&publish_video_strategy_type=2&source=channel_pc_web&sec_user_id=MS4wLjABAAAAvOU5GclmETa4jehXAEspnMfYJQZAbwcJzfUFhZk4cP8&version_code=160100&version_name=16.1.0&cookie_enabled=true&screen_width=1920&screen_height=1080&browser_language=zh-CN&browser_platform=Win32&browser_name=Mozilla&browser_version=5.0+(Windows+NT+10.0%3B+Win64%3B+x64)+AppleWebKit%2F537.36+(KHTML,+like+Gecko)+Chrome%2F92.0.4515.107+Safari%2F537.36&browser_online=true"]


# with open('signature.js', 'r') as f:
#     ctx = execjs.compile(f.read())
#     print(ctx.call("glb._$jsvmprt", s))

headers = {

    'user-agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.107 Safari/537.36",
    "withcredentials": "true"
}


res = requests.get("https://www.douyin.com/aweme/v1/web/user/profile/other/?device_platform=webapp&aid=6383&channel=channel_pc_web&publish_video_strategy_type=2&source=channel_pc_web&sec_user_id=MS4wLjABAAAAuiQPSt1dmEFPGlYPgRWG032GF7F1-8LV4pWbPKtOFdI&version_code=160100&version_name=16.1.0&cookie_enabled=true&screen_width=1920&screen_height=1080&browser_language=zh-CN&browser_platform=Win32&browser_name=Mozilla&browser_version=5.0+(Windows+NT+10.0%3B+Win64%3B+x64)+AppleWebKit%2F537.36+(KHTML,+like+Gecko)+Chrome%2F92.0.4515.107+Safari%2F537.36&browser_online=true" + "&_signature=" + "Asdasdasdasdada", headers=headers)


if res.status_code == 200:
    print("Yes")
else :
    print(res.status_code)


print(res.text)
