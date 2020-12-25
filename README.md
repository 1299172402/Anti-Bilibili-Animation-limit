# Anti-Bilibili-Animation-limit
Why I can not see my favourite animation?????


之前在12.15左右，biliplus的接口被哔站封锁，我不能看港澳台的番剧了！！！！！

于此，kghost也同步停止服务，鉴于2020年10月新番采用app限定形式，故开始尝试破解。

## 1.使用VPN（但我不想翻过大陆防火墙）

## 2.使用阿里云计算办法
目前的最省钱方案：

referer： https://github.com/ipcjs/bilibili-helper/issues/710#issuecomment-748976481

给愿意搞的海外党一个简易小教程：
#### 1.注册一个阿里云账号
#### 2.打开function compute功能
#### 3.在ServicesanndFunctions里面选择Create Function
image

![](https://user-images.githubusercontent.com/8595983/102781902-87864a80-43ec-11eb-97f8-8dd27b3d35ee.png)

#### 4.创建一个http function
image

![](https://user-images.githubusercontent.com/8595983/102781935-966cfd00-43ec-11eb-8081-1ed9dbbc7bc3.png)
#### 5.Service Name, Function Name都可以随便填，Runtime改成php7.2，其他的设置可以把memory改到最小（这个function大概就用50MB），timeout可以适当减少（根据网络状况而定，我设置了15秒）
image

![](https://user-images.githubusercontent.com/8595983/102782087-da600200-43ec-11eb-9239-200a23022bfb.png)

#### 6.进入你的function后把index.php用这个链接里的内容覆盖（覆盖后记得保存！！！Save）：https://raw.githubusercontent.com/zzc10086/grocery_store/master/bili_proxy/aliyun_Serverless_BPplayurl.php
image

![](https://user-images.githubusercontent.com/8595983/102782241-24e17e80-43ed-11eb-9b66-e12e32f0ac8c.png)

#### 7.在同一个页面下方，找到http地址：
image
![](https://user-images.githubusercontent.com/8595983/102782302-3d519900-43ed-11eb-806b-45ed5e8f53cb.png)
#### 8.把这个地址放进插件的自定义代理中：
image
![](https://user-images.githubusercontent.com/8595983/102782364-58240d80-43ed-11eb-8b48-81d032cf86d6.png)
然后刷新一下，重新授权一下就可以用了。

如果是需要香港服务器应该也可以在阿里云页面-上面修改成香港服务器，应该也可以测试不同服务器的速度，默认是上海，b站也是base上海所以应该速度是可以的，我没测试就是了……
image
![](https://user-images.githubusercontent.com/8595983/102782466-80ac0780-43ed-11eb-80eb-aad238b6943e.png)
阿里云提供每个月100万次免费计算，测试了下看一个视频用了10次计算左右所以肯定是用不完了……（流量会收费，海外阿里云是0.117美刀/GB，解析一次地址就几十kb，用量应该是非常少的）
