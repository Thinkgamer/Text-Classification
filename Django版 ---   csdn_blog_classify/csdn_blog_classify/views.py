#coding:utf8
from django.http import HttpResponse
from django.template import loader,Context
import result_classify
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def show(request):
    if request.method=="POST":
        try:
            title = request.POST.get('title')
            content = request.POST.get('content')
            tag = request.POST.get('tag')
            selfcate = request.POST.get('selfcate')
        except:
            pass

        fp = open("csdn_blog_classify/content.txt","w")
        fp.write(title.encode('utf8')+"\n"+content.encode('utf8')+"\n"+tag.encode('utf8'))
        fp.close()

        result = result_classify.result()
        print selfcate
        if not selfcate:
            iforno = "你没有填写个人分类"
        elif str(selfcate.lower()) in str(result.lower()):
            iforno="Right"
        else:
            iforno="Wrong"

        t =loader.get_template('index.html')
        c = Context({
            "result":result,
            "iforno":iforno,
        })
        return HttpResponse(t.render(c))


    else:
        t =loader.get_template('index.html')
        c = Context({

        })
        return HttpResponse(t.render(c))