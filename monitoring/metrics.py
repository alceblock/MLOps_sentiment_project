from prometheus_client import Counter, Histogram, Gauge

# model's PERFORMANCE
MODEL_ACCURACY = Gauge(
    "model_accuracy",
    "Accuracy of the model (real-time)"
)
MODEL_F1 = Gauge(
    "model_f1",
    "F1 score of the model (real-time)"
)
MODEL_PRECISION = Gauge(
    "model_precision",
    "Precision of the model (real-time)"
)
MODEL_RECALL = Gauge(
    "model_recall",
    "Recall of the model (real-time)"
)

# GENERAL metrics
CORRECT_PREDICTIONS = Counter(
    "model_correct_predictions_total",
    "Correct predictions"
)
TOTAL_LABELED = Counter(
    "model_labeled_samples_total",
    "Total labeled samples"
)

# model's SENTIMENT
SENTIMENT_COUNT = Counter(
    "sentiment_predictions_total",
    "Number of predictions per sentiment",
    ["label"]
)


# Useful metrics
PREDICTION_CONFIDENCE = Histogram(
    "prediction_confidence",
    "Prediction confidence distribution"
)

INPUT_TEXT_LENGTH = Histogram(
    "input_text_length",
    "Length of input text"
)

# Request metrics
REQUEST_COUNT = Counter(
    "http_requests_total",
    "Total HTTP requests",
    ["endpoint", "method"]
)

REQUEST_LATENCY = Histogram(
    "http_request_latency_seconds",
    "HTTP request latency",
    ["endpoint"]
)


########
# from prometheus_client import Counter, Histogram
# #from prometheus_client import Gauge

# # # model's PERFORMANCE
# # MODEL_ACCURACY = Gauge("model_accuracy", "Accuracy of the model")
# # MODEL_F1 = Gauge("model_f1", "F1 score of the model")
# # MODEL_PRECISION = Gauge("model_precision", "Precision of the model")
# # MODEL_RECALL = Gauge("model_recall", "Recall of the model")

# # model's SENTIMENT
# REQUEST_COUNT = Counter(
#     "sentiment_requests_total",
#     "Total requests"
# )

# REQUEST_LATENCY = Histogram(
#     "sentiment_request_latency_seconds",
#     "Latency"
# )

# POSITIVE_COUNT = Counter("sentiment_positive", "positive tweets")
# NEGATIVE_COUNT = Counter("sentiment_negative", "negative tweets")
# NEUTRAL_COUNT = Counter("sentiment_neutral", "neutral tweets")