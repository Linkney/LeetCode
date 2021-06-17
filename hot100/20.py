# class Solution:
#     def isValid(self, s: str) -> bool:
#         while '{}' in s or '()' in s or '[]' in s:
#             s = s.replace('{}', '')
#             s = s.replace('[]', '')
#             s = s.replace('()', '')
#         return s == ''


# 栈
def isValid(s: str) -> bool:
    stack = []
    # .pop(-1) 出栈default=-1=last .append 入栈 len() 数目
    for i in range(len(s)):
        if s[i] in ["(", "[", "{"]:
            stack.append(s[i])
        else:  # ) ] }
            if len(stack) == 0:
                return False
            else:
                check = stack.pop()
                if (s[i] == ")" and check == "(") or (s[i] == "]" and check == "[") or (s[i] == "}" and check == "{"):
                    continue
                else:
                    return False
    # 扫完清完
    if len(stack) == 0:
        return True
    else:
        return False


if __name__ == '__main__':
    s = "()"
    print(isValid(s))
