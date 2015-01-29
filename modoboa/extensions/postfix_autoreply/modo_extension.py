# coding: utf-8
"""
Postfix auto-replies plugin.

This module provides a way to integrate Modoboa auto-reply
functionality into Postfix.

"""

from django.utils.translation import ugettext_lazy

from modoboa.core.extensions import ModoExtension, exts_pool
from modoboa.lib import events, parameters


class PostfixAutoreply(ModoExtension):

    """
    Auto-reply (vacation) functionality using Postfix.

    """
    name = "postfix_autoreply"
    label = "Postfix autoreply"
    version = "1.0"
    description = ugettext_lazy(
        "Auto-reply (vacation) functionality using Postfix")

    def load(self):
        from modoboa.extensions.postfix_autoreply.app_settings import (
            ParametersForm
        )
        parameters.register(
            ParametersForm, ugettext_lazy("Automatic replies"))
        from modoboa.extensions.postfix_autoreply import general_callbacks

exts_pool.register_extension(PostfixAutoreply)


@events.observe("ExtraUprefsRoutes")
def extra_routes():
    from django.conf.urls import url

    return [
        url(r'^user/autoreply/$',
            'modoboa.extensions.postfix_autoreply.views.autoreply',
            name="autoreply")
    ]