import random

from click._compat import raw_input


class suiji():
    def suijis(self):
        # name = raw_input('请输入姓名（以逗号分隔）：')
        # name = name.split('，')
        name = ['李梦妍', '陈丽娜', '郭  欣', '骆庆福', '刘志峥']
        mission = raw_input('请输入任务（以逗号分隔）：')

        mission = mission.split('，')

        for n in name:
            m = random.choice(mission)
            print(n+'的任务是'+m)
            mission.remove(m)
if __name__ == '__main__':
     suiji().suijis()