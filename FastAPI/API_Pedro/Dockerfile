FROM python:3.8.2

WORKDIR /app

RUN pip3 install sqlalchemy
RUN pip3 install fastapi
RUN pip3 install pydantic
RUN pip3 install "uvicorn[standard]"


EXPOSE 8000

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]