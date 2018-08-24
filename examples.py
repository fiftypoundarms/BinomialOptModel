from eu_option import EuroOption

option_eu = EuroOption(
    217.58,
    215,
    0.05,
    0.1,
    40,
    {"tk": "AAPL", "is_cal": True, "start": "2017-08-18", "end": "2018-08-18"},
)

print(option_eu.price())
