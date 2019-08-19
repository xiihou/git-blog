from flask import Flask
from App.settings import envs
from App.views import init_blue
from App.ext import init_ext

def create_app():

    app = Flask(__name__,template_folder='../templates')
    #初始化app 加载配置文件
    app.config.from_object(envs.get('develop'))

    # 初始化蓝图 路由
    init_blue(app)

    # 初始化  第三方库
    init_ext(app)


    return app
