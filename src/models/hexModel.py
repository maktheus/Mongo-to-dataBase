# InletPressure	OutletPressure	OutletTemperature	InverterSpeed	Time
# 16.930.580.139.160.100	10.111.397.705.078.100	8.330.850.219.726.560	4552.0	2023-02-16 02:29:31
class hexModel:
    def __init__(InletPressure, OutletPressure, OutletTemperature, InverterSpeed, Time):
        self.InletPressure = InletPressure
        self.OutletPressure = OutletPressure
        self.OutletTemperature = OutletTemperature
        self.InverterSpeed = InverterSpeed
        self.Time = Time

    def __repr__(self):
        return f"hexModel(InletPressure={self.InletPressure}, OutletPressure={self.OutletPressure}, OutletTemperature={self.OutletTemperature}, InverterSpeed={self.InverterSpeed}, Time={self.Time})"

    def __str__(self):
        return f"hexModel(InletPressure={self.InletPressure}, OutletPressure={self.OutletPressure}, OutletTemperature={self.OutletTemperature}, InverterSpeed={self.InverterSpeed}, Time={self.Time})"
