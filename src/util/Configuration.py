# Objects must inherit from Configuration if they need to be configured at startup. If objects do not need to be
# manually differentiated at startup, they do not need to be configured.

class Configuration(object):
    # methods to create ClassDef, read properties into class

    def __init__(self):
        self.write_class_def()

    def write_class_def(self):
        class_name = type(self).__name__
        class_def_filename = 'configs/class_defs/' + class_name + 'Def.py'
        with open(class_def_filename, 'w') as of:
            of.write('### Class definition is automatically generated. ###\n')
            of.write('### DO NOT MODIFY. ###\n')
            of.write('\n')
            of.write('class {}(object):\n'.format(class_name + 'Def'))
            of.write('\n')
            of.write('\tdef __init__(self,\n')
            for attr in vars(self):
                of.write('\t\t{},\n'.format(attr))
            of.write('\t)\n')

