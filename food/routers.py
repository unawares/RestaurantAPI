from rest_framework.routers import Route, DynamicDetailRoute, SimpleRouter

class WithSlugReadOnlyRouter(SimpleRouter):
    routes = [
        Route(
            url=r'^{prefix}/(?P<slug>[\w-]+)/$',
            mapping={'get': 'list'},
            name='{basename}-list',
            initkwargs={'suffix': 'List'}
        ),
        Route(
            url=r'^{prefix}/(?P<slug>[\w-]+)/{lookup}/$',
            mapping={'get': 'retrieve'},
            name='{basename}-detail',
            initkwargs={'suffix': 'Detail'}
        ),
    ]
