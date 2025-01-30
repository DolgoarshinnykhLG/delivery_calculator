from enum import Enum


class FragileType(Enum):
    FRAGILE = 300
    NOT_FRAGILE = 0


class CargoDimensions(Enum):
    LARGE = 200
    LITTLE = 100


class Workload(Enum):
    VERY_HIGH = 1.6
    HIGH = 1.4
    INCREASED = 1.2
    NORMAL = 1


class DeliveryDistance(Enum):
    MORE_30 = 300
    UNTIL_30 = 200
    UNTIl_10 = 100
    UNTIL_2 = 50
