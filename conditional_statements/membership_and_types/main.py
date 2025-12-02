# Product details
description = "Imported honey, raw and unfiltered"
price = "5.99"
count = 120
contains_raw = "raw" in description
contains_Imported = "Imported" in description
price_is_float = type(price) == float
count_is_int = type(count) == int
print(f"Contains 'raw': {contains_raw}")
print(f"Contains 'Imported': {contains_Imported}")
print(f"Is price a float?: {price_is_float}")
print(f"Is count an integer?: {count_is_int}")