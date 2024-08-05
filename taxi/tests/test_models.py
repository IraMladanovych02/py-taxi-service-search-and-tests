from django.contrib.auth import get_user_model
from django.test import TestCase

from taxi.models import Manufacturer, Car


class ModelTests(TestCase):

    def test_manufacturer_str(self):
        manufacturer = Manufacturer.objects.create(name="test")
        self.assertEqual(str(manufacturer), manufacturer.name)

    def test_driver_str(self):
        driver = get_user_model().objects.create(
            username="test",
            password="test123",
            first_name="test_first",
            last_name="test_last",
        )
        self.assertEqual(
            str(driver),
            f"{driver.username} ({driver.first_name} {driver.last_name})"
        )

    def test_car_str(self):
        manufacturer = Manufacturer.objects.create(name="test")
        car = Car.objects.create(model="test", manufacturer=manufacturer)
        self.assertEqual(str(car), car.model)
