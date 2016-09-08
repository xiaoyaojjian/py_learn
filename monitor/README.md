监控系统
server:
    server.py: 服务端主程序
    conf:
        setting.py: redis 连接信息
        services: 监控指标定义
            hosts.py: 监控组定义
    core: 核心功能
client:
    client.py: 客户端主程序
    setting.py: redis 连接信息
    plugins: 监控脚本