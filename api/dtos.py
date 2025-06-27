class ImageDTO:
    def __init__(self, predicted_class, confidence):
        self.predicted_class = predicted_class
        self.confidence = confidence

    def __str__(self):
        return f"{self.predicted_class} ({self.confidence:.2f})"
