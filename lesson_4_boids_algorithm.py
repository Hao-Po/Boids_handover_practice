"""
這個練習融合了lesson1-3, 綜合這些技能 加上 import已經幫你寫好的function
可以寫出boids_algorithmn的三個行為function

group是個存放UAV的dictionary, 長相如下
group = {
    "UAV01" : {
        "drone_id" : int,
        "drone" : Boid()
    },

    "UAV02" : {
        "drone_id" : int,
        "drone" : Boid()
    },

    "UAV03" : {
        "drone_id" : int,
        "drone" : Boid()
    },
}
"""
from lesson_4_lat_long_distance import lat_long_distance

distance_function = lat_long_distance()

class Coordinate:
    def __init__(self, longitude=0.0, latitude=0.0, altitude=0.0):
        self.longitude = longitude
        self.latitude = latitude
        self.altitude = altitude

class Velocity:
    def __init__(self, velocity_x=0.0, velocity_y=0.0, velocity_z=0.0):
        self.velocity_x = velocity_x
        self.velocity_y = velocity_y
        self.velocity_z = velocity_z

class Boid:
    def __init__(self, longitude, latitude, altitude, velocity_x, velocity_y, velocity_z):
        """
        Boid這個class有6個內參數, 在宣告的時候藉由外部參數引入初始化:
        1. longitude 
        2. latitude 
        3. altitude 
        4. velocity_x 
        5. velocity_y 
        6. velocity_z
        """
        # 初始化/宣告 class mumber的位置
        ...


    def cohesion(self, group):
        # 完成boids_cohesion行為, 藉由給定的group, 算出該集中的位置(3維:含經度、緯度、高度), 並且return回去
        # 注意group的型態, 能運算的東西在哪裡, 怎麼取出來

        cohesion_point = Coordinate(0.0, 0.0, 0.0)
        
        ...
        
        return cohesion_point

    def alignment(self, group):
        # 完成boids_alignment行為, 藉由給定的group, 算出該的平均速度方向(3維:含velocity_x、velocity_y、velocity_z), 並且return回去
        # 注意group的型態, 能運算的東西在哪裡, 怎麼取出來

        alignment_velocity = Velocity(0.0, 0.0, 0.0)

        ...

        return alignment_velocity
    
    def separation(self, group):
        # 完成boids_separation行為, 藉由給定的group, 算出該迴避的速度方向(2維:velocity_x、velocity_y), 並且return回去
        # 注意group的型態, 能運算的東西在哪裡, 怎麼取出來, 無人機之間的距離怎麼算
        # 注意: 迴避向量算法 (點-點)、要倒數(距離越近、迴避速度越大)、小心分母=0

        separation_velocity = Velocity(0.0, 0.0, 0.0)
        minDistance = 3
        
        ...
        
        return separation_velocity