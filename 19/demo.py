import scrapy									# 导入框架

class QuotesSpider(scrapy.Spider):
    name = "quotes"							# 定义爬虫名称
    def start_requests(self):
        # 设置爬取目标的地址
        urls = [
            'http://quotes.toscrape.com/page/1/',
            'http://quotes.toscrape.com/page/2/',
        ]
        # 获取所有地址，有几个地址发送几次请求
        for url in urls:
            # 发送网络请求
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        # 获取页数
        page = response.url.split("/")[-2]
        # 根据页数设置文件名称
        filename = 'quotes-%s.html' % page
        # 以写入文件模式打开文件，如果没有该文件将创建该文件
        with open(filename, 'wb') as f:
            # 向文件中写入获取的html代码
            f.write(response.body)
        # 输出保存文件的名称
        self.log('Saved file %s' % filename)
