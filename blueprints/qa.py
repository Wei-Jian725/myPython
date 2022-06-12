# -*- coding:utf-8 -*-
_author_ = 'weijian'

from flask import Blueprint,render_template

#此文件为问答页面的各种操作

bp = Blueprint('qa',__name__,url_prefix="/") #/为基础路由，访问问答时需经过这个路由

@bp.route('/')
def index():
    return render_template('index.html')
