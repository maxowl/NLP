import re
from robobrowser import RoboBrowser

browser = RoboBrowser(user_agent='a python robot')
browser.open('http://www.royin.go.th/dictionary/lookup_domain.php')

# Inspect the browser session
#browser.session.cookies['_gh_sess']         # BAh7Bzo...
#browser.session.headers['User-Agent']       # a python robot

# Search the parsed HTML
'''browser.select('div.teaser-icon')       # [<div class="teaser-icon">
                                        # <span class="mega-octicon octicon-checklist"></span>
                                        # </div>,
                                        # ...
browser.find(class_=re.compile(r'column', re.I))    # <div class="one-third column">
                                                    # <div class="teaser-icon">
                                                    # <span class="mega-octicon octicon-checklist"></span>
                                                    # ...'''