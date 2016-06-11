import requests
import csv

legend_data = {}
with open("legend_data4.csv") as fp:
    reader = csv.reader(fp)
    for line in reader:
        legend_data[line[1]] = line[0]
# print legend_data



# requests.packages.urllib3.disable_warnings()

view_name = "bioimplendt"
title = "Impaired:  Biota"
style = "wms_water_bioimplen"


def create_layer(name, title, style):
    auth = ("admin", "geoserver")
    headers = {'Content-type': 'text/xml'}
    data = "<featureType><name>%s</name><title>%s</title></featureType>" % (view_name, title)

    url = "http://localhost/geoserver/rest/workspaces/wms/datastores/db/featuretypes"
    requests.post(url, data=data, headers=headers, auth=auth)

    url = "http://localhost/geoserver/rest/layers/wms:%s" % view_name
    data = "<layer><defaultStyle><name>%s</name><workspace>wms</workspace></defaultStyle></layer>" % style
    requests.put(url, data=data, headers=headers, auth=auth)

create_layer(view_name, title, style)

mymaps = ["frst", 'ftwt', 'hbwt', 'open', 'shrb']
years = [10, 20, 30, 40, 50]
scenarios = ['x', "a", "b", "c", "d", "e"]

for mymap in mymaps:
    for year in years:
        for scenario in scenarios:
            view_name = "%s%sdt_%s" % (mymap, year, scenario)
            title = legend_data[mymap] + " Loss Since 2000 (pct) 20%s" % year
            title = title.replace("pct", "%")
            style = "wms_%s" % mymap

            # print view_name
            # print title
            # print style
            # create_layer(view_name, title, style)

for year in years:
    view_name = "urb%sdt" % year
    title = "Urban Land Cover (%)"
    style = "wms_%s" % "urban"
    print view_name
    print title
    print style
    create_layer(view_name, title, style)

for year in years:
    view_name = "fsupp%sdt" % year
    title = "Mean Urban Density w/in 500 mile radius"
    style = "wms_%s" % "fire"
    print view_name
    print title
    print style
    create_layer(view_name, title, style)

for year in years:
    view_name = "rds%sdt" % year
    title = "Mean Length/Area of Major Highways (m/ha)"
    style = "wms_%s" % "trans"
    print view_name
    print title
    print style
    create_layer(view_name, title, style)

view_name = "manudt"
title = "Manure Application (kg/ha/yr)"
style = "wms_%s" % "nutrient_manu"
print view_name
print title
print style
create_layer(view_name, title, style)
