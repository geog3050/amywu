import arcpy

folder = "C:/Users/amywu/OneDrive - University of Iowa/Documents/0_Geospatial Programming/Class Projects/03-30-2024_quiz6Proj"

arcpy.env.workspace=folder

def calculatePercentAreaOfPolygonAInPolygonB(input_geodatabase, fcPolygonA, fcPolygonB, idFieldPolygonB=None):
    arcpy.AddField_management(fcPolygonB, "pctAinB", "DOUBLE")
    fields = ["SHAPE@", "SHAPE@AREA", "pctAinB"]
    intersection = arcpy.Intersect_analysis([fcpolygonA, fcPolygonB, "intersect", "ALL", "", "INPUT"])
    
    if idFieldPolygonB is not None:
        fields.append(idFieldPolygonB) # add idfield if provided
    with arcpy.da.SearchCursor(intersection, fields) as cursor:
        for row in cursor:
            polygonB_area= row[0].area 
            intersect_area= row[1]
            pctAinB = (intersection / polygonB_area) 
            row[0].setValue("pctAinB", pctAinB)
            cursor.updateRow(row)

# Example usage:
input_geodatabase = r"C:/Users/amywu/OneDrive - University of Iowa/Documents/0_Geospatial Programming/Class Projects/03-30-2024_quiz6Proj/quiz6.gdb"
fcPolygonA = "parks"
fcPolygonB = "block_groups"
# idFieldPolygonB = "OBJECTID"

calculatePercentAreaOfPolygonAInPolygonB(input_geodatabase, fcPolygonA, fcPolygonB)
