# -*- coding:utf-8 -*-
_author_ = 'weijian'

import wtforms
from wtforms.validators import length,email

class LoginForm(wtforms.Form):
    email = wtforms.StringField(validators=[length(min=5,max=20),email()]) #validators位验证器，验证长度length，验证邮箱格式email
    password = wtforms.StringField(validators=[length(min=6,max=20)])
