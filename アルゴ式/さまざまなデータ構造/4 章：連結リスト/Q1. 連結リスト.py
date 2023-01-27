# 連結リストの各ノード
class Node:
    def __init__(self, value=""):
        self.next = None  # 次がどのノードを指すか
        self.value = value  # ノードの値


# ノードの初期化
nil = Node()
nil.next = nil


# 連結リストの先頭に要素を追加
def insert(v):
    v.next = nil.next  # vの次を現在の先頭にする
    nil.next = v  # 先頭をvにする


# 入力
Q = int(input())
for query in range(Q):
    type, S = input().split()
    if type == "0":
        # ノードを作成する
        v = Node(S)
        insert(v)
    else:
        # 先頭からk個(=S)を出力する
        