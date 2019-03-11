import time


class HtmlOutput(object):
    """
    对解析得到的数据进行渲染,再当前目录输出一个带时间戳命名的html文件
    """
    def __init__(self):
        self.datas = []

    def collect_data(self, data):
        if data is None:
            return
        self.datas.append(data)

    def output_html(self):
        file_name = time.strftime("%Y-%m-%d_%H-%M-%S")
        with open("out_%s.html" % file_name, "w", encoding="utf-8") as f_out:
            f_out.write(r"""
                            <html>
                                <head>
                                <link rel="stylesheet"href="https://cdn.bootcss.com/bootstrap/3.3.7/css/bootstrap.min.css"
                                    integrity="sha384-BVYiiSIFeK1dGmJRAkycuHAHRg32OmUcww7on3RYdg4Va+PmSTsz/K68vbdEjh4u" crossorigin="anonymous"></head>
                                <body>
                                <table class="table table-bordered table-hover">
                            """)
            item_css = ['active', 'success', 'warning', 'info']
            for data in self.datas:
                index = self.datas.index(data) % len(item_css)
                f_out.write(r'<tr class="'+item_css[index]+r'">')
                f_out.write('<td>%s</td>' % data["url"])
                f_out.write('<td>%s</td>' % data["title"])
                f_out.write('<td>%s</td>' % data["summary"])
                f_out.write('</tr>')

            f_out.write("</table>")
            f_out.write("</body>")
            f_out.write("</html>")

