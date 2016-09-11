# flask基础项目


### 介绍
+ 调整目录结构，方便代码管理,

```
.
├── app                 -- 功能模块目录, 如： app/auth
├── cli                 -- 命令行工具/任务, demo: cli/cli_task_demo.py
├── config              -- 配置文件目录
├── file_tree_decrption -- 项目文件目录树
├── docs                -- 文档目录
├── Makefile            -- js、css压缩配置
├── manage.py           -- flask运行接口
├── README.md           -- 读我 :p
├── requirements.txt    -- pip依赖，请用 pip install -r requirements.txt 安装本项目的依赖
├── app/static          -- 静态文件目录，其中 static/vendors 内放的是第三方的静态文件，比如bootsrap的
├── app/templates       -- 文件模板目录，其中 static/layouts 内放一些共用的上级模板，用于继承
├── app/common          -- 公共配置目录，静态变量，公共函数
├── app/module          -- 公共模块目录，提供给其他模块使用
└── vendors             -- 第三方系统工具目录，比如appt

```

### 部署安装

参考 [install guide] docs/install_guide.md


### 参考
+ [官方](http://docs.jinkan.org/docs/flask/)
+ [《Flask Web Development》 完整笔记](http://www.jianshu.com/p/6b5eeff43360)
+ [欢迎进入Flask大型教程项目！](http://www.pythondoc.com/flask-mega-tutorial/)
