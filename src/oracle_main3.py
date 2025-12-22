import src.oracleutil as orautil


if __name__ == '__main__':
    conn = orautil.get_connection()
    orautil.close_connection(conn)
    