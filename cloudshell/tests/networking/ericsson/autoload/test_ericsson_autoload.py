from unittest import TestCase
import threading
from cloudshell.networking.ericsson.ipos.ericsson_ipos_resource_driver import EricssonIPOSResourceDriver
from cloudshell.networking.cisco.autoload.cisco_generic_snmp_autoload import CiscoGenericSNMPAutoload
from cloudshell.core.logger.qs_logger import get_qs_logger
from cloudshell.networking.ericsson.seos.ericsson_seos_resource_driver import EricssonSEOSResourceDriver
from cloudshell.shell.core.context import ResourceCommandContext, ReservationContextDetails, ResourceContextDetails
from cloudshell.snmp.quali_snmp import QualiSnmp


class TestEricssonAutoload(TestCase):
    SUPPORTED_OS = ['NXOS', 'NX-OS', 'IOS', 'Cat OS', 'IOS XR', 'IOSXR', 'IOS-XR']

    def _check_relative_path(self, resources):
        relative_path = []
        for resource in resources:
            if resource.relative_address in relative_path:
                return False
            else:
                relative_path.append(resource.relative_address)
        return True

    def test_is_loads_SSR8004_correctly(self):
        print '-----------SSR80020------------'
        context = ResourceCommandContext()
        context.resource = ResourceContextDetails()
        context.resource.name = 'SSR8020'
        context.reservation = ReservationContextDetails()
        context.reservation.reservation_id = 'test_SSR8020_reservation_id'
        context.resource.attributes = {}
        context.resource.attributes['User'] = 'test'
        context.resource.attributes['Password'] = 'test'
        context.resource.attributes['Enable Password'] = 'test'
        context.resource.attributes['CLI Connection Type'] = 'Telnet'
        context.resource.attributes['SNMP Read Community'] = 'test'
        context.resource.attributes['SNMP Version'] = '2'
        context.resource.address = '10.126.75.215'
        result = EricssonIPOSResourceDriver().get_inventory(context)
        self.assertIsNotNone(result)
        self.assertIsNotNone(result.resources)
        self.assertIsNotNone(result.attributes)
        chassis = [resource for resource in result.resources if 'Chassis' in resource.name]
        modules = [resource for resource in result.resources if resource.model == 'Generic Module']
        ports = [resource for resource in result.resources if resource.model == 'Generic Port']
        port_channels = [resource for resource in result.resources if resource.model == 'Generic Port Channel']
        power_ports = [resource for resource in result.resources if resource.model == 'Generic Power Port']
        sub_modules = [resource for resource in result.resources if 'Sub Module' in resource.name]
        trash_chrs = [attribute for attribute in result.attributes if type(attribute.attribute_value) is str and
                      '\\s' in attribute.attribute_value]
        if len(trash_chrs) > 0:
            for char in trash_chrs:
                print char.relative_address + ': ' + char.attribute_name + ' = ' + char.attribute_value
        self.assertTrue(len(chassis) == 1)
        self.assertTrue(len(ports) == 62)
        self.assertTrue(len(modules) == 2)
        self.assertTrue(len(sub_modules) == 0)
        self.assertTrue(len(port_channels) == 0)
        self.assertTrue(len(power_ports) == 4)
        self.assertFalse(len(trash_chrs) > 0)
        self.assertTrue(self._check_relative_path(result.resources))
        print len(chassis)
        print len(ports)
        print len(modules)
        print len(sub_modules)
        print len(port_channels)
        print str(len(power_ports)) + '\n'

    def test_is_loads_SSRsim1_correctly(self):
        print '-----------SSRsim1------------'
        context = ResourceCommandContext()
        context.resource = ResourceContextDetails()
        context.resource.name = 'SSRsim1'
        context.reservation = ReservationContextDetails()
        context.reservation.reservation_id = 'test_SSRsim1_reservation_id'
        context.resource.attributes = {}
        context.resource.attributes['User'] = 'test'
        context.resource.attributes['Password'] = 'test'
        context.resource.attributes['Enable Password'] = 'test'
        context.resource.attributes['CLI Connection Type'] = 'Telnet'
        context.resource.attributes['SNMP Read Community'] = 'test'
        context.resource.attributes['SNMP Version'] = '2'
        context.resource.address = '10.126.144.213'
        result = EricssonIPOSResourceDriver().get_inventory(context)
        self.assertIsNotNone(result)
        self.assertIsNotNone(result.resources)
        self.assertIsNotNone(result.attributes)
        chassis = [resource for resource in result.resources if 'Chassis' in resource.name]
        modules = [resource for resource in result.resources if resource.model == 'Generic Module']
        ports = [resource for resource in result.resources if resource.model == 'Generic Port']
        port_channels = [resource for resource in result.resources if resource.model == 'Generic Port Channel']
        power_ports = [resource for resource in result.resources if resource.model == 'Generic Power Port']
        sub_modules = [resource for resource in result.resources if 'Sub Module' in resource.name]
        trash_chrs = [attribute for attribute in result.attributes if type(attribute.attribute_value) is str and
                      '\\s' in attribute.attribute_value]
        if len(trash_chrs) > 0:
            for char in trash_chrs:
                print char.relative_address + ': ' + char.attribute_name + ' = ' + char.attribute_value
        self.assertTrue(len(chassis) == 1)
        self.assertTrue(len(ports) == 50)
        self.assertTrue(len(modules) == 2)
        self.assertTrue(len(sub_modules) == 0)
        self.assertTrue(len(port_channels) == 0)
        self.assertTrue(len(power_ports) == 8)
        self.assertFalse(len(trash_chrs) > 0)
        self.assertTrue(self._check_relative_path(result.resources))
        print len(chassis)
        print len(ports)
        print len(modules)
        print len(sub_modules)
        print len(port_channels)
        print str(len(power_ports)) + '\n'

    def test_is_loads_SSRsim2_correctly(self):
        print '-----------SSRsim2------------'
        context = ResourceCommandContext()
        context.resource = ResourceContextDetails()
        context.resource.name = 'SSRsim2'
        context.reservation = ReservationContextDetails()
        context.reservation.reservation_id = 'test_SSRsim2_reservation_id'
        context.resource.attributes = {}
        context.resource.attributes['User'] = 'test'
        context.resource.attributes['Password'] = 'test'
        context.resource.attributes['Enable Password'] = 'test'
        context.resource.attributes['CLI Connection Type'] = 'Telnet'
        context.resource.attributes['SNMP Read Community'] = 'test'
        context.resource.attributes['SNMP Version'] = '2'
        context.resource.address = '10.126.144.214'
        result = EricssonIPOSResourceDriver().get_inventory(context)
        self.assertIsNotNone(result)
        self.assertIsNotNone(result.resources)
        self.assertIsNotNone(result.attributes)
        chassis = [resource for resource in result.resources if 'Chassis' in resource.name]
        modules = [resource for resource in result.resources if resource.model == 'Generic Module']
        ports = [resource for resource in result.resources if resource.model == 'Generic Port']
        port_channels = [resource for resource in result.resources if resource.model == 'Generic Port Channel']
        power_ports = [resource for resource in result.resources if resource.model == 'Generic Power Port']
        sub_modules = [resource for resource in result.resources if 'Sub Module' in resource.name]
        trash_chrs = [attribute for attribute in result.attributes if type(attribute.attribute_value) is str and
                      '\\s' in attribute.attribute_value]
        if len(trash_chrs) > 0:
            for char in trash_chrs:
                print char.relative_address + ': ' + char.attribute_name + ' = ' + char.attribute_value
        self.assertTrue(len(chassis) == 1)
        self.assertTrue(len(ports) == 50)
        self.assertTrue(len(modules) == 2)
        self.assertTrue(len(sub_modules) == 0)
        self.assertTrue(len(port_channels) == 0)
        self.assertTrue(len(power_ports) == 8)
        self.assertFalse(len(trash_chrs) > 0)
        self.assertTrue(self._check_relative_path(result.resources))
        print len(chassis)
        print len(ports)
        print len(modules)
        print len(sub_modules)
        print len(port_channels)
        print str(len(power_ports)) + '\n'

    def test_is_loads_SE600_correctly(self):
        print '-----------SE600------------'
        context = ResourceCommandContext()
        context.resource = ResourceContextDetails()
        context.resource.name = 'SE600'
        context.reservation = ReservationContextDetails()
        context.reservation.reservation_id = 'test_SE600_reservation_id'
        context.resource.attributes = {}
        context.resource.attributes['User'] = 'test'
        context.resource.attributes['Password'] = 'test'
        context.resource.attributes['Enable Password'] = 'test'
        context.resource.attributes['CLI Connection Type'] = 'Telnet'
        context.resource.attributes['SNMP Read Community'] = 'test'
        context.resource.attributes['SNMP Version'] = '2'
        context.resource.address = '10.126.133.172'
        result = EricssonSEOSResourceDriver().get_inventory(context)
        self.assertIsNotNone(result)
        self.assertIsNotNone(result.resources)
        self.assertIsNotNone(result.attributes)
        chassis = [resource for resource in result.resources if 'Chassis' in resource.name]
        modules = [resource for resource in result.resources if resource.model == 'Generic Module']
        ports = [resource for resource in result.resources if resource.model == 'Generic Port']
        port_channels = [resource for resource in result.resources if resource.model == 'Generic Port Channel']
        power_ports = [resource for resource in result.resources if resource.model == 'Generic Power Port']
        sub_modules = [resource for resource in result.resources if 'Sub Module' in resource.name]
        trash_chrs = [attribute for attribute in result.attributes if type(attribute.attribute_value) is str and
                      '\\s' in attribute.attribute_value]
        if len(trash_chrs) > 0:
            for char in trash_chrs:
                print char.relative_address + ': ' + char.attribute_name + ' = ' + char.attribute_value
        self.assertTrue(len(chassis) == 1)
        self.assertTrue(len(ports) == 22)
        self.assertTrue(len(modules) == 4)
        self.assertTrue(len(sub_modules) == 0)
        self.assertTrue(len(port_channels) == 0)
        self.assertTrue(len(power_ports) == 0)
        self.assertFalse(len(trash_chrs) > 0)
        self.assertTrue(self._check_relative_path(result.resources))
        print len(chassis)
        print len(ports)
        print len(modules)
        print len(sub_modules)
        print len(port_channels)
        print str(len(power_ports)) + '\n'
