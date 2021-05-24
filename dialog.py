import re
import functions, buttons
from viberbot.api.messages.url_message import URLMessage
from viberbot.api.messages.text_message import TextMessage

def main(viber, viber_request, condition):
    if re.match(r'(?i).*(лабораторн).*\d.*', condition):
        viber.send_messages(viber_request.sender.id, [URLMessage(media=functions.send_task_for_lab(functions.parse_digits_from_text(condition)))])
    elif re.match(r'(?i).*(дякую).*', condition):
        viber.send_messages(viber_request.sender.id, [TextMessage(text="Нема за що, звертайся ще 😉.")])
    elif re.match(r'(?i).*не можу зробити лабораторну.*', condition):
        viber.send_messages(viber_request.sender.id, [TextMessage(text="У тебе все вийде 😉, я у тебе вірю 😘. Тримай шоколадку 🍫")])