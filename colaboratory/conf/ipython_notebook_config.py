from __future__ import unicode_literals

c = get_config()

# c.IPKernelApp.pylab = 'inline'
c.NotebookApp.open_browser = False
c.NotebookApp.ip = '*'
c.NotebookApp.port = 8080
# c.NotebookApp.notebook_dir = u'/root/ipython/notebooks'
# c.NotebookApp.ipython_dir = u'/root/ipython'
c.NotebookApp.enable_mathjax = True
# c.NotebookApp.browser = u''
c.NotebookApp.password = u'sha1:f7ed4d0b578a:2e7eb752977c2249a3f90b99c68856656a0985fd'
