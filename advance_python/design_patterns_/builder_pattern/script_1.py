"""
FACTORY DESIGN PATTERN METHOD
The new computer analogy might help to distinguish between a Builder pattern and
a Factory pattern. Assume that you want to buy a new computer. If you decide to
buy a specific preconfigured computer model, for example, the latest Apple 1.4 GHz
Mac mini, you use the Factory pattern. All the hardware specifications are already
predefined by the manufacturer, who knows what to do without consulting you. The
manufacturer typically receives just a single instruction. Code-wise, this would look
like the following
"""

MINI14 = '1.4GHz Mac Mini'

class AppleFactory:

    class MacMini14:
        def __init__(self) -> None:
            self.memory = 4   # in GB
            self.hdd    = 500 # in GB
            self.gpu    = "Intel HD Graphics 5000"

        def __str__(self) -> str:
            info = (f'Model: {MINI14}',
                    f'Memory: {self.memory}GB',
                    f'HDD: {self.hdd}GB',
                    f'Graphics Card: {self.gpu}')
            return '\n'.join(info)

    def build_computer(self, model):
        if (model == 'MINI14'):
            return self.MacMini14()
        else:
            print(f"I don't know how to build - {model}")

afac = AppleFactory()
mac_mini = afac.build_computer('MINI14')
print(mac_mini)
print('\n\n')

"""
BUILDER DESIGN PATTERN METHOD
Another option is buying custom PC. In this case, you use the builder pattern. You are
the director that gives order to manufacturer (builder) about your ideal computer specification.
"""

class Computer:
    def __init__(self, serial_number) -> None:
        self.serial = serial_number
        self.memory = None # in GB
        self.hdd    = None # in GB
        self.gpu    = None

    def __str__(self) -> str:
        info = (f'Memory: {self.memory}GB',
                f'HDD: {self.hdd}GB',
                f'Graphics Card: {self.gpu}')
        return '\n'.join(info)

class ComputerBuilder:
    def __init__(self) -> None:
        self.computer = Computer('AG23385193')

    def configure_memory(self, amount):
        self.computer.memory = amount

    def configure_hdd(self, amount):
        self.computer.hdd = amount

    def configure_gpu(self, gpu_model):
        self.computer.gpu = gpu_model

class HardwareEngineer:
    def __init__(self) -> None:
        self.builder = None

    def construct_computer(self, memory, hdd, gpu):
        self.builder = ComputerBuilder()
        [step for step in (self.builder.configure_memory(memory),
                           self.builder.configure_hdd(hdd),
                           self.builder.configure_gpu(gpu))]

    @property
    def computer(self):
        return self.builder.computer

engineer = HardwareEngineer()
engineer.construct_computer(hdd=500, memory=8, gpu='GeForce GTX 3080Ti')
computer = engineer.computer
print(computer)
