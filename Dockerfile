# Python 3.11 베이스 이미지 사용
FROM python:3.11-slim

# 작업 디렉토리 설정
WORKDIR /code

# Poetry 설치
RUN pip install poetry

# 프로젝트 파일 복사
COPY pyproject.toml poetry.lock* ./

# Poetry를 사용하여 의존성 설치
RUN poetry config virtualenvs.create false \
    && poetry install --no-interaction --no-ansi

# 애플리케이션 코드 복사
COPY app /code/app

# 포트 8000 노출
EXPOSE 8000

# 애플리케이션 실행
CMD ["poetry", "run", "uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
