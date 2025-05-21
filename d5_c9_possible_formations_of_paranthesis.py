# s = ""
# n = 3
# def pp(s):
#     if len(s) == n*2:
#         print(s)
#         return
#     pp(s+"(")
#     pp(s+")")
# pp(s)

s = ""
n = 3
def pp(s):
    if len(s) == n*2:
        print(s)
        return
    pp(s+"(")
    pp(s+")")
pp(s)