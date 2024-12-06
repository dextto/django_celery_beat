from celery import shared_task


@shared_task(bind=True, max_retries=3, default_retry_delay=2)
def add(self, x, y):
    try:
        # 오류를 발생시키는 코드
        1 / 0
    except ZeroDivisionError as exc:
        # 재시도
        raise self.retry(exc=exc)

    return x + y
