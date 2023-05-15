import unittest
from lesson_1_class import Boid
from lesson_2_dictionary import dictionary_practice

dp = dictionary_practice()


class TestClass(unittest.TestCase):
    def test_dict_add(self):
        uav = Boid(121.223456, 25.665374, 10.003, 1, 2, 3)
        dp.dict_add(uav_name="UAV01", drone_id=1, drone=uav)
        self.assertEqual(dp.group["UAV01"]["drone_id"], 1)
        self.assertEqual(dp.group["UAV01"]["drone"], uav)

        uav = Boid(121.12345, 25.12345, 9.003, 4, 5, 6)
        dp.dict_add(uav_name="UAV02", drone_id=2, drone=uav)
        self.assertEqual(dp.group["UAV02"]["drone_id"], 2)
        self.assertEqual(dp.group["UAV02"]["drone"], uav)

    def test_dict_modify(self):
        uav = Boid(121.223456, 25.665374, 10.003, 1, 2, 3)
        dp.dict_add(uav_name="UAV01", drone_id=1, drone=uav)
        dp.dict_modify(uav_name="UAV01", new_drone_id=3, new_velocity_x=7, new_velocity_y=8, new_velocity_z=9)
        self.assertEqual(dp.group["UAV01"]["drone_id"], 3)
        self.assertEqual(dp.group["UAV01"]["drone"].velocity_x, 7)
        self.assertEqual(dp.group["UAV01"]["drone"].velocity_y, 8)
        self.assertEqual(dp.group["UAV01"]["drone"].velocity_z, 9)

        uav = Boid(121.12345, 25.12345, 9.003, 4, 5, 6)
        dp.dict_add(uav_name="UAV02", drone_id=2, drone=uav)
        dp.dict_modify(uav_name="UAV02", new_drone_id=0, new_velocity_x=1, new_velocity_y=2, new_velocity_z=3)
        self.assertEqual(dp.group["UAV02"]["drone_id"], 0)
        self.assertEqual(dp.group["UAV02"]["drone"].velocity_x, 1)
        self.assertEqual(dp.group["UAV02"]["drone"].velocity_y, 2)
        self.assertEqual(dp.group["UAV02"]["drone"].velocity_z, 3)

    def test_dict_del(self):
        feedback = dp.dict_del("UAV01")
        self.assertEqual(feedback, True)
        feedback = dp.dict_del("UAV01")
        self.assertEqual(feedback, None)

    def test_dict_return_value(self):
        uav = Boid(121.223456, 25.665374, 10.003, 1, 2, 3)
        dp.dict_add(uav_name="UAV03", drone_id=1, drone=uav)
        uav_position = dp.dict_return_value(uav_name="UAV03")
        self.assertEqual(uav_position["longitude"], 121.223456)
        self.assertEqual(uav_position["latitude"], 25.665374)
        self.assertEqual(uav_position["altitude"], 10.003)


if __name__ == '__main__':
    unittest.main()
