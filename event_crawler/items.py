from scrapy.item import Item, Field

class EventItem(Item):
    artist = Field()
    venue = Field()
    date = Field()
    price = Field()
