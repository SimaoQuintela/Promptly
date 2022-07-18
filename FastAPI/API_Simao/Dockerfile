FROM python:3.9.7

COPY ./src /app

WORKDIR /app

RUN pip3 install sqlalchemy
RUN pip3 install fastapi
RUN pip3 install pydantic
RUN pip3 install "uvicorn[standard]"


CMD ["uvicorn", "main:app", "--reload"]