import pymysql

__host = 'localhost'
__user = 'root'
__password = 'csl92021164'
__db = 'agent_based_model'

###############################################################################
##############################         ########################################
############################## SQL Ser ########################################
##############################         ########################################
###############################################################################


def __Connect_mysql():
    mydb = pymysql.connect(
        host=__host,
        user=__user,
        password=__password,
        database=__db,

    )
    return mydb


def Sql_Execute_Many(sql, records):
    db = __Connect_mysql()
    with db:
        with db.cursor() as cursor:
            cursor.executemany(sql, records)
        db.commit()


def Sql_Execute(sql, records):
    db = __Connect_mysql()
    with db:
        with db.cursor() as cursor:
            cursor.execute(sql, records)
        db.commit()


def Sql_Fetch_All_Command(sql1, sql2):
    db = __Connect_mysql()
    with db:
        with db.cursor() as cursor:
            cursor.execute(sql1)
            cursor.execute(sql2)
            ra = cursor.fetchall()
        db.commit()
    return ra


def Sql_Execute_Command(sql):
    db = __Connect_mysql()
    with db:
        with db.cursor() as cursor:
            cursor.execute(sql)
        db.commit()


def Sql_Fetch_All(sql):
    db = __Connect_mysql()
    ra = ()
    with db:
        with db.cursor() as cursor:
            cursor.execute(sql)
            ra = cursor.fetchall()
        db.commit()
    return ra


def Sql_Fetch_Many(sql, iteration, num):
    db = __Connect_mysql()
    ra = ()
    with db:
        with db.cursor() as cursor:
            cursor.execute(sql)
            for _ in range(iteration):
                ra = ra + cursor.fetchmany(num)
        db.commit()
    return ra


# ###############################################################################
# ##############################   Aysn  ########################################
# ############################## SQL Ser ########################################
# ##############################         ########################################
# ###############################################################################
# import aiomysql
# import asyncio

# async def Async_Connect_mysql(MAX_SIZE:int):
#     pool = await aiomysql.create_pool(
#         host = __host,
#         user = __user,
#         password = __password,
#         db = __db,
#         minsize = 5,
#         maxsize = MAX_SIZE
#     )
#     return pool

# async def Async_Pool_Close(pool:aiomysql.create_pool):
#     pool.close()


# async def Async_Sql_Fetch_All_Command(pool:aiomysql.create_pool, sql1:str, sql2:str):
#     async with pool.acquire() as conn:
#         async with conn.cursor() as cursor:
#             await cursor.execute(sql1)
#             await cursor.execute(sql2)
#             ra = await cursor.fetchall()

#     return ra

# async def Async_Sql_Fetch_All(pool:aiomysql.create_pool, sql:str):
#     async with pool.acquire() as conn:
#         async with conn.cursor() as cursor:
#             await cursor.execute(sql)
#             ra = await cursor.fetchall()


#     return ra


# async def Async_Sql_Exectue_Many(pool:aiomysql.create_pool, sql:str, records:list):
#     async with pool.acquire() as conn:
#         async with conn.cursor() as cursor:
#             await cursor.executemany(sql, records)
#         await conn.commit()


if __name__ == "__main__":
    import cProfile
