
EXACT = 'exact'
GT = 'gt'
GTE = 'gte'
LT = 'lt'
LTE = 'lte'
ICONTAINS = 'icontains'
IN = 'in'
STARTS_WITH = 'istartswith'
ENDS_WITH = 'iendswith'
IS_NULL = 'isnull'
JSON_ICONTAINS = 'json_icontains'
COVEREDBY = 'coveredby'
DEFAULT_LOOKUP = EXACT

by_gql = {
    'eq': EXACT,
    'gt': GT,
    'gte': GTE,
    'lt': LT,
    'lte': LTE,
    'containsI': ICONTAINS,
    'in': IN,
    'startsWithI': STARTS_WITH,
    'endsWithI': ENDS_WITH,
    'isNull': IS_NULL,
    'jsonContainsI': JSON_ICONTAINS,
    'coveredBy': COVEREDBY
}

gql = dict(map(lambda x: (x[1], x[0]), by_gql.items()))
