from webob import Request 

r = Request.blank("/wiki/HTML")
r.http_version = 'HTTP/1.1'
r.host = 'ru.wikipedia.org'
r.environ["SERVER_NAME"] = 'ru.wikipedia.org'
r.accept = "text/html"
r.user_agent = "Mozilla/5.0 (X11; U; Linux i686; ru; rv:1.9b5) Gecko/2008050509 Firefox/3.0b5"

print(r)
print('^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^')
print(r.get_response())
print('*********************************')

r = Request.blank("/ip")
r.http_version = 'HTTP/1.1'
r.host = 'httpbin.org'
r.environ["SERVER_NAME"] = 'httpbin.org'
r.accept = "*/*"
r.user_agent = "Mozilla/5.0 (X11; U; Linux i686; ru; rv:1.9b5) Gecko/2008050509 Firefox/3.0b5"

print(r)
print('^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^')
print(r.get_response())
print('*********************************')

r = Request.blank("/get?foo=bar&1=2&2/0&error=True")
r.http_version = 'HTTP/1.1'
r.host = 'httpbin.org'
r.environ["SERVER_NAME"] = 'httpbin.org'
r.accept = "*/*"
r.user_agent = "Mozilla/5.0 (X11; U; Linux i686; ru; rv:1.9b5) Gecko/2008050509 Firefox/3.0b5"

print(r)
print('^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^')
print(r.get_response())
print('*********************************')

