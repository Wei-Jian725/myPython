# -*- coding:utf-8 -*-
_author_ = 'weijian'


from flask import Blueprint,render_template
from exts import mail
from flask_mail import Message

bp = Blueprint('user',__name__,url_prefix="/user") #/user为基础路由，访问user时需经过这个路由

@bp.route('/login')
def login():
    return render_template('login.html')


@bp.route('/register')
def register():
    return render_template('register.html')

@bp.route('/mail')
def my_mail():
    message = Message(
        subject='邮箱测试',
        recipients=['649514913@qq.com'],
        body='这是测试邮件',
        sender='753563304@qq.com'
    )
    mail.send(message)
    return 'success'