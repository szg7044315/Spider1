from http import cookiejar
from urllib import request, error
from urllib.parse import urlparse


class HtmlDownLoader(object):
    """
    http请求下载器,处理request封装数据:cookie\代理\请求头等
    retry_count默认为3,当请求异常时,用于尝试再次请求
    """
    def download(self, url, retry_count=3, headers=None, proxy=None, data=None):
        if url is None:
            return
        try:
            req = request.Request(url, headers=headers, data=data)
            cookie = cookiejar.CookieJar()
            cookie_process = request.HTTPCookieProcessor(cookie)
            opener = request.build_opener()
            if proxy:
                proxies = {urlparse(url).scheme : proxy}
                opener.add_handler(request.ProxyHandler(proxies))
            content = opener.open(req).read()

        except error.URLError as e:
            print("HtmlDownLoader download error",e.reason)
            content = None
            if retry_count > 0:
                if hasattr(e, "code") and 500>= e.code < 600:
                    #发生错误时,判断错误代码,若属于服务器异常,可尝试重新请求链接
                    return self.download(url, retry_count - 1, headers, proxy, data)
        return  content

