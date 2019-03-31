# -*- coding: utf-8 -*-

class boTool:
    def __init__(self):
        return

    def clearTag_old(self, text):
        import lxml
        from lxml.html.clean import Cleaner

        cleaner = Cleaner()
        cleaner.javascript = True # This is True because we want to activate the javascript filter
        cleaner.style = True # This is True because we want to activate the styles & stylesheet filter
        cleaner.links = True
        cleaner.meta = True
        cleaner.forms = True
        cleaner.embedded = True
        cleaner.frames = True
        cleaner.remove_unknown_tags= True
        #cleaner.allow_tags=['']
        cleaner.kill_tags = ['img']
        cleaner.remove_tags=['strong','div','body','br','a', 'p','blockquote','h3', 'ol', 'li', 'font']
        return cleaner.clean_html(lxml.html.document_fromstring(text)).decode('utf-8')
        # return lxml.html.tostring(cleaner.clean_html(lxml.html.document_fromstring(text))).decode('utf-8')

    def clearTag(self, text):
        import lxml
        from lxml.html.clean import Cleaner
        try:
           cleaner = Cleaner(remove_unknown_tags = False)
           cleaner.allow_tags=['']
           return lxml.html.tostring(cleaner.clean_html(lxml.html.document_fromstring(text)), encoding='unicode').replace('<div>','').replace('</div>','').replace('&#13;','').replace('\'','\\\'').rstrip('\n\n')  
        except :
            return ''
