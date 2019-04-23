## Installation

Run the [pip](https://pip.pypa.io/en/stable/) command to install the latest version:

```bash
   pip install git+https://github.com/sitmena/sitech-django-middlewares.git
```

## Usage

**- Request Middleware:** 
 access the [Request](https://docs.djangoproject.com/en/2.2/ref/request-response/#httprequest-objects) or [User](https://docs.djangoproject.com/en/2.2/ref/request-response/#django.http.HttpRequest.user) Object Inside the Models, Signals, Tasks ... etc.
 
 1)Add `sitech_middlewares.request.RequestMiddleware` to `MIDDLEWARE`
 2)Add 'from sitech_middlewares.request import get_current_request'
 3)Call `get_current_request()` to obtain the current HttpRequest object.


