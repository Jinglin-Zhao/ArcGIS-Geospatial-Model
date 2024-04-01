import arcpy
arcpy.ImportToolbox(r"@\Data Management Tools.tbx")
arcpy.management.XYTableToPoint(
    in_table=r"C:\Users\Lenovo\Desktop\APD_Reported_Crimes_by_Neighborhood.xlsx\APD_Reported_Crimes_by_Neighbor$",
    out_feature_class=r"C:\Users\Lenovo\Documents\ArcGIS\Projects\Crime dataset Albany NY\Crime dataset Albany NY.gdb\Albany_crime",
    x_field="longitude",
    y_field="latitude",
    z_field=None,
    coordinate_system='GEOGCS["GCS_WGS_1984",DATUM["D_WGS_1984",SPHEROID["WGS_1984",6378137.0,298.257223563]],PRIMEM["Greenwich",0.0],UNIT["Degree",0.0174532925199433]];-400 -400 1000000000;-100000 10000;-100000 10000;8.98315284119521E-09;0.001;0.001;IsHighPrecision'
)
