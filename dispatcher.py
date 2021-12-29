import typing as t
from werkzeug.exceptions import NotFound

if t.TYPE_CHECKING:
    from _typeshed.wsgi import StartResponse
    from _typeshed.wsgi import WSGIApplication
    from _typeshed.wsgi import WSGIEnvironment


class SubdomainDispatcher:

    def __init__(
            self,
            mounts: t.Optional[t.Dict[str, "WSGIApplication"]] = None,
    ) -> None:
        self.mounts = mounts or {}

    def __call__(
            self, environ: "WSGIEnvironment", start_response: "StartResponse"
    ) -> t.Iterable[bytes]:
        script = environ.get("HTTP_HOST")
        subdomain = script.split('.')[0]
        if subdomain in self.mounts:
            app = self.mounts[subdomain]
        else:
            return NotFound()

        return app(environ, start_response)
