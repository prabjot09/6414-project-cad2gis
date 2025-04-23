import arcpy
import os

def preprocess_cad(input_cad, output_gdb, output_fc_prefix="Processed_CAD"):
    """
    Preprocesses CAD data for ArcGIS Pro.
    
    Parameters:
    input_cad (str): Path to the input CAD dataset (.dwg or .dxf file).
    output_gdb (str): Path to the output geodatabase where the cleaned data will be stored.
    output_fc_prefix (str): Prefix for the output feature classes.
    """
    
    arcpy.env.workspace = output_gdb
    arcpy.env.overwriteOutput = True

    # Convert CAD to Geodatabase
    arcpy.conversion.CADToGeodatabase(input_cad, output_gdb, output_fc_prefix)
    
    # Define feature classes from CAD
    feature_classes = {
        "points": f"{output_fc_prefix}_POINT",
        "lines": f"{output_fc_prefix}_LINE",
        "polygons": f"{output_fc_prefix}_POLYGON",
        "annotations": f"{output_fc_prefix}_ANNOTATION",
        "multipatch": f"{output_fc_prefix}_MULTIPATCH"
    }
    
    # Remove unused layers and construction lines (by filtering unnecessary layers)
    for fc_type, fc in feature_classes.items():
        if arcpy.Exists(fc):
            with arcpy.da.UpdateCursor(fc, ["Layer"]) as cursor:
                for row in cursor:
                    layer_name = row[0].lower()
                    if "construction" in layer_name or "unused" in layer_name:
                        cursor.deleteRow()  # Remove unwanted layers
            print(f"Filtered unused layers and construction lines in {fc}")

    # Flatten 3D elements (convert Z values to 0)
    if arcpy.Exists(feature_classes["lines"]):
        flat_fc = f"{feature_classes['lines']}_Flat"
        arcpy.management.FeatureTo3DByAttribute(feature_classes["lines"], flat_fc, "Shape@XY", 0)
        print(f"Flattened 3D elements in {feature_classes['lines']}")

    # Explode Blocks and Groups
    if arcpy.Exists(feature_classes["lines"]):
        exploded_fc = f"{feature_classes['lines']}_Exploded"
        arcpy.management.MultipartToSinglepart(feature_classes["lines"], exploded_fc)
        print(f"Exploded blocks and groups in {feature_classes['lines']}")

    # Fix Annotations: Reposition & Convert CAD Text to GIS Annotation Layer
    if arcpy.Exists(feature_classes["annotations"]):
        annotation_fc = f"{feature_classes['annotations']}_Fixed"
        arcpy.management.FeatureToPoint(feature_classes["annotations"], annotation_fc, "INSIDE")
        print(f"Repositioned and fixed annotations in {feature_classes['annotations']}")

    print("CAD Preprocessing Completed Successfully!")

# Example Usage
input_cad_file = r"C:\CAD_Files\example.dwg"
output_geodatabase = r"C:\GIS_Projects\CAD_Preprocessed.gdb"
preprocess_cad(input_cad_file, output_geodatabase)


import arcpy
import os

def preprocess_cad(input_cad, output_gdb, output_fc_prefix="Processed_CAD"):
    """
    Preprocesses CAD data for ArcGIS Pro.
    
    Parameters:
    input_cad (str): Path to the input CAD dataset (.dwg or .dxf file).
    output_gdb (str): Path to the output geodatabase where the cleaned data will be stored.
    output_fc_prefix (str): Prefix for the output feature classes.
    """
    
    arcpy.env.workspace = output_gdb
    arcpy.env.overwriteOutput = True

    # Convert CAD to Geodatabase
    arcpy.conversion.CADToGeodatabase(input_cad, output_gdb, output_fc_prefix)
    
    # Define feature classes from CAD
    feature_classes = {
        "points": f"{output_fc_prefix}_POINT",
        "lines": f"{output_fc_prefix}_LINE",
        "polygons": f"{output_fc_prefix}_POLYGON",
        "annotations": f"{output_fc_prefix}_ANNOTATION",
        "multipatch": f"{output_fc_prefix}_MULTIPATCH"
    }
    
    # Remove unused layers and construction lines (by filtering unnecessary layers)
    for fc_type, fc in feature_classes.items():
        if arcpy.Exists(fc):
            with arcpy.da.UpdateCursor(fc, ["Layer"]) as cursor:
                for row in cursor:
                    layer_name = row[0].lower()
                    if "construction" in layer_name or "unused" in layer_name:
                        cursor.deleteRow()  # Remove unwanted layers
            print(f"Filtered unused layers and construction lines in {fc}")

    # Flatten 3D elements (convert Z values to 0)
    if arcpy.Exists(feature_classes["lines"]):
        flat_fc = f"{feature_classes['lines']}_Flat"
        arcpy.management.FeatureTo3DByAttribute(feature_classes["lines"], flat_fc, "Shape@XY", 0)
        print(f"Flattened 3D elements in {feature_classes['lines']}")

    # Explode Blocks and Groups
    if arcpy.Exists(feature_classes["lines"]):
        exploded_fc = f"{feature_classes['lines']}_Exploded"
        arcpy.management.MultipartToSinglepart(feature_classes["lines"], exploded_fc)
        print(f"Exploded blocks and groups in {feature_classes['lines']}")

    # Fix Annotations: Reposition & Convert CAD Text to GIS Annotation Layer
    if arcpy.Exists(feature_classes["annotations"]):
        annotation_fc = f"{feature_classes['annotations']}_Fixed"
        arcpy.management.FeatureToPoint(feature_classes["annotations"], annotation_fc, "INSIDE")
        print(f"Repositioned and fixed annotations in {feature_classes['annotations']}")

    print("CAD Preprocessing Completed Successfully!")

# Example Usage
input_cad_file = r"C:\Users\porthern\Downloads\GTAA2.dwg"
output_geodatabase = r"C:\Users\porthern\AppData\Local\Temp\ArcGISProTemp2440\Untitled\Default.gdb"
preprocess_cad(input_cad_file, output_geodatabase)


import arcpy
import os

def preprocess_cad(input_cad, output_gdb, output_fc_prefix="Processed_CAD"):
    """
    Preprocesses CAD data for ArcGIS Pro.
    
    Parameters:
    input_cad (str): Path to the input CAD dataset (.dwg or .dxf file).
    output_gdb (str): Path to the output geodatabase where the cleaned data will be stored.
    output_fc_prefix (str): Prefix for the output feature classes.
    """
    
    arcpy.env.workspace = output_gdb
    arcpy.env.overwriteOutput = True

    # Convert CAD to Geodatabase
    arcpy.conversion.CADToGeodatabase(input_cad, output_gdb, output_fc_prefix)
    
    # Define feature classes from CAD
    feature_classes = {
        "points": f"{output_fc_prefix}_POINT",
        "lines": f"{output_fc_prefix}_LINE",
        "polygons": f"{output_fc_prefix}_POLYGON",
        "annotations": f"{output_fc_prefix}_ANNOTATION",
        "multipatch": f"{output_fc_prefix}_MULTIPATCH"
    }
    
    # Remove unused layers and construction lines (by filtering unnecessary layers)
    for fc_type, fc in feature_classes.items():
        if arcpy.Exists(fc):
            with arcpy.da.UpdateCursor(fc, ["Layer"]) as cursor:
                for row in cursor:
                    layer_name = row[0].lower()
                    if "construction" in layer_name or "unused" in layer_name:
                        cursor.deleteRow()  # Remove unwanted layers
            print(f"Filtered unused layers and construction lines in {fc}")

    # Flatten 3D elements (convert Z values to 0)
    if arcpy.Exists(feature_classes["lines"]):
        flat_fc = f"{feature_classes['lines']}_Flat"
        arcpy.management.FeatureTo3DByAttribute(feature_classes["lines"], flat_fc, "Shape@XY", 0)
        print(f"Flattened 3D elements in {feature_classes['lines']}")

    # Explode Blocks and Groups
    if arcpy.Exists(feature_classes["lines"]):
        exploded_fc = f"{feature_classes['lines']}_Exploded"
        arcpy.management.MultipartToSinglepart(feature_classes["lines"], exploded_fc)
        print(f"Exploded blocks and groups in {feature_classes['lines']}")

    # Fix Annotations: Reposition & Convert CAD Text to GIS Annotation Layer
    if arcpy.Exists(feature_classes["annotations"]):
        annotation_fc = f"{feature_classes['annotations']}_Fixed"
        arcpy.management.FeatureToPoint(feature_classes["annotations"], annotation_fc, "INSIDE")
        print(f"Repositioned and fixed annotations in {feature_classes['annotations']}")

    print("CAD Preprocessing Completed Successfully!")

# Example Usage
input_cad_file = r"C:\Users\porthern\Downloads\GTAA 2.dwg"
output_geodatabase = r"C:\Users\porthern\AppData\Local\Temp\ArcGISProTemp2440\Untitled\Default.gdb"
preprocess_cad(input_cad_file, output_geodatabase)


import arcpy
import os

def preprocess_cad(input_cad, output_gdb, output_fc_prefix="Processed_CAD"):
    """
    Preprocesses CAD data for ArcGIS Pro.
    
    Parameters:
    input_cad (str): Path to the input CAD dataset (.dwg or .dxf file).
    output_gdb (str): Path to the output geodatabase where the cleaned data will be stored.
    output_fc_prefix (str): Prefix for the output feature classes.
    """
    
    arcpy.env.workspace = output_gdb
    arcpy.env.overwriteOutput = True

    # Convert CAD to Geodatabase
    arcpy.conversion.CADToGeodatabase(input_cad, output_gdb, output_fc_prefix)
    
    # Define feature classes from CAD
    feature_classes = {
        "points": f"{output_fc_prefix}_POINT",
        "lines": f"{output_fc_prefix}_LINE",
        "polygons": f"{output_fc_prefix}_POLYGON",
        "annotations": f"{output_fc_prefix}_ANNOTATION",
        "multipatch": f"{output_fc_prefix}_MULTIPATCH"
    }
    
    # Remove unused layers and construction lines (by filtering unnecessary layers)
    for fc_type, fc in feature_classes.items():
        if arcpy.Exists(fc):
            with arcpy.da.UpdateCursor(fc, ["Layer"]) as cursor:
                for row in cursor:
                    layer_name = row[0].lower()
                    if "construction" in layer_name or "unused" in layer_name:
                        cursor.deleteRow()  # Remove unwanted layers
            print(f"Filtered unused layers and construction lines in {fc}")

    # Flatten 3D elements (convert Z values to 0)
    if arcpy.Exists(feature_classes["lines"]):
        flat_fc = f"{feature_classes['lines']}_Flat"
        arcpy.management.FeatureTo3DByAttribute(feature_classes["lines"], flat_fc, "Shape@XY", 0)
        print(f"Flattened 3D elements in {feature_classes['lines']}")

    # Explode Blocks and Groups
    if arcpy.Exists(feature_classes["lines"]):
        exploded_fc = f"{feature_classes['lines']}_Exploded"
        arcpy.management.MultipartToSinglepart(feature_classes["lines"], exploded_fc)
        print(f"Exploded blocks and groups in {feature_classes['lines']}")

    # Fix Annotations: Reposition & Convert CAD Text to GIS Annotation Layer
    if arcpy.Exists(feature_classes["annotations"]):
        annotation_fc = f"{feature_classes['annotations']}_Fixed"
        arcpy.management.FeatureToPoint(feature_classes["annotations"], annotation_fc, "INSIDE")
        print(f"Repositioned and fixed annotations in {feature_classes['annotations']}")

    print("CAD Preprocessing Completed Successfully!")

# Example Usage
input_cad_file = r"C:\Users\porthern\Downloads\GTAA 2.dwg"
output_geodatabase = r"C:\Users\porthern\AppData\Local\Temp\ArcGISProTemp2440\Untitled\Default.gdb"
preprocess_cad(input_cad_file, output_geodatabase)


import arcpy
import os

def preprocess_cad(input_cad, output_gdb, output_fc_prefix="Processed_CAD"):
    """
    Preprocesses CAD data for ArcGIS Pro.
    
    Parameters:
    input_cad (str): Path to the input CAD dataset (.dwg or .dxf file).
    output_gdb (str): Path to the output geodatabase where the cleaned data will be stored.
    output_fc_prefix (str): Prefix for the output feature classes.
    """
    
    arcpy.env.workspace = output_gdb
    arcpy.env.overwriteOutput = True

 # Set a reference scale (e.g., 1000)
    reference_scale = 1000
    
    # Convert CAD to Geodatabase
    arcpy.conversion.CADToGeodatabase(input_cad, output_gdb, output_fc_prefix, reference_scale)
    
    # Define feature classes from CAD
    feature_classes = {
        "points": f"{output_fc_prefix}_POINT",
        "lines": f"{output_fc_prefix}_LINE",
        "polygons": f"{output_fc_prefix}_POLYGON",
        "annotations": f"{output_fc_prefix}_ANNOTATION",
        "multipatch": f"{output_fc_prefix}_MULTIPATCH"
    }
    
    # Remove unused layers and construction lines (by filtering unnecessary layers)
    for fc_type, fc in feature_classes.items():
        if arcpy.Exists(fc):
            with arcpy.da.UpdateCursor(fc, ["Layer"]) as cursor:
                for row in cursor:
                    layer_name = row[0].lower()
                    if "construction" in layer_name or "unused" in layer_name:
                        cursor.deleteRow()  # Remove unwanted layers
            print(f"Filtered unused layers and construction lines in {fc}")

    # Flatten 3D elements (convert Z values to 0)
    if arcpy.Exists(feature_classes["lines"]):
        flat_fc = f"{feature_classes['lines']}_Flat"
        arcpy.management.FeatureTo3DByAttribute(feature_classes["lines"], flat_fc, "Shape@XY", 0)
        print(f"Flattened 3D elements in {feature_classes['lines']}")

    # Explode Blocks and Groups
    if arcpy.Exists(feature_classes["lines"]):
        exploded_fc = f"{feature_classes['lines']}_Exploded"
        arcpy.management.MultipartToSinglepart(feature_classes["lines"], exploded_fc)
        print(f"Exploded blocks and groups in {feature_classes['lines']}")

    # Fix Annotations: Reposition & Convert CAD Text to GIS Annotation Layer
    if arcpy.Exists(feature_classes["annotations"]):
        annotation_fc = f"{feature_classes['annotations']}_Fixed"
        arcpy.management.FeatureToPoint(feature_classes["annotations"], annotation_fc, "INSIDE")
        print(f"Repositioned and fixed annotations in {feature_classes['annotations']}")

    print("CAD Preprocessing Completed Successfully!")

# Example Usage
input_cad_file = r"C:\Users\porthern\Downloads\GTAA 2.dwg"
output_geodatabase = r"C:\Users\porthern\AppData\Local\Temp\ArcGISProTemp2440\Untitled\Default.gdb"
preprocess_cad(input_cad_file, output_geodatabase)



