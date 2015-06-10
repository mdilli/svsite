
from django.utils.translation import ugettext_lazy as _
from django.core.urlresolvers import reverse
from grappelli.dashboard import modules, Dashboard
from grappelli.dashboard.utils import get_admin_site_name


class CustomIndexDashboard(Dashboard):

    def init_with_context(self, context):
        site_name = get_admin_site_name(context)

        # list of models
        self.children.append(modules.AppList(
            _('Data'),
            column=1,
            collapsible=False,
        ))

        # append another link list module for "support".
        self.children.append(modules.LinkList(
            _('Links'),
            column=2,
            children=[
                {
                    'title': u'Homepage',
                    'url': '/',
                    'external': False,
                },
                {
                    'title': _('FileBrowser'),
                    'url': '/admin/filebrowser/browse/',
                    'external': False,
                },
                {
                    'title': _('Make backup'),
                    'url': reverse('backup'),
                    'external': False,
                },
                {
                    'title': _('Restore backup'),
                    'url': reverse('restore'),
                    'external': False,
                },

            ]
        ))

        # append a recent actions module
        self.children.append(modules.RecentActions(
            _('Changes'),
            limit=10,
            collapsible=True,
            column=2,
        ))


