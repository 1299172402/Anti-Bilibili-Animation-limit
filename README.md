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

#### 6.进入你的function后把index.php用这个链接里的内容覆盖（覆盖后记得保存！！！Save）：

https://raw.githubusercontent.com/zzc10086/grocery_store/master/bili_proxy/aliyun_Serverless_BPplayurl.php

https://github.com/zzc10086/grocery_store/blob/master/bili_proxy/BPplayurl.php

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

#### 9.把这个地址放入哔哩漫游的香港服务器中（去除https://）

#### 测试结果

https://github.com/1299172402/Anti-Bilibili-Animation-limit#阿里云测试结果

## 3.仅使用app的解决办法

仿照 https://github.com/SocialSisterYi/bilibili-API-collect/issues/24#issuecomment-659955015 的地址建立

https://app.bilibili.com/x/playurl?access_key=xxxxx3669686a5c264ed64e651c63c71&aid=99999999&appkey=iVGUTjsxvpLeuDCf&build=5370000&buvid=XXD9E43D7A1EBB6669597650E3EE417D9E7F5&cid=171776208&device=android&expire=1597289802&fnval=16&fnver=0&force_host=0&mid=174438027&mobi_app=android&npcybs=0&otype=json&platform=android&qn=32&ts=1594974158&sign=b10febf17d65fb76cd3102006ef8318f

B站似乎很信任来自app端的请求，即使timestamp与现在时间相差很远，access_key有点特别，但只要sign校验成功，就可以播放。（但是对于区域还是有所限制）

#### 测试结果

https://github.com/1299172402/Anti-Bilibili-Animation-limit#app的测试结果





### 阿里云测试结果

