import unittest
from lesson_1_class import Boid

uav_longitude = 121.223456
uav_latitude = 25.665374
uav_altitude = 10.003
uav_velocity_x = 1
uav_velocity_y = 2
uav_velocity_z = 3
uav = Boid(uav_longitude, uav_latitude, uav_altitude,
           uav_velocity_x, uav_velocity_y, uav_velocity_z)


class TestClass(unittest.TestCase):
    def test_initial(self):
        self.assertEqual(uav.longitude, 121.223456)
        self.assertEqual(uav.latitude, 25.665374)
        self.assertEqual(uav.altitude, 10.003)
        self.assertEqual(uav.velocity_x, 1)
        self.assertEqual(uav.velocity_y, 2)
        self.assertEqual(uav.velocity_z, 3)

    def test_update_position(self):
        uav.update_position(new_longitude=122.12345, new_latitude=26.44321, new_altitude=9)
        self.assertEqual(uav.longitude, 122.12345)
        self.assertEqual(uav.latitude, 26.44321)
        self.assertEqual(uav.altitude, 9)
        uav.update_position(new_longitude=127.32145, new_latitude=12.44321, new_altitude=7)
        self.assertEqual(uav.longitude, 127.32145)
        self.assertEqual(uav.latitude, 12.44321)
        self.assertEqual(uav.altitude, 7)

    def test_update_velocity(self):
        uav.update_velocity(new_velocity_x=4, new_velocity_y=5, new_velocity_z=6)
        self.assertEqual(uav.velocity_x, 4)
        self.assertEqual(uav.velocity_y, 5)
        self.assertEqual(uav.velocity_z, 6)
        uav.update_velocity(new_velocity_x=7, new_velocity_y=8, new_velocity_z=9)
        self.assertEqual(uav.velocity_x, 7)
        self.assertEqual(uav.velocity_y, 8)
        self.assertEqual(uav.velocity_z, 9)


if __name__ == '__main__':
    unittest.main()
