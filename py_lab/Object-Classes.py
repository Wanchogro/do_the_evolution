class Router2:
    '''Router Class Formatted'''
    def __init__(self, model, osversion, ip_addr):
       '''initialize values'''
       self.model = model
       self.osversion = osversion
       self.ip_addr = ip_addr

    def getdesc(self):
        '''return a formatted description of the router'''
        desc = f'Router Model        :{self.model}\n'\
               f'Software Version    :{self.osversion}\n'\
               f'Management Address  :{self.ip_addr}\n'
        return desc

class Switch(Router2):
    def getdesc(self)
    '''return a formatted description of the Switch'''
        desc = f'Switch Model :{self.model}\n'
               f'Software Version :{self.swversion}\n'
               f'Switch Management Address:{self.ip_add}'
        return desc

rtra = Router2('iosV', '15.6.7', '10.10.10.1')
rtrb = Router2('isr4221', '16.9.5', '10.10.10.5')
swa = Switch('Cat9300', '16.9.5', '10.10.10.8')

print('Rtr1\n', rtra.getdesc(), '\n', sep='')
print('Rtr2\n', rtrb.getdesc(), '\n', sep='')
print('Sw1\n', swa.getdesc(), '\n', sep='')
