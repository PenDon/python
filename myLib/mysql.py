import pymysql

class Mysql:
    """
    pymysql数据库操作
    """
    type = "mysql"
    host = "localhost"
    port = 3306
    user = "root"
    pwd = "root"
    dbName = "dbname"  # change this to your database name
    charset = "utf8"
    cursor = ""
    sql = ""
    debug = False

    def __init__(self, dbName, debug=False):
        # 调试时创建类附加 debug = True
        self.dbName = dbName
        connect = pymysql.connect(host=self.host, port=self.port, user=self.user, passwd=self.pwd, db=self.dbName,
                                  charset=self.charset)
        self.debug = debug
        self.cursor = connect.cursor()

    def execute_sql(self, sql: str):
        self.sql = sql
        if self.debug:
            return self.sql
        self.cursor.execute(self.sql)
        return self.cursor.fetchall()

    def select(self, selections: "list", table_name: "str", conditions=None):
        """
        封装数据库查询语句
        :rtype: str
        :type table_name: str 表名
        :type selections: list 选中列 example: ["id","title"]
        :param conditions: 查询条件 example: ["id>1","title like test"]
        :return:
        """
        select = ','.join([self.quote_fields(s) for s in selections])
        self.sql = f"SELECT {select} FROM {self.quote_fields(table_name)}"
        if conditions:
            condition = ' AND '.join(conditions)
            self.sql += f" WHERE {condition}"
            # @todo: parse conditions with quote_fields and quote_values
        try:
            if not self.debug:
                self.cursor.execute(self.sql)
                return self.cursor.fetchall()
        except Exception as e:
            print(e)
            self.get_sql()
            return False

        # 调试阶段，返回sql
        return self.sql

    def insert(self, table_name: "str", values: "list", columns=None):
        """
        封装数据库插入语句，列表形式
        :param columns: 列名
        :type values: list 值
        :type table_name: str 表名
        :return:
        """
        self.sql = f"INSERT INTO {self.quote_fields(table_name)}"
        values = [self.quote_values(value) for value in values]
        if columns:
            self.sql += '(' + ",".join(columns) + ')' + ' VALUES (' + ','.join(values) + ');'
        else:
            self.sql += ' VALUES (' + ','.join(values) + ');'
        try:
            if not self.debug:
                self.cursor.execute(self.sql)
                return True
        except Exception as e:
            print(e)
            self.get_sql()
            return False
        return self.sql

    def batch_insert(self, table_name, values, columns=None):
        """
        批量插入数据
        考虑键值对字典插入
        :param table_name:
        :param values:
        :param columns:
        :return:
        """
        self.sql = f"INSERT INTO {self.quote_fields(table_name)}"
        if columns:
            self.sql += ' (' + ','.join(columns) + ')' + ' VALUES '
        else:
            self.sql += ' VALUES'
        join_array = []
        for value in values:
            value = [self.quote_values(v) for v in value]
            join_array.append('(' + ','.join(value) + ')')
        self.sql += ' ' + ','.join(join_array)
        if self.debug:
            # 调试返回sql
            return self.sql

        return self.cursor.execute(self.sql)

    def update(self, table_name: "str", column: "str", conditions: "dict"):
        # @todo update table set column = value where conditions
        pass

    def delete(self):
        # @todo delete from table where conditions
        pass

    def get_sql(self):
        """
        打印sql语句
        :return:
        """
        print("Your SQL:" + self.sql)

    def close(self):
        self.cursor.close()

    @staticmethod
    def quote_fields(table_name):
        """
        :return `{tableName}`
        :param table_name:str
        """
        return '`' + table_name + '`'

    @staticmethod
    def quote_values(value):
        """
        :return '{value}'
        :param value:str
        """
        return "'" + str(value) + "'"
