from iocbuilder import Device, AutoSubstitution, SetSimulation
from iocbuilder.arginfo import *

from iocbuilder.modules.asyn import AsynPort
from iocbuilder.modules.ADCore import ADCore, ADBaseTemplate, includesTemplates, makeTemplateInstance
from iocbuilder.modules.ADGenICam import GenICam

class aravisCameraTemplate(AutoSubstitution):
    TemplateFile="aravisCamera.template"

class aravisCamera(GenICam):
    '''Creates a aravisCamera camera areaDetector driver'''
    Dependencies = (GenICam,)
    # This tells xmlbuilder to use PORT instead of name as the row ID
    UniqueName = "PORT"
    _SpecificTemplate = aravisCameraTemplate
    def __init__(self,P,R,PORT, ID, CLASS, PV_ALIAS, BUFFERS = 50, MEMORY = -1, **args):
        # Init the superclass
        self.__super.__init__(P,R,PORT,ID,CLASS,PV_ALIAS,BUFFERS,MEMORY)
        # Update the attributes of self from the commandline args
        self.__dict__.update(locals())
        # Make an instance of our template
        makeTemplateInstance(self._SpecificTemplate, locals(), args)
        # Backwards compatible Manta
        # Init the camera specific class

    # __init__ arguments
    ArgInfo = makeArgInfo(__init__,
        P    = Simple('PV Prefix', str),
        R    = Simple('PV Suffix', str),
        PORT    = Simple('Port name for the camera', str),
        ID      = Simple('Cam ip address, hostname, MAC address, or ID <manufacturer>-<serial>, (e.g. Prosilica-02-2166A-06844)', str),
        CLASS   = Choice('Camera class for custom commands',
                         ["AVT_Manta_G235B","AVT_Manta_G609B","AVT_Manta_G125B","AVT_Mako_G234C","AVT_Manta_G235C","AVT_Prosilica_GC655C","AVT_Mako_1_52","Prosilica_GC","AVT_Manta_1_44","AVT_Manta_G125C","AVT_Mako_G125C"]),
        PV_ALIAS   = Choice('Use alias template to keep some key PV names the same',
                         [0,1]),
        BUFFERS = Simple('Maximum number of NDArray buffers to be created for '
                         'plugin callbacks', int),
        MEMORY  = Simple('Max memory to allocate, should be maxw*maxh*nbuffer '
                         'for driver and all attached plugins', int))


    def Initialise(self):
        #print "aravisConfig(const char *portName, const char *cameraName, size_t maxMemory, int priority, int stackSize)"
        print 'aravisConfig("%(PORT)s", "%(ID)s", %(MEMORY)d, 0,1)' % self.__dict__

    # Device attributes
    LibFileList = ['ADAravis']
    DbdFileList = ['ADAravisSupport']



