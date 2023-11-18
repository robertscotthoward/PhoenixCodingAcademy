import sys
import os
import markdown

# Get this file's path so we can find the libs/
thisFile = os.path.abspath(sys.argv[0])
thisPath = os.path.dirname(thisFile)
root = os.path.abspath(os.path.join(thisPath, os.path.relpath('../..')))
sys.path.insert(0, root)

import libs.tools as tools

md = '''
$X = Y$
'''
html = markdown.markdown(md, extensions=[
      'pymdownx.arithmatex',
      #'mdx_math',
      #'mathjax',
      # 'eqnmath',
      # 'alignmath',
      'fenced_code',
      'md_mermaid',
      ])
print('===================')
print(html)
