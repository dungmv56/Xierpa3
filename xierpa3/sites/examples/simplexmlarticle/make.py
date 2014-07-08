# -*- coding: UTF-8 -*-
# -----------------------------------------------------------------------------
#    xierpa server
#    Copyright (c) 2014+  buro@petr.com, www.petr.com, www.xierpa.com
#    
#    X I E R P A  3
#    Distribution by the MIT License.
#
# -----------------------------------------------------------------------------
#
#    make.py
#
import webbrowser
from xierpa3.attributes import Em, Px, Perc, Color
from xierpa3.toolbox.transformer import TX
from xierpa3.adapters import XmlFileAdapter
from xierpa3.components import Theme, Page, Column, Container
from xierpa3.builders.cssbuilder import CssBuilder
from xierpa3.builders.htmlbuilder import HtmlBuilder
from xierpa3.descriptors.blueprint import BluePrint
from xierpa3.descriptors.media import Media # Include type of Style that holds @media parameters.

# Define the two component here. Normally these would come from a component library,
# where the BluePrint values function as API to adjust the component instance behavior
# from the outside.

class ArticleAdapter(XmlFileAdapter):
    u"""Inherit from the <b>FileAdapter</b> to read the example XML article file."""
    
    def getArticle(self, id=None):
        u"""Redefine this method of the standard <b>FileAdapter</b> always to answer
        the one example article. Normal usage is that the <b>id</b> attribute is connected
        to the current url, as available from <b>builder.getCurrentArticleId()</b>.
        The builders always know the request parameters, such as the url of the page."""
        return self.getCachedArticle('manifest-on-skills')

class SimpleArticle(Column):
    u"""The <b>SimpleArticle</b> class is a simplified example component, similar to the main 
    <b>Article</b> component, showing how an XML article file can be used as “database”
    for content structure."""
    def buildColumn(self, b):
        articleData = self.adapter.getArticle(id=b.getCurrentArticleId())
        self.buildArticleData(b, articleData)

    def buildArticleData(self, b, articleData):
        b.img(src=articleData.poster)
        b.br()
        b.text(articleData.category)
        b.br()
        b.text('AAAAAA')
        
class SimpleXmlArticle(Theme):
    # Get Constants->Config as class variable, so inheriting classes can redefine values.
    C = Theme.C

    TITLE = u'The Simple Website Example Page' # Use as title of window.

    BODYSIZE = Px(12)
    BODYLEADING = Em(1.4)
    BODYFAMILY = '"Hermes FB Book", Verdana, sans'
    HEADFAMILY = '"Hermes FB Semibold", Impact, sans'
    
    CC = Theme # Inherit the constants from the parent class.
    
    URL_FONTS = [
        # Note that this package contains the a set of latest featured font, and may be changed in the future.
        # If using the font in this package, safest is to refer to the functional constant names below,
        # instead of making a direct reference to the family name.
        # Of course, taking your own account at //www.webtype.com is even better :)
        C.XIERPA3_DEMOFONTS, # Webtype @fontface fonts, to be used for localhost demo purposes.
    ]    

    def baseStyle(self):
        s = self.newStyle() # Answer root style without selector
        s.addStyle('body', fontfamily=self.BODYFAMILY, fontsize=self.BODYSIZE, lineheight=self.BODYLEADING)
        s.addStyle('h1, h2, h3, h4, h5, p.lead', fontfamily=self.HEADFAMILY)
        s.addStyle('h6', fontfamily=self.BODYFAMILY)
        s.addStyle('div', float=self.C.LEFT, width=Perc(100))
        return s
    
    def baseComponents(self):
        # Create the component instances
        from xierpa3.sites.examples import simplexmlarticle
        # Root path where to find the article XML file for this example page.
        articleRoot = TX.module2Path(simplexmlarticle) + '/files/articles/' 
        adapter = ArticleAdapter(articleRoot) # Preferred adapter class for articles in this site.
        # Create the article component to contain articles answered by the adapter.
        article = SimpleArticle(adapter=adapter) 
        # Put the article in a container for automatic responsive behavior
        container = Container(components=article, backgroundcolor=Color('yellow'))
        # The class is also the page name in the url.
        homePage = Page(class_=self.C.TEMPLATE_INDEX, name=self.C.TEMPLATE_INDEX, fonts=self.URL_FONTS,
            title=self.TITLE, css=self.C.URL_CSS, components=container)
        return [homePage]
    
    def make(self, root=None):
        u"""The instance of this class builds CSS and HTML files at the optional path <b>root</b>.
        If not defined, then the default ~/Desktop/Xierpa3Examples/[component.name] is used as export path,
        as set by Builder.DEFAULT_ROOTPATH"""
        
        cssBuilder = CssBuilder()
        self.build(cssBuilder)
        cssBuilder.save(self, root) 
        htmlBuilder = HtmlBuilder()
        self.build(htmlBuilder)
        return htmlBuilder.save(self, root)  
    
if __name__ == '__main__':
    # This construction "__name__ == '__main__'" makes this Python file only 
    # be executed when called in direct mode, such as "python make.py" in the terminal.         
    # Since no rootPath is added to make(), the file export is in ~/Desktop/Xierpa3Examples/Featuring1/   
    path = SimpleXmlArticle().make()
    webbrowser.open(path)