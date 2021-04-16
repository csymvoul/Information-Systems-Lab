import time
import random
from prometheus_client import Metric

class Collector(object):
    def __init__(self,service, metrics=dict):
        self._service = service
        self._labels = {}
        self._set_labels()
        self._metrics = metrics

    def _set_labels(self):
        self._labels.update({'application': self._service[0],'replicas': self._service[1]})

    def _get_metrics(self):
        #time.sleep(random.uniform(0.1, 0.4))
        #return metrics
        return self._metrics

    def collect(self):
        metrics = self._get_metrics()

        if metrics:
            for k, v in metrics.items():
                metric = Metric(k, k, 'gauge')
                labels = {}
                labels.update(self._labels)
                metric.add_sample(k, value=v, labels=labels)

                if metric.samples:
                    yield metric
                else:
                    pass
