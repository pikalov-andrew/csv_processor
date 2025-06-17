from .avg import AvgAggregation
from .max import MaxAggregation
from .min import MinAggregation

AGGREGATIONS = {
    "avg": AvgAggregation(),
    "min": MinAggregation(),
    "max": MaxAggregation()
}
