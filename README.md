Custom error pages
=================

Pages for errors :
- 400 (bad request)
- 401 (forbidden)
- 404 (not found)
- 500 (server error)

# Installation
Add `cdtx.django_error_handlers` in your INSTALLED_APPS

In your urls.py, reference the error handlers
``` python
handler400 = 'cdtx.django_error_handlers.views.handler400'
handler403 = 'cdtx.django_error_handlers.views.handler403'
handler404 = 'cdtx.django_error_handlers.views.handler404'
handler500 = 'cdtx.django_error_handlers.views.handler500'
```
