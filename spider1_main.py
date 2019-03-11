import url_manager
import html_downloader
import html_parser
import html_output


class Spider1Main(object):
    """
    爬取百度百科 Android 关键词相关词及简介并输出为一个HTML tab网页
    第一次痛点:对各种依赖库API不熟悉导致方法不知道用途
    """
    def __init__(self):
        self.urls = url_manager.UrlManager()
        self.downloader = html_downloader.HtmlDownLoader()
        self.parser = html_parser.HtmlParser()
        self.out_put = html_output.HtmlOutput()

    def crawl(self,root_url):
        count = 1
        self.urls.add_new_url(root_url)
        while self.urls.has_new_url():

            try:
                new_url = self.urls.get_new_url()
                print("crawl %d : %s" % (count, new_url))
                headers = {
                    "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.100 Safari/537.36"
                }
                html_content = self.downloader.download(new_url, retry_count=2, headers=headers)
                new_urls, new_data = self.parser.parse(new_url, html_content, "utf-8")
                self.urls.add_new_urls(new_urls)
                self.out_put.collect_data(new_data)
                if count >= count_limit:
                    break
                count = count + 1
            except Exception as e:
                print("crawl failed!\n" + str(e))
        self.out_put.output_html()


if __name__ == "__main__":
    rootUrl = "https://baike.baidu.com/item/Android/60243?fromtitle=%E5%AE%89%E5%8D%93&fromid=5389782&fr=aladdin"
    count_limit = 3
    objSpider1 = Spider1Main()
    objSpider1.crawl(rootUrl)
