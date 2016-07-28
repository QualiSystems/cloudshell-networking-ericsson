import inject
from collections import OrderedDict
import re

from cloudshell.networking.networking_utils import *
from cloudshell.networking.operations.connectivity_operations import ConnectivityOperations
from cloudshell.cli.command_template.command_template_service import add_templates, get_commands_list
from cloudshell.shell.core.context_utils import get_resource_name


class EricssonConnectivityOperations(ConnectivityOperations):
    def __init__(self, cli=None, logger=None, api=None, resource_name=None):
        ConnectivityOperations.__init__(self)
        self._cli = cli
        self._logger = logger
        self._api = api
        try:
            self.resource_name = get_resource_name()
        except Exception:
            raise Exception('CiscoHandlerBase', 'Failed to get ResourceName.')

    @property
    def logger(self):
        if self._logger is None:
            try:
                self._logger = inject.instance('logger')
            except:
                raise Exception('CiscoConnectivityOperations', 'Failed to get logger.')
        return self._logger

    @property
    def cli(self):
        if self._cli is None:
            try:
                self._cli = inject.instance('cli_service')
            except:
                raise Exception('CiscoConnectivityOperations', 'Failed to get cli_service.')
        return self._cli

    @property
    def api(self):
        if self._api is None:
            try:
                self._api = inject.instance('api')
            except:
                raise Exception('CiscoConnectivityOperations', 'Failed to get api handler.')
        return self._api

    def send_config_command_list(self, command_list, expected_map=None):
        """Send list of config commands

        :param command_list: list of commands
        :return output from cli
        :rtype: string
        """

        result = self.cli.send_command_list(command_list, expected_map=expected_map)
        self.cli.exit_configuration_mode()
        return result

    def _get_resource_full_name(self, port_resource_address, resource_details_map):
        """Recursively search for port name on the resource

        :param port_resource_address: port resource address
        :param resource_details_map: full device resource structure
        :return: full port resource name (Cisco2950/Chassis 0/FastEthernet0-23)
        :rtype: string
        """

        result = None
        for port in resource_details_map.ChildResources:
            if port.FullAddress in port_resource_address and port.FullAddress == port_resource_address:
                return port.Name
            if port.FullAddress in port_resource_address and port.FullAddress != port_resource_address:
                result = self._get_resource_full_name(port_resource_address, port)
            if result is not None:
                return result
        return result

    def _does_interface_support_qnq(self, interface_name):
        """Validate whether qnq is supported for certain port

        """

        result = False
        self.cli.send_config_command('interface {0}'.format(interface_name))
        output = self.cli.send_config_command('switchport mode ?')
        if 'dot1q-tunnel' in output.lower():
            result = True
        self.cli.exit_configuration_mode()
        return result

    @staticmethod
    def _load_vlan_command_templates():
        """Load all required Commandtemplates to configure valn on certain port

        """

        # add_templates(ETHERNET_COMMANDS_TEMPLATES)
        # add_templates(VLAN_COMMANDS_TEMPLATES)
        # add_templates(ENTER_INTERFACE_CONF_MODE)
        pass

    def add_vlan(self, vlan_range, port, port_mode, qnq, ctag):
        """Configure specified vlan range in specified switchport mode on provided port

        :param vlan_range: range of vlans to be added, if empty, and switchport_type = trunk,
        trunk mode will be assigned
        :param port: List of interfaces Resource Full Address
        :param port_mode: type of adding vlan ('trunk' or 'access')
        :param qnq: QNQ parameter for switchport mode dot1nq
        :param ctag: CTag details
        :return: success message
        :rtype: string
        """

        return 'Vlan Configuration Completed.'

    def remove_vlan(self, vlan_range, port, port_mode):
        """
        Remove vlan from port
        :param vlan_range: range of vlans to be added, if empty, and switchport_type = trunk,
        trunk mode will be assigned
        :param port: List of interfaces Resource Full Address
        :param port_mode: type of adding vlan ('trunk' or 'access')
        :return: success message
        :rtype: string
        """

        return 'Remove Vlan Completed.'

    def validate_vlan_methods_incoming_parameters(self, vlan_range, port, port_mode):
        """Validate add_vlan and remove_vlan incoming parameters

        :param vlan_range: vlan range (10,20,30-40)
        :param port_list: list of port resource addresses ([192.168.1.1/0/34, 192.168.1.1/0/42])
        :param port_mode: switchport mode (access or trunk)
        """

        self.logger.info('Validate incoming parameters for vlan configuration:')
        if not port:
            raise Exception('CiscoHandlerBase: validate_vlan_methods_incoming_parameters ', 'Port list can\'t be empty.')

        if vlan_range == '' and port_mode == 'access':
            raise Exception('CiscoHandlerBase: validate_vlan_methods_incoming_parameters',
                            'Switchport type is Access, vlan id/range can\'t be empty.')

        if (',' in vlan_range or '-' in vlan_range) and port_mode == 'access':
            raise Exception('CiscoHandlerBase: validate_vlan_methods_incoming_parameters',
                            'Interface in Access mode, vlan range is not allowed, only one vlan can be assigned.')

    def get_port_name(self, port):
        """Get port name from port resource full address

        :param port: port resource full address (192.168.1.1/0/34)
        :return: port name (FastEthernet0/23)
        :rtype: string
        """

        port_resource_map = self.api.GetResourceDetails(self.resource_name)
        temp_port_full_name = self._get_resource_full_name(port, port_resource_map)
        if not temp_port_full_name:
            err_msg = 'Failed to get port name.'
            self.logger.error(err_msg)
            raise Exception('Cisco OS: get_port_name', err_msg)

        temp_port_name = temp_port_full_name.split('/')[-1]
        if 'port-channel' not in temp_port_full_name.lower():
            temp_port_name = temp_port_name.replace('-', '/')

        self.logger.info('Interface name validation OK, portname = {0}'.format(temp_port_name))
        return temp_port_name

    def configure_vlan_on_interface(self, commands_dict):
        """Configure vlan on specified interface/s

        :param commands_dict: dictionary of parameters
        :return: success message
        :rtype: string
        """

        return 'Vlan configuration completed.'

    def configure_vlan(self, ordered_parameters_dict):
        """Configure vlan

        :param ordered_parameters_dict: dictionary of parameters
        :return: success message
        :rtype: string
        """

        return 'Vlan configuration completed.'
