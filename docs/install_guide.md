## 安装说明

### 1. clone 代码库

+ 服务器ssh的 deploy key 加到对应gitlab项目

### 2. 设置virtualenvwrapper

(教程)[http://virtualenvwrapper.readthedocs.org/en/latest/install.html]

```shell
mkvirtualenv [project_name]_env  # 如果第一次部署需要此步创建虚拟环境，之后直接workon [project_name]_env 即可
```

### 3. 安装依赖包

- 根据 apt-get.md安装里面需要的包
- workon [project_name]_env
- pip install -r requirements.txt  #  *[2] [3]
- 部分包pip会无法正常安装，需要自行下载源码安装, 或根据提示加入允许外部包的参数, 如: pyDes

### 4. 配置config.py

+ 配置LOG输入路径，修改权限让 www-data可以读写
+ 配置database链接
+ 配置cache配置
+ 配置hosts
+ 配置文件路径
+ 配置变量

### 5. 配置uwsgi

- 安装:

```shell
sudo apt-get install uwsgi uwsgi-plugin-python
```

- 配置
- 依赖参考 [4]
- 参考 docs/flask.ini


### 6. 配置nginx

- 参考 docs/nginx.conf


### 7.配置Emperor模式

- 参考官方supervisor配置使用(http://uwsgi-docs.readthedocs.org/en/latest/tutorials/Django_and_nginx.html)
- 使用Emperor模式,当修改uwsgi配置文件，emperor会重新启动vassal，即重新加载配置文件
```
# create a directory for the vassals
sudo mkdir /etc/uwsgi
sudo mkdir /etc/uwsgi/vassals
# symlink from the default config directory to your config file
sudo ln -s /home/ymserver/vhost/gateway/flask_base/docs/uwsgi.ini /etc/uwsgi/vassals/
# run the emperor
uwsgi --emperor /etc/uwsgi/vassals --uid www-data --gid www-data
```
- supervisor 参考 docs/supervisor.conf


### 8.运行
- 配置完成后在项目主目录下可以运行测试,默认127.0.0.1：5000

```python
    python manage runserver
```

+ 创建db

```python
    python manage shell
    >>> db.create_all()
```

+ 创建用户

```python
    python manage shell
    >>> print readme
    >>> create_user(xxxx, xxx, xxx)
```


### 9.重启
- 命令行启动，根据uwsig配置文件，reload配置目录下：touch reload
```shell
uwsgi --ini flask.ini
cd /home/ymserver/vhost/gateway/flask_base
touch reload
```
- supervisor配置启动
```shell
supervisorctl
restart uwsgi_flask
```


### 备注

```
[1] py虚拟环境安装
(教程)[http://virtualenvwrapper.readthedocs.org/en/latest/install.html]

[2] mysqldb 可能缺少 mysql_config
sudo apt-get install libmysqlclient-dev python-dev

[3] pyDes 不能pip安装
下载
cd tmp
wget  http://twhiteman.netfirms.com/pyDES/pyDes-2.0.1.tar.gz
tar -zxvf pyDes-2.0.1.tar.gz
cd pyDes-2.0.1
python setup.py install

[4] 安装 uwsgi
sudo apt-get install uwsgi uwsgi-plugin-python
```
