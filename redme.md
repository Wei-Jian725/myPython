#˵��
1�����Ҫ���У���������������������ո񣬻���ֱ�Ӱ�tab��


#web-flask���

##jinja2ģ�������
https://zlkt.net/book/detail/10/278  
�������൱����һ���������ѵ�ǰ�ı������뵽�������У�Ȼ������������Լ��Ĺ��ܣ��ٷ�����Ӧ��ֵ��֮���ٽ������Ⱦ��ҳ���� 
�ɲ鿴���ӣ�pythonWeb����app2����about.html

##HTMLģ��������
1��if���  
��ͨ���ж���ͼ�����е�ֵ����HTMLģ���б�дif�������ж�  
�ɲ鿴���ӣ�pythonWeb����app2����control.html 

2��for in���  
��ѭ��������ͼ�����е�����  
�ɱ����ֵ����ݺ��б�����  
�ɲ鿴���ӣ�pythonWeb����app2����control.html 

##ģ��̳�
�����͵ײ�����ƿ��Թ��ã����絼������ÿ��ģ�鶼ʹ��ͬһ�����������м����ݲ�һ��
 pythonWeb����templates����base.html

##���þ�̬�ļ�
1���ڸ�Ŀ¼�´���һ���ļ��й̶�����Ϊstatic��������css�ļ���css�ļ�������HTML��  
2������Ҫ����css�ļ���HTML�ļ�����link��ǩ����css�ļ���

##��ͼ��������
app
1����ͼ���ɾ��ȷ�����룬������ȫ������ͬһ��py�ļ���    
��ͼ���ļ�����blueprintsĿ¼��    
ÿһ�����ܷ���һ���ļ���


##�½����ݿ�
1������Navicat��  
2�������������Ҽ�����ѡ���½����ݿ⡪�����ݿ�����дΪ�Լ���д�ġ����ַ���utf8mb4����ȷ��    


##flask-sqlalchemy
1��SQLAlchemy��flask��SQLAlchemy������
    a��SQLAlchemy��һ��������ORM��ܣ��ɶ�����flask���ڣ�Ҳ������������Ŀ��ʹ��  
    ��������Django��ʹ�á�  
    b��flask��SQLAlchemy����SQLAlchemy��һ����װ���ܸ��ʺ���flask��ʹ�á�  
2��pip install flask-sqlalchemy ,pymysql
    
3�����ݿ�����ñ���
HOSTNAME = '127.0.0.1'  
PORT     = '3306'  
DATABASE = 'xt_flask'  
USERNAME = 'root'  
PASSWORD = 'root'  
DB_URI = 'mysql+pymysql://{}:{}@{}:{}/{}'.format(USERNAME,PASSWORD,HOSTNAME,PORT,DATABASE)  

4���������ݿ�����
engine = create_engine(DB_URI)
 


    
##ORMģ�����ݵ���ɾ�Ĳ�
����app3�в鿴����

##������ORM����ӳ��
https://zlkt.net/book/detail/10/297  
�ļ���һ��Ҫ����Ϊapp����Ȼ�ᱨ��  
����·��web-ORM-app�в鿴����  

1����װflask-Migrate    
pip install flask-migrate

2����ʼ��  ֻ��Ҫ��һ�������������������Ļ���flask db migrate��һ����ʼִ��
flask db init  

3������һ��Ǩ�ƽű�  -m�������޸�˵��,��˵������version���ļ���������ʾ
flask db migrate -m  "firt commit"  


4�������ݿ�ű�ӳ�䵽���ݿ���  
flask db upgrade

5�������ñ����ɾ�Ĳ����ݣ�����һ��·�ɣ�����д����ɾ�Ĳ�Ĳ������������������ʵ�ַ���������  
���ݵ���ɾ�Ĳ������

##����֤
��ҳ������֤�������ȷ�ԣ��Ϳ�����ȥ���ݿ����֤��  
https://zlkt.net/book/detail/10/298  
pip install flask-wtf  
������֤��   
pip install email_validator  
wtform����֤����form


#ǰ�˿��
bootstrap   
https://v4.bootcss.com/docs/getting-started/introduction/   

