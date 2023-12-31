from mycroft import MycroftSkill, intent_file_handler


import .Paper

class PaperAssistant(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)
        self.log.info("assistant has loaded")

    @intent_file_handler('assistant.paper.intent')
    def handle_assistant_paper(self, message):
        self.log.info("assistant has entered intent handler")
        self.speak_dialog('assistant.paper')
        my_paper = Paper.Paper("1904.12956")
        self.speak(str(my_paper.arxiv_id))


def create_skill():
    return PaperAssistant()

