# OAVelocity	Peakmg	RMSmg	Kurtosis	CrestFactor	Skewness	Deviation	Peak-to-Peak Displacement	Time
# 247	1295	916	22	1167	-5	289	23	2023-02-16 2:31:19


class WiseModel:
    def __init__(
        OAVelocity,
        Peakmg,
        RMSmg,
        Kurtosis,
        CrestFactor,
        Skewness,
        Deviation,
        PeaktoPeakDisplacement,
        Time,
    ):
        self.OAVelocity = OAVelocity
        self.Peakmg = Peakmg
        self.RMSmg = RMSmg
        self.Kurtosis = Kurtosis
        self.CrestFactor = CrestFactor
        self.Skewness = Skewness
        self.Deviation = Deviation
        self.PeaktoPeakDisplacement = PeaktoPeakDisplacement
        self.Time = Time

    def __repr__(self):
        return f"WiseModel(OAVelocity={self.OAVelocity}, Peakmg={self.Peakmg}, RMSmg={self.RMSmg}, Kurtosis={self.Kurtosis}, CrestFactor={self.CrestFactor}, Skewness={self.Skewness}, Deviation={self.Deviation}, PeaktoPeakDisplacement={self.PeaktoPeakDisplacement}, Time={self.Time})"

    def __str__(self):
        return f"WiseModel(OAVelocity={self.OAVelocity}, Peakmg={self.Peakmg}, RMSmg={self.RMSmg}, Kurtosis={self.Kurtosis}, CrestFactor={self.CrestFactor}, Skewness={self.Skewness}, Deviation={self.Deviation}, PeaktoPeakDisplacement={self.PeaktoPeakDisplacement}, Time={self.Time})"
