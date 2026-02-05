import csv
import os

EMPLOYEE_CSV = os.path.join(os.path.dirname(__file__), 'employees.csv')


def add_employee():
    emp_id = input('従業員ID: ')
    name = input('名前: ')
    dept = input('部署: ')
    with open(EMPLOYEE_CSV, 'a', newline='', encoding='utf-8') as f:
        writer = csv.writer(f)
        writer.writerow([emp_id, name, dept])
    print('従業員を追加しました。')


def list_employees():
    if not os.path.exists(EMPLOYEE_CSV):
        print('従業員データがありません。')
        return
    with open(EMPLOYEE_CSV, 'r', encoding='utf-8') as f:
        reader = csv.reader(f)
        print('ID\t名前\t部署')
        for row in reader:
            print('\t'.join(row))


def main():
    while True:
        print('\n1: 従業員追加  2: 一覧表示  9: 終了')
        cmd = input('番号を選択: ')
        if cmd == '1':
            add_employee()
        elif cmd == '2':
            list_employees()
        elif cmd == '9':
            print('終了します')
            break
        else:
            print('無効な入力です')


if __name__ == '__main__':
    main()
