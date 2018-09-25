import random
class suiji():
    def suijis(self):

        name = ['梦妍', '丽娜']
        mission = ['基本内容', '费用预算']
        for n in name:
            m = random.choice(mission)
            print(n+'的任务是'+m)
            mission.remove(m)
if __name__ == '__main__':
     suiji().suijis()