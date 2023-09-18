from Config.Config import Config
from CFL.CFL import CFL

config = Config()
cfl = CFL(cflPage=config.getCFLPage(), emailTest=config.getEmailTest(), passwordTest=config.getPasswordTest())

cfl.run()