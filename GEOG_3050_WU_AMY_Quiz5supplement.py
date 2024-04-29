import arcpy

print(arcpy.env.workspace)

folder = "C:/Users/amywu/OneDrive - University of Iowa/Documents/0_Geospatial Programming/Class Projects/02-19-2024_Project/chp9Data/"

arcpy.env.workspace=folder

print(arcpy.env.workspace)

fcList=arcpy.ListFeatureClasses()
print(fcList)

fcAirports = 'airports.shp'

fcFields = arcpy.ListFields(fcAirports)
for field in fcFields:
    print(field.name)

arcpy.management.AddField(fcAirports, "buffer", "LONG") 
fields = ['FEATURE', 'TOT_ENP', 'buffer']
print(fields)

with arcpy.da.UpdateCursor(fcAirports, fields) as cursor:
    # column [0] = FEATURE
    # column [1] = TOT_ENP
    # column [2] = buffer
    for row in cursor:
        if row[1] > 1000:  # TOT_ENP should be > 1000
            if row[0] == "Airport":
                if row[1] > 10000:  # for TOT_ENP > 10k,
                    row[2] = 15000  # buffer=15k
                else:
                    row[2] = 10000
            elif row[0] == "Seaplane Base":  # for TOT_ENP > 1k
                row[2] = 7500  # buffer=7.5k   
        cursor.updateRow(row)
print("done")

arcpy.CopyFeatures_management(fcAirports, folder + "buffer_airports.shp")
