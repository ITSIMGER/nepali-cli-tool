mock_schedule = {
    1: ["6:00 AM - 9:00 AM", "5:00 PM - 8:00 PM"],
    2: ["7:00 AM - 10:00 AM", "6:00 PM - 9:00 PM"],
    3: ["8:00 AM - 11:00 AM", "4:00 PM - 7:00 PM"],
}

def get_schedule(ward: int) -> str:
    schedule = mock_schedule.get(ward)
    if schedule:
        return ", ".join(schedule)
    return "No schedule found for this ward."
