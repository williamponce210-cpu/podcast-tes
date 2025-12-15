import yaml
import xml.etree.ElementTree as xml_tree

with open('feed.yaml', 'r', encoding='utf-8') as file:
    yaml_data = yaml.safe_load(file)

LINK_PREFIX = "https://williamponce210-cpu.github.io/podcast-tes"

rss = xml_tree.Element(
    'rss',
    {
        'version': '2.0',
        'xmlns:itunes': 'http://www.itunes.com/dtds/podcast-1.0.dtd'
    }
)

channel = xml_tree.SubElement(rss, 'channel')

xml_tree.SubElement(channel, 'title').text = yaml_data.get('title', '')
xml_tree.SubElement(channel, 'link').text = LINK_PREFIX
xml_tree.SubElement(channel, 'language').text = yaml_data.get('language', 'en-us')
xml_tree.SubElement(channel, 'description').text = yaml_data.get('description', '')
xml_tree.SubElement(channel, 'itunes:subtitle').text = yaml_data.get('subtitle', '')
xml_tree.SubElement(channel, 'itunes:author').text = yaml_data.get('author', '')

image_path = yaml_data.get('image', '/images/artwork.jpg')
xml_tree.SubElement(
    channel,
    'itunes:image',
    {'href': LINK_PREFIX + image_path}
)

xml_tree.SubElement(
    channel,
    'itunes:category',
    {'text': yaml_data.get('category', 'Technology')}
)

for item in yaml_data.get('items', []):
    it = xml_tree.SubElement(channel, 'item')

    xml_tree.SubElement(it, 'title').text = item.get('title', '')
    xml_tree.SubElement(it, 'description').text = item.get('description', '')
    xml_tree.SubElement(it, 'pubDate').text = item.get('published', '')
    xml_tree.SubElement(it, 'itunes:author').text = yaml_data.get('author', '')
    xml_tree.SubElement(it, 'itunes:duration').text = item.get('duration', '00:00:00')

    xml_tree.SubElement(
        it,
        'enclosure',
        {
            'url': LINK_PREFIX + item.get('file', ''),
            'type': 'audio/mpeg',
            'length': str(item.get('length', 0))
        }
    )

xml_tree.ElementTree(rss).write(
    'podcast.xml',
    encoding='UTF-8',
    xml_declaration=True
)

print("XML GENERADO CORRECTAMENTE")
