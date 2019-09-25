# # coding=utf-8
#
# from django.template import Library
# from custom_flatpages.models import SousRubrique
# from content.models import Pole, Centre
#
#
# RUBRIQUE = (
#     ("nos_patients", "NOS PATIENTS"),
#     ("notre_hopitale", "Notre Hôpital"),
# )
#
# register = Library()
#
#
# @register.inclusion_tag('includes/menu.html')
# def get_menu():
#     return {
#         "poles": Pole.objects.values('titre', 'slug'),
#         "centres": Centre.objects.values('titre', 'slug'),
#         "sous_rubrique_nos_patients": SousRubrique.objects.filter(rubrique="NOS PATIENTS").exclude(hide=True).order_by("ordre"),
#         "sous_rubrique_notre_hopitale": SousRubrique.objects.filter(rubrique="Notre Hopital").exclude(hide=True).order_by("ordre"),
#     }
#
#
# @register.inclusion_tag('includes/footer.html')
# def get_footer():
#     pole = Pole.objects.first()
#     centre = Centre.objects.first()
#     if pole is None:
#         pole = Pole()
#         pole.slug = "404"
#     if centre is None:
#         centre = Centre()
#         centre.slug = "404"
#
#     return {
#         "pole": pole,
#         "centre": centre,
#         "sous_rubrique_nos_patients": SousRubrique.objects.filter(rubrique="NOS PATIENTS").exclude(hide=True).order_by("ordre"),
#         "sous_rubrique_notre_hopitale": SousRubrique.objects.filter(rubrique="Notre Hopital").exclude(hide=True).order_by("ordre"),
#     }