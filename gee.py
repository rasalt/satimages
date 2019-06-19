## Reference: https://stackoverflow.com/questions/39219705/how-to-download-images-using-google-earth-engines-python-api
## Reference: https://developers.google.com/earth-engine/exporting
import ee
ee.Initialize()
landsat = ee.Image('LANDSAT/LC08/C01/T1_TOA/LC08_123032_20140515')

c1 = [84.28586591,    27.42846051] 
c2 = [84.28724124,    27.42850423] 
c3 = [84.28578211,    27.42716335]
c4 = [84.28731738,    27.42719899]

geometry = [c1, c2, c3, c4]
task_config = {
#  'description': 'imageToDriveExample',
  'image': 'landsat',
  'description': 'imagetogcs',
  'bucket': 'gee-ex',
  'filenamePrefix': 'exampleExp',
  'scale': 30,  
  'region': geometry
  }

task = ee.batch.Export.image.toCloudStorage(landsat, 'exportExample', task_config)
#task = ee.batch.Export.image.toCloudStorage(task_config)
task.start()

