import arcpy
import os

gdb_path = r"D:\Second Year\Sem 3\Programming_for_GIS_III\Assignments\Assignment_6_Working_with_Cursors_2\Practical_5_6_ProProject\05_06_Working_with_Cursors.gdb"
fc_name ="MajorAttractions"

fc_path = os.path.join(gdb_path, fc_name)

fields_list = ["NAME", "ESTAB", "HISTORIC"]

with arcpy.da.UpdateCursor(fc_path, fields_list) as u_cursor:
    for row in u_cursor:
        establishment_year = row[1]

        if establishment_year < 1960:
            row[2] = "YES"
        else:
            row[2] = "NO"

        u_cursor.updateRow(row)

print("Process Completed")










