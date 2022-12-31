## GoTo-友联接力-GoTo后端

![GoTologo](https://www.sunzishaokao.com/cdn/gotolink/gitee/Gotologo.jpg)

# 介绍：

项目后端使用Go的GIN框架进行编写，我们已经开源了核心功能！

## 部署

下载适用于您目标机器操作系统、CPU架构的主程序，直接运行即可。

```bash
# 解压程序包
tar -zxvf GoTo_OS_ARCH_VERSION.tar.gz

# 赋予执行权限
chmod +x ./GoTo

# 初次启动GoTo,此步会生成配置文件,需更改配置文件内的所有内容
./GoTo

# 运行内置的数据库脚本
./GoTo -i true

# 启动 GoTo
./GoTo
```

## 构建

> 注意，目前GoTo后端只开源核心功能，如需更高级功能，请使用我们官方授权版！

自行构建前需要拥有 `Go >= 1.19` 等必要依赖并下载后端源码。

### 编译项目

```bash
go build -o GoTo_Dev
```

### 启动它！

由于自编译版本功能与正式版差异较大，数据库需要自行导入。请在goto后端源码中 `MysqlUtil/sql.sql`将此文件在数据库内执行。

```bash
# 初次启动GoTo,此步会生成配置文件,需更改配置文件内的所有内容
./GoTo

# 启动GoTo
./GoTo_Dev
```

