from mycroft import MycroftSkill, intent_file_handler


class PaperAssistant(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)

    @intent_file_handler('assistant.paper.intent')
    def handle_assistant_paper(self, message):
        self.speak_dialog('assistant.paper')


def create_skill():
    return PaperAssistant()

