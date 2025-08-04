from googleapiclient.discovery import build
from google.oauth2 import service_account

def create_calendar_event(title, date, time, duration_minutes, location):
    credentials = service_account.Credentials.from_service_account_file("credentials.json")
    service = build("calendar", "v3", credentials=credentials)
    start = f"{date}T{time}:00"
    end = f"{date}T{int(time.split(':')[0])+duration_minutes//60}:{int(time.split(':')[1])}:00"
    event = {
        "summary": title,
        "start": {"dateTime": start, "timeZone": "UTC"},
        "end": {"dateTime": end, "timeZone": "UTC"},
        "location": location
    }
    created = service.events().insert(calendarId="primary", body=event).execute()
    return {"id": created["id"], "summary": created["summary"]}
