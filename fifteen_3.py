'''
15.3 연습문제: if, elif, else 모두 사용하기
다음 소스 코드를 완성하여 변수 x가 11과 20 사이면 '11~20', 21과 30 사이면 '21~30', 아무것도 해당하지 않으면 '아무것도 해당하지 않음'이
출력되게 만드세요.
 
<실행 결과>
    5 (입력)
    아무것도 해당하지 않음
'''

n=int(input())
if 11<=n<=20:
    print("11~20")
elif 21<=n<=30:
    print("21~30")
else:
    print("아무것도 해당하지 않음")
