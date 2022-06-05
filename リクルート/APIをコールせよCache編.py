import sys
import requests
import json

def main(argv):

    # 引数が2つでない場合はエラー
    if len(argv) != 2:
        print('error!')
        sys.exit(1)
    # 2番目の引数が数字でなければエラー
    elif not argv[1].isdigit():
        print('error!')
        sys.exit(1)

    base_url = 'http://challenge-server.code-check.io/api/recursive/ask'
    # 引数を代入
    seed = argv[0]
    n = int(argv[1])

    def f(n):
        if n == 0:
            return 1
        elif n == 2:
            return 2
        elif n % 2 == 0:
            return f(n - 1) + f(n - 2) + f(n - 3) + f(n - 4)
        else:
            # seedとnをパラメータに指定してAPIコール
            params = {'seed': seed, 'n': n}
            r = requests.get(base_url, params=params)

            # レスポンスをJSON形式に変換
            data = json.loads(r.text)

            # レスポンスから結果を取得
            return data['result']

    # 出力
    print(f(n))


if __name__ == '__main__':
    main(sys.argv[1:])
