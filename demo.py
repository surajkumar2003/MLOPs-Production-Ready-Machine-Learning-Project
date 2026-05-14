import numpy as np

np.float_ = np.float64
np.int_ = np.int64
np.complex_ = np.complex128

from us_visa.pipeline.training_pipeline import TrainingPipeline

obj = TrainingPipeline()
obj.run_pipeline()