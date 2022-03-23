# POST发送数据包完成校园网认证
## Apple快捷指令请看 [Apple.md](https://github.com/z1zhang/AutoLoginWiFi/blob/master/Apple.md)
由于处于开发阶段，故可能存在很多缺陷

✅2022-3-22 添加Apple快捷指令

✅2022-3-17 POST完成校园网认证
### 使用方法：

下载main.py代码到本地，然后编写bat文件，你需要修改的部分：（大约在9-11行）

```python
user_account = ''  # 账号
user_type = ''  # 类型
user_pwd = ''  # 密码
```

| 类型   | 类型代码   |
|------|:-------|
| 中国移动 | cmcc   |
| 中国联通 | unicom |
| 校园网  | zzulis |

### bat示范：

```shell
cd E:\Program Projects\PycharmProjects\AutoLoginWiFi

python main.py
```

可以把bat文件放到`C:\ProgramData\Microsoft\Windows\Start Menu\Programs\Startup`下实现开机自启动