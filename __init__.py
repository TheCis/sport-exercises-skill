from mycroft import MycroftSkill, intent_file_handler


class SportExercises(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)

    @intent_file_handler('exercises.sport.intent')
    def handle_exercises_sport(self, message):
        self.speak_dialog('exercises.sport')


def create_skill():
    return SportExercises()

