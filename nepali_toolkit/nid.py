def validate(nid_number: str) -> bool:
    if not nid_number.isdigit():
        return False
    if len(nid_number) not in (10, 12):
        return False
    if not nid_number.startswith(("20", "99")):
        return False
    return True
