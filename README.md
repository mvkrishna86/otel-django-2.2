# otel-django-2.2
Test Django 2.2 Application with OpenTelemetry Auto instrumentation

## Run application
```
cd mysite
opentelemetry-bootstrap --action=install
opentelemetry-instrument python3 manage.py runserver 0.0.0.0:8000 --noreload`
```
