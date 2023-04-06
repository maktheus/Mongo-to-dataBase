class IteModel:
    def __init__(
        temperature,
        frequency,
        phaseA_voltage,
        phaseA_current,
        phaseA_pwr_factor,
        phaseA_active,
        phaseA_reactive,
        phaseA_tc_config,
        phaseB_voltage,
        phaseB_current,
        phaseB_pwr_factor,
        phaseB_active,
        phaseB_reactive,
        phaseB_tc_config,
        phaseC_voltage,
        phaseC_current,
        phaseC_pwr_factor,
        phaseC_active,
        phaseC_reactive,
        phaseC_tc_config,
        time,
    ):
        self.temperature = temperature
        self.frequency = frequency
        self.phaseA_voltage = phaseA_voltage
        self.phaseA_current = phaseA_current
        self.phaseA_pwr_factor = phaseA_pwr_factor
        self.phaseA_active = phaseA_active
        self.phaseA_reactive = phaseA_reactive
        self.phaseA_tc_config = phaseA_tc_config
        self.phaseB_voltage = phaseB_voltage
        self.phaseB_current = phaseB_current
        self.phaseB_pwr_factor = phaseB_pwr_factor
        self.phaseB_active = phaseB_active
        self.phaseB_reactive = phaseB_reactive
        self.phaseB_tc_config = phaseB_tc_config
        self.phaseC_voltage = phaseC_voltage
        self.phaseC_current = phaseC_current
        self.phaseC_pwr_factor = phaseC_pwr_factor
        self.phaseC_active = phaseC_active
        self.phaseC_reactive = phaseC_reactive
        self.phaseC_tc_config = phaseC_tc_config
        self.time = time

    def __repr__(self):
        return f"iteModel(temperature={self.temperature}, frequency={self.frequency}, phaseA_voltage={self.phaseA_voltage}, phaseA_current={self.phaseA_current}, phaseA_pwr_factor={self.phaseA_pwr_factor}, phaseA_active={self.phaseA_active}, phaseA_reactive={self.phaseA_reactive}, phaseA_tc_config={self.phaseA_tc_config}, phaseB_voltage={self.phaseB_voltage}, phaseB_current={self.phaseB_current}, phaseB_pwr_factor={self.phaseB_pwr_factor}, phaseB_active={self.phaseB_active}, phaseB_reactive={self.phaseB_reactive}, phaseB_tc_config={self.phaseB_tc_config}, phaseC_voltage={self.phaseC_voltage}, phaseC_current={self.phaseC_current}, phaseC_pwr_factor={self.phaseC_pwr_factor}, phaseC_active={self.phaseC_active}, phaseC_reactive={self.phaseC_reactive}, phaseC_tc_config={self.phaseC_tc_config}, time={self.time})"

    def __str__(self):
        return f"iteModel(temperature={self.temperature}, frequency={self.frequency}, phaseA_voltage={self.phaseA_voltage}, phaseA_current={self.phaseA_current}, phaseA_pwr_factor={self.phaseA_pwr_factor}, phaseA_active={self.phaseA_active}, phaseA_reactive={self.phaseA_reactive}, phaseA_tc_config={self.phaseA_tc_config}, phaseB_voltage={self.phaseB_voltage}, phaseB_current={self.phaseB_current}, phaseB_pwr_factor={self.phaseB_pwr_factor}, phaseB_active={self.phaseB_active}, phaseB_reactive={self.phaseB_reactive}, phaseB_tc_config={self.phaseB_tc_config}, phaseC_voltage={self.phaseC_voltage}, phaseC_current={self.phaseC_current}, phaseC_pwr_factor={self.phaseC_pwr_factor}, phaseC_active={self.phaseC_active}, phaseC_reactive={self.phaseC_reactive}, phaseC_tc_config={self.phaseC_tc_config}, time={self.time})"