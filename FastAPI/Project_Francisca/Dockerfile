FROM python:3.9.7

COPY ./src app/src

WORKDIR /app

#considere usar algo no minimo como o requirements ou um gerenciador de virtual env
#como o poetry por exemplo. quando se faz pip install sem espeficicar versao
#pode acontecer de em producao a versao instalada ser diferente da local, possibilitando erros
RUN pip3 install sqlalchemy
RUN pip3 install fastapi
RUN pip3 install pydantic
RUN pip3 install "uvicorn[standard]"


EXPOSE 8000

CMD ["uvicorn", "src.main:app", "--host", "0.0.0.0", "--port", "8000"]