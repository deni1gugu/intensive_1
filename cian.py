import cianparser

moscow_parser = cianparser.CianParser(location="Долгопрудный")
data = moscow_parser.get_flats(deal_type="sale", rooms=1, with_saving_csv=True, additional_settings={"start_page":1, "end_page":20}, with_extra_data = True)

print(data[0])