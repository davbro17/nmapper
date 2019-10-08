from libnmap.parser import NmapParser

"""
report = NmapParser.parse_fromfile('./test.xml')

for host in report.hosts:
    if host.is_up():
        print(host.address)
        print(host.os_match_probabilities())
        print(host.mac)
"""
tmpl = '''
<?xml version="1.0" encoding="UTF-8"?>
<mxfile host="www.draw.io" modified="2019-10-07T01:34:52.296Z" agent="Mozilla/5.0 (X11; Fedora; Linux x86_64; rv:66.0) Gecko/20100101 Firefox/66.0" etag="dw-FbYD5rTcg-bjx4kcR" version="12.0.2" pages="1">
  <diagram id="4wd9mYppPiAM_AUK81lr" name="Page-1">
    <mxGraphModel dx="768" dy="657" grid="1" gridSize="10" guides="1" tooltips="1" connect="1" arrows="1" fold="1" page="1" pageScale="1" pageWidth="850" pageHeight="1100" math="0" shadow="0">
      <root>
        <mxCell id="0"/>
        <mxCell id="1" parent="0"/>i
        {cells}
        </root>
    </mxGraphModel>
  </diagram>
</mxfile>
'''
print(tmpl.format(cells="TEST"))