阿里云的办法可以支持获取非2020年10月番剧的下载地址，测试了不分段flv地址，可以下载
(用自己以前写的脚本测试，时间2020.12.25 21：04，番剧md28229298，ss33865，出租女友)
```
C:\Users\2184232017>python D:\xxx\SimpleCoding\AnimeDownload\master\AnimeDownload.py
Welcome to Bilibili Animation Download
Creative By ZhiyuShang With LOVE
[Referer](https://github.com/1299172402/AnimeDownload)
md: 28229298
https://api.bilibili.com/pgc/web/season/section?season_id=33865
{'aid': 456273732, 'cid': 222747655, 'title': '01 出租女友'}
{'aid': 243992438, 'cid': 213647372, 'title': '02 前女友與女友'}
{'aid': 371473632, 'cid': 216210355, 'title': '03 海與女友'}
{'aid': 796566924, 'cid': 218881896, 'title': '04 朋友和女友'}
{'aid': 839246427, 'cid': 221625716, 'title': '05 溫泉和女友'}
{'aid': 796638766, 'cid': 224496832, 'title': '06 女友與女友'}
{'aid': 969252540, 'cid': 227142356, 'title': '07 暫時女友與女友'}
{'aid': 499475245, 'cid': 229872552, 'title': '08 聖誕節與女友'}
{'aid': 456921248, 'cid': 232174839, 'title': '09 謊言與女友'}
{'aid': 542036253, 'cid': 234388213, 'title': '10 朋友的女友'}
{'aid': 584656003, 'cid': 236572218, 'title': '11 真相與女友'}
{'aid': 499665570, 'cid': 238956055, 'title': '12 告白與女友'}
area[tw/hk/sg/cn/(none)]: ali
is_xml_download?
is_bcc_download?
is_admination_download?y
{'code': 0, 'message': 'success', 'result': {'accept_format': 'hdflv2,flv,flv720,flv480,mp4', 'code': 0, 'durl': [{'size': 185175397, 'ahead': '', 'length': 1467131, 'vhead': '', 'backup_url': [], 'url': 'https://upos-hz-mirrorakam.akamaized.net/upgcxcode/55/76/222747655/222747655_nb2-1-80.flv?e=ig8euxZM2rNcNbh17WdVhoMzhWUVhwdEto8g5X10ugNcXBlqNxHxNEVE5XREto8KqJZHUa6m5J0SqE85tZvEuENvNo8g2ENvNo8i8o859r1qXg8xNEVE5XREto8GuFGv2U7SuxI72X6fTr859r1qXg8gNEVE5XREto8z5JZC2X2gkX5L5F1eTX1jkXlsTXHeux_f2o859IB_&uipk=5&nbs=1&deadline=1608914688&gen=playurl&os=akam&oi=804448936&trid=d867d67bf57d4e52939e7d9b05f1045ep&platform=pc&upsig=ca8984add9445d4a4eadc7cce50fd45d&uparams=e,uipk,nbs,deadline,gen,os,oi,trid,platform&hdnts=exp=1608907488~hmac=3bcaff20ddba05ad851895cb664246c73b3746597f0d26648beb0180fbbd9897&mid=0&orderid=0,1&agrr=0&logo=80000000', 'order': 1, 'md5': ''}], 'seek_param': 'start', 'is_preview': 0, 'no_rexcode': 0, 'format': 'flv', 'fnval': 0, 'video_project': True, 'fnver': 0, 'support_formats': [{'display_desc': '1080P', 'superscript': '高码率', 'need_login': True, 'format': 'hdflv2', 'description': '高清 1080P+', 'need_vip': True, 'quality': 112, 'new_description': '1080P 高码率'}, {'display_desc': '1080P', 'superscript': '', 'need_login': True, 'format': 'flv', 'description': '高清 1080P', 'quality': 80, 'new_description': '1080P 高清'}, {'display_desc': '720P', 'superscript': '', 'need_login': True, 'format': 'flv720', 'description': '高清 720P', 'quality': 64, 'new_description': '720P  高清'}, {'display_desc': '480P', 'superscript': '', 'format': 'flv480', 'description': '清晰 480P', 'quality': 32, 'new_description': '480P 清晰'}, {'display_desc': '360P', 'superscript': '', 'format': 'mp4', 'description': '流畅 360P', 'quality': 16, 'new_description': '360P 流畅'}], 'message': '', 'type': 'FLV', 'accept_quality': [112, 80, 64, 32, 16], 'bp': 0, 'quality': 80, 'timelength': 1467131, 'result': 'suee', 'seek_type': 'offset', 'has_paid': False, 'from': 'local', 'video_codecid': 7, 'accept_description': ['高清 1080P+', '高清 1080P', '高清 720P', '清晰 480P', '流畅 360P'], 'status': 2}}
{'code': 0, 'message': 'success', 'result': {'accept_format': 'hdflv2,flv,flv720,flv480,mp4', 'code': 0, 'durl': [{'size': 200557925, 'ahead': '', 'length': 1467110, 'vhead': '', 'backup_url': [], 'url': 'https://upos-hz-mirrorakam.akamaized.net/upgcxcode/72/73/213647372/213647372_nb2-1-80.flv?e=ig8euxZM2rNcNbhMhwdVhoMz7wdVhwdEto8g5X10ugNcXBlqNxHxNEVE5XREto8KqJZHUa6m5J0SqE85tZvEuENvNo8g2ENvNo8i8o859r1qXg8xNEVE5XREto8GuFGv2U7SuxI72X6fTr859r1qXg8gNEVE5XREto8z5JZC2X2gkX5L5F1eTX1jkXlsTXHeux_f2o859IB_&uipk=5&nbs=1&deadline=1608914689&gen=playurl&os=akam&oi=804448936&trid=1bfea1584ad345849e6b2c1465d2ecf9p&platform=pc&upsig=b0777c9358aeefb4446edb317f14c7c0&uparams=e,uipk,nbs,deadline,gen,os,oi,trid,platform&hdnts=exp=1608907489~hmac=8cff1d8b214f6084ce321ebf728c74df22e19523d1721250bd534e8235f3f41f&mid=0&orderid=0,1&agrr=0&logo=80000000', 'order': 1, 'md5': ''}], 'seek_param': 'start', 'is_preview': 0, 'no_rexcode': 0, 'format': 'flv', 'fnval': 0, 'video_project': True, 'fnver': 0, 'support_formats': [{'display_desc': '1080P', 'superscript': '高码率', 'need_login': True, 'format': 'hdflv2', 'description': '高清 1080P+', 'need_vip': True, 'quality': 112, 'new_description': '1080P 高码率'}, {'display_desc': '1080P', 'superscript': '', 'need_login': True, 'format': 'flv', 'description': '高清 1080P', 'quality': 80, 'new_description': '1080P 高清'}, {'display_desc': '720P', 'superscript': '', 'need_login': True, 'format': 'flv720', 'description': '高清 720P', 'quality': 64, 'new_description': '720P  高清'}, {'display_desc': '480P', 'superscript': '', 'format': 'flv480', 'description': '清晰 480P', 'quality': 32, 'new_description': '480P 清晰'}, {'display_desc': '360P', 'superscript': '', 'format': 'mp4', 'description': '流畅 360P', 'quality': 16, 'new_description': '360P 流畅'}], 'message': '', 'type': 'FLV', 'accept_quality': [112, 80, 64, 32, 16], 'bp': 0, 'quality': 80, 'timelength': 1467110, 'result': 'suee', 'seek_type': 'offset', 'has_paid': False, 'from': 'local', 'video_codecid': 7, 'accept_description': ['高清 1080P+', '高清 1080P', '高清 720P', '清晰 480P', '流畅 360P'], 'status': 2}}
{'code': 0, 'message': 'success', 'result': {'accept_format': 'hdflv2,flv,flv720,flv480,mp4', 'code': 0, 'durl': [{'size': 208795324, 'ahead': '', 'length': 1467132, 'vhead': '', 'backup_url': [], 'url': 'https://upos-hz-mirrorakam.akamaized.net/upgcxcode/55/03/216210355/216210355_nb2-1-80.flv?e=ig8euxZM2rNcNbhB7WdVhoMz7WUVhwdEto8g5X10ugNcXBlqNxHxNEVE5XREto8KqJZHUa6m5J0SqE85tZvEuENvNo8g2ENvNo8i8o859r1qXg8xNEVE5XREto8GuFGv2U7SuxI72X6fTr859r1qXg8gNEVE5XREto8z5JZC2X2gkX5L5F1eTX1jkXlsTXHeux_f2o859IB_&uipk=5&nbs=1&deadline=1608914689&gen=playurl&os=akam&oi=804448936&trid=cfcac9d1daf84dc3a47db61e806d594dp&platform=pc&upsig=a2a25f0018fda80a50c35c2e9166f6ec&uparams=e,uipk,nbs,deadline,gen,os,oi,trid,platform&hdnts=exp=1608907489~hmac=a960521f38c0af5bf9e89474ac66d7558d35922e8f9a0a30fc84414efe00ed7a&mid=0&orderid=0,1&agrr=0&logo=80000000', 'order': 1, 'md5': ''}], 'seek_param': 'start', 'is_preview': 0, 'no_rexcode': 0, 'format': 'flv', 'fnval': 0, 'video_project': True, 'fnver': 0, 'support_formats': [{'display_desc': '1080P', 'superscript': '高码率', 'need_login': True, 'format': 'hdflv2', 'description': '高清 1080P+', 'need_vip': True, 'quality': 112, 'new_description': '1080P 高码率'}, {'display_desc': '1080P', 'superscript': '', 'need_login': True, 'format': 'flv', 'description': '高清 1080P', 'quality': 80, 'new_description': '1080P 高清'}, {'display_desc': '720P', 'superscript': '', 'need_login': True, 'format': 'flv720', 'description': '高清 720P', 'quality': 64, 'new_description': '720P  高清'}, {'display_desc': '480P', 'superscript': '', 'format': 'flv480', 'description': '清晰 480P', 'quality': 32, 'new_description': '480P 清晰'}, {'display_desc': '360P', 'superscript': '', 'format': 'mp4', 'description': '流畅 360P', 'quality': 16, 'new_description': '360P 流畅'}], 'message': '', 'type': 'FLV', 'accept_quality': [112, 80, 64, 32, 16], 'bp': 0, 'quality': 80, 'timelength': 1467132, 'result': 'suee', 'seek_type': 'offset', 'has_paid': False, 'from': 'local', 'video_codecid': 7, 'accept_description': ['高清 1080P+', '高清 1080P', '高清 720P', '清晰 480P', '流畅 360P'], 'status': 2}}
{'code': 0, 'message': 'success', 'result': {'accept_format': 'hdflv2,flv,flv720,flv480,mp4', 'code': 0, 'durl': [{'size': 202849775, 'ahead': '', 'length': 1467131, 'vhead': '', 'backup_url': [], 'url': 'https://upos-hz-mirrorakam.akamaized.net/upgcxcode/96/18/218881896/218881896_nb2-1-80.flv?e=ig8euxZM2rNcNbhM7WdVhoMz7wUVhwdEto8g5X10ugNcXBlqNxHxNEVE5XREto8KqJZHUa6m5J0SqE85tZvEuENvNo8g2ENvNo8i8o859r1qXg8xNEVE5XREto8GuFGv2U7SuxI72X6fTr859r1qXg8gNEVE5XREto8z5JZC2X2gkX5L5F1eTX1jkXlsTXHeux_f2o859IB_&uipk=5&nbs=1&deadline=1608914690&gen=playurl&os=akam&oi=804448936&trid=8db67c9e64c04e2885b7b1927522ae00p&platform=pc&upsig=d8c322cc45103e93ef0cd26f83dd75f8&uparams=e,uipk,nbs,deadline,gen,os,oi,trid,platform&hdnts=exp=1608907490~hmac=428efb5a655f682b9db5c294b54e612e32afa9ad13f746e5890e55644f6983e5&mid=0&orderid=0,1&agrr=0&logo=80000000', 'order': 1, 'md5': ''}], 'seek_param': 'start', 'is_preview': 0, 'no_rexcode': 0, 'format': 'flv', 'fnval': 0, 'video_project': True, 'fnver': 0, 'support_formats': [{'display_desc': '1080P', 'superscript': '高码率', 'need_login': True, 'format': 'hdflv2', 'description': '高清 1080P+', 'need_vip': True, 'quality': 112, 'new_description': '1080P 高码率'}, {'display_desc': '1080P', 'superscript': '', 'need_login': True, 'format': 'flv', 'description': '高清 1080P', 'quality': 80, 'new_description': '1080P 高清'}, {'display_desc': '720P', 'superscript': '', 'need_login': True, 'format': 'flv720', 'description': '高清 720P', 'quality': 64, 'new_description': '720P  高清'}, {'display_desc': '480P', 'superscript': '', 'format': 'flv480', 'description': '清晰 480P', 'quality': 32, 'new_description': '480P 清晰'}, {'display_desc': '360P', 'superscript': '', 'format': 'mp4', 'description': '流畅 360P', 'quality': 16, 'new_description': '360P 流畅'}], 'message': '', 'type': 'FLV', 'accept_quality': [112, 80, 64, 32, 16], 'bp': 0, 'quality': 80, 'timelength': 1467131, 'result': 'suee', 'seek_type': 'offset', 'has_paid': False, 'from': 'local', 'video_codecid': 7, 'accept_description': ['高清 1080P+', '高清 1080P', '高清 720P', '清晰 480P', '流畅 360P'], 'status': 2}}
{'code': 0, 'message': 'success', 'result': {'accept_format': 'hdflv2,flv,flv720,flv480,mp4', 'code': 0, 'durl': [{'size': 181732058, 'ahead': '', 'length': 1467132, 'vhead': '', 'backup_url': [], 'url': 'https://upos-hz-mirrorakam.akamaized.net/upgcxcode/16/57/221625716/221625716-1-80.flv?e=ig8euxZM2rNcNbhV7zUVhoMzhwuBhwdEto8g5X10ugNcXBlqNxHxNEVE5XREto8KqJZHUa6m5J0SqE85tZvEuENvNo8g2ENvNo8i8o859r1qXg8xNEVE5XREto8GuFGv2U7SuxI72X6fTr859r1qXg8gNEVE5XREto8z5JZC2X2gkX5L5F1eTX1jkXlsTXHeux_f2o859IB_&uipk=5&nbs=1&deadline=1608914690&gen=playurl&os=akam&oi=804448936&trid=13323098401246828035d68464a2e94cp&platform=pc&upsig=6fecb507c5c7e3487513b4fc0bc6a5a9&uparams=e,uipk,nbs,deadline,gen,os,oi,trid,platform&hdnts=exp=1608907490~hmac=327bd2529eebd7b5a27bca68c6f4ed2f43e4cbd87043957df2bb9c9cfb9f1350&mid=0&orderid=0,1&agrr=0&logo=80000000', 'order': 1, 'md5': ''}], 'seek_param': 'start', 'is_preview': 0, 'no_rexcode': 0, 'format': 'flv', 'fnval': 0, 'video_project': True, 'fnver': 0, 'support_formats': [{'display_desc': '1080P', 'superscript': '高码率', 'need_login': True, 'format': 'hdflv2', 'description': '高清 1080P+', 'need_vip': True, 'quality': 112, 'new_description': '1080P 高码率'}, {'display_desc': '1080P', 'superscript': '', 'need_login': True, 'format': 'flv', 'description': '高清 1080P', 'quality': 80, 'new_description': '1080P 高清'}, {'display_desc': '720P', 'superscript': '', 'need_login': True, 'format': 'flv720', 'description': '高清 720P', 'quality': 64, 'new_description': '720P 高清'}, {'display_desc': '480P', 'superscript': '', 'format': 'flv480', 'description': '清晰 480P', 'quality': 32, 'new_description': '480P 清晰'}, {'display_desc': '360P', 'superscript': '', 'format': 'mp4', 'description': '流畅 360P', 'quality': 16, 'new_description': '360P 流畅'}], 'message': '', 'type': 'FLV', 'accept_quality': [112, 80, 64, 32, 16], 'bp': 0, 'quality': 80, 'timelength': 1467132, 'result': 'suee', 'seek_type': 'offset', 'has_paid': False, 'from': 'local', 'video_codecid': 7, 'accept_description': ['高清 1080P+', '高清 1080P', '高清 720P', '清晰 480P', '流畅 360P'], 'status': 2}}
{'code': 0, 'message': 'success', 'result': {'accept_format': 'hdflv2,flv,flv720,flv480,mp4', 'code': 0, 'durl': [{'size': 202424413, 'ahead': '', 'length': 1467132, 'vhead': '', 'backup_url': [], 'url': 'https://upos-hz-mirrorakam.akamaized.net/upgcxcode/32/68/224496832/224496832_nb2-1-80.flv?e=ig8euxZM2rNcNbhMhbUVhoMz7wNBhwdEto8g5X10ugNcXBlqNxHxNEVE5XREto8KqJZHUa6m5J0SqE85tZvEuENvNo8g2ENvNo8i8o859r1qXg8xNEVE5XREto8GuFGv2U7SuxI72X6fTr859r1qXg8gNEVE5XREto8z5JZC2X2gkX5L5F1eTX1jkXlsTXHeux_f2o859IB_&uipk=5&nbs=1&deadline=1608914691&gen=playurl&os=akam&oi=804448936&trid=f1b3f4a700cd4a0794679c1402da95d5p&platform=pc&upsig=42be67a25da39a332de245d832e37e14&uparams=e,uipk,nbs,deadline,gen,os,oi,trid,platform&hdnts=exp=1608907491~hmac=b0b709f55a96dcfc711a5ab84e4702c2bb6979a4842b00a372b5d9a534a74c64&mid=0&orderid=0,1&agrr=0&logo=80000000', 'order': 1, 'md5': ''}], 'seek_param': 'start', 'is_preview': 0, 'no_rexcode': 0, 'format': 'flv', 'fnval': 0, 'video_project': True, 'fnver': 0, 'support_formats': [{'display_desc': '1080P', 'superscript': '高码率', 'need_login': True, 'format': 'hdflv2', 'description': '高清 1080P+', 'need_vip': True, 'quality': 112, 'new_description': '1080P 高码率'}, {'display_desc': '1080P', 'superscript': '', 'need_login': True, 'format': 'flv', 'description': '高清 1080P', 'quality': 80, 'new_description': '1080P 高清'}, {'display_desc': '720P', 'superscript': '', 'need_login': True, 'format': 'flv720', 'description': '高清 720P', 'quality': 64, 'new_description': '720P  高清'}, {'display_desc': '480P', 'superscript': '', 'format': 'flv480', 'description': '清晰 480P', 'quality': 32, 'new_description': '480P 清晰'}, {'display_desc': '360P', 'superscript': '', 'format': 'mp4', 'description': '流畅 360P', 'quality': 16, 'new_description': '360P 流畅'}], 'message': '', 'type': 'FLV', 'accept_quality': [112, 80, 64, 32, 16], 'bp': 0, 'quality': 80, 'timelength': 1467132, 'result': 'suee', 'seek_type': 'offset', 'has_paid': False, 'from': 'local', 'video_codecid': 7, 'accept_description': ['高清 1080P+', '高清 1080P', '高清 720P', '清晰 480P', '流畅 360P'], 'status': 2}}
{'code': 0, 'message': 'success', 'result': {'accept_format': 'hdflv2,flv,flv720,flv480,mp4', 'code': 0, 'durl': [{'size': 201820460, 'ahead': '', 'length': 1467132, 'vhead': '', 'backup_url': [], 'url': 'https://upos-hz-mirrorakam.akamaized.net/upgcxcode/56/23/227142356/227142356_nb2-1-80.flv?e=ig8euxZM2rNcNbhMhbUVhoMz7wNBhwdEto8g5X10ugNcXBlqNxHxNEVE5XREto8KqJZHUa6m5J0SqE85tZvEuENvNo8g2ENvNo8i8o859r1qXg8xNEVE5XREto8GuFGv2U7SuxI72X6fTr859r1qXg8gNEVE5XREto8z5JZC2X2gkX5L5F1eTX1jkXlsTXHeux_f2o859IB_&uipk=5&nbs=1&deadline=1608914691&gen=playurl&os=akam&oi=804448936&trid=d697b9bd157047d3b707d7947dd31300p&platform=pc&upsig=7ad001cfe529ec18fff23c839585379d&uparams=e,uipk,nbs,deadline,gen,os,oi,trid,platform&hdnts=exp=1608907491~hmac=7ded3fc4f1cdae84ded04e88628c0e246f7ca3b42eec19539ac9d272a654ed7a&mid=0&orderid=0,1&agrr=0&logo=80000000', 'order': 1, 'md5': ''}], 'seek_param': 'start', 'is_preview': 0, 'no_rexcode': 0, 'format': 'flv', 'fnval': 0, 'video_project': True, 'fnver': 0, 'support_formats': [{'display_desc': '1080P', 'superscript': '高码率', 'need_login': True, 'format': 'hdflv2', 'description': '高清 1080P+', 'need_vip': True, 'quality': 112, 'new_description': '1080P 高码率'}, {'display_desc': '1080P', 'superscript': '', 'need_login': True, 'format': 'flv', 'description': '高清 1080P', 'quality': 80, 'new_description': '1080P 高清'}, {'display_desc': '720P', 'superscript': '', 'need_login': True, 'format': 'flv720', 'description': '高清 720P', 'quality': 64, 'new_description': '720P  高清'}, {'display_desc': '480P', 'superscript': '', 'format': 'flv480', 'description': '清晰 480P', 'quality': 32, 'new_description': '480P 清晰'}, {'display_desc': '360P', 'superscript': '', 'format': 'mp4', 'description': '流畅 360P', 'quality': 16, 'new_description': '360P 流畅'}], 'message': '', 'type': 'FLV', 'accept_quality': [112, 80, 64, 32, 16], 'bp': 0, 'quality': 80, 'timelength': 1467132, 'result': 'suee', 'seek_type': 'offset', 'has_paid': False, 'from': 'local', 'video_codecid': 7, 'accept_description': ['高清 1080P+', '高清 1080P', '高清 720P', '清晰 480P', '流畅 360P'], 'status': 2}}
{'code': 0, 'message': 'success', 'result': {'accept_format': 'hdflv2,flv,flv720,flv480,mp4', 'code': 0, 'durl': [{'size': 194783612, 'ahead': '', 'length': 1467111, 'vhead': '', 'backup_url': [], 'url': 'https://upos-hz-mirrorakam.akamaized.net/upgcxcode/52/25/229872552/229872552_nb2-1-80.flv?e=ig8euxZM2rNcNbhzhwdVhoMzhzdVhwdEto8g5X10ugNcXBlqNxHxNEVE5XREto8KqJZHUa6m5J0SqE85tZvEuENvNo8g2ENvNo8i8o859r1qXg8xNEVE5XREto8GuFGv2U7SuxI72X6fTr859r1qXg8gNEVE5XREto8z5JZC2X2gkX5L5F1eTX1jkXlsTXHeux_f2o859IB_&uipk=5&nbs=1&deadline=1608914692&gen=playurl&os=akam&oi=804448936&trid=75304b584f944d9f971843efff836cf8p&platform=pc&upsig=26c1909ad49949baa2857d2141783847&uparams=e,uipk,nbs,deadline,gen,os,oi,trid,platform&hdnts=exp=1608907492~hmac=95b3470050279ab84ab0f52940bbcc39e656535764e1cc2fff49daf8cbb01611&mid=0&orderid=0,1&agrr=0&logo=80000000', 'order': 1, 'md5': ''}], 'seek_param': 'start', 'is_preview': 0, 'no_rexcode': 0, 'format': 'flv', 'fnval': 0, 'video_project': True, 'fnver': 0, 'support_formats': [{'display_desc': '1080P', 'superscript': '高码率', 'need_login': True, 'format': 'hdflv2', 'description': '高清 1080P+', 'need_vip': True, 'quality': 112, 'new_description': '1080P 高码率'}, {'display_desc': '1080P', 'superscript': '', 'need_login': True, 'format': 'flv', 'description': '高清 1080P', 'quality': 80, 'new_description': '1080P 高清'}, {'display_desc': '720P', 'superscript': '', 'need_login': True, 'format': 'flv720', 'description': '高清 720P', 'quality': 64, 'new_description': '720P  高清'}, {'display_desc': '480P', 'superscript': '', 'format': 'flv480', 'description': '清晰 480P', 'quality': 32, 'new_description': '480P 清晰'}, {'display_desc': '360P', 'superscript': '', 'format': 'mp4', 'description': '流畅 360P', 'quality': 16, 'new_description': '360P 流畅'}], 'message': '', 'type': 'FLV', 'accept_quality': [112, 80, 64, 32, 16], 'bp': 0, 'quality': 80, 'timelength': 1467111, 'result': 'suee', 'seek_type': 'offset', 'has_paid': False, 'from': 'local', 'video_codecid': 7, 'accept_description': ['高清 1080P+', '高清 1080P', '高清 720P', '清晰 480P', '流畅 360P'], 'status': 2}}
{'code': 0, 'message': 'success', 'result': {'accept_format': 'hdflv2,flv,flv720,flv480,mp4', 'code': 0, 'durl': [{'size': 204225713, 'ahead': '', 'length': 1467131, 'vhead': '', 'backup_url': [], 'url': 'https://upos-hz-mirrorakam.akamaized.net/upgcxcode/39/48/232174839/232174839_nb2-1-80.flv?e=ig8euxZM2rNcNbhM7zUVhoMz7wuBhwdEto8g5X10ugNcXBlqNxHxNEVE5XREto8KqJZHUa6m5J0SqE85tZvEuENvNo8g2ENvNo8i8o859r1qXg8xNEVE5XREto8GuFGv2U7SuxI72X6fTr859r1qXg8gNEVE5XREto8z5JZC2X2gkX5L5F1eTX1jkXlsTXHeux_f2o859IB_&uipk=5&nbs=1&deadline=1608914693&gen=playurl&os=akam&oi=804448936&trid=baec4952993e4b318803cdc598c89ba7p&platform=pc&upsig=d531b6503c052fdd39c318d280ac3156&uparams=e,uipk,nbs,deadline,gen,os,oi,trid,platform&hdnts=exp=1608907493~hmac=13b3c23cecb6b7e18b9f19ecd22712120a448c968f72a39252a830a2d1fdb14c&mid=0&orderid=0,1&agrr=0&logo=80000000', 'order': 1, 'md5': ''}], 'seek_param': 'start', 'is_preview': 0, 'no_rexcode': 0, 'format': 'flv', 'fnval': 0, 'video_project': True, 'fnver': 0, 'support_formats': [{'display_desc': '1080P', 'superscript': '高码率', 'need_login': True, 'format': 'hdflv2', 'description': '高清 1080P+', 'need_vip': True, 'quality': 112, 'new_description': '1080P 高码率'}, {'display_desc': '1080P', 'superscript': '', 'need_login': True, 'format': 'flv', 'description': '高清 1080P', 'quality': 80, 'new_description': '1080P 高清'}, {'display_desc': '720P', 'superscript': '', 'need_login': True, 'format': 'flv720', 'description': '高清 720P', 'quality': 64, 'new_description': '720P  高清'}, {'display_desc': '480P', 'superscript': '', 'format': 'flv480', 'description': '清晰 480P', 'quality': 32, 'new_description': '480P 清晰'}, {'display_desc': '360P', 'superscript': '', 'format': 'mp4', 'description': '流畅 360P', 'quality': 16, 'new_description': '360P 流畅'}], 'message': '', 'type': 'FLV', 'accept_quality': [112, 80, 64, 32, 16], 'bp': 0, 'quality': 80, 'timelength': 1467131, 'result': 'suee', 'seek_type': 'offset', 'has_paid': False, 'from': 'local', 'video_codecid': 7, 'accept_description': ['高清 1080P+', '高清 1080P', '高清 720P', '清晰 480P', '流畅 360P'], 'status': 2}}
{'code': 0, 'message': 'success', 'result': {'accept_format': 'hdflv2,flv,flv720,flv480,mp4', 'code': 0, 'durl': [{'size': 196094621, 'ahead': '', 'length': 1467132, 'vhead': '', 'backup_url': [], 'url': 'https://upos-hz-mirrorakam.akamaized.net/upgcxcode/13/82/234388213/234388213_nb2-1-80.flv?e=ig8euxZM2rNcNbhzhbUVhoMzhzNBhwdEto8g5X10ugNcXBlqNxHxNEVE5XREto8KqJZHUa6m5J0SqE85tZvEuENvNo8g2ENvNo8i8o859r1qXg8xNEVE5XREto8GuFGv2U7SuxI72X6fTr859r1qXg8gNEVE5XREto8z5JZC2X2gkX5L5F1eTX1jkXlsTXHeux_f2o859IB_&uipk=5&nbs=1&deadline=1608914694&gen=playurl&os=akam&oi=804448936&trid=b1e871017f114c0fb5f5875abc6bfb88p&platform=pc&upsig=122dfb34e344fce706b64d236b71ebea&uparams=e,uipk,nbs,deadline,gen,os,oi,trid,platform&hdnts=exp=1608907494~hmac=2d4459a6b4e6872e3e335ff33d0f77385eb05defacc186f17144f9336ee25aed&mid=0&orderid=0,1&agrr=0&logo=80000000', 'order': 1, 'md5': ''}], 'seek_param': 'start', 'is_preview': 0, 'no_rexcode': 0, 'format': 'flv', 'fnval': 0, 'video_project': True, 'fnver': 0, 'support_formats': [{'display_desc': '1080P', 'superscript': '高码率', 'need_login': True, 'format': 'hdflv2', 'description': '高清 1080P+', 'need_vip': True, 'quality': 112, 'new_description': '1080P 高码率'}, {'display_desc': '1080P', 'superscript': '', 'need_login': True, 'format': 'flv', 'description': '高清 1080P', 'quality': 80, 'new_description': '1080P 高清'}, {'display_desc': '720P', 'superscript': '', 'need_login': True, 'format': 'flv720', 'description': '高清 720P', 'quality': 64, 'new_description': '720P  高清'}, {'display_desc': '480P', 'superscript': '', 'format': 'flv480', 'description': '清晰 480P', 'quality': 32, 'new_description': '480P 清晰'}, {'display_desc': '360P', 'superscript': '', 'format': 'mp4', 'description': '流畅 360P', 'quality': 16, 'new_description': '360P 流畅'}], 'message': '', 'type': 'FLV', 'accept_quality': [112, 80, 64, 32, 16], 'bp': 0, 'quality': 80, 'timelength': 1467132, 'result': 'suee', 'seek_type': 'offset', 'has_paid': False, 'from': 'local', 'video_codecid': 7, 'accept_description': ['高清 1080P+', '高清 1080P', '高清 720P', '清晰 480P', '流畅 360P'], 'status': 2}}
{'code': 0, 'message': 'success', 'result': {'accept_format': 'hdflv2,flv,flv720,flv480,mp4', 'code': 0, 'durl': [{'size': 194190468, 'ahead': '', 'length': 1467217, 'vhead': '', 'backup_url': [], 'url': 'https://upos-hz-mirrorakam.akamaized.net/upgcxcode/18/22/236572218/236572218_nb2-1-80.flv?e=ig8euxZM2rNcNbhzhwdVhoMzhzdVhwdEto8g5X10ugNcXBlqNxHxNEVE5XREto8KqJZHUa6m5J0SqE85tZvEuENvNo8g2ENvNo8i8o859r1qXg8xNEVE5XREto8GuFGv2U7SuxI72X6fTr859r1qXg8gNEVE5XREto8z5JZC2X2gkX5L5F1eTX1jkXlsTXHeux_f2o859IB_&uipk=5&nbs=1&deadline=1608914694&gen=playurl&os=akam&oi=804448936&trid=ec853320bf784381bd44eba34641f5fbp&platform=pc&upsig=1d58945e2f18bb13ebee24b28806ee35&uparams=e,uipk,nbs,deadline,gen,os,oi,trid,platform&hdnts=exp=1608907494~hmac=67d3b8df19c3445a1801ff0c216ce3d5af16f8cdc718eef383ec99f8770d81e4&mid=0&orderid=0,1&agrr=0&logo=80000000', 'order': 1, 'md5': ''}], 'seek_param': 'start', 'is_preview': 0, 'no_rexcode': 0, 'format': 'flv', 'fnval': 0, 'video_project': True, 'fnver': 0, 'support_formats': [{'display_desc': '1080P', 'superscript': '高码率', 'need_login': True, 'format': 'hdflv2', 'description': '高清 1080P+', 'need_vip': True, 'quality': 112, 'new_description': '1080P 高码率'}, {'display_desc': '1080P', 'superscript': '', 'need_login': True, 'format': 'flv', 'description': '高清 1080P', 'quality': 80, 'new_description': '1080P 高清'}, {'display_desc': '720P', 'superscript': '', 'need_login': True, 'format': 'flv720', 'description': '高清 720P', 'quality': 64, 'new_description': '720P  高清'}, {'display_desc': '480P', 'superscript': '', 'format': 'flv480', 'description': '清晰 480P', 'quality': 32, 'new_description': '480P 清晰'}, {'display_desc': '360P', 'superscript': '', 'format': 'mp4', 'description': '流畅 360P', 'quality': 16, 'new_description': '360P 流畅'}], 'message': '', 'type': 'FLV', 'accept_quality': [112, 80, 64, 32, 16], 'bp': 0, 'quality': 80, 'timelength': 1467217, 'result': 'suee', 'seek_type': 'offset', 'has_paid': False, 'from': 'local', 'video_codecid': 7, 'accept_description': ['高清 1080P+', '高清 1080P', '高清 720P', '清晰 480P', '流畅 360P'], 'status': 2}}
{'code': 0, 'message': 'success', 'result': {'accept_format': 'hdflv2,flv,flv720,flv480,mp4', 'code': 0, 'durl': [{'size': 206972216, 'ahead': '', 'length': 1437158, 'vhead': '', 'backup_url': [], 'url': 'https://upos-hz-mirrorakam.akamaized.net/upgcxcode/55/60/238956055/238956055_nb2-1-80.flv?e=ig8euxZM2rNcNbhjhwdVhoMz7bdVhwdEto8g5X10ugNcXBlqNxHxNEVE5XREto8KqJZHUa6m5J0SqE85tZvEuENvNo8g2ENvNo8i8o859r1qXg8xNEVE5XREto8GuFGv2U7SuxI72X6fTr859r1qXg8gNEVE5XREto8z5JZC2X2gkX5L5F1eTX1jkXlsTXHeux_f2o859IB_&uipk=5&nbs=1&deadline=1608914695&gen=playurl&os=akam&oi=804448936&trid=6a45c1d168d245a4b61ae9c6e23fe577p&platform=pc&upsig=a1e6d500cc42f932a233cc928f1adeef&uparams=e,uipk,nbs,deadline,gen,os,oi,trid,platform&hdnts=exp=1608907495~hmac=b4f5c267a284cd3d09f15892147448b8b1526191e669effae7f08f9564408885&mid=0&orderid=0,1&agrr=0&logo=80000000', 'order': 1, 'md5': ''}], 'seek_param': 'start', 'is_preview': 0, 'no_rexcode': 0, 'format': 'flv', 'fnval': 0, 'video_project': True, 'fnver': 0, 'support_formats': [{'display_desc': '1080P', 'superscript': '高码率', 'need_login': True, 'format': 'hdflv2', 'description': '高清 1080P+', 'need_vip': True, 'quality': 112, 'new_description': '1080P 高码率'}, {'display_desc': '1080P', 'superscript': '', 'need_login': True, 'format': 'flv', 'description': '高清 1080P', 'quality': 80, 'new_description': '1080P 高清'}, {'display_desc': '720P', 'superscript': '', 'need_login': True, 'format': 'flv720', 'description': '高清 720P', 'quality': 64, 'new_description': '720P  高清'}, {'display_desc': '480P', 'superscript': '', 'format': 'flv480', 'description': '清晰 480P', 'quality': 32, 'new_description': '480P 清晰'}, {'display_desc': '360P', 'superscript': '', 'format': 'mp4', 'description': '流畅 360P', 'quality': 16, 'new_description': '360P 流畅'}], 'message': '', 'type': 'FLV', 'accept_quality': [112, 80, 64, 32, 16], 'bp': 0, 'quality': 80, 'timelength': 1437158, 'result': 'suee', 'seek_type': 'offset', 'has_paid': False, 'from': 'local', 'video_codecid': 7, 'accept_description': ['高清 1080P+', '高清 1080P', '高清 720P', '清晰 480P', '流畅 360P'], 'status': 2}}
D:\xxx\SimpleCoding\AnimeDownload\master\aria2c.exe --referer="https://www.bilibili.com/" --input-file="D:/xxx/SimpleCoding/AnimeDownload/master/AnimeDownload\s33865.txt" --file-allocation=falloc --dir="D:/xxx/SimpleCoding/AnimeDownload/master/AnimeDownload\s33865-出租女友（僅限港澳台地區）" -c --max-concurrent-downloads=8 --split=20 --load-cookies=D:\xxx\SimpleCoding\AnimeDownload\master\bilibili.cookies --max-connection-per-server=16 --user-agent=Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36

12/25 20:44:54 [NOTICE] Downloading 12 item(s)

Download Results:
gid   |stat|avg speed  |path/URI
======+====+===========+=======================================================
239fa3|OK  |   0.9MiB/s|D:/xxx/SimpleCoding/AnimeDownload/master/AnimeDownload/s33865-出租女友（僅限港澳台地區）/01 出租女友.flv
5523df|OK  |   0.9MiB/s|D:/xxx/SimpleCoding/AnimeDownload/master/AnimeDownload/s33865-出租女友（僅限港澳台地區）/05 溫泉和女友.flv
9e771d|OK  |   903KiB/s|D:/xxx/SimpleCoding/AnimeDownload/master/AnimeDownload/s33865-出租女友（僅限港澳台地區）/06 女友與女友.flv
093e8c|OK  |   862KiB/s|D:/xxx/SimpleCoding/AnimeDownload/master/AnimeDownload/s33865-出租女友（僅限港澳台地區）/07 暫時女友與女友.flv
2de9c0|OK  |   849KiB/s|D:/xxx/SimpleCoding/AnimeDownload/master/AnimeDownload/s33865-出租女友（僅限港澳台地區）/08 聖誕節與女友.flv
d16685|OK  |   857KiB/s|D:/xxx/SimpleCoding/AnimeDownload/master/AnimeDownload/s33865-出租女友（僅限港澳台地區）/04 朋友和女友.flv
b96ed1|OK  |   792KiB/s|D:/xxx/SimpleCoding/AnimeDownload/master/AnimeDownload/s33865-出租女友（僅限港澳台地區）/02 前女友與女友.flv
14cb69|OK  |   813KiB/s|D:/xxx/SimpleCoding/AnimeDownload/master/AnimeDownload/s33865-出租女友（僅限港澳台地區）/03 海與女友.flv
70c633|OK  |   2.1MiB/s|D:/xxx/SimpleCoding/AnimeDownload/master/AnimeDownload/s33865-出租女友（僅限港澳台地區）/11 真相與女友.flv
6cdd51|OK  |   1.4MiB/s|D:/xxx/SimpleCoding/AnimeDownload/master/AnimeDownload/s33865-出租女友（僅限港澳台地區）/09 謊言與女友.flv
1a7868|OK  |   1.4MiB/s|D:/xxx/SimpleCoding/AnimeDownload/master/AnimeDownload/s33865-出租女友（僅限港澳台地區）/10 朋友的女友.flv
33cb67|OK  |   2.0MiB/s|D:/xxx/SimpleCoding/AnimeDownload/master/AnimeDownload/s33865-出租女友（僅限港澳台地區）/12 告白與女友.flv

Status Legend:
(OK):download completed.
Animation Download Process Finished.
Press Enter to exit.


```

但根据其他人的测试哔哩哔哩在前端js里可能添加了识别当前ip的脚本导致无法在网页上播放。
可以尝试禁用那一段js，或者通过扩展修改js。


### app的测试结果

referer：https://github.com/SocialSisterYi/bilibili-API-collect/blob/master/other/API_auth.md

```python
    #url = "https://app.bilibili.com/x/playurl"
    url = "https://173583120xxxxxx7.cn-hongkong.fc.aliyuncs.com/2016-08-15/proxy/bili/removelimit/" # 地址已隐藏
    ts = int(time.time())

    
    # 测试中 忧国的莫里亚蒂（限定） 第一集-直接改（失败）
    #body = f"access_key=xxxxx35fac7cc6cc12b98325b53020c1&aid=627455788&appkey=iVGUTjsxvpLeuDCf&build=5370000&buvid=XY412F34F7C09E5D417D5BDACC727A3258263&cid=253193011&device=android&expire=1597289802&fnval=0&fnver=0&force_host=0&mid=688418886&mobi_app=android&npcybs=0&otype=json&platform=android&qn=80&ts={ts}"
    
    # 测试中 忧国的莫里亚蒂（限定） 第一集-类似改（失败）
    #body = "access_key=xxxxx3669686a5c264ed64e651c63c71&aid=627455788&appkey=iVGUTjsxvpLeuDCf&build=5370000&buvid=XXD9E43D7A1EBB6669597650E3EE417D9E7F5&cid=253193011&device=android&expire=1597289802&fnval=0&fnver=0&force_host=0&mid=688418886&mobi_app=android&npcybs=0&otype=json&platform=android&qn=112&ts=1594974158"
    # 测试中 在魔王城说晚安（限定） 第十一集-类似改（失败）有可能是body不对
    #body = "access_key=xxxxx3669686a5c264ed64e651c63c71&aid=330714489&appkey=iVGUTjsxvpLeuDCf&build=5370000&buvid=XXD9E43D7A1EBB6669597650E3EE417D9E7F5&cid=266547816&device=android&expire=1597289802&fnval=0&fnver=0&force_host=0&mid=688418886&mobi_app=android&npcybs=0&otype=json&platform=android&qn=112&ts=1594974158"
    #res = {'code': -404, 'message': '啥都木有', 'ttl': 1, 'data': None}(~~有可能是国家不对~~)

    # succeed 原始
    #body = "access_key=xxxxx3669686a5c264ed64e651c63c71&aid=99999999&appkey=iVGUTjsxvpLeuDCf&build=5370000&buvid=XXD9E43D7A1EBB6669597650E3EE417D9E7F5&cid=171776208&device=android&expire=1597289802&fnval=0&fnver=0&force_host=0&mid=174438027&mobi_app=android&npcybs=0&otype=json&platform=android&qn=112&ts=1594974158"
    
    # succeed oneroom第三季第一集(国内)
    #body = "access_key=xxxxx3669686a5c264ed64e651c63c71&aid=884840446&appkey=iVGUTjsxvpLeuDCf&build=5370000&buvid=XXD9E43D7A1EBB6669597650E3EE417D9E7F5&cid=244951054&device=android&expire=1597289802&fnval=0&fnver=0&force_host=0&mid=928123&mobi_app=android&npcybs=0&otype=json&platform=android&qn=112&ts=1594974158"
    #res = {'code': -404, 'message': '啥都木有', 'ttl': 1, 'data': None} (国外网址)
    #res = {xxx}（国内网址，可以正常解析）

    # 出租女友（香港可以） av456273732  md: 28229298
    #body = "access_key=xxxxx3669686a5c264ed64e651c63c71&aid=456273732&appkey=iVGUTjsxvpLeuDCf&build=5370000&buvid=XXD9E43D7A1EBB6669597650E3EE417D9E7F5&cid=222747655&device=android&expire=1597289802&fnval=0&fnver=0&force_host=0&mid=11783021&mobi_app=android&npcybs=0&otype=json&platform=android&qn=112&ts=1594974158"
    # 香港ali实验成功！！！！

    body_result = CalcSign("iVGUTjsxvpLeuDCf", "aHRmhWMLkdeMuILqORnYZocwMBpMEOdt", body)
    url = url + "?" + body_result
    res = json.loads(requests.get(url).text)
    print(url)
    print(res)

```

