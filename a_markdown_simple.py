"""
Markdown Custom class extension for Python-Markdown
=========================================

    >>> import markdown
    >>> md = markdown.Markdown(extensions=['a_markdown_simple'])
    >>> md.convert('i love!!red|spam!!')
    u'<p>i love<span class="red">spam</span></p>'

    >>> md.convert('{{summary_title}}')
    u'<p><summary>summary_title</summary></p>'


"""
from __future__ import absolute_import
from __future__ import unicode_literals
import markdown
from markdown import Extension
from markdown.inlinepatterns import Pattern
from markdown.blockprocessors import BlockProcessor
import re
import xml.etree.ElementTree as etree



#!!red|str!! >> <span class="red">spam</span>'
SPAN_CLASS = r'[!]{2}(?P<class>.+?)[|](?P<text>.+?)[!]{2}'

class MyExtension(Extension):
    def extendMarkdown(self, md, md_globals):

        #span_class
        span_class=SpanClassPattern(SPAN_CLASS, md)
        md.inlinePatterns['custom_span_class'] = span_class


class SpanClassPattern(Pattern):
    def handleMatch(self, matched):

        cls = matched.group("class")
        text = matched.group("text")

        line = markdown.util.etree.Element("span")
        line.set("class", cls)
        line.text = markdown.util.AtomicString(text)
        return line

def makeExtension(*args, **kwargs):
    return MyExtension(*args, **kwargs)

if __name__ == "__main__":
    import doctest
    doctest.testmod(
            #verbose=True
            )
    
