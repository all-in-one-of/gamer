# -*- coding: utf-8 -*-
"""
Created on Mon Mar 19 11:36:12 2012

@author: Ludovic Autin
"""
import os

#base helper class
from upy.pluginAdaptor import pluginAdaptor

import c4d

class general_plugClass(pluginAdaptor):
    host = "c4d"
    def __init__(self,**kw):
        pluginAdaptor.__init__(self,**kw)
#        c4d.plugins.TagData.__init__(self,)
        self.plugin_id =  1025244        
        prefpath=c4d.storage.GeGetC4DPath(1)
        os.chdir(prefpath)
        os.chdir(".."+os.sep)
        self.prefdir = os.path.abspath(os.curdir)
        self.setup()
        self.gui = None
        
    
    def setIcon(self,image_filename=None,image_name=None):
#        dir, file = os.path.split(__file__)
        self.plugin_icon = c4d.bitmaps.BaseBitmap()
        if image_filename is not None :
            self.plugin_icon.InitWith(image_filename)  
        elif image_name is not None :
            self.plugin_icon.InitWith(os.path.join(self.prefdir+os.sep+"plugins"+os.sep+self.plugin_name,"res",image_name)) 

    def setGeRessource(self,res,path=None):
        if path is None :
            path = os.path.join(self.prefdir+os.sep+"plugins"+os.sep+self.plugin_name,"res")
        return res.Init(path)
     
#    @classmethod
    def register(self,classObject,Object,**kw):
        #should create some file and folder ?
        #test plugin folder
        if Object is None :
            Object = self
        global __res__
        __res__ = kw["res"]            
        r= self.setGeRessource(__res__)  
        print (self.plugin_class)          
        if self.plugin_class=="tag":            
            c4d.plugins.RegisterTagPlugin(id=Object.plugin_id, str=Object.plugin_name,
                              info=c4d.TAG_MULTIPLE|c4d.TAG_EXPRESSION|c4d.TAG_VISIBLE,
                              g=classObject, description=Object.plugin_tooltip, icon=Object.plugin_icon)
        elif self.plugin_class=="command":
            c4d.plugins.RegisterCommandPlugin(id=Object.plugin_id, str=Object.plugin_name,
                                     help=Object.plugin_tooltip,
                                     dat=Object,info=0, icon=Object.plugin_icon)
            print "hasregistred"
                 
                            
    def unregister(self):
        pass
    
    def getType(self):
        pass
 
    def runCommands(self,*args,**kw):
        pass
   
    def setRunCommands(self,runCommands=None):
        self.runCommands = runCommands
    
    def Execute(self, tag, doc, op, bt, priority, flags):
        self.runCommands()
        return c4d.EXECUTIONRESULT_OK

    def setgui(self,dname):
        pass
 
    def resetgui(self,dname):
        pass
    
       
class pluginTag(general_plugClass,c4d.plugins.TagData):
    plugin_class = "tag"


class pluginCommand(general_plugClass,c4d.plugins.CommandData):
    plugin_class = "command"
    def Execute(self, doc):
         # create the dialog
         dname=doc.GetDocumentName()
         self.runCommands() 
         if self.hasGui and self.gui is None :
             self.setgui(dname)
         return self.gui.Open(self.plugin_id,defaultw=self.gui.w, defaulth=self.gui.h)
    
    def RestoreLayout(self, sec_ref):
         print "restore",sec_ref    
         doc=c4d.documents.GetActiveDocument()
         dname=doc.GetDocumentName()
         #print doc,dname,c4d.mv
         if self.hasGui and self.gui is None :
            self.resetgui(dname)
         self.gui.restored=True
         return self.gui.Restore(pluginid=self.plugin_id,secret=sec_ref)

def get(pType):
    if pType == "tag":
        return pluginTag,c4d.plugins.TagData
    elif pType == "command":
        return pluginCommand,c4d.plugins.CommandData
    return None