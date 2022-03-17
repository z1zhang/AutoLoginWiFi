# post发送数据包完成校园网认证

由于处于开发阶段，故可能存在很多缺陷

### 使用方法：

下载代码到本地，然后编写bat文件 你需要修改的部分：

user_data = {

    "DDDDD": ",0,你的学号@运营商代码",eg：,0,541900000000@cmcc
    "upass": "你的密码",

}

| 运营商  | 运营商代码  |
|------|--------|
| 中国移动 | cmcc   |
| 中国联通 | unicom |
| 校园网  | zzulis |

### eg：

`e:`

`cd E:\Program Projects\PycharmProjects\AutoLoginWiFi`

`python main.py`

可以把bat文件放到`C:\ProgramData\Microsoft\Windows\Start Menu\Programs\Startup`下实现开机自启动