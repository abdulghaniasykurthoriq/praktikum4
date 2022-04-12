from bad_lsp import Bicycle as BadBicycle
from good_lsp import Bicycle as GoodBicycle

bad_bicycle = BadBicycle('Caribow',20)
good_bicycle = GoodBicycle('Caribow', 20)

bad_bicycle.start_engine()
good_bicycle.start_moving()