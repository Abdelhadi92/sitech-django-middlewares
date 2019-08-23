from django.conf import settings
from django.db import models

from sitech_middlewares.request import get_current_user


class UserForeignKey(models.ForeignKey):
    """Model field UserForeignKey
    Saves a reference to a user. By using the `sitech_middlewares.request.RequestMiddleware`
    """
    description = _(u"User")

    def __init__(self, auto_user=False, auto_user_add=False, **kwargs):
        self.auto_user, self.auto_user_add = auto_user, auto_user_add

        kwargs['to'] = settings.AUTH_USER_MODEL

        if auto_user or auto_user_add:
            kwargs['on_delete'] = kwargs.get('on_delete', models.SET_NULL)
            kwargs['null'] = kwargs.get('null', True)
            kwargs['blank'] = kwargs.get('blank', True)
            kwargs['editable'] = kwargs.get('editable', False)
            # todo: related name to be concatenated with the model name to fit in the abstract model approach

        super(UserForeignKey, self).__init__(**kwargs)

    def pre_save(self, model_instance, add):
        object_user = self.value_from_object(model_instance)
        current_user = get_current_user()

        if current_user.pk and (self.auto_user or (self.auto_user_add and add and not object_user)):
            setattr(model_instance, self.name, current_user)

        return super(UserForeignKey, self).pre_save(model_instance, add)
