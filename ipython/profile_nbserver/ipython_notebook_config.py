from __future__ import unicode_literals

c = get_config()

# c.IPKernelApp.pylab = 'inline'
c.NotebookApp.open_browser = False
c.NotebookApp.ip = '*'
c.NotebookApp.port = 8888
# c.NotebookApp.notebook_dir = u'/root/ipython/notebooks'
# c.NotebookApp.ipython_dir = u'/root/ipython'
c.NotebookApp.enable_mathjax = True
# c.NotebookApp.browser = u''
c.NotebookApp.password = u'sha1:d291a0ca750b:48b26eb834f35673cacaa6572c8439e294c83c06'
