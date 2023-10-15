import arcpy
import os

gdb_path = r"D:\Second Year\Sem 3\Programming_for_GIS_III\Assignments\Assignment_6_Working_with_Cursors_2\Practical_5_6_ProProject\05_06_Working_with_Cursors.gdb"
fc_name ="MajorAttractions"

fc_path = os.path.join(gdb_path, fc_name)

fields_list = ["NAME", "ESTAB", "ADDR", "CITYNM", "ZIP", "EMP", "ACRES"]

record = ("New Town Restaurant", 2021, "841 STREET","SAN DIEGO", 92101, 150, 10)

i_cursor = arcpy.da.InsertCursor(fc_path, fields_list)

i_cursor.insertRow(record)

print("Process Completed")