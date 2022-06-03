# 入力例:1000
# 出力例:one thousand
# 入力例:12345
# 出力例:one hundred twenty three thousand four hundred fifty five
# 入力例:123.330
# 出力例:one hundred twenty three point three three zero
# 入力例:100
# 出力例:one hundred

X = 1000
# Xを英語表記に変換する関数
def toEnglish(x):
    if x < 20:
        return ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine", "ten", "eleven", "twelve", "thirteen", "fourteen", "fifteen", "sixteen", "seventeen", "eighteen", "nineteen"][x]
    if x < 100:
        return toEnglish(x // 10) + "ty" + toEnglish(x % 10)
    if x < 1000:
        return toEnglish(x // 100) + " hundred" + toEnglish(x % 100)
    if x < 1000000:
        return toEnglish(x // 1000) + " thousand" + toEnglish(x % 1000)
    if x < 1000000000:
        return toEnglish(x // 1000000) + " million" + toEnglish(x % 1000000)
    if x < 1000000000000:
        return toEnglish(x // 1000000000) + " billion" + toEnglish(x % 1000000000)

print(toEnglish(X))