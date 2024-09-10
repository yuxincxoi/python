# 타입검사기
# 사용할 메서드 : input print type

def type_test():
    text = input("input : ")
    if type(text) == str:
        print("문자열입니다.")
    elif type(text) == int:
        print("int입니다.")
        
type_test()