# Copyright (c) 2012 - Samuel Loretan <tynril at gmail.com>
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

import urllib2
try:
    import json
except ImportError:
    import simplejson as json

class Gw2Spidy:
    """This utility class allows easy access to the GW2Spidy data."""
    headers = {'User-Agent': 'gw2spidy.py'}

    @staticmethod
    def getTypesList():
        """Get a list of item types and subtypes."""
        return Gw2Spidy._request('types')['results']

    @staticmethod
    def getDisciplinesList():
        """Get a list of crafting disciplines."""
        return Gw2Spidy._request('disciplines')['results']

    @staticmethod
    def getRaritiesList():
        """Get a list of item rarities."""
        return Gw2Spidy._request('rarities')['results']

    @staticmethod
    def getAllItemsList():
        """Get a list of all items."""
        return Gw2Spidy._request('all-items', 'all')['results']

    @staticmethod
    def getItemsOfType(typeId):
        """Get a list of all items of a certain type."""
        return Gw2Spidy._request('all-items', str(typeId))['results']

    @staticmethod
    def getItemData(itemId):
        """Get the data of a particular item. High frequency of update."""
        return Gw2Spidy._request('item', str(itemId))['result']

    @staticmethod
    def getItemBuyListings(itemId, allPages = False):
        """Get a list of all buy offers for a certain item."""
        return Gw2Spidy._paginatedRequest(allPages, 'listings', str(itemId), 'buy')

    @staticmethod
    def getItemSellListings(itemId, allPages = False):
        """Get a list of all sell offers for a certain item."""
        return Gw2Spidy._paginatedRequest(allPages, 'listings', str(itemId), 'sell')

    @staticmethod
    def searchItems(name, allPages = False):
        """Search items by name. Might be slow, not recommended."""
        return Gw2Spidy._paginatedRequest(allPages, 'item-search', name)

    @staticmethod
    def getAllRecipesList(allPages = False):
        """Get a list of all crafting recipes."""
        return Gw2Spidy._paginatedRequest(allPages, 'recipes', 'all')

    @staticmethod
    def getRecipesOfDiscipline(disciplineId, allPages = False):
        """Get a list of all crafting recipes for a certain discipline."""
        return Gw2Spidy._paginatedRequest(allPages, 'recipes', str(disciplineId))

    @staticmethod
    def getRecipeData(recipeId):
        """Get the data of a particular recipe."""
        return Gw2Spidy._request('recipe', str(recipeId))

    @staticmethod
    def getGemPrice():
        """Get the current gem/gold conversion rate."""
        return Gw2Spidy._request('gem-price')

    @staticmethod
    def _paginatedRequest(allPages, *args):
        """Handle paginated requests, downloading all pages if requested."""
        data = []
        currentPage = 0
        while True:
            newData = Gw2Spidy._request(*(args + (str(currentPage),)))
            if not allPages:
                return newData['results']
            data.extend(newData['results'])
            currentPage = currentPage + 1
            if newData['page'] == newData['last_page']:
                break
        return data

    @staticmethod
    def _request(*args):
        """Makes a request on the GW2Spidy API."""
        url = 'http://www.gw2spidy.com/api/v0.9/json/' + '/'.join(args)
	r = urllib2.Request(url, headers=Gw2Spidy.headers)
	if 'Cookie' not in Gw2Spidy.headers:
	    resp = urllib2.urlopen(r)
	    if 'set-cookie' in resp.headers:
		Gw2Spidy.headers['Cookie'] = resp.headers['set-cookie'].split(';', 1)[0]
	    return json.loads(resp.read())
        return json.loads(urllib2.urlopen(r).read())
