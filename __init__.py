from mycroft import MycroftSkill, intent_file_handler

from .arxiv_handler import get_pdf

class PaperAssistant(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)
        self.log.info("assistant has loaded")

    @intent_file_handler('assistant.paper.intent')
    def handle_assistant_paper(self, message):
        self.log.info("assistant has entered intent handler")
        self.speak_dialog('assistant.paper')
        self.speak_dialog('assistant.research')
        fn = get_pdf()
        self.speak_dialog(fn)


def create_skill():
    return PaperAssistant()

