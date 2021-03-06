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
#    documentation.py
#
#    @@@ Under development
#
#    The documentation component shows an automatic generated manual, derived
#    from nameing and docstrings of a given set of classes.
#
import inspect
import xierpa3
from xierpa3.components.container import Container
from xierpa3.attributes import Em, Color
from xierpa3.descriptors.blueprint import BluePrint

class Documentation(Container):

    #    @@@ Under development

    # Get Constants->Config as class variable, so inheriting classes can redefine values.
    C = Container.C 

    BLUEPRINT = BluePrint( 
        h2FontSize=Em(2), doc_h2FontSoze=u'h2 font size.',
        h2Color=Color('#202020'), doc_h2Color=u'h2 color', 
        h3FontSize=Em(1.5), doc_h3FontSoze=u'h3 font size.',
        test='TEST',
    )
    def buildContainerBlock(self, b):
        if b.isType(('css', 'sass')): # @@@ Clean up, using model article?
            self.buildDocStyle(b) # Separate CSS for first chapter and the rest.
        else:
            self.buildDoc(b, xierpa3)
    
    def buildDocStyle(self, b):
        s = self.style
        b.div(class_='label')
        b.h3(fontsize=s.h3FontSize)
        b.span(class_='classSource', color='green')
        b._span()
        b._h3()
        b._div()
        b.h2(class_='h2', fontsize=s.h2FontSize, color=s.h2Color)
        b._h2()
         
    
    def buildDocNavigation(self, b, module=None, modulepath='', i=0):
        u"""Traverses through the Xierpa object hierarchy."""
        max = 2

        if i == max:
            return

        b.ul()
        for name, obj in inspect.getmembers(module):
            if self.isboring(name):
                continue
            self.li()
            params = {'d': modulepath + '&' + name}
            b.a(href=self.e['path'], params=params)
            b.text(name)
            b._a()
            self.buildDocNavigation(b, obj, modulepath + '&' + name, i + 1)
            b._li()
        b._ul()

    def getBoring(self):
        more_boring = ['timedelta', 'sys', 'os', 'mojo', 'contributions', '__builtins__']
        boring = dir(type('dummy', (object,), {}))
        for b in more_boring:
            boring.append(b)

        return boring

    def isBoring(self, name):
        if name in ['timedelta', 'sys', 'os', 'mojo']:
            return True
        if name.startswith('__'):
            return True
        return False

    def buildDoc(self, b, module):
        u"""
        Uses the inspect module to extract documentation from objects. Skips boring classes.    
        """
        modulePath = module.__file__.replace('/__init__.pyc', '')
        b.h1(fontsize=Em(2), color='#202020', lineheight=Em(1.4))
        b.text(modulePath.replace('&', u'→'))
        b._h1()
    
        # Recursively collect all classes
        modules = self.getModules('xierpa3', module)
        for m in modules:
            b.h2(fontsize=Em(1.5), lineheight=Em(1.4))
            b.text(m.__name__)
            b._h2()
            classes = self.getClasses(m)
            if len(classes):
                for cls in classes:
                    self.showClass(b, cls)
                
    def getModules(self, rootName, module, modules=None):
        if modules is None:
            modules = []
        for name, obj in inspect.getmembers(module):
            if self.isBoring(name):
                continue
            if inspect.ismodule(obj):
                if not obj in modules and rootName in `obj`:
                    modules.append(obj) 
                    self.getModules(rootName, obj, modules)
        return modules
    
    def getClasses(self, module, classes=None):
        if classes is None:
            classes = []
        for name, obj in inspect.getmembers(module):
            if self.isBoring(name):
                continue
            if inspect.isclass(obj):
                if not obj in classes:
                    classes.append(obj)
        return classes
    
        """
        b.div(class_='documentation', margintop=Em(0.5))
        for name, obj in inspect.getmembers(module):
            if self.isBoring(name):
                continue
            b.div(class_="label", width='20%', float=self.LEFT, clear=self.BOTH,
                display=self.BLOCK,  bordertop='1px solid black')
            b.h2(fontsize=Em(1.5), width=Perc(100), lineheight=Em(1.4))
            if inspect.isclass(obj):
                b.text(u'✏ ')
                b.span(class_="classSource")
                b.text('class')
                b._span()
            elif inspect.isfunction(obj):
                b.span(class_="functionSource")
                b.text('function')
                b._span()
            else: # It is folder name, make it appear as title
                b.text(name.capitalize())
            b._h2()
            
            b.div(class_='description', bordertop='1px solid black')
            if hasattr(obj, '__doc__') and obj.__doc__:
                b.text(obj.__doc__)
            self.showObj(b, obj)
            b._div()
            b._tr()
        b._table()
        """
    def showClass(self, b, cls):
        b.div(class_="label", marginleft=Em(3), width='20%', float=self.LEFT, clear=self.BOTH,
            display=self.BLOCK,  bordertop='1px solid black', backgroundcolor='#EEEEEE')
        b.h3(fontsize=Em(1.5), lineheight=Em(1.4))
        b.span(class_="classSource", color='green')
        b.text('class')
        b._span()
        b.text(cls.__name__)
        b._h3()
        #for name, obj in inspect.getmembers(module):
            # method test: if inspect.
        b._div()
        b.div(width='74%', float=self.LEFT, backgroundcolor='#DDDDDD')
        if hasattr(cls, '__doc__') and cls.__doc__:
            try:
                b.text(cls.__doc__)
            except Exception, e:
                b.text(`e`)
                print e
        b._div()
