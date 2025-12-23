# DML(Data Manipulation Language): insert, update, delete
from oracledb import DatabaseError

from src.oracleutil.connect import get_connection


def insert_dept(dept_no, dept_name, location):
    """dept_ex 테이블에 새로운 행을 삽입."""
    with get_connection() as conn:
        with conn.cursor() as cursor:
            try:
                sql = 'insert into dept_ex values (:dept_no, :dept_name, :location)'

                # 가변길이 키워드 아규먼트 방식으로 아규먼트들을 전달.
                # cursor.execute(sql, dept_no=dept_no, dept_name=dept_name, location=location)

                # positional argument 방식으로 아규먼트들을 전달.
                cursor.execute(sql, {
                    'dept_no': dept_no,
                    'dept_name': dept_name,
                    'location': location
                })
                conn.commit()
                print('1개 행 삽입 성공')
            except DatabaseError as e:
                print(e)


if __name__ == '__main__':
    insert_dept(12, 'Dev', 'Busan')
