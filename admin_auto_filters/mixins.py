from .filters import AutocompleteFilter


class AdminAutoFiltersMixin(object):
    class Media:
        js = (
            "admin/js/jquery.init.js",
            "django-admin-autocomplete-filter/js/autocomplete_filter_qs.js",
        )

    def __init__(self, *args, **kwargs):
        autocomplete_filters = ()
        for filter_tuple in self.autocomplete_list_filter:
            parameter_name = filter_tuple[1]
            filterClassName = "AutocompleteFilter%s" % (parameter_name,)
            filterClassArgs = {"parameter_name": parameter_name}
            filterClass = type(filterClassName, (AutocompleteFilter,), filterClassArgs)
            autocomplete_filters += (filterClass,)

        self.list_filter = autocomplete_filters + self.list_filter

        super().__init__(*args, **kwargs)
