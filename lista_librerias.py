from datetime import datetime

import pkg_resources

modulos_instalados = pkg_resources.working_set
modulos_instalados_list = sorted(["%s==%s" % (i.key, i.version) for i in modulos_instalados])

for m in modulos_instalados_list:
	print(m)
