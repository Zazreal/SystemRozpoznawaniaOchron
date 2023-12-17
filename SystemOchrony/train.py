from imageai.Classification.Custom import ClassificationModelTrainer
import os

execution_path = os.getcwd()
print(execution_path)
model_trainer = ClassificationModelTrainer()
model_trainer.setModelTypeAsDenseNet121()
model_trainer.setDataDirectory(os.path.join(execution_path,"SHOES"))
model_trainer.trainModel(num_objects=2, num_experiments=50, enhance_data=True, batch_size=16, show_network_summary=True,save_full_model=True) 