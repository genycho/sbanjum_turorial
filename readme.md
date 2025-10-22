# Welcome to OpenAPI TC Generator Project

## 설명

(1) OpenAPI 스펙 문서(swagger 파일 등)로부터 정보를 추출하여, 관련 테스트 지식/노하우 기반 테스트 케이스를 생성하고, 원하는 형태의 테스트(코드)를 생성 

(2) 


## Running this exercise locally
```
	execute the below pytest command in IDE terminal venv

```


## Local Setting Guide

### Prerequisites
install the following libraries:

* python -m venv venv # 파이썬 가상환경 만들기

* source ./venv/bin/activate # 가상환경 활성화

* pip install pytest


S반점 FastAPI 실행 방법: 

커맨드라인에서 다음 명령어 실행 

uvicorn src.employee.jumwon:app --reload

후 브라우저에서 다음 URL로 접근.

(직접 호출) http://127.0.0.1:8000 

(Swagger 보기) http://127.0.0.1:8000/docs


#어디까지 하다 말았는지 너무 뜨문뜨문해서 기억이 안 나서 여기에 기록하기. 

2024/12/19 get_tc_analyzer.py 완료. 
2025/-1/06 post, put, delete 등의 이전 코드를 단순 복붙.
2025/03/31 전체 테스트 코드 만들었더니 post multipart가 문제. 
