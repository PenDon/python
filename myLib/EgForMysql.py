"""
Mysql库 查询/插入操作示例

"""

from myLib.mysql import Mysql

mysql = Mysql(debug=True)

# select
print(mysql.select(['id', 'column1', 'column2'], 'table_name'))

# Result:
# SELECT `id`,`column1`,`column2` FROM `table_name`

# insert
print(mysql.insert('table_name', ['value1', 'value2', 'value3']))

# Result:
# INSERT INTO `table_name` VALUES ('value1','value2','value3')

# batch_insert
print(mysql.batch_insert('table_name', [['value1-1', 'value1-2', 'value1-3'], ['value2-1', 'value2-2', 'value2-3']]))

# Result:
# INSERT INTO `table_name` VALUES ('value1-1','value1-2','value1-3'),('value2-1','value2-2','value2-3')
