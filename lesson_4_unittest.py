import unittest
from lesson_4_boids_algorithm import Boid

uav01 = Boid(121.537266, 25.042751, 10, 1, 2, 3)
uav02 = Boid(121.537260, 25.042751, 10, 4, 5, 6)
uav03 = Boid(121.537426, 25.042862, 10, 7, 8, 9)
group = {
    "UAV01": {
        "drone_id": 1,
        "drone": uav01
    },
    "UAV02": {
        "drone_id": 2,
        "drone": uav02
    },
    "UAV03": {
        "drone_id": 3,
        "drone": uav03
    },
}


class TestClass(unittest.TestCase):
    def test_cohesion(self):
        answer = uav01.cohesion(group)
        self.assertEqual(answer.longitude, 121.53731733333332)
        self.assertEqual(answer.latitude, 25.042788)
        self.assertEqual(answer.altitude, 10)

        answer = uav02.cohesion(group)
        self.assertEqual(answer.longitude, 121.53731733333332)
        self.assertEqual(answer.latitude, 25.042788)
        self.assertEqual(answer.altitude, 10)

        answer = uav03.cohesion(group)
        self.assertEqual(answer.longitude, 121.53731733333332)
        self.assertEqual(answer.latitude, 25.042788)
        self.assertEqual(answer.altitude, 10)

    def test_alignment(self):
        answer = uav01.alignment(group)
        self.assertEqual(answer.velocity_x, 4)
        self.assertEqual(answer.velocity_y, 5)
        self.assertEqual(answer.velocity_z, 6)

        answer = uav02.alignment(group)
        self.assertEqual(answer.velocity_x, 4)
        self.assertEqual(answer.velocity_y, 5)
        self.assertEqual(answer.velocity_z, 6)

        answer = uav03.alignment(group)
        self.assertEqual(answer.velocity_x, 4)
        self.assertEqual(answer.velocity_y, 5)
        self.assertEqual(answer.velocity_z, 6)

    def test_separation(self):
        answer = uav01.separation(group)
        self.assertEqual(answer.velocity_x, 166666.6666927136)
        self.assertEqual(answer.velocity_y, 0.0)
        self.assertEqual(answer.velocity_z, 0.0)

        answer = uav02.separation(group)
        self.assertEqual(answer.velocity_x, -166666.6666927136)
        self.assertEqual(answer.velocity_y, 0.0)
        self.assertEqual(answer.velocity_z, 0.0)

        answer = uav03.separation(group)
        self.assertEqual(answer.velocity_x, 0.0)
        self.assertEqual(answer.velocity_y, 0.0)
        self.assertEqual(answer.velocity_z, 0.0)


if __name__ == '__main__':
    unittest.main()
