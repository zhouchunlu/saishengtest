import json

from django.http import JsonResponse
from django.views import View

from rank.MyEncoder import MyEncoder
from rank.models import RankModel
from django_redis import get_redis_connection

RANK_KEY = "rank"


class RankView(View):
    """
    客户端上传客户端号和分数(注意：并不会上传排名,客户端无法上传排名),同一个客户端可以多次上传分数，取最新的一次分数
    客户端查询排行榜
    """

    def get(self, request):

        result = {
            "code": 1,
            "msg": "ERROR"
        }
        try:
            client = request.GET['client']
            start = int(request.GET['start'])
            end = int(request.GET['end'])

            if not client:
                result['code'] = 10001
                result['msg'] = "client param is null, please check it!"
                return JsonResponse(result)
            if not start:
                start = 1
            if not end:
                end = 10

            conn = get_redis_connection('default')

            client_rank = conn.zrevrank(RANK_KEY, client)
            client_score = conn.zscore(RANK_KEY, client)
            if client_rank and client_score:
                sort_result = conn.zrevrange(RANK_KEY, start-1, end-1, withscores=True, score_cast_func=int)

                data = []
                for i in range(len(sort_result)):
                    client_i, score_i = sort_result[i]
                    data.append({
                        "rank": int(start) + i,
                        "client": client_i,
                        "score": score_i
                    })

                data.append({
                        "rank": int(client_rank)+1,
                        "client": client,
                        "score": int(client_score)
                    })
                result.update({
                    "data": data
                })
                result['code'] = 0
                result['msg'] = "SUCCESS"
            else:
                result['code'] = 10002
                result['msg'] = "client not exists!"
                return JsonResponse(result)
        except Exception as e:
            result['msg'] = repr(e)

        return JsonResponse(result, encoder=MyEncoder)

    def post(self, request):
        result = {
            "code": 1,
            "msg": "ERROR"
        }
        try:
            data = json.loads(request.body)
            client = data.get("client")
            score = data.get("score")

            if client and score:
                rank_model = RankModel(client=client, score=score)
                rank_model.save()

                conn = get_redis_connection('default')
                score_old = conn.zscore(RANK_KEY, client)
                if not score_old:
                    conn.zadd(RANK_KEY, {client: score})
                elif score > score_old:
                    conn.zadd(RANK_KEY, {client: score})
                else:
                    pass

                result = {
                    "code": 0,
                    "msg": "SUCCESS"
                }
        except Exception as e:
            result['msg'] = repr(e)

        return JsonResponse(result)
