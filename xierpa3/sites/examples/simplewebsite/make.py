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
from xierpa3.attributes import Perc, Color, Em, Px
from xierpa3.components import Theme, Page, Container, Component
from xierpa3.builders.cssbuilder import CssBuilder
from xierpa3.builders.htmlbuilder import HtmlBuilder
from xierpa3.descriptors.blueprint import BluePrint
from xierpa3.descriptors.media import Media # Include type of Style that holds @media parameters.

# For sake of the example define two component classes here. Normally these would come 
# from a component library, where the BluePrint values function as API to adjust the 
# component instance behavior from the outside.
  
class MainColumn(Component):
    CC = Component
    
    BLUEPRINT = BluePrint(
        width=Perc(70), doc_width=u'Main column width', float=CC.LEFT, 
        backgroundColor='yellow', doc_backgroundColor=u'Main column background color.', 
    )                
    def buildBlock(self, b):
        s = self.style
        b.div(class_=self.getClassName(),
            width=s.width, backgroundcolor=s.backgroundColor, padding=Em(1), lineheight=Em(1.3),
            media=Media(max=self.M_MOBILE_MAX, backgroundcolor=s.backgroundColorMobile, 
              fontsize=Em(2), width=Perc(100), margin=0, lineheight=Em(1.3),
            )
        )
        article = self.adapter.get(self.ADAPTER_ARTICLE)
        print article
        b.h1()
        b.text(article.headline)
        b._h1()
        b.p()
        b.text(article.text)
        b._p()
        b._div(comment=self.getClassName())
          
class SideColumn(Component):
    CC = Component
    
    BLUEPRINT = BluePrint(
        width=Perc(20), doc_width=u'Side bar width', float=CC.LEFT, # @@@@ Should be 30
        backgroundColor='orange', doc_backgroundColor=u'Side column background color.',                  
        backgroundColorMobile=Color('#888'), doc_backgroundColorMobile=u'Side bar background color for mobile.',  
    )                
    def buildBlock(self, b):
        s = self.style
        b.div(class_=self.getClassName(), 
            width=s.width, backgroundcolor=s.backgroundColor, padding=Em(1), lineheight=Em(1.3),
            media=Media(max=self.M_MOBILE_MAX, backgroundcolor=s.backgroundColorMobile, 
              fontsize=Em(2), width=Perc(100), margin=0, lineheight=Em(1.3),
            )
        )
        article = self.adapter.get(self.ADAPTER_ARTICLE)
        b.h1()
        b.text(article.headline)
        b._h1()
        b.p()
        b.text(article.text)
        b._p()
        b._div(comment=self.getClassName())
        
class SimpleWebSite(Theme):
    TITLE = u'The Simple Website Example Page' # Use as title of window.

    BODYFAMILY = '"Hermes FB Book"'
    HEADFAMILY = '"Hermes FB Semibold"'
    
    BODYSIZE = Px(12)
    BODYLEADING = Em(1.4)
    
    CC = Theme # Inherit the constants from the parent class.

    URL_FONTS = [
        # Note that this package contains the a set of latest featured font, and may be changed in the future.
        # If using the font in this package, safest is to refer to the functional constant names below,
        # instead of making a direct reference to the family name.
        # Of course, taking your own account at //www.webtype.com is even better :)
        Theme.XIERPA3_DEMOFONTS, # Webtype @fontface fonts, to be used for localhost demo purposes.
    ]    

    def baseStyle(self):
        s = self.newStyle() # Answer root style without selector
        s.addStyle('body', fontfamily=self.BODYFAMILY, fontsize=self.BODYSIZE, lineheight=self.BODYLEADING)
        s.addStyle('h1, h2, h3, h4, h5, p.lead', fontfamily=self.HEADFAMILY)
        s.addStyle('h6', fontfamily=self.BODYFAMILY)
        s.addStyle('div', float=self.LEFT, width=self.C100)
        return s
    
    def baseComponents(self):
        # Create the component instances
        side = SideColumn()
        main = MainColumn()
        container = Container(components=(side, main)) # Create the single page instance, containing the 2 components
        # The class is also the page name in the url.
        homePage = Page(class_=self.TEMPLATE_INDEX, name=self.TEMPLATE_INDEX, fonts=self.URL_FONTS,
            title=self.TITLE, css=self.URL_CSS, components=container)
        return [homePage]
    
    def make(self):
        cssBuilder = CssBuilder()
        self.build(cssBuilder)
        cssBuilder.save(self) 
        htmlBuilder = HtmlBuilder()
        self.build(htmlBuilder)
        return htmlBuilder.save(self)  
    
if __name__ == '__main__':
    # This construction "__name__ == '__main__'" makes this Python file only 
    # be executed when called in direct mode, such as "python make.py" in the terminal.         
    SimpleWebSite().make()
    