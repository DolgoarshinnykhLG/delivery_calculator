from typing import Optional

from app.enums import FragileType, CargoDimensions, Workload, DeliveryDistance
from config import DELIVERY_COST_MIN


class DeliveryCalculator:
    def __init__(self):
        self.__cost = 0

    @property
    def cost(self) -> float:
        return self.__cost

    @cost.setter
    def cost(self, value: int) -> None:
        if value < DELIVERY_COST_MIN:
            self.__cost = DELIVERY_COST_MIN
        else:
            self.__cost = value

    def calculate(
            self,
            distance: DeliveryDistance,
            dimensions: CargoDimensions,
            delivery_load: Workload,
            fragile_type: FragileType
    ) -> Optional[float]:
        if fragile_type is fragile_type.FRAGILE and distance is DeliveryDistance.MORE_30:
            return

        self.cost = (distance.value + dimensions.value + fragile_type.value) * delivery_load.value

        return self.cost
