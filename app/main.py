import random

import uvicorn
from fastapi import FastAPI
from fastapi.responses import Response
from prometheus_client import (
    CONTENT_TYPE_LATEST,
    Counter,
    Gauge,
    Histogram,
    Summary,
    generate_latest,
)

app: FastAPI = FastAPI()

# Counter: 누적되는 메트릭 (예: 총 요청 수)
request_count: Counter = Counter('http_requests_total', 'Total HTTP Requests')

# Gauge: 증가하거나 감소할 수 있는 메트릭 (예: 현재 활성 사용자 수)
active_users: Gauge = Gauge('active_users', 'Number of active users')

# Histogram: 값의 분포를 측정 (예: 요청 처리 시간)
request_latency: Histogram = Histogram('request_latency_seconds', 'Request latency in seconds')

# Summary: Histogram과 유사하지만 sliding time window over events를 계산
request_size: Summary = Summary('request_size_bytes', 'Request size in bytes')

@app.get("/")
async def root() -> dict[str, str]:
    request_count.inc()
    active_users.set(random.randint(1, 100))  # 임의의 활성 사용자 수 설정
    request_latency.observe(random.random())  # 임의의 요청 처리 시간 기록
    request_size.observe(random.randint(100, 10000))  # 임의의 요청 크기 기록
    return {"message": "Hello World"}

@app.get("/metrics")
async def metrics() -> Response:
    return Response(generate_latest(), media_type=CONTENT_TYPE_LATEST)

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
