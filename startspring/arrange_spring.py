#全ての温泉の名前と所在地(県)を取得し、温泉毎のhtml名のリストと、温泉の名前と所在地をひとかたまりをkeyとする辞書をもつクラスを作成
#views.pyで使用する
#辞書はユーザから温泉を選択する際の「温泉名と県」をボタンの値として使うため

import sys, os
sys.path.append("C:\\Users\\Owner\\python_practice\\spring_all")
from make_list1 import List_make
import pykakasi

spring_name = []
spring_location = []

os.chdir("C:\\Users\\Owner\\python_practice\\spring_all")
List_spring = List_make()
List_spring.list_operate()
spring_name = List_spring.name
spring_location = List_spring.location

#ローマ字に変換するモデル
kakasi = pykakasi.kakasi()
kakasi.setMode('J', 'a')
kakasi.setMode('K', 'a')
kakasi.setMode('H', 'a')
conversion = kakasi.getConverter()


class Arrange_spring():
    same_judge = []
    name_set = {}
    for name, location in zip(spring_name, spring_location):
        name_data = name.split('（')

        name_con = conversion.do(name_data[0])
        name_con = name_con.replace("'", '')
        name_con = name_con.replace(" ", '')
        name_con = name_con.replace(".", '')

        if len(name_data) == 2:
            name_con2 = name_data[1]
            name_con2 = conversion.do(name_con2)
            name_con2 = name_con2.replace('）', '')
            name_con2 = name_con2.replace("'", '')
            name_con2 = name_con2.replace(" ", '')
            name_con2 = name_con2.replace(".", '')
        else:
            name_con2 = '1'

        loc_con = conversion.do(location)
        loc_con = loc_con.replace('ken', '')

        total_name = name_con + '_' + name_con2 + '_' +  loc_con
        if total_name in same_judge:
            name_con2 = '2'
        same_judge.append(total_name)
        name_set[name+"-"+location] = total_name



    


    

    