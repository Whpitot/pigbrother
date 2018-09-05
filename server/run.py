# -*-coding:utf8-*-

from app import create_app
from log import logger
import time

app = create_app()

if __name__ == "__main__": # 当前模块为启动模块，执行命令
    logger.info('application start!')
    logger.info(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()) )
    app.run(debug=True, port=5000)
    