from .filters import AutocompleteFilter


class AdminAutoFiltersMixin(object):
    class Media:
        js = (
            "admin/js/jquery.init.js",
            "django-admin-autocomplete-filter/js/autocomplete_filter_qs.js",
        )

    def __init__(self, *args, **kwargs):
        autocomplete_filters = ()
        for name in self.autocomplete_list_filter:
            filterClass = type(
                "AutocompleteFilterForMixin",
                (AutocompleteFilter,),
                {"parameter_name": name},
            )
            autocomplete_filters += (filterClass,)

        self.list_filter = autocomplete_filters + self.list_filter

        super().__init__(*args, **kwargs)
