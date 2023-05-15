"""
Boid這個class有6個內參數，在宣告的時候藉由外部參數引入初始化:
1. longitude 2. latitude 3. altitude 4. velocity_x 5. velocity_y 6. velocity_z
update_position / update_velocity 這兩個Function，藉由外部參數引入修改class member的數值

寫code使這個class完整
"""



class Boid:
    def __init__(self, longitude, latitude, altitude, velocity_x, velocity_y, velocity_z):
        # 初始化/宣告 class mumber的位置
        self.longitude = longitude
        self.latitude = latitude
        self.altitude = altitude
        self.velocity_x = velocity_x
        self.velocity_y = velocity_y
        self.velocity_z = velocity_z
    
    def update_position(self, new_longitude, new_latitude, new_altitude):
        # 更新位置的Function
        self.longitude = new_longitude
        self.latitude = new_latitude
        self.altitude = new_altitude
    
    def update_velocity(self, new_velocity_x, new_velocity_y, new_velocity_z):
        # 更新速度的Function
        self.velocity_x = new_velocity_x
        self.velocity_y = new_velocity_y
        self.velocity_z = new_velocity_z