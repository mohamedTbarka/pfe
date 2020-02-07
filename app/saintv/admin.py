# encoding=utf-8 :


from django.contrib import admin

from . import models
from .models import Response, Ticket


class TicketTabularInlineAdmin(admin.TabularInline):
    model = Ticket
    extra = 0


class ParticipantAdmin(admin.ModelAdmin):
    inlines = [TicketTabularInlineAdmin, ]
    list_display = (
        'id',
        'full_name',
        'email',
        'telephone',
        'created_at',
        'updated_at',
    )
    list_filter = (
        'created_at',
        'updated_at',

    )


class ResponseTabularInlineAdmin(admin.TabularInline):
    model = Response
    extra = 0


class QuestionAdmin(admin.ModelAdmin):
    inlines = [ResponseTabularInlineAdmin, ]
    list_display = ('id', 'question', 'created_at', 'updated_at',)
    list_filter = (
        'created_at',
        'updated_at',
    )


class ParticipationAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'hash_code',
        'participant',
        'question',
        'response',
        'source',
        'medium',
        'campaign',
        'created_at',
        'updated_at',
    )
    list_filter = (
        'created_at',
        'updated_at',
    )


class TicketAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'ticket',
        'participant',
        'created_at',
        'updated_at',
    )
    list_filter = (
        'created_at',
        'updated_at',
    )
    readonly_fields = ("ticket_base64",)

def _register(model, admin_class):
    admin.site.register(model, admin_class)


_register(models.Participant, ParticipantAdmin)
_register(models.Question, QuestionAdmin)
_register(models.Participation, ParticipationAdmin)
_register(models.Ticket, TicketAdmin)
