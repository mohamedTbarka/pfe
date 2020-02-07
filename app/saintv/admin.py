# encoding=utf-8 :


from django.contrib import admin
from django.utils.html import format_html

from . import models
from .models import Response, Participation


class ParticipationTabularInlineAdmin(admin.TabularInline):
    model = Participation
    exclude = ("ticket_base64", "ticket")
    extra = 0

    def imagem_logo(self, obj):
        return format_html('<img src="data:;base64,{}" height="100", width="100">', obj.ticket_base64)

    imagem_logo.short_description = "Ticket"

    readonly_fields = ("imagem_logo",)


class ParticipantAdmin(admin.ModelAdmin):
    inlines = (ParticipationTabularInlineAdmin,)
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
    raw_id_fields = ("participant", "question",)
    exclude = ("ticket_base64", "ticket")

    def imagem_logo(self, obj):
        return format_html('<img src="data:;base64,{}">', obj.ticket_base64)

    imagem_logo.short_description = "Ticket"

    readonly_fields = ("imagem_logo",)


def _register(model, admin_class):
    admin.site.register(model, admin_class)


_register(models.Participant, ParticipantAdmin)
_register(models.Question, QuestionAdmin)
_register(models.Participation, ParticipationAdmin)
