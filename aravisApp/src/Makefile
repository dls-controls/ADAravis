TOP=../..

include $(TOP)/configure/CONFIG

LIBRARY_IOC_Linux += ADAravis

# The following are compiled and added to the support library
ADAravis_SRCS += arvFeature.cpp
ADAravis_SRCS += ADAravis.cpp

DBD += ADAravisSupport.dbd

USR_INCLUDES +=  $(addprefix -I, $(GLIB_INCLUDE))

# We need to link against aravis
USR_INCLUDES += -I$(ARAVIS)/include/aravis-0.6
aravis_DIR     = $(ARAVIS_LIB)
USR_LIBS     += aravis-0.6



USR_LIBS += ADGenICam

USR_LIBS += glib-2.0

include $(TOP)/configure/RULES
