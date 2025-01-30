import pytest as pytest

from app.delivery_calculator import DeliveryCalculator
from app.enums import FragileType, CargoDimensions, Workload, DeliveryDistance
from config import DELIVERY_COST_MIN


class TestDeliveryCalculator:
    @pytest.mark.parametrize(
        "delivery_type, fragile_type, dimensions_type, workload_type",
        (
                (DeliveryDistance.UNTIl_10, FragileType.FRAGILE, CargoDimensions.LARGE, Workload.HIGH),
                (DeliveryDistance.MORE_30, FragileType.NOT_FRAGILE, CargoDimensions.LITTLE, Workload.VERY_HIGH),
                (DeliveryDistance.UNTIL_30, FragileType.FRAGILE, CargoDimensions.LARGE, Workload.INCREASED)
        )
    )
    def test_delivery_calculator(self, delivery_type, fragile_type, dimensions_type, workload_type):
        cost = DeliveryCalculator().calculate(delivery_type, dimensions_type, workload_type, fragile_type)

        assert cost == (delivery_type.value + dimensions_type.value + fragile_type.value) * workload_type.value, \
            f"Сумма доставки расчиталась некорректно: {cost}"

    @pytest.mark.parametrize(
        "delivery_type, fragile_type, dimensions_type, workload_type",
        ((DeliveryDistance.UNTIL_2, FragileType.NOT_FRAGILE, CargoDimensions.LITTLE, Workload.NORMAL),))
    def test_less_than_min_cost(self, delivery_type, fragile_type, dimensions_type, workload_type):
        cost = DeliveryCalculator().calculate(delivery_type, dimensions_type, workload_type, fragile_type)

        assert cost == DELIVERY_COST_MIN, f"Сумма доставки расчиталась некорректно: {cost}"

    def test_fragile_long_delivery(self):
        cost = DeliveryCalculator().calculate(
            DeliveryDistance.MORE_30, CargoDimensions.LITTLE, Workload.VERY_HIGH, FragileType.FRAGILE)

        assert cost is None, f"Сумма доставки рассчиталась для хрупкого груза на расстояние {DeliveryDistance.MORE_30}"
