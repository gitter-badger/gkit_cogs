"""Vape naysh y'all.

Ordered a vape juice and can't remember what that wacky name actually
means for your vaping experience? Well come on over friendo, I've got
just the thing for you.

Can currently lookup vape juices on the following websites:

  - [x] Blue Dot Vapors (bdv)
  - [ ] White Label Juice Co. (wlj)

NOTE: Vaporizers and the associated liquids/juices are regulated under the
same laws as tobacco as of August 8, 2016. Please see the federal registrar
entry for further information:

    https://www.federalregister.gov/documents/2016/05/10/2016-10685/deeming-tobacco-products-to-be-subject-to-the-federal-food-drug-and-cosmetic-act-as-amended-by-the

Neither I, nor the Red creators, staff, or community, promote underage use of
tobacco.
"""

import discord
from discord.ext import commands

try:
    # check if BeautifulSoup4 is installed
    from bs4 import BeautifulSoup
    soupAvailable = True
except ValueError:
    soupAvailable = False

import aiohttp
import random


class VapeNayshError(Exception):
    pass


class VapeNaysh:

    def __init__(self, bot):
        self.bot = bot

    @commands.group(name='vape', pass_context=True)
    async def vape(self, context):
        if not soupAvailable:
            await self.bot.say('Sorry, you need BeautifulSoup4 installed.')
        if context.invoked_subcommand is None:
            await self.bot.say('Type `[p]help vape` for info.')

    @vape.command(
        name='bdv', aliases=['bluedot', 'bluedotvapors'])
    async def bdv(self, *, flavor: str):
        await self.get_flavor(flavor, 0)

    @vape.command(name='wlj', aliases=['whitelabel', 'whitelabeljuiceco'])
    async def wlj(self, *, flavor: str):
        await self.get_flavor(flavor, 1)

    async def get_flavor(self, flavor, mode):
        if not flavor:
            await self.bot.say("Type `[p]help vape wlj` for info.")
        else:
            if mode is 0:
                url = (
                    'https://www.bluedotvapors.com/' +
                    'collections/eliquid/products/' +
                    flavor.replace(' ', '-'))
            elif mode is 1:
                url = (
                    'https://whitelabeljuiceco.com/' +
                    'collections/whitelabel-juice/products/' +
                    flavor.replace(' ', '-')) + '-100ml'
            async with aiohttp.ClientSession() as session:
                async with session.get(url) as response:
                    if response.status is 200:
                        data = await response.text()
                        soup = BeautifulSoup(data, 'html.parser')

                        description = self.get_description(soup, mode)
                        rating = self.get_rating(soup, mode)
                        rating_str = (
                            (':fire:' * rating) +
                            (':heavy_multiplication_x:' * (5 - rating)))

                        reviews = self.get_reviews(soup, mode)
                        reviews_str = ' _**~' + str(reviews) + ' reviews**_'

                        img_url = 'http:' + self.get_image(soup, mode)

                        if rating >= 4:
                            tag = ':boom:'
                        elif rating < 3:
                            tag = ':zzz:'
                        else:
                            tag = ''

                        name = self.get_name(soup, mode)
                        name_str = '_**' + name + '**_ ' + tag

                        embed = discord.Embed(colour=0x6441A4, title=name_str)
                        embed.set_thumbnail(url=img_url)
                        embed.add_field(
                            name='Buy', value=url)
                        embed.add_field(
                            name='Description', value=description)
                        embed.add_field(
                            name='Rating', value=(rating_str + reviews_str))
                        await self.bot.say(embed=embed)
                    else:
                        await self.bot.say(
                            'Sorry, could not find your flavor: {}'.format(
                                flavor))

    def get_rating(self, soup, mode):
        if mode is 0:
            return int(float(soup.find(
                'div', {'itemprop': 'aggregateRating'}).find(
                    'span').find(
                        'meta', {'itemprop': 'ratingValue'}).get(
                            'content')))
        elif mode is 1:
            return int(float(soup.find(
                'meta', {'itemprop': 'ratingValue'}).get('content')))
        return -1

    def get_reviews(self, soup, mode):
        if mode is 0:
            return soup.find(
                'div', {'itemprop': 'aggregateRating'}).find(
                    'span').find(
                        'meta', {'itemprop': 'reviewCount'}).get('content')
        elif mode is 1:
            return soup.find('meta', {
                'itemprop': 'reviewCount'}).get('content')
        return ''

    def get_name(self, soup, mode):
        if mode is 0 or mode is 1:
            return soup.find('h1', {'itemprop': 'name'}).getText()
        return ''

    def get_description(self, soup, mode):
        if mode is 0:
            return soup.find('div', {
                'id': 'full_description'}).find('p').getText()
        elif mode is 1:
            return soup.find('div', {
                'itemprop': 'description'}).find('p').getText()
        return ''

    def get_image(self, soup, mode):
        if mode is 0:
            return soup.find('img', {'id': 'productPhotoImg'}).get('src')
        elif mode is 1:
            imgs = soup.find_all(
                'img', {'class': 'ProductImg-product'})
            return imgs[random.randint(0, len(imgs))].get('src')
        return ''


def setup(bot):
    bot.add_cog(VapeNaysh(bot))
