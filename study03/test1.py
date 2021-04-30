import pymysql as pymysql
# 1. 连接数据库，
conn = pymysql.connect(
    host="localhost",  # 指示host表明是本地MySQL还是远程
    port=3306,
    user="root",  # 用户名
    password="mysql321",  # 密码
    db="study03",  # 要连接的数据库名
    charset="utf8mb4",  # 指定字符集，可以解决中文乱码
    cursorclass=pymysql.cursors.DictCursor  # 固定写法，类似于jdbc里边的加载驱动
)
# ****python, 必须有一个游标对象， 用来给数据库发送sql语句并执行.
# 2. 创建游标对象，
cur = conn.cursor()
# 3. 对于数据库进行增删改查

# 1). ************************创建数据表**********************************
print("**********创建表**********")
try:
    # 使用 execute() 方法执行 SQL，如果表存在则删除
    cur.execute("DROP TABLE IF EXISTS Student")
    create_sqli = "create table Student (id int, name varchar(30));"   # sql语句
    cur.execute(create_sqli)    # 执行sql语句
except Exception as e:
    print("创建数据表失败:", e)
else:
    print("创建数据表成功;")

## 2). *********************插入数据****************************
print("\n**********插入数据**********")
try:
    insert_sql = "insert into Student values(0, 'fjy');"
    cur.execute(insert_sql)
    sql = "select * from Student;"
except Exception as e:
    print("插入数据失败:", e)
else:
    # 如果是插入数据， 一定要提交数据， 不然数据库中找不到要插入的数据;
    conn.commit()
    print("插入数据成功;")
    cur.execute(sql)
    result = cur.fetchall()  # 默认不返回查询结果集， 返回数据记录数。
    print(result)

# 3). *********************插入多条数据****************************
try:
    info = [(i, "hi%s" %(i)) for i in range(1, 10)]

    # # *********************第一种方式********************
    # # %s必须手动添加一个字符串， 否则就是一个变量名， 会报错.
    # insert_sql = "insert into Student values(%d, '%s');"
    # for item in info:
    #     print('insert语句:', insert_sql %item)
    #     cur.execute(insert_sql %item)

     # *********************第二种方式********************
    insert_sql = "insert into Student values(%s, %s);"
    cur.executemany(insert_sql, info)
except Exception as e:
    print("插入多条数据失败:", e)
else:
    # 如果是插入数据， 一定要提交数据， 不然数据库中找不到要插入的数据;
    conn.commit()
    print("插入多条数据成功;")
    cur.execute(sql)
    result = cur.fetchall()  # 默认不返回查询结果集， 返回数据记录数。
    print(result)

# 4). **************************数据库查询*****************************
print("\n**********查询**********")
sql = "select * from Student;"
result = cur.execute(sql)  # 默认不返回查询结果集， 返回数据记录数。
print(result)
print(cur.fetchone())     # 1). 获取下一个查询结果集;
print(cur.fetchone())
print(cur.fetchone())
print(cur.fetchmany(4))   # 2). 获取制定个数个查询结果集；
info = cur.fetchall()     # 3). 获取所有的查询结果
print(info)
print(len(info))
print(cur.rowcount)       # 4). 返回执行sql语句影响的行数
#  5). **************************移动游标指针*****************************
print(cur.fetchmany(3))
print("正在移动指针到最开始......")
cur.scroll(0, 'absolute')
print(cur.fetchmany(3))
print("正在移动指针到倒数第2个......")
print(cur.fetchall())    # 移动到最后
cur.scroll(-2, mode='relative')
print(cur.fetchall())

# 6). **************************数据库删除*****************************
try:
   print("\n**********删除**********")
   delete_sql = "delete from Student where name='fjy';"
   result = cur.execute(delete_sql)  # 默认不返回查询结果集， 返回数据记录数。
   conn.commit()   # 数据库修改后，需要使用commit()语句提交，不提交，修改不会生效
   sql = "select * from Student;"
   cur.execute(sql)
   result = cur.fetchall()  # 默认不返回查询结果集， 返回数据记录数。
   print(result)
except Exception as e:
    print("删除失败:", e)
else:
    print("删除成功！！！")

# 7). **************************改*****************************
try:
    print("\n**********改**********")
    update_sql = "update Student set name = 'hello world 1' where id=1;"
    result = cur.execute(update_sql)  # 默认不返回查询结果集， 返回数据记录数。
    conn.commit()   # 数据库修改后，需要使用commit()语句提交，不提交，修改不会生效
    sql = "select * from Student;"
    cur.execute(sql)
    result = cur.fetchall()  # 默认不返回查询结果集， 返回数据记录数。
    print(result)
except Exception as e:
    print("update失败:", e)
else:
    print("update成功！！！")

# 4. 关闭游标
cur.close()
# 5. 关闭连接
conn.close()
