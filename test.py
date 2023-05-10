
print("action test")

def func(x):
    return x + 1

# 테스트 함수
def test_answer():
    assert func(3) == 5, '오류입니다.'