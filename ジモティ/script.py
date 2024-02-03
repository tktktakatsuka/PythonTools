__all__ = ['script']

# Don't look below, you will not understand this Python code :) I don't.

from js2py.pyjs import *
# setting scope
var = Scope( JS_BUILTINS )
set_global_object(var)

# Code follows:
var.registers(['setEmail'])
@Js
def PyJsHoisted_setEmail_(id, this, arguments, var=var):
    var = Scope({'id':id, 'this':this, 'arguments':arguments}, var)
    var.registers(['id'])
    var.get('document').callprop('getElementById', var.get('id')).put('value', Js('user_email'))
PyJsHoisted_setEmail_.func_name = 'setEmail'
var.put('setEmail', PyJsHoisted_setEmail_)
pass
pass


# Add lib to the module scope
script = var.to_python()