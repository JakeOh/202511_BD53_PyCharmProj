import src.oracleutil as orautil


def input_integer(msg):
    while True:
        try:
            number = int(input(msg))
            return number
        except ValueError:
            print('입력값은 정수여야 합니다.')


def show_main_menu():
    print()
    print('[0]종료 [1]테이블 생성 [2]테이블 삭제 [3]전체검색 [4]부서번호 검색 [5]부서이름 검색')
    menu = input_integer('메뉴 선택>> ')
    return menu


def search_by_dept_no():
    dept_no = input_integer('부서번호 입력>> ')
    orautil.select_by_deptno(dept_no)


def search_by_dept_name():
    dept_name = input('부서이름 입력>> ')
    orautil.select_by_dname(dept_name)


def main():
    run = True
    while run:
        menu = show_main_menu()
        if menu == 0:
            run = False
        elif menu == 1:
            orautil.create_table()  # dept_ex 테이블 생성
        elif menu == 2:
            orautil.drop_table()  # dept_ex 테이블 삭제
        elif menu == 3:
            orautil.select_all()  # dept_ex 테이블의 전체 레코드를 검색
        elif menu == 4:
            search_by_dept_no()
        elif menu == 5:
            search_by_dept_name()
        else:
            print('메뉴 번호는 0~5까지 정수만 가능합니다.')

    print('===== 프로그램 종료 =====')


if __name__ == '__main__':
    main()
