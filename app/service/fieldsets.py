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
        'fields': ("facebook", "twitter", "youtube", "instagram",)
    }),

    (u"Plan images", {
        'fields': ("rdc", "first_floor", "second_floor")
    }),

    (u"Parallax images", {
        'fields': ("background_image",
                   "background_image2",
                   "parallax_mobile_image",
                   "parallax_mobile_image2",)
    }),

    (u"Banners", {
        'fields': ("bureau_banner",
                   "hotel_banner",
                   "decouvrir_banner",)
    }),

)
