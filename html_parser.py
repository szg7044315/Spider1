import re
from urllib.parse import urljoin

from bs4 import BeautifulSoup


class HtmlParser(object):
    """
    处理http请求获得的内容,根据需要山选出需要的数据
    """
    def parse(self, url, content, url_encode="utf-8"):
        if url is None or content is None:
            return
        soup =BeautifulSoup(content, "html.parser", from_encoding=url_encode)
        new_urls = self._get_new_urls(url, soup)
        new_data = self._get_new_data(url, soup)
        return new_urls, new_data

    def _get_new_urls(self, url, soup):
        new_urls = set()
        links = soup.find_all("a", href=re.compile(r"/item/\w+"))
        for link in links:
            url_path = link["href"]
            new_url = urljoin(url, url_path)
            new_urls.add(new_url)
        return new_urls

    def _get_new_data(self, url, soup):
        data = {"url": url}
        title_node = soup.find("dd", class_="lemmaWgt-lemmaTitle-title").find("h1")
        data["title"] = title_node.get_text()
        sumary_node = soup.find("div", class_="lemma-summary")
        data["summary"] = sumary_node.get_text()
        return data

