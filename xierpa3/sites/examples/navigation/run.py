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
#    Demo site for the simple "navigation" example.
#    The "run.py" program creates the files:
#        files/css/style.scss
#        files/css/style.css
#        files/helloWorld.html
#    from the one NavigationExample theme instance by applying respectively the
#    CssBuilder and HtmlBuilder to the theme.
#    Each of the builders takes the information from the theme to build its
#    own type of file.
#
from xierpa3.constants.constants import C
from xierpa3.attributes import Em
from xierpa3.components import Theme, Page, Column, MobileNavigation, Navigation
from xierpa3.builders.cssbuilder import CssBuilder
from xierpa3.builders.htmlbuilder import HtmlBuilder

class ExampleColumn(Column):
    def buildBlock(self, b):
        b.div(class_='column', color='#222', marginleft='10%', width='50%', 
              float=C.LEFT, backgroundcolor='#EEE', padding=Em(2), 
              fontfamily='Georgia', fontsize=Em(1), lineheight=Em(1.4))
        b.p(textindent=Em(1))
        b._p()
        b.p(class_='start', textindent=0)
        b._p()
        b.p(class_='end', fontweight=C.BOLD, marginbottom=Em(1),
            margintop=Em(0.5), textindent=0)
        b._p()
        b.blockquote(margin=Em(1), fontsize=Em(1.2), lineheight=Em(1.3),
            fontstyle=C.ITALIC)
        b._blockquote()
        for item in self.adapter.getArticle(self).items:
            b.text(item)
        b._div()
        
class NavigationExample(Theme):
    u"""The <b>HelloWorld</b> class implements a basic Hello World page, running as
    batch process, saving the result as an HTML file. Double click the generated file or
    drag to a browser see the result."""
    TITLE = u'The navigation example page.' # Use as title of window.

    def getRootPath(self):
        u"""Get the root path for the "files/" directory, so the builder knows where to 
        write the HTML file."""
        from xierpa3.sites.examples import navigation
        return navigation.__path__[0]

    def baseComponents(self):
        u"""Create a theme site with just one single template home page. Answer a list
        of page instances that are used as templates for this site."""
        # Create an instance (=object) of components to be placed on the page.
        mobileNavigation = MobileNavigation()
        navigation = Navigation()
        column = ExampleColumn()
        # Create an instance (=object) of the page, containing the navigation components.
        homePage = Page(components=(mobileNavigation, navigation, column), title=self.TITLE)
        # Answer a list of types of pages for this site.
        return [homePage]
    
if __name__ == '__main__':
    # This construction "__name__ == '__main__'" makes the Python file only 
    # be executed when called in direct mode, such as "python run.py" in the terminal. 
    
    # Create an "instance" (=object) of type "NavigationExample". The type (=class) defines
    # the behavior of the object that is made by calling the class.
    site = NavigationExample()
    
    # C S S
    # Create the main CSS builder instance to build the CSS part of the site with.
    cssBuilder = CssBuilder()
    # Compile (=build) the SCSS to CSS and save the file.
    cssBuilder.save(site) 

    # H T M L
    # Create the main HTML builder instance to build the HTML part of the site with.
    htmlBuilder = HtmlBuilder()
    # Compile the HTML and save the resulting HTML file in "files/hellowork.html".
    htmlBuilder.save(site) 
