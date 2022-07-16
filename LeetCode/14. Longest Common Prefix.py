class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        # 最小の文字列を取得
        shortest = min(strs, key=len)
        # 最小の文字列を基準に比較
        for i, ch in enumerate(shortest):
            for other in strs:
                if other[i] != ch:
                    # 比較した文字が違う場合は前の文字までを返す
                    return shortest[:i]
        # 最後まで一致したらそのまま帰す
        return shortest
