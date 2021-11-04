import requests
res = requests.get('https://api.ipify.org/', proxies={"http": "http://43.129.200.135:6969"})
print(res.text)
# import asyncio
#
# import aiohttp
#
# async def fun():
#     async with aiohttp.ClientSession() as session:
#         async with session.get('https://api.ipify.org/', proxy="http://localhost:11000") as response:
#             res = await response.text()
#             print(res)
#
# loop = asyncio.get_event_loop()
# loop.run_until_complete(fun())


