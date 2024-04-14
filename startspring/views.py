from typing import Any
from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import TemplateView   
import sys,  pykakasi
sys.path.append("C:\\Users\\Owner\\python_practice\\springproject\\startspring")
from ranking_get import Ranking_get
from arrange_spring import Arrange_spring



#一番初めのページへの遷移
def startspring(request):
    #リクエストがあった→温泉検索が行われた
    if request.method == "POST":
        #温泉検索で入力された温泉名をローマ字に変換
        spring_get = request.POST.get('search')
        kakasi = pykakasi.kakasi()
        kakasi.setMode('J', 'a')
        kakasi.setMode('K', 'a')
        kakasi.setMode('H', 'a')
        conversion = kakasi.getConverter()
        spring_get = conversion.do(spring_get)
        
        #全ての温泉のhtmlの名前に変換したものをリストとして保持する
        all_spring = Arrange_spring()
        all_spring_get = all_spring.same_judge #温泉のhtml名を取得
        all_spring_nameset = all_spring.name_set #温泉の名前と県のひとかたまりをkeyとした辞書を取得
        
        match = []

        same_search = {}

        #入力された温泉名が用意されている温泉名の一部において一致するものがあればmatchに格納していく
        for each_spring in all_spring_get:
            if spring_get in each_spring:
                match.append(each_spring)

        #matchの要素が1つであれば、そのままmatchの要素(html名)を持ちいてhtmlを表示する
        if len(match) == 1:
            return render(request, 'spring_each/'+match[0]+".html")
        elif len(match) == 0:#matchの要素が0であれば、検索結果に該当するものが無いことを示すhtmlを表示する
            return render(request, 'spring_noexit.html')
        else: #matchの要素が複数あれば、ユーザーに選択されるページのhtmlを表示する
            for each_spring in match:
                for key, value in all_spring_nameset.items():
                    if each_spring == value:
                        same_search[key] = value
            context = {
                'same_search': same_search,
            }
            return render(request, 'search-spring.html', context)
    else:#リクエストがなければ、start.htmlを表示する
        return render(request, 'start.html')

#contact.htmlを表示する
class Contact(TemplateView):
    template_name = 'contact.html'

#springlist.htmlを表示する
class SpringList(TemplateView):
    template_name = 'springlist.html'

#qualityexp.htmlを表示する
class QualityExp(TemplateView):
    template_name = 'qualityexp.html'

#ranking.htmlを表示する
class Ranking(TemplateView):
    template_name = 'ranking.html'

    #それぞれのランキングのファイルの情報を取得してranking.htmlに送る
    def get_context_data(self, **kwargs):
        context =  super().get_context_data(**kwargs)

        information = []

        inf = Ranking_get("total_rank.csv")
        inf.list_get()

        inf_atmos = Ranking_get("atmos_rank.csv")
        inf_atmos.list_get()

        inf_food = Ranking_get("food_rank.csv")
        inf_food.list_get()

        inf_quality = Ranking_get("quality_rank.csv")
        inf_quality.list_get()

        #それぞれのランキングを一次元配列として格納
        information = inf.ranking_inf + inf_atmos.ranking_inf + inf_food.ranking_inf + inf_quality.ranking_inf

        context["tweets"] = information
        return context

#springlistから情報を与えられ、それに応じたhtmlを返す関数
def prefecture(request):
    #kakasiは与えられた情報をローマ字に変換するため
    kakasi = pykakasi.kakasi()
    kakasi.setMode('J', 'a')
    conversion = kakasi.getConverter()
    var1 = request.POST.get('id1')
    pref = conversion.do(var1)

    return render(request, 'prefectures/'+pref+".html")  

#それぞれの温泉のhtmlを表示する(都道府県からの遷移)
def spring_each(request):
    spring_name = request.POST.get('id2')
    return render(request, 'spring_each/'+spring_name+".html")

#それぞれの温泉のhtmlを表示する(温泉検索で該当が複数あった場合の遷移)
def spring_search(request):
    each_search = request.POST.get('id3')
    return render(request, 'spring_each/'+each_search+".html")
    