app的参数表

link: https://github.com/1299172402/Anti-Bilibili-Animation-limit/blob/main/get_access_key.py

main()获得access_key

test()测试用

```
https://app.bilibili.com/x/playurl?
access_key=xxxxx3669686a5c264ed64e651c63c71 验证密钥
aid=99999999
appkey=iVGUTjsxvpLeuDCf 扫码后登录可以得到
build=5370000 
#build      | num  | 版本         | APP方式必要 | 可为`6082000` |
buvid=XXD9E43D7A1EBB6669597650E3EE417D9E7F5
      XY412F34F7C09E5D417D5BDACC727A3258263
#| buvid  | str  | 设备ID  | 非必要 | 为操作登录接口时Cookie中的`buvid3`可为任意值 |
从https://www.bilibili.com/h5/validate/device的f12
https://api.bilibili.com/x/safecenter/user_devices?csrf=a16ee5026cdb94845b29b759d75aeb71&local_id=342abf29fedaf70e5758b0340c62c122&bili_local_id=C156972D961DB1F4B66177FFA555CDF2201909102109189BD41BD05E8324BD29的查询
cid=171776208
device=android
expire=1597289802
| expire        | num  | 到期时间？           | 时间戳？<br />作用尚不明确    
fnval=0
fnver=0
force_host=0
mid=174438027
目标用户uid
http://api.bilibili.com/x/web-interface/view?aid=xxxxxx可以查询
mobi_app=android
npcybs=0
otype=json
platform=android
qn=32
ts=1594974158 
sign=b10febf17d65fb76cd3102006ef8318f

这个你要先给参数按照key排序，再计算。

Welcome to Bilibili Animation Download
Creative By ZhiyuShang With LOVE
[Referer](https://github.com/1299172402/AnimeDownload)
md: 28230147
https://api.bilibili.com/pgc/web/season/section?season_id=34643
{'aid': 627455788, 'cid': 253193011, 'title': '01 伯爵的犯罪'}
{'aid': 457466778, 'cid': 246625128, 'title': '02 緋色之瞳 第一幕'}
{'aid': 627592518, 'cid': 248726680, 'title': '03 緋色之瞳 第二幕'}
{'aid': 202532216, 'cid': 250890489, 'title': '04 稀少的種子'}
{'aid': 457700991, 'cid': 253081767, 'title': '05 橋上的舞者'}
{'aid': 800316414, 'cid': 255348592, 'title': '06 諾亞提克號事件 第一幕'}
{'aid': 372823745, 'cid': 257739968, 'title': '07 諾亞提克號事件 第二幕'}
{'aid': 542949771, 'cid': 260195069, 'title': '08 夏洛克 · 福爾摩斯的研究 第一幕'}
{'aid': 670619534, 'cid': 262674687, 'title': '09 夏洛克 · 福爾摩斯的研究 第二幕'}
{'aid': 458077121, 'cid': 265355153, 'title': '10 兩名偵探 第一幕'}
{'aid': 330713495, 'cid': 268029852, 'title': '11 兩名偵探 第二幕'}


C:\Users\2184232017>python D:\xxx\SimpleCoding\tv.danmaku.bili\get_access_key.py
------ QRcodeURL BEGIN ------
https://passport.bilibili.com/x/passport-tv-login/h5/qrcode/auth?auth_code=6dc710c01527b618beb93c384bfafb01
------ QRcodeURL END ------
[auth_code] 6dc710c01527b618beb93c384bfafb01
Are you scan finished?[Enter]
[uid] xxxx66638
[access_key] xxxxxxxfac7cc6cc12b98325b53020c1
[refresh_token] xxxx2f500ea99f248f2d787439160fc1


One Room
Welcome to Bilibili Animation Download
Creative By ZhiyuShang With LOVE
[Referer](https://github.com/1299172402/AnimeDownload)
md: 28230234
https://api.bilibili.com/pgc/web/season/section?season_id=34715
{'aid': 884840446, 'cid': 244951054, 'title': '01 琴川晶很亲切'}
{'aid': 842418806, 'cid': 244948454, 'title': '02 琴川晶很在意'}
{'aid': 800023156, 'cid': 247319897, 'title': '03 琴川晶没有说'}
{'aid': 202548488, 'cid': 249710071, 'title': '04 琴川晶培育中'}
{'aid': 372627787, 'cid': 251947200, 'title': '05 桃原奈月要说服'}
{'aid': 797687309, 'cid': 254365005, 'title': '06 七桥御乃梨向前迈步'}
{'aid': 585359497, 'cid': 256453542, 'title': '07 织崎纱耶要谢罪'}
{'aid': 885402308, 'cid': 258959056, 'title': '08 织崎纱耶在应援'}
{'aid': 585419844, 'cid': 261411032, 'title': '09 织崎纱耶察觉到'}
{'aid': 628109165, 'cid': 263963363, 'title': '10 织崎纱耶打扰了'}
{'aid': 203171289, 'cid': 266627051, 'title': '11 花坂结衣吓一跳'}
{'aid': 843218847, 'cid': 269269571, 'title': '12 花坂结衣在身边'}

```
