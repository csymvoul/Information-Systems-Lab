import time

class Monitoring():
    def __init__(self,application,replicas):
        self.application = application
        self.replicas = replicas
        self.metrics = {}
        self.metrics['start_time'] = time.time()
    def setMetric(self,name,value):
        self.metrics[name] = value
    def increment(self,name):
        if not name in self.metrics:
            self.metrics[name] = 1
        else:
            self.metrics[name] +=1
    def add(self,name,amount):
        if not name in self.metrics:
            self.metrics[name] = amount
        else:
            self.metrics[name] +=amount
        self.metrics['throughout_'+name] = int(float(self.metrics[name])/(time.time() - self.metrics['start_time']))
    def getMetrics(self):
        return self.metrics
    def getIdentity(self):
        return self.application, self.replicas
