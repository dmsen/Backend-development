import  re
from .models import Guid,Article,Tag
# from django.db.models import Count
def guid_info(request):
    # 导航栏展示
    guids = Guid.objects.filter(guid_enable=True)
    # 右边的推荐区域
    tuijian = Article.objects.all().order_by('?')[0]

    # e = Article.objects.all().annotate(Count('view_times'))
    # print(e[1])
    # 热门项目区域
    allremen = Article.objects.all().order_by('view_times')[:6].reverse
    # 右边热门标签区域
    all_tag = Tag.objects.all()
    renmentag = sorted([(tag.article_set.all().count(),tag.tag_name_cn,tag.id) for tag in all_tag],reverse=True)[:12]
    # print(renmentag)
    dict = {}
    for i in renmentag:
        dict['count'] = i[0]
        dict['name']  = i[1]
        dict['id']  = i[2]
    print(dict)





    # 最近更新区域
    zuijin = Article.objects.all().order_by('publish_date')[:3].reverse



    result = re.search(r'/sub_test1/(\d+)',request.path_info)
    # 导航栏高亮显示
    if result:
        current_tag_id = result.group()[11:]
        # print(result.group()[-1])
        print(current_tag_id)

    else:
        current_tag_id = 0
    # return locals()
    # 上下文处理器传递
    return {'current_tag_id':current_tag_id,'guids':guids,'Tuijian':tuijian,'Allremen':allremen,'Renmentag':renmentag,'Zuijin':zuijin}