# -*- coding: utf-8 -*-

"""
***************************************************************************
    ProcessingConfig.py
    ---------------------
    Date                 : August 2012
    Copyright            : (C) 2012 by Victor Olaya
    Email                : volayaf at gmail dot com
***************************************************************************
*                                                                         *
*   This program is free software; you can redistribute it and/or modify  *
*   it under the terms of the GNU General Public License as published by  *
*   the Free Software Foundation; either version 2 of the License, or     *
*   (at your option) any later version.                                   *
*                                                                         *
***************************************************************************
"""

__author__ = 'Victor Olaya'
__date__ = 'August 2012'
__copyright__ = '(C) 2012, Victor Olaya'

# This will get replaced with a git SHA1 when you do a git archive

__revision__ = '$Format:%H$'

import os

from PyQt4.QtCore import QPyNullVariant, QCoreApplication, QSettings
from PyQt4.QtGui import QIcon
from processing.tools.system import defaultOutputFolder
import processing.tools.dataobjects


class ProcessingConfig:

    OUTPUT_FOLDER = 'OUTPUTS_FOLDER'
    RASTER_STYLE = 'RASTER_STYLE'
    VECTOR_POINT_STYLE = 'VECTOR_POINT_STYLE'
    VECTOR_LINE_STYLE = 'VECTOR_LINE_STYLE'
    VECTOR_POLYGON_STYLE = 'VECTOR_POLYGON_STYLE'
    SHOW_RECENT_ALGORITHMS = 'SHOW_RECENT_ALGORITHMS'
    USE_SELECTED = 'USE_SELECTED'
    USE_FILENAME_AS_LAYER_NAME = 'USE_FILENAME_AS_LAYER_NAME'
    KEEP_DIALOG_OPEN = 'KEEP_DIALOG_OPEN'
    SHOW_DEBUG_IN_DIALOG = 'SHOW_DEBUG_IN_DIALOG'
    RECENT_ALGORITHMS = 'RECENT_ALGORITHMS'
    PRE_EXECUTION_SCRIPT = 'PRE_EXECUTION_SCRIPT'
    POST_EXECUTION_SCRIPT = 'POST_EXECUTION_SCRIPT'
    SHOW_CRS_DEF = 'SHOW_CRS_DEF'
    WARN_UNMATCHING_CRS = 'WARN_UNMATCHING_CRS'
    DEFAULT_OUTPUT_RASTER_LAYER_EXT = 'DEFAULT_OUTPUT_RASTER_LAYER_EXT'
    DEFAULT_OUTPUT_VECTOR_LAYER_EXT = 'DEFAULT_OUTPUT_VECTOR_LAYER_EXT'

    settings = {}
    settingIcons = {}

    @staticmethod
    def initialize():
        icon = QIcon(os.path.dirname(__file__) + '/../images/alg.png')
        ProcessingConfig.settingIcons['General'] = icon
        ProcessingConfig.addSetting(Setting(
            ProcessingConfig.tr('General'),
            ProcessingConfig.SHOW_DEBUG_IN_DIALOG,
            ProcessingConfig.tr('Show extra info in Log panel'), True))
        ProcessingConfig.addSetting(Setting(
            ProcessingConfig.tr('General'),
            ProcessingConfig.KEEP_DIALOG_OPEN,
            ProcessingConfig.tr('Keep dialog open after running an algorithm'), False))
        ProcessingConfig.addSetting(Setting(
            ProcessingConfig.tr('General'),
            ProcessingConfig.USE_SELECTED,
            ProcessingConfig.tr('Use only selected features'), True))
        ProcessingConfig.addSetting(Setting(
            ProcessingConfig.tr('General'),
            ProcessingConfig.USE_FILENAME_AS_LAYER_NAME,
            ProcessingConfig.tr('Use filename as layer name'), False))
        ProcessingConfig.addSetting(Setting(
            ProcessingConfig.tr('General'),
            ProcessingConfig.SHOW_RECENT_ALGORITHMS,
            ProcessingConfig.tr('Show recently executed algorithms'), True))
        ProcessingConfig.addSetting(Setting(
            ProcessingConfig.tr('General'),
            ProcessingConfig.OUTPUT_FOLDER,
            ProcessingConfig.tr('Output folder'), defaultOutputFolder(),
            valuetype=Setting.FOLDER))
        ProcessingConfig.addSetting(Setting(
            ProcessingConfig.tr('General'),
            ProcessingConfig.SHOW_CRS_DEF,
            ProcessingConfig.tr('Show layer CRS definition in selection boxes'), True))
        ProcessingConfig.addSetting(Setting(
            ProcessingConfig.tr('General'),
            ProcessingConfig.WARN_UNMATCHING_CRS,
            ProcessingConfig.tr("Warn before executing if layer CRS's do not match"), True))
        ProcessingConfig.addSetting(Setting(
            ProcessingConfig.tr('General'),
            ProcessingConfig.RASTER_STYLE,
            ProcessingConfig.tr('Style for raster layers'), '',
            valuetype=Setting.FILE))
        ProcessingConfig.addSetting(Setting(
            ProcessingConfig.tr('General'),
            ProcessingConfig.VECTOR_POINT_STYLE,
            ProcessingConfig.tr('Style for point layers'), '',
            valuetype=Setting.FILE))
        ProcessingConfig.addSetting(Setting(
            ProcessingConfig.tr('General'),
            ProcessingConfig.VECTOR_LINE_STYLE,
            ProcessingConfig.tr('Style for line layers'), '',
            valuetype=Setting.FILE))
        ProcessingConfig.addSetting(Setting(
            ProcessingConfig.tr('General'),
            ProcessingConfig.VECTOR_POLYGON_STYLE,
            ProcessingConfig.tr('Style for polygon layers'), '',
            valuetype=Setting.FILE))
        ProcessingConfig.addSetting(Setting(
            ProcessingConfig.tr('General'),
            ProcessingConfig.PRE_EXECUTION_SCRIPT,
            ProcessingConfig.tr('Pre-execution script'), '',
            valuetype=Setting.FILE))
        ProcessingConfig.addSetting(Setting(
            ProcessingConfig.tr('General'),
            ProcessingConfig.POST_EXECUTION_SCRIPT,
            ProcessingConfig.tr('Post-execution script'), '',
            valuetype=Setting.FILE))
        ProcessingConfig.addSetting(Setting(
            ProcessingConfig.tr('General'),
            ProcessingConfig.RECENT_ALGORITHMS,
            ProcessingConfig.tr('Recent algs'), '', hidden=True))
        extensions = processing.tools.dataobjects.getSupportedOutputVectorLayerExtensions()
        ProcessingConfig.addSetting(Setting(
            ProcessingConfig.tr('General'),
            ProcessingConfig.DEFAULT_OUTPUT_VECTOR_LAYER_EXT,
            ProcessingConfig.tr('Default output vector layer extension'), extensions[0],
                                valuetype=Setting.SELECTION, options=extensions))
        extensions = processing.tools.dataobjects.getSupportedOutputRasterLayerExtensions()
        ProcessingConfig.addSetting(Setting(
            ProcessingConfig.tr('General'),
            ProcessingConfig.DEFAULT_OUTPUT_RASTER_LAYER_EXT,
            ProcessingConfig.tr('Default output raster layer extension'), extensions[0],
                                valuetype=Setting.SELECTION, options=extensions))

    @staticmethod
    def setGroupIcon(group, icon):
        ProcessingConfig.settingIcons[group] = icon

    @staticmethod
    def getGroupIcon(group):
        if group == ProcessingConfig.tr('General'):
            return QIcon(os.path.dirname(__file__) + '/../images/alg.png')
        if group in ProcessingConfig.settingIcons:
            return ProcessingConfig.settingIcons[group]
        else:
            return QIcon(os.path.dirname(__file__) + '/../images/alg.png')

    @staticmethod
    def addSetting(setting):
        ProcessingConfig.settings[setting.name] = setting

    @staticmethod
    def removeSetting(name):
        del ProcessingConfig.settings[name]

    @staticmethod
    def getSettings():
        '''Return settings as a dict with group names as keys and lists of settings as values'''
        settings = {}
        for setting in ProcessingConfig.settings.values():
            if setting.group not in settings:
                group = []
                settings[setting.group] = group
            else:
                group = settings[setting.group]
            group.append(setting)
        return settings

    @staticmethod
    def readSettings():
        for setting in ProcessingConfig.settings.values():
            setting.read()

    @staticmethod
    def getSetting(name):
        if name in ProcessingConfig.settings.keys():
            v = ProcessingConfig.settings[name].value
            if isinstance(v, QPyNullVariant):
                v = None
            return v
        else:
            return None

    @staticmethod
    def setSettingValue(name, value):
        if name in ProcessingConfig.settings.keys():
            ProcessingConfig.settings[name].setValue(value)
            ProcessingConfig.settings[name].save()

    @staticmethod
    def tr(string, context=''):
        if context == '':
            context = 'ProcessingConfig'
        return QCoreApplication.translate(context, string)


class Setting:

    """A simple config parameter that will appear on the config dialog.
    """
    STRING = 0
    FILE = 1
    FOLDER = 2
    SELECTION = 3
    FLOAT = 4
    INT = 5

    def __init__(self, group, name, description, default, hidden=False, valuetype=None,
                 validator=None, options=None):
        self.group = group
        self.name = name
        self.qname = "Processing/Configuration/" + self.name
        self.description = description
        self.default = default
        self.hidden = hidden
        if valuetype is None:
            if isinstance(default, (int, long)):
                valuetype = self.INT
            elif isinstance(default, float):
                valuetype = self.FLOAT
        self.valuetype = valuetype
        self.options = options
        if validator is None:
            if valuetype == self.FLOAT:
                def checkFloat(v):
                    try:
                        float(v)
                    except ValueError:
                        raise ValueError(self.tr('Wrong parameter value:\n%s') % unicode(v))
                validator = checkFloat
            elif valuetype == self.INT:
                def checkInt(v):
                    try:
                        int(v)
                    except ValueError:
                        raise ValueError(self.tr('Wrong parameter value:\n%s') % unicode(v))
                validator = checkInt
            elif valuetype in [self.FILE, self.FOLDER]:
                def checkFileOrFolder(v):
                    if v and not os.path.exists(v):
                        raise ValueError(self.tr('Specified path does not exist:\n%s') % unicode(v))
                validator = checkFileOrFolder
            else:
                validator = lambda x: True
        self.validator = validator
        self.value = default

    def setValue(self, value):
        self.validator(value)
        self.value = value

    def read(self):
        qsettings = QSettings()
        value = qsettings.value(self.qname, None)
        if value is not None:
            self.value = self._deserialize_value(value)

    def save(self):
        serialized = self._serialize_value()
        QSettings().setValue(self.qname, serialized)

    def _deserialize_value(self, stored_value):
        """Convert the value read in QSettings back to its concrete type

        This method should be reimplemented by classes that provide custom
        valuetypes where the representation used by PyQt to store the value
        of the instance may need to be specified. The default implementation
        does nothing.
        """
        return stored_value

    def _serialize_value(self):
        """Store this instance's value in QSettings

        This method should be reimplemented by classes that provide custom
        valuetypes where the representation used by PyQt to store the value
        of the instance may need to be specified. The default implementation
        does nothing.
        """
        return self.value

    def _build_config_gui(self, config_group, group_label):
        """Build GUI elements for this setting.

        This method allows an AlgorithmProvider to specify a more complex
        GUI for its configuration settings.

        Processing supplies a ready-made GUI for all items of the types
        defined by this class, which covers the needs of most algorithm
        providers. However, some providers may need to use more complex
        types for their settings such as lists of strings or dictionaries.
        These types may also require custom GUI elements.
        Whenever there is such a need, the client code can reimplement
        this method (in a new class, derived from this one) and provide
        the custom GUI elements.

        The default implementation does nothing, thus delegating to
        Processing the creation of the ready-made GUI elements for the
        predefined setting types. In order to define custom GUI elements
        just be sure to return True, as this tells Processing that this
        setting's GUI is not to be automatically created.

        example:

        .. code:: python

           class MySpecializedSetting(ProcessingConfig.Setting):

               def _build_config_gui(self, config_group, group_label):
                   empty_item = QtGui.QStandardItem()
                   empty_item.setEditable(False)
                   config_group.insertRow(0, [label, empty_item])
                   for sub_value in self.value:
                       new_item = QtGui.QStandardItem(sub_value)
                       empty_item = QtGui.QStandardItem()
                       empty_item.setEditable(False)
                       label.appendRow([new_item, empty_item])
                   return True

        :param setting:
        :type setting: ProcessingConfig.Setting
        :param config_group:
        :type config_group: PyQt4.QtGui.QStandardItem
        :param label:
        :type label: PyQt4.QtGui.QStandardItem
        :return:
        :rtype: bool
        """

        return False



    def __str__(self):
        return self.name + '=' + unicode(self.value)

    def tr(self, string, context=''):
        if context == '':
            context = 'ProcessingConfig'
        return QCoreApplication.translate(context, string)
