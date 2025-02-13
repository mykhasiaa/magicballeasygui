import easygui
import random
responselist = ["Так", "Ні", "Точно так", "Можливо", "Впевнено так", "Коли рак на горі свисне", "Ну нє",
                "Навіть не думай", "Цікаве питання, хз", "Хто зна"]
while True:
    question = easygui.enterbox("Вітаємо! Введіть своє запитання:",
                                "Магічна куля",
                                image="magicball.gif")
    if question is None:
        break
    result = easygui.msgbox(random.choice(responselist),
                            "Магічна куля",
                            image="emojiface.gif")

    choice = easygui.buttonbox("Продовжити чи вийти?",
                               "Магічна куля",
                               ["Продовжити", "Вийти"])
    if choice == "Вийти":
        easygui.msgbox("До побачення :)",
                       "Магічна куля",
                       image="byeface.gif")
        break
    else:
        continue