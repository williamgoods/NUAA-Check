# Bug南航- i南航 自动打卡系统
## 使用方法
1. 将本项目fork到自己的仓库
2. 在**自己的**github的settings(对，就是上面一栏code issues最后一个，点进去左边找到secrets里面设置下secrets,详见[参数配置](#canshu)
3. clone自己的项目一份到本地，使用`pip install -r requirements.txt`安装项目依赖,新建文件key.txt，填写内容为上步中设置的key
4. 使用谷歌或edge浏览器打开 [打卡链接](https://m.nuaa.edu.cn/ncov/wap/default/index) ，按F12打开控制台，手动进行打卡，按照如下方式复制curl命令
![](https://cdn.jsdelivr.net/gh/li1553770945/images/20220509103352.png)
5. 在项目目录新建data.txt，把刚刚复制的内容粘贴进去，运行encrypt.py
6. 提交并push新的代码

<h2 id="canshu">参数配置</h2>

sckey：在 [Server酱](https://sct.ftqq.com/sendkey) 绑定微信找到SendKey填入  
key：加解密的密钥，自己定义的一串**长度为32**的不规则字符，例如:"lo9878iij6vfdni09fp9l0p12fgy6los"

## 注意：
1. github的workflow过一段时间会失效（github会发邮件通知）,需要手动重新开启
2. 如果您要修改打卡时间，请修改nuaa.yaml中的` - cron: '01 16 * * *'`,01代表分钟，16代表小时。请注时间是GMT时间，也就是比北京时间慢8个小时。
3. 程序设定每天00:01打卡，但是经过实际测试有很长延迟，可能为一小时左右
4. 如果后续打卡内容出现变化，您只要更重复使用方法——步骤4-5即可

### 免责声明
本程序仅供学习参考，不得利用本程序替代手动打卡使用，如出现瞒报等行为与本程序无关。请在clone或fork后24小时内删除，否则后果自负！

t
