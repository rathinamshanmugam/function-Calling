def book_reservation(name, date, time, guests, location):
    return {
        "status": "confirmed",
        "reservation": f"{guests} guests at {location} on {date} at {time}",
        "confirmation_code": "RSV12345"
    }
