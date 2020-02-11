from import_export import resources
from .models import Question, Participant, Participation


class QuestionResource(resources.ModelResource):
    class Meta:
        model = Question
        exclude = ('updated_at',)
        export_order = ('id',)


class ParticipantResource(resources.ModelResource):
    class Meta:
        model = Participant
        exclude = ('updated_at',)
        export_order = ('id',)


class ParticipationResource(resources.ModelResource):
    class Meta:
        model = Participation
        exclude = ('updated_at', 'hash_code', 'ticket', 'ticket_base64',)
        export_order = ('id', 'participant', 'question', "response",)

    def dehydrate_response(self, participation):
        if participation.response:
            return '%s' % (participation.response.response)
        return None

    def dehydrate_question(self, participation):
        if participation.question:
            return '%s' % (participation.question.question)
        return None

    def dehydrate_participant(self, participation):
        if participation.participant:
            return '%s' % (participation.participant.full_name)
        return None
