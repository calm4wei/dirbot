from scrapy.item import Item, Field


class Website(Item):

    name = Field()
    description = Field()
    url = Field()

class PersonLink(Item):
    name = Field()
    url = Field()

class Person(Item):
    name = Field()
    url = Field()
    description = Field()
