'''
js_manager.py\n
For anything js_tweaker needs to access from other OldGlory modules\n

libraries needed: jsbeautifier, jsmin
'''

import old_glory
import backend
import js_tweaker

import sys
import re

class ValuesJSHandler:
    pass

class ConfigJSHandler:
    '''
    data            Yaml data, from yaml.safe_load(f)
    config          config dictionary, from the likes of backend.load_config()
    f_data_list     Filtered Yaml data (split by file, enabled tweaks only)
    '''
    def __init__(self, data, config):
        self.default = "libraryroot.js"
        self.reg_value = re.compile("(@[A-Za-z]+@)")
        
        self.data = data
        self.config = config
        self.f_data_by_file = self.get_js_enabled_data_by_file()
        
    def get_js_enabled_data_by_file(self):
        f_data_by_file = {self.default: {}}
        for tweak in self.data:
            try:
                if tweak in self.config["JS_Settings"] and self.config["JS_Settings"][tweak] == '1':
                    print("Tweak Enabled " + tweak)
                    #The dictionary containing 1 tweak's data
                    tweak_data = self.data[tweak]
                    if "file" not in tweak_data:
                        print ("  USING DEFAULT " + self.default + " for: " + tweak)
                        f_data_by_file[self.default][tweak] = tweak_data
                    else:
                        #if the filename doesn't exist yet in dict, create it
                        if tweak_data["file"] not in f_data_by_file:
                            f_data_by_file[tweak_data["file"]] = {}
                        f_data_by_file[tweak_data["file"]][tweak] = tweak_data
                else:
                    print("NOT ENABLED " + tweak)
                                                
            except KeyError:
                print("Tweak " + tweak + " has no strings to find and replace, skipping", file=sys.stderr)
                continue
        return f_data_by_file
    
    def get_js_value_from_config(self, value_name):
        if value_name in self.config["JS_Values"]:
            return self.config["JS_Values"][value_name]
        else:
            return "0"
        
    def replace_js_values(self, tweak_data):
        '''
        tweak_data  The dictionary containing 1 tweak's data
        '''       
        for find_repl in tweak_data["strings"]:
            pass
        pass
    
    def get_line(self, data_dict):
        for k, v in data_dict.items():
            if isinstance(v, dict):
                data_dict[k] = self.get_line(self, v)
            else:
                return re.sub(self.reg_value, )
            
def process_yaml():
    y_handler = js_tweaker.YamlHandler("js_tweaks.yml")
    c_handler = ConfigJSHandler(y_handler.data, backend.load_config())
    #add @values
    #add refs
    #sub regex
    #escape characters