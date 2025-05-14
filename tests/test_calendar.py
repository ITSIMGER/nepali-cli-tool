from nepali_toolkit import calendar

def test_ad_to_bs():
    result = calendar.convert("AD", "2023-01-01")
    assert result.startswith("2079")

def test_bs_to_ad():
    result = calendar.convert("BS", "2080-01-01")
    assert result.startswith("202")
