from xbmcswift2 import Plugin, xbmcgui
from resources.lib import mainaddon

plugin = Plugin()
url1 = "https://anchor.fm/s/ef064ec/podcast/rss"
@plugin.route('/')
def main_menu():
    items = [
        {
            'label': plugin.get_string(30001), 
            'path': plugin.url_for('episodes1'),
            'thumbnail': "https://is2-ssl.mzstatic.com/image/thumb/Podcasts113/v4/50/cd/76/50cd7644-4e3f-f422-1ef4-16cf59cdd064/mza_2962122923947545873.jpg/600x600bb.jpg"},
        {
            'label': plugin.get_string(30000),
            'path': plugin.url_for('episodes'),
            'thumbnail': "https://is2-ssl.mzstatic.com/image/thumb/Podcasts113/v4/50/cd/76/50cd7644-4e3f-f422-1ef4-16cf59cdd064/mza_2962122923947545873.jpg/600x600bb.jpg"},
    ]
    return items

@plugin.route('/episodes1/'
def episodes1():
    soup1 = mainaddon.get_soup1(url1)
    playable_podcast1 = mainaddon.get_playable_podcast1(soup1)
    items = mainaddon.compile_playable_podcast1(playable_podcast1)
    return items
@plugin.route('/episodes/')
def episodes():
    soup1 = mainaddon.get_soup1(url1)
    playable_podcast = mainaddon.get_playable_podcast(soup1)
    items = mainaddon.compile_playable_podcast(playable_podcast)
    return items
if __name__ == '__main__':
    plugin.run()
