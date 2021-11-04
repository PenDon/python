import requests

res = requests.post('https://www.hongkongdisneyland.com/zh-cn/tickets-api/promotion/ws', json={"parameters": [
    {"type": '', "parameter": {"pk": "c96af76f-5c7f-4006-bb6d-171ce7940eb7", "uri": "online-merchandise-gm"}}],
    "payloadId": "562363c3-4761-42df-bbbe-0c4155f8c231", "nameId": '',
    "serviceName": "storefront.ThemeParkTicket", "method": "getPage"})
print(res.status_code)
print(res.content)

json = {"parameters": [
    {"type": '', "parameter": {"pk": "c96af76f-5c7f-4006-bb6d-171ce7940eb7", "uri": "online-merchandise-gm"}}],
        "payloadId": "4009bfa9-5c1f-656d-8f56-cc84ae847471", "nameId": '', "serviceName": "storefront.ThemeParkTicket",
        "method": "getPage"}
