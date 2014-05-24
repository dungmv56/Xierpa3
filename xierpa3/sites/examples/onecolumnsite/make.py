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
#    run.py
#
#    Demo site for the simple "onecolumnsite" example.
#    The "run.py" program creates the files:
#        files/css/style.scss
#        files/css/style.css
#        files/oneColumnSite.html
#    from the one OneColumnSite theme instance by applying respectively the
#    CssBuilder and HtmlBuilder to the theme.
#    Each of the builders takes the information from the theme to build its
#    own type of file.
#
import webbrowser
from xierpa3.constants.constants import C
from xierpa3.attributes import Em, Margin
from xierpa3.components import Theme, Page, Column
from xierpa3.builders.cssbuilder import CssBuilder
from xierpa3.builders.htmlbuilder import HtmlBuilder
from xierpa3.descriptors.style import Media

class ExampleColumn(Column):

    CSS_BODYFONT = '"BentonSansRE"'
    CSS_HEADFONT = '"BentonSansCond Medium"'
    
    def buildBlock(self, b):
        u"""Build the column. Note that although the "div" suggest that it is just
        HTML building there, the method get called both with <b>b</b> as CssBuilder
        and as HtmlBuilder. Each builder will filter out the appropriate attributes and
        translates it into its own syntax. The HTML tags generated by the article
        are set in CSS by the empty statements."""
        b.div(class_='column', color='#222', margin=Margin(0, self.AUTO, 0, self.AUTO), 
              width='50%', maxwidth=700, minwidth=300, backgroundcolor='#EEE', 
              padding=Em(2), fontfamily='Georgia', fontsize=Em(1), 
              lineheight=Em(1.4),
              media=Media(max=self.M_MOBILE, margin=0))
        # Since the self.adapter.getArticle answers an article that already 
        # includes XHTML tags, we cannot do the styling there. In order to 
        # define the unique CSS styles, a blank document content is created 
        # for the CssBuilder to evaluate, so we have all the definitions inside 
        # div.column, in case they are used in the article.
        if b.isType(self.TYPE_CSS):
            self.buildCssColumnTemplate(b)
        else:
            for data in self.adapter.getFeaturedArticles(self):
                # Build the headline without style attribute, as these are already defined
                # in the self.buildCssColumnTemplate call.
                b.h1()
                b.text(data.headline)
                b._h1()
                if data.image:
                    # Build the image that came with the featured article, if it exists.
                    # Make it class autowidth to solve the width="100%" incompatibility
                    # between browsers.
                    b.img(src=data.image, class_=self.CLASS_AUTOWIDTH)
                # Output the rest of the featured article.
                b.text(data.item)
            # Add some more volume to the blurb article. 
            data = self.adapter.getArticle(self)
            b.h2()
            b.text(data.headline)
            b._h2()
            for item in data.items:
                b.text(item)
        b._div()
        
    def buildCssColumnTemplate(self, b):
        u"""Build the single CSS for all expected tags in an article that is answered
        by <b>self.adapter</b>. We cannot check on that here, since the content may
        vary and even is hidden by e.g. calls to a PHP adapter.""" 
        b.h1(fontfamily=self.CSS_HEADFONT, color='#888', fontsize=Em(1.6), lineheight=Em(1.1),
             marginbottom=Em(0.5))
        # Headling made by BlurbAdapter
        b._h1()
        b.h2(fontfamily=self.CSS_HEADFONT, fontstyle=self.ITALIC, color='#444', 
             fontsize=Em(1.4), lineheight=Em(1.2), margintop=Em(1), marginbottom=Em(0.5))
        # Headling made by BlurbAdapter
        b._h2()
        b.img(margintop=Em(0.5), marginbottom=Em(0.5))
        b.p(textindent=Em(1))
        # Main paragraphs have an indent.
        b._p()
        b.p(class_='start', textindent=0)
        # The start paragraph (the element before was not a <p>) has no indent.
        b._p()
        b.p(class_='end', fontweight=self.BOLD, marginbottom=Em(1),
            margintop=Em(0.5), textindent=0)
        # Mark the end paragraph (the element after is not a <p>) in case something
        # special needs to be done, e.g. change the marginbottom.
        # @@@ TODO: Mark as p.end preceding <blockquote> too.
        b._p()
        b.blockquote(padding=Margin(Em(0.5), Em(1)), fontsize=Em(1.2), lineheight=Em(1.3),
            margintop=Em(0.5), marginbottom=Em(0.5), #border=Border('solid', 2, Color('E1E2E2')),
            fontstyle=self.ITALIC, backgroundcolor='#DDD', color=self.BLACK)
        # Italic blockquotes with an indent and backgroundcolor.
        b._blockquote()

class OneColumnSite(Theme):
    u"""The <b>TextColumn</b> generates an HTML file with a column of random blurb text. 
    Double click the generated file or drag to a browser see the result."""
    TITLE = u'The Single Column Example Page.' # Use as title of window.

    URL_FONTS = (
        # Topaz (Benton Sans RE)
        'http://cloud.webtype.com/css/7aa22aa1-1709-4b55-b95c-3413d3e5280a.css',
    )
    # The single column is filled by the self.adapter article query result.
    # The default self.adapter (if nothing else is defined) is the BlurbAdapter,
    # which generates random pieces of text.
    
    def baseComponents(self):
        u"""Create a theme site with just one single template home page. Answer a list
        of page instances that are used as templates for this site."""
        # Create an instance (=object) of components to be placed on the page.
        column = ExampleColumn()
        # Create an instance (=object) of the page, containing the navigation components.
        homePage = Page(components=(column,), title=self.TITLE, fonts=self.URL_FONTS)
        # Answer a list of types of pages for this site. In this case just one template.
        return [homePage]
    
    def make(self):
        u"""Make the instance of this class to build CSS and HTML."""
        # Create an "instance" (=object) of type "HelloWorldLayout". The type (=class) defines
        # the behavior of the object that is made by calling the class.

        # C S S
        # Create the main CSS builder instance to build the CSS part of the site.
        cssBuilder = CssBuilder()
        # Compile (=build) the SCSS to CSS and save the file in "css/style.css".
        cssBuilder.save(self) 
    
        # H T M L
        # Create the main HTML builder instance to build the HTML part of the site.
        htmlBuilder = HtmlBuilder()
        # Compile the HTML and save the resulting HTML file in "helloWorld.html".
        # Answer the path, so we can open the file with a browser.
        return htmlBuilder.save(self)  
    
if __name__ == '__main__':
    # This construction "__name__ == '__main__'" makes this Python file only 
    # be executed when called in direct mode, such as "python make.py" in the terminal.         
    path = OneColumnSite().make()
    webbrowser.open(path)
    