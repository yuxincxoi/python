# 타입검사기
# 사용할 메서드 : input print type

# 노드켜줘 앱
# input으로 '노드'라는 단어가 포험되면 cli REPL 환경인 node가 실행되도록 명령
# '타입'이라는 단어가 포함되면 타입 검사

import subprocess

def type_test():
    try:
        text = int(input("input : "))
        print("int입니다.")
    except ValueError:
        print("문자열입니다.")
        
def run_node():
    subprocess.run(["node"], shell=True)