from flask import Flask
import config
from exts import db,mail
from blueprints import qa_bp #已经先存放在了init文件中
from blueprints import user_bp #引用蓝图中的模块
from blueprints import other_bp


app = Flask(__name__)
app.config.from_object(config)
db.init_app(app)
mail.init_app(app) #将APP继承到mail中，之后才能发邮件

#使蓝图中的方法生效
app.register_blueprint(qa_bp)
app.register_blueprint(user_bp)
app.register_blueprint(other_bp)




if __name__ == '__main__':
    app.run(host='0.0.0.0',port=5000,debug=True)