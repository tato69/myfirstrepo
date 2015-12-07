from pygoogle import pygoogle

g = pygoogle('microsoft')
g.pages = 1
print '*Found %s results*'%(g.get_result_count())
print g.get_urls()
g.display_results()
