import csv
import os

ORGANIZATION_CSV = os.path.join(os.path.dirname(__file__), 'organizations.csv')


def add_organization():
    org_id = input('組織ID: ')
    org_name = input('組織名: ')
    parent_id = input('親組織ID (なければ空欄): ')
    with open(ORGANIZATION_CSV, 'a', newline='', encoding='utf-8') as f:
        writer = csv.writer(f)
        writer.writerow([org_id, org_name, parent_id])
    print('組織を追加しました。')


def list_organizations():
    if not os.path.exists(ORGANIZATION_CSV):
        print('組織データがありません。')
        return
    with open(ORGANIZATION_CSV, 'r', encoding='utf-8') as f:
        reader = csv.reader(f)
        print('組織ID\t組織名\t親組織ID')
        for row in reader:
            print('\t'.join(row))


def main():
    while True:
        print('\n1: 組織追加  2: 一覧表示  9: 終了')
        cmd = input('番号を選択: ')
        if cmd == '1':
            add_organization()
        elif cmd == '2':
            list_organizations()
        elif cmd == '9':
            print('終了します')
            break
        else:
            print('無効な入力です')


if __name__ == '__main__':
    main()
