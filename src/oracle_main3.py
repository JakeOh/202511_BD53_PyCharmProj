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
    print('[0]종료 [1]테이블 생성 [2]테이블 삭제 [3]전체검색')
    menu = input_integer('메뉴 선택>> ')
    return menu


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
            print('TODO 전체 검색')
        else:
            print('메뉴 번호는 0~3까지 정수만 가능합니다.')

    print('===== 프로그램 종료 =====')


if __name__ == '__main__':
    main()
