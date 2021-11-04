sku = 'sku'
price = 'price'
commit = 'cc'
url = 'dasd'
sql = f"insert into product()value('{sku}', '{price}', '{commit}', '{url}')"
sql = "insert into product()value(" + sku + ',' + price + ',' + commit + ',' + url + ",)";
print(sql)
