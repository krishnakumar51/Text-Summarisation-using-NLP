from textSummarizer.config.configuration import ConfigurationManager
from textSummarizer.coponents.model_evalutaion import ModelEvaluation
from textSummarizer.logging import logger


class ModelEvaluationPipeline:
    def __init__(self):
        pass

    def main(self):
        config = ConfigurationManager()
        model_evaluation_config = config.get_model_evaluation_config()
        model_evaluation = ModelEvaluation(config=model_evaluation_config)
        model_evaluation.evaluate()