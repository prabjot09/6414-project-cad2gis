## 6414 Project - CAD 2 GIS: Project Experiments and Source Code

**__Please use your own CAD files and Map images by replacing the file paths in the .ipynb notebooks with your own datasets. The datasets used in this project were proprietary material, however the visualized results can be found in the Jupiter Notebook outputs and in the project report.__**

The implementation of our automated CAD 2 GIS conversion is done through **4 key steps** represented by the following 4 folders:
- **Preproc** (Preprocessing): The steps applied to clean the CAD data to perform the necessary steps required to ensure it is convertable into a GIS model and some additional steps to make the process smoother.
- **Georef** (Georeferencing): The computer vision-based methods used to identify matching points between a CAD and GIS image to find coordinates known as `control points`. These points are then used to map points on a CAD image to real geographical coordinates to "geographically reference" the CAD model onto a map in GIS software.
- **FeatureExtract** (Feature Extraction): The methods used to convert the geospatial line/point data within GIS models to numerical features with labels that can be used as a training set for machine learning models.
- **ML** (Quality Control - Machine Learning): The machine learning techniques used to train models to predict conversion errors that occured after the CAD model has been successfully georeferenced to the correct geospatial coordinates in a GIS model. These models use the previously extracted features.

**Key Notes**:
- All files are `.ipynb` Jupiter Notebooks with the exception of the preprocessing which is in a single `.py` file.
- One additional file under the root for the end-2-end processing (note: it only detects error type 1). This code outputs a shapefile which can then be viewed on GIS software.

---------------------------------
The following subsections list more details about the provided folders.

### Georef:
- `EarlyGeorefExp1.ipynb` and `EarlyGeorefExp2.ipynb`: These are the earlier experiments for georeferencing that used methods that didn't initially succeed.
- `EarlyGeorefExp3.ipynb`: Contains further experiments that were finally able to successfully identify control points using the SIFT methods.
- `ControlPoints1.ipynb`: A clean file that is capable of finding the control points for the GTAA (Pearson Airport), the main dataset used for experimentations thus far.
- `ControlPoints2.ipynb`: A clean file for successfully finding control points for 3 additional datasets: OP, US Virgin Airport and Pendrys.
- `GeorefFinalSteps.ipynb`: A clean script to find matching points, derive key points as coordinates and use those to convert a CAD model into a GIS map.

### FeatureExtract:
- `Error1_Feature_Extraction.ipynb`: Generates features for ML training for Error Type 1 (Text being treated as lines, instead of annotations) 
- `Error2_Feature_Extraction.ipynb`: Generates features for ML training for Error Type 2 (Lines crossing over at intersections where they should have terminated)

### ML:
- Error Detection for Error Type 1:
  - **[BEST]** SupervisedType1.ipynb: Supervised Techniques to detect this error
  - UnsupervisedType1.ipynb: Unsupervised Techniques to detect this error
  - MoreType1ML.ipynb: Mix of additional supervised and unsupervised techniques attempted
- Error Detection for Error Type 2: 
  - Semi-supervisedType2.ipynb: Semi-Supervised Techniques to detect this error
  - **[BEST]** SupervisedType2.ipynb: Supervised Techniques to detect this error
  - UnsupervisedType2.ipynb: Unsupervised Techniques to detect this error
