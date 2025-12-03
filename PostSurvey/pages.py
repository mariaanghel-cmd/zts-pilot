from otree.api import *
from .models import C, Subsession, Group, Player


class PerceptionsAndFeedback(Page):
    form_model = 'player'

    def vars_for_template(self):
        return dict(
            condition=self.session.config.get('news_condition', 'control'),
        )


    def get_form_fields(self):
        condition = self.session.config.get('news_condition', 'control')
        if condition in ['positive', 'negative']:
            return ['news_valence', 'feedback_text']
        return ['feedback_text']

page_sequence = [
    PerceptionsAndFeedback,
]
