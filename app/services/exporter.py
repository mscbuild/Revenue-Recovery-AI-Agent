import pandas as pd

class Exporter:
    def to_csv(self, alerts, filename="outputs/submissions.csv"):
        df = pd.DataFrame(alerts)
        df.to_csv(filename, index=False)
        return filename
