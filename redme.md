#说明
1、如果要换行，在文字最后面输入两个空格，或者直接按tab键


#web-flask框架

##jinja2模板过滤器
https://zlkt.net/book/detail/10/278  
过滤器相当于是一个函数，把当前的变量传入到过滤器中，然后过滤器根据自己的功能，再返回相应的值，之后再将结果渲染到页面中 
可查看例子：pythonWeb——app2——about.html

##HTML模板控制语句
1、if语句  
可通过判断视图函数中的值，在HTML模板中编写if语句进行判断  
可查看例子：pythonWeb——app2——control.html 

2、for in语句  
可循环遍历视图函数中的数据  
可遍历字典数据和列表数据  
可查看例子：pythonWeb——app2——control.html 

##模板继承
顶部和底部的设计可以公用，比如导航栏。每个模块都使用同一个导航栏，中间内容不一样
 pythonWeb——templates——base.html

##引用静态文件
1、在根目录下创建一个文件夹固定命名为static，里面存放css文件，css文件可修饰HTML；  
2、在需要引用css文件的HTML文件中以link标签引用css文件。

##蓝图和子域名
app
1、蓝图：可均匀分配代码，不至于全部放在同一个py文件中    
蓝图的文件放在blueprints目录下    
每一个功能放在一个文件中


##新建数据库
1、连接Navicat；  
2、在连接名上右键——选择新建数据库——数据库名填写为自己想写的——字符集utf8mb4——确定    


##flask-sqlalchemy
1、SQLAlchemy和flask—SQLAlchemy的区别
    a、SQLAlchemy是一个独立的ORM框架，可独立于flask存在，也可以在其他项目中使用  
    ，比如在Django中使用。  
    b、flask—SQLAlchemy：对SQLAlchemy的一个封装，能更适合在flask中使用。  
2、pip install flask-sqlalchemy ,pymysql
    
3、数据库的配置变量
HOSTNAME = '127.0.0.1'  
PORT     = '3306'  
DATABASE = 'xt_flask'  
USERNAME = 'root'  
PASSWORD = 'root'  
DB_URI = 'mysql+pymysql://{}:{}@{}:{}/{}'.format(USERNAME,PASSWORD,HOSTNAME,PORT,DATABASE)  

4、创建数据库引擎
engine = create_engine(DB_URI)
 


    
##ORM模型数据的增删改查
可在app3中查看详情

##灵活管理ORM与表的映射
https://zlkt.net/book/detail/10/297  
文件名一定要设置为app，不然会报错  
可在路径web-ORM-app中查看详情  

1、安装flask-Migrate    
pip install flask-migrate

2、初始化  只需要第一次做这个操作，新增表的话从flask db migrate这一步开始执行
flask db init  

3、生成一个迁移脚本  -m后面是修改说明,改说明会在version的文件名称中显示
flask db migrate -m  "firt commit"  


4、将数据库脚本映射到数据库中  
flask db upgrade

5、创建好表后，增删改查数据，定义一个路由，下面写上增删改查的操作，浏览器中输入访问地址，就能完成  
数据的增删改查操作了

##表单验证
在页面中验证输入的正确性，就可以免去数据库的验证了  
https://zlkt.net/book/detail/10/298  
pip install flask-wtf  
邮箱验证器   
pip install email_validator  
wtform表单验证——form


#前端框架
bootstrap   
https://v4.bootcss.com/docs/getting-started/introduction/   

