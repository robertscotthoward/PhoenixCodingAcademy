import markdown

md = '''
~~~mermaid
graph LR
INPUT1 --> PROCESS1([PROCESS1])
~~~
'''

html = markdown.markdown(md, extensions=[
      'fenced_code', # triple backticks
      'md_mermaid'])

print(html)