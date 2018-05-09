###基于cookie的简易签到

> 可配合crontab进行京东自动领金币,贴吧自动签到,smzdm自动签到等

1. chrome安装[EditThisCooike](https://chrome.google.com/webstore/detail/editthiscookie/fngmhnnpilhplaeedifhccceomclgfbg/reviews)插件
2. 使用 EditThisCooike 复制cookie到粘贴板 ![](http://ww3.sinaimg.cn/large/633e0588jw1f6ahc8i0mnj20um0yy42o.jpg)
3. 把复制的cookie粘贴到目录 cookie/<site-name>.json, 例如: cookie/tieba.json
4. 修改sign.py文件,为字典 sign_dict 增加元素 ![](http://ww4.sinaimg.cn/large/633e0588jw1f6ahis8g1kj20n1081dgn.jpg)

