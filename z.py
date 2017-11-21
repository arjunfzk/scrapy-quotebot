import scrapy

class quotes(scrapy.Spider):
	name="quotes"
	start_urls=['http://quotes.toscrape.com']

	def parse(self, response):

		self.log('I just visited' + response.url)	
		for quote in response.css('div.quote'):

			item= {
				'author_name':quote.css('small.author::text').extract_first(),
				'text':quote.css('span.text::text').extract_first(),

				'tags':quote.css('a.tag::text').extract(),
			}
			yield item
		nex=response.css('li.next > a::attr(href)').extract_first()
		if nex:
			nex=response.urljoin(nex)
			yield scrapy.Request(url=nex,callback=self.parse)