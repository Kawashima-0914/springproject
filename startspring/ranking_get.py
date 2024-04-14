import csv
import os
#views.pyで使用する


#温泉のランキングが格納されているpathを引数として受け取り、温泉の順位と温泉名と所在地を保持するクラス
class Ranking_get():
    ranking_inf = []

    def __init__(self, ranking_path):
        self.ranking_path = ranking_path

    def list_get(self):
        os.chdir("C:\\Users\\Owner\\python_practice\\spring_rank")
        with open(self.ranking_path, 'r', encoding='UTF-8') as f:
            reader = csv.reader(f)
            i = 0
            for data in reader:
                if i % 2 == 0 and i != 0:
                    if '\u3000' in data[1]:
                        data[1] = data[1].replace('\u3000', '')
                    self.ranking_inf.append(data[0])
                    self.ranking_inf.append(data[1])
                    self.ranking_inf.append(data[2])
                i += 1

    
#inf = []
#sample = Ranking_get("total_rank.csv")
#sample.list_get()
#inf.append(sample.ranking_inf)
#sample1 = Ranking_get("atmos_rank.csv")
#sample1.list_get()
#inf.append(sample1.ranking_inf)
#print(inf)



    
    