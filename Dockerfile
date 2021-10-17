FROM python:3.9
WORKDIR /pattern_learning
COPY ./requirements.txt /pattern_learning/requirements.txt
RUN pip install --no-cache-dir --upgrade -r /pattern_learning/requirements.txt
COPY ./ /pattern_learning/
CMD ["uvicorn", "main:APP", "--host", "0.0.0.0", "--port", "80"]