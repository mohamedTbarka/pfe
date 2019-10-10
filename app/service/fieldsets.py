# -*- coding: utf-8 -*-

fieldsets_preferences = (
    # (None, {
    #     'fields': ()
    # }),

    (u"Infos ", {
        'fields': ("title", "address", "open_hour", "close_hour", "copyright", "icon", "logo",)
    }),

    (u"Contact", {
        'fields': ("phone", "email",)
    }),

    (u"Réseaux Sociaux", {
        'classes': ('collapse', 'extrapretty'),
        'fields': ("facebook", "twitter", "youtube", "instagram",)
    }),

    (u"Plan images", {
        'classes': ('collapse', 'extrapretty'),
        'fields': ("rdc", "first_floor", "second_floor")
    }),

    (u"Parallax images", {
        'classes': ('collapse', 'extrapretty'),
        'fields': ("background_image",
                   "background_image2",
                   "parallax_mobile_image",
                   "parallax_mobile_image2",)
    }),

    (u"Banners", {
        'classes': ('collapse', 'extrapretty'),
        'fields': ("bureau_banner",
                   "hotel_banner",
                   "decouvrir_banner",
                   "compagne_banner",
                   "event_banner",
                   "promotion_banner",
                   )
    }),

    (u"Home images", {
        'classes': ('collapse', 'extrapretty'),
        'fields': ("shopping_image",
                   "restauration_image",
                   "cinema_image",
                   "culture_loisirs_image",
                   "hypermarche_image",
                   "promotion_image",
                   "event_image",
                   "compagne_image",
                   )
    }),

)
