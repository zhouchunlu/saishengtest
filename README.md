# RankList 排行榜服务
### 1、客户端上传客户端号和分数(注意：并不会上传排名,客户端无法上传排名),同一个客户端可以多次上传分数，取最新的一次分数
```python
url：rankapi/rank
method: POST
body:{
        "client":"客户端1", //客户端号，必填
        "score":1000       //分数，必填，1...10000000
    }
result:
    {
        "code": 0,          //状态码
        "msg": "SUCCESS",   //信息
        "datetime": "2020-04-28 23:46:02"  //时间
    }
```
### 2、客户端查询排行榜
```python
url：rankapi/rank
method: GET
param：
    client："客户端1"  //客户端号，必填
    start：  1        //排名开始名次， 可缺省， 默认为1
    end：10           //排名结束名次， 可缺省， 默认为10
result：
    {
        "code": 0,                          //状态码
        "msg": "SUCCESS",                   //信息
        "datetime": "2020-04-29 00:29:09",  //时间
        "data": [
            {
                "rank": 1,                  //排名
                "client": "客户端3",         //客户端号
                "score": 1003               //分数
            },
            {
                "rank": 2,
                "client": "客户端2",
                "score": 1002
            },
            {
                "rank": 3,
                "client": "客户端1",
                "score": 1000
            },
            {
                "rank": 1,
                "client": "客户端3",
                "score": 1003
            }
        ]
    }
```
# compareVersion 版本比较
## compareVersion.py
