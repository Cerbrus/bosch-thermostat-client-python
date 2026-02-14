from .ivt import IVTGateway, IVTMBLanGateway
from .oauth2 import Oauth2Gateway
from .nefit import NefitGateway
from .easycontrol import EasycontrolGateway
from bosch_thermostat_client.const.ivt import IVT, IVT_MBLAN
from bosch_thermostat_client.const import OAUTH2
from bosch_thermostat_client.const.nefit import NEFIT
from bosch_thermostat_client.const.oauth2 import BRUDERUS
from bosch_thermostat_client.const.easycontrol import EASYCONTROL


def gateway_chooser(device_type=IVT):
    return {
        IVT: IVTGateway,
        NEFIT: NefitGateway,
        EASYCONTROL: EasycontrolGateway,
        IVT_MBLAN: IVTMBLanGateway,
        OAUTH2: Oauth2Gateway,
        BRUDERUS: Oauth2Gateway,
    }[device_type]
