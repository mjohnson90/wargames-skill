from mycroft import MycroftSkill, intent_file_handler


class Wargames(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)

    @intent_file_handler('wargames.intent')
    def handle_wargames(self, message):
        self.speak_dialog('wargames')


def create_skill():
    return Wargames()

