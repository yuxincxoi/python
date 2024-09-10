# 타입검사기
# 사용할 메서드 : input print type

def type_test():
    try:
        text = int(input("input : "))
        print("int입니다.")
    except ValueError:
        print("문자열입니다.")
        
type_test()