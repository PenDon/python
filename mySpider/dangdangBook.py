import requests
from lxml import etree

host_url = 'http://product.dangdang.com/'

headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) '
                  'Chrome/74.0.3729.157 Safari/537.36',
    # 'referer': "https://mall.jd.com/",
    'cookie': "dest_area=country_id%3D9000%26province_id%3D111%26city_id%20%3D0%26district_id%3D0%26town_id%3D0; "
              "__permanent_id=20210630113401784224149622058826451; ddscreen=2; "
              "secret_key=a063b967bf123c4ad743e1f96f11b787; permanent_key=20210702114816251735522770cd3a06; "
              "bind_custid=0; bind_union_id=UID_FC31B8A1649260A49A8F9DBCA90923F0; tx_nickname=tq3F9A==; "
              "tx_open_id=60D1B9E50AFAF8DB0E43AD50B73A4B49; "
              "tx_figureurl=http://thirdqq.qlogo.cn/g?b=oidb&k=EHkBoAsubZ6NSUjc6DaSrw&s=640&t=1624676442; "
              "bind_cust_third_id=2088722363771435; __out_refer=1625197865%7C!%7Cmemberexprod.alipay.com%7C!%7C; "
              "__visit_id=20210702115104780262511297954190284; bind_mobile=13122995191; "
              "USERNUM=sXHEKSMToOPu3ITs/dde2A==; "
              "order_follow_source=-%7C-O-123%7C%2311%7C%23login_third_alipay%7C%230%7C%23; LOGIN_TIME=1625197914764; "
              "login_dang_code=20210702115214484662595314c85784; "
              "smidV2=202107021152202560196e8f3ad592dd5cf3a5c7ffee6000ece4153c2bbdbc0; "
              "alipay_request_from=https://login.dangdang.com/signin.aspx?returnurl=http%253A%252F%252Fproduct"
              ".dangdang.com%252F1845873646.html; "
              "login.dangdang.com=.AYH=2021070211564607463499140&.ASPXAUTH=4IdqF0IyqzqONpS11PaeNaqfYZcv7mYi/xP+wtuM1"
              "+DA9Y/DJRdXvA==; dangdang.com=email=MTMxMjI5OTUxOTE2ODc1MkBkZG1vYmlscGhvbmVfX3VzZXIuY29t&nickname"
              "=&display_id=2597870520233&customerid=AJM1yKz/rIbacLiBOgTD/g==&viptype=fUmmOrKWDFY=&show_name=131%2A"
              "%2A%2A%2A5191; ddoy=email=1312299519168752%40ddmobilphone__user.com&nickname=&agree_date=1"
              "&validatedflag=0&uname=13122995191&utype=1&.ALFG=on&.ALTM=1625198218; "
              "sessionID=pc_db63310968656192e599ea6d1d78f15d770bbf7ddd93595781cab71de982a04c; "
              "__dd_token_id=20210702115658922862604118e56e9b; MDD_username=131****5191; "
              "MDD_custId=UwxjotA+0GW+ljj41ualmQ%3D%3D; MDD_channelId=70000; MDD_fromPlatform=307; "
              "__rpm=%7Cmix_317715...1625198243079; __trace_id=20210702115736020337435270162115378; "
              "pos_6_start=1625198256046; pos_6_end=1625198256252",
}


res = requests.get(host_url, headers=headers).text

print(res)
