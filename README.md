## Installation

Run the [pip](https://pip.pypa.io/en/stable/) command to install the latest version:

```bash
   pip install git+https://github.com/sitmena/sitech-django-middlewares.git@v1.0
```

## Usage

**- Request Middleware:** 
 access the [Request](https://docs.djangoproject.com/en/2.2/ref/request-response/#httprequest-objects) or [User](https://docs.djangoproject.com/en/2.2/ref/request-response/#django.http.HttpRequest.user) Object Inside the Models, Signals, Tasks ... etc.
 
 - Add `sitech_middlewares.request.RequestMiddleware` to `MIDDLEWARE`
 - Add `from sitech_middlewares.request import get_current_request, get_current_user`
 - Call `get_current_request()` to obtain the current HttpRequest object.
 - Call `get_current_user()` to obtain the current User object.
 
 - UserForeignKey model field: This field extends a regular ForeignKey model field, and has the option to automatically set the currently logged in user on insert and/or update.

```python
    from django.db import models
    from sitech_middlewares.fields import UserForeignKey

    class MyModel(models.Model):
        my_data = models.CharField(max_length=64, verbose_name="Very important data that are somehow related to a user")
        user = UserForeignKey(auto_user_add=True, verbose_name="The user that is automatically assigned", related_name="mymodels")
```
*``auto_user``  Automatically sets the current user everytime the object is saved (e.g., created or updated). This is useful for *last modified by* information.
<br>
*``auto_user_add`` Automatically sets the current user when the object is first created. This is useful for *created by* information.
