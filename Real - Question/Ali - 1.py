'''
阿里笔试题

    不包含重复字符 长度为 m ，至少包含一个数字和两个小写字母的密码
        且字符字典序为严格升序

    输入：
        m 密码长度 n 键位数
        n 个各不相同的字符
    输出：
        所有密码组合可能性 以字典序升序输出 太多的话 输出前 666666个
    例子：
        输入：
        3 4
        n k 6 9
        输出：
        6kn
        9kn
'''

m, n = map(int, input().strip().split())
code = list(map(str, input().strip().split()))

code.sort()
print("code:", code)

english = []
number = []
index = -1

for i in range(len(code)):
    if code[i] >= 'a':
        index = i
        break

# 左闭右开
english = code[index:]
number = code[0:index]

print("english:", english)
print("number:", number)

password = []


