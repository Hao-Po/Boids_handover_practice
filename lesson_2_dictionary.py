"""
uav是一個dictionary
有兩個固定的key: 1. "drone_id"  2. "drone" 長相如下

uav = {
    "drone_id" : int,
    "drone" : Boid()
} 

Boid()是lesson_1寫的class
---------------------------------------------------
group是一個dictionary 
key為string型態 ex."UAV01", "UAV02"
value為dict型態, 存放uav資訊, 長相如下

group = {
    uav_name(string) : uav(dict),
    uav_name(string) : uav(dict)
}

這是一個練習dictionary操作的class
會練習到【新增】、【修改】、【刪除】、【取值】
"""


class dictionary_practice:
    def __init__(self, ):
        self.group = dict()

    def dict_add(self, uav_name, drone_id, drone):
        # 給你uav_name, drone_id, drone的value, 把它新增到group裡面 長相如上
        ...

    def dict_modify(self, uav_name, new_drone_id, new_velocity_x, new_velocity_y, new_velocity_z):
        # 給你需要修改的uav_name, 它有了新的drone_id, uav有了新的速度 把它從group裡面修改
        # 注意思考 如何修改uav的member
        ...

    def dict_del(self, uav_name):
        # 給你需要刪除的uav_name, 把它從group裡面刪除,
        # 如果刪除成功, return True
        # 如果原本uav_name並不存在group裡面, return None

        return feedback

    def dict_return_value(self, uav_name):
        # 給你uav_name, 做一個內含uav的數值的dictionary回傳
        # 長相如下:
        # uav_position = {
        #   "longitude" : ...,
        #   "latitude" : ...,
        #   "altitude" : ...
        # }

        return uav_position
