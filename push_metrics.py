from prometheus_client import CollectorRegistry, Gauge, push_to_gateway

registry = CollectorRegistry()
g = Gauge('model_accuracy', 'Model Accuracy', registry=registry)
g.set(0.89)  # Example value

push_to_gateway('localhost:9091', job='mlops-housing-training', registry=registry)

