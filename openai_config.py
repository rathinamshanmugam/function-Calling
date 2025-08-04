import openai, json
from tools.weather import get_weather
from tools.stocks import get_stock_price
from tools.stripe_order import place_order
from tools.calendar_event import create_calendar_event
from tools.reservation import book_reservation
from tools.custom_api import get_custom_data

openai.api_key = "YOUR_OPENAI_API_KEY"

functions = [
    # weather, stocks, order, calendar, reservation, custom_api...
    # (all JSON schemas shown earlier)
]

function_map = {
    "get_weather": get_weather,
    "get_stock_price": get_stock_price,
    "place_order": place_order,
    "create_calendar_event": create_calendar_event,
    "book_reservation": book_reservation,
    "get_custom_data": get_custom_data,
}

def run_conversation(user_input):
    messages = [{"role": "user", "content": user_input}]
    while True:
        response = openai.ChatCompletion.create(
            model="gpt-4-0613",
            messages=messages,
            functions=functions,
            function_call="auto"
        )

        msg = response["choices"][0]["message"]
        if msg.get("function_call"):
            name = msg["function_call"]["name"]
            args = json.loads(msg["function_call"]["arguments"])
            result = function_map[name](**args)
            messages.append(msg)
            messages.append({
                "role": "function",
                "name": name,
                "content": json.dumps(result)
            })
        else:
            return msg["content"]
