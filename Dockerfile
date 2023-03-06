FROM python:3

WORKDIR /usr/src/app

COPY . .

RUN pip3 install -i https://pypi.douban.com/simple/ -U pip 

RUN pip3 config set global.index-url https://pypi.tuna.tsinghua.edu.cn/simple/

RUN pip install --no-cache-dir -r requirements.txt

CMD [ "python", "./main.py" ]