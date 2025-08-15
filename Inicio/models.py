# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=150)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.IntegerField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.IntegerField()
    is_active = models.IntegerField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class Cajas(models.Model):
    id_caja = models.AutoField(db_column='Id_caja', primary_key=True)  # Field name made lowercase.
    saldo_inicial = models.DecimalField(db_column='Saldo_inicial', max_digits=12, decimal_places=5)  # Field name made lowercase.
    saldo_anterior = models.DecimalField(db_column='Saldo_anterior', max_digits=12, decimal_places=5)  # Field name made lowercase.
    saldo_actual = models.DecimalField(db_column='Saldo_actual', max_digits=12, decimal_places=5)  # Field name made lowercase.
    saldo_final = models.DecimalField(db_column='Saldo_final', max_digits=12, decimal_places=5)  # Field name made lowercase.
    fecha_apertura = models.DateTimeField(db_column='Fecha_apertura')  # Field name made lowercase.
    fecha_cierre = models.DateTimeField(db_column='Fecha_cierre')  # Field name made lowercase.
    estado_caja = models.IntegerField(db_column='Estado_caja')  # Field name made lowercase.
    id_emp_cj = models.ForeignKey('Empleados', models.DO_NOTHING, db_column='Id_emp_cj')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'cajas'


class Clientes(models.Model):
    id_cliente = models.AutoField(db_column='Id_cliente', primary_key=True)  # Field name made lowercase.
    nombre_cliente = models.CharField(db_column='Nombre_cliente', max_length=45)  # Field name made lowercase.
    apellido_cliente = models.CharField(db_column='Apellido_cliente', max_length=45)  # Field name made lowercase.
    correo_clientes = models.CharField(db_column='Correo_clientes', max_length=45)  # Field name made lowercase.
    telefono_cliente = models.CharField(db_column='Telefono_cliente', max_length=45)  # Field name made lowercase.
    dni_cliente = models.CharField(db_column='DNI_cliente', max_length=45)  # Field name made lowercase.
    estado_cliente = models.IntegerField(db_column='Estado_cliente')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'clientes'


class Compras(models.Model):
    id_compra = models.AutoField(db_column='Id_compra', primary_key=True)  # Field name made lowercase.
    nombre_compra = models.CharField(db_column='Nombre_compra', max_length=455)  # Field name made lowercase.
    cantidad_compra = models.IntegerField(db_column='Cantidad_compra')  # Field name made lowercase.
    fecha_compra = models.DateField(db_column='Fecha_compra')  # Field name made lowercase.
    precio_compra = models.DecimalField(db_column='Precio_compra', max_digits=12, decimal_places=5)  # Field name made lowercase.
    descripcion_compra = models.CharField(db_column='Descripcion_compra', max_length=455)  # Field name made lowercase.
    id_empleado_fk = models.ForeignKey('Empleados', models.DO_NOTHING, db_column='Id_empleado_fk')  # Field name made lowercase.
    id_caja_fk = models.ForeignKey(Cajas, models.DO_NOTHING, db_column='Id_caja_fk')  # Field name made lowercase.
    id_cliente_fk = models.ForeignKey(Clientes, models.DO_NOTHING, db_column='Id_cliente_fk')  # Field name made lowercase.
    estado_compra = models.IntegerField(db_column='Estado_compra', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'compras'


class DetalleCompras(models.Model):
    id_detalle_compra = models.AutoField(db_column='Id_detalle_compra', primary_key=True)  # Field name made lowercase.
    precio_unitario_dtc = models.DecimalField(db_column='Precio_unitario_dtc', max_digits=12, decimal_places=5)  # Field name made lowercase.
    subtotal_dtc = models.DecimalField(db_column='Subtotal_dtc', max_digits=12, decimal_places=5)  # Field name made lowercase.
    descuento_dtc = models.DecimalField(db_column='Descuento_dtc', max_digits=12, decimal_places=5)  # Field name made lowercase.
    total_dtc = models.DecimalField(db_column='Total_dtc', max_digits=12, decimal_places=5)  # Field name made lowercase.
    fecha_entrega_dtc = models.DateField(db_column='Fecha_entrega_dtc')  # Field name made lowercase.
    descripcion_dtc = models.CharField(db_column='Descripcion_dtc', max_length=445, blank=True, null=True)  # Field name made lowercase.
    estado_dtc = models.IntegerField(db_column='Estado_dtc')  # Field name made lowercase.
    id_compra_dtc = models.ForeignKey(Compras, models.DO_NOTHING, db_column='Id_compra_dtc')  # Field name made lowercase.
    id_producto_dtc = models.ForeignKey('Productos', models.DO_NOTHING, db_column='Id_producto_dtc')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'detalle_compras'


class DetalleSolicOc(models.Model):
    id_detalle_solic_oc = models.AutoField(db_column='Id_detalle_solic_OC', primary_key=True)  # Field name made lowercase.
    cantidad_producto_oc = models.IntegerField(db_column='Cantidad_producto_OC')  # Field name made lowercase.
    precio_unitario_oc = models.DecimalField(db_column='Precio_unitario_OC', max_digits=12, decimal_places=5)  # Field name made lowercase.
    sub_total_oc = models.DecimalField(db_column='Sub_total_OC', max_digits=12, decimal_places=5)  # Field name made lowercase.
    fecha_oc = models.DateField(db_column='Fecha_OC')  # Field name made lowercase.
    decripcion_oc = models.CharField(db_column='Decripcion_OC', max_length=455)  # Field name made lowercase.
    estado_oc = models.IntegerField(db_column='Estado_OC')  # Field name made lowercase.
    id_solicitud_oc = models.ForeignKey('SolicitudOrdenCompras', models.DO_NOTHING, db_column='Id_solicitud_OC')  # Field name made lowercase.
    id_provxprod_oc = models.ForeignKey('Provxprod', models.DO_NOTHING, db_column='Id_provXprod_OC')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'detalle_solic_oc'


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.PositiveSmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    id = models.BigAutoField(primary_key=True)
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'


class EmpRoles(models.Model):
    id_rol_emp = models.AutoField(db_column='Id_rol_emp', primary_key=True)  # Field name made lowercase.
    id_rol_emp_emp = models.ForeignKey('Empleados', models.DO_NOTHING, db_column='Id_rol_emp_emp')  # Field name made lowercase.
    id_rol_emp_rol = models.ForeignKey('Roles', models.DO_NOTHING, db_column='Id_rol_emp_rol')  # Field name made lowercase.
    estado_emp_rol = models.IntegerField(db_column='Estado_emp_rol', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'emp_roles'


class Empleados(models.Model):
    id_emp = models.AutoField(db_column='Id_emp', primary_key=True)  # Field name made lowercase.
    nombre_emp = models.CharField(db_column='Nombre_emp', max_length=45)  # Field name made lowercase.
    apellido_emp = models.CharField(db_column='Apellido_emp', max_length=45)  # Field name made lowercase.
    dni_emp = models.CharField(db_column='DNI_emp', max_length=45)  # Field name made lowercase.
    direccion_emp = models.CharField(db_column='Direccion_emp', max_length=455)  # Field name made lowercase.
    telefono_emp = models.IntegerField(db_column='Telefono_emp')  # Field name made lowercase.
    correo_emp = models.CharField(db_column='Correo_emp', max_length=100)  # Field name made lowercase.
    estado_emp = models.IntegerField(db_column='Estado_emp')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'empleados'


class Mascotas(models.Model):
    id_mascotas = models.AutoField(db_column='Id_mascotas', primary_key=True)  # Field name made lowercase.
    estado_mascota = models.IntegerField(db_column='Estado_mascota', blank=True, null=True)  # Field name made lowercase.
    id_cliente_masc = models.ForeignKey(Clientes, models.DO_NOTHING, db_column='Id_cliente_masc')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'mascotas'


class OrdenCompras(models.Model):
    id_orden_compra = models.AutoField(db_column='Id_orden_compra', primary_key=True)  # Field name made lowercase.
    fecha_emision_orden = models.DateField(db_column='Fecha_emision_orden')  # Field name made lowercase.
    total_orden = models.DecimalField(db_column='Total_orden', max_digits=12, decimal_places=5)  # Field name made lowercase.
    estado_orden = models.IntegerField(db_column='Estado_orden')  # Field name made lowercase.
    id_solicitud_orc = models.ForeignKey('SolicitudOrdenCompras', models.DO_NOTHING, db_column='Id_solicitud_orc')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'orden_compras'


class PrecioServicios(models.Model):
    id_precio_servicio = models.AutoField(db_column='Id_precio_servicio', primary_key=True)  # Field name made lowercase.
    id_servicio_preser = models.ForeignKey('Servicios', models.DO_NOTHING, db_column='Id_servicio_preser')  # Field name made lowercase.
    precio_unitario_preser = models.DecimalField(db_column='Precio_unitario_preser', max_digits=12, decimal_places=5)  # Field name made lowercase.
    precio_completo_preser = models.DecimalField(db_column='Precio_completo_preser', max_digits=12, decimal_places=5)  # Field name made lowercase.
    descripcion_precio_servicio = models.CharField(db_column='Descripcion_precio_servicio', max_length=455, blank=True, null=True)  # Field name made lowercase.
    estado_precio_servicio = models.IntegerField(db_column='Estado_precio_servicio', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'precio_servicios'


class Productos(models.Model):
    id_prod = models.AutoField(db_column='Id_prod', primary_key=True)  # Field name made lowercase.
    nombre_prod = models.CharField(db_column='Nombre_prod', max_length=45)  # Field name made lowercase.
    stock_prod = models.CharField(db_column='Stock_prod', max_length=45)  # Field name made lowercase.
    precio_prod = models.DecimalField(db_column='Precio_prod', max_digits=12, decimal_places=5)  # Field name made lowercase.
    unidad_media_prod = models.CharField(db_column='Unidad_media_prod', max_length=45)  # Field name made lowercase.
    categoria_prod = models.CharField(db_column='Categoria_prod', max_length=45)  # Field name made lowercase.
    estado_prod = models.IntegerField(db_column='Estado_prod', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'productos'


class Proveedoress(models.Model):
    id_prov = models.AutoField(db_column='Id_prov', primary_key=True)  # Field name made lowercase.
    nombre_prov = models.CharField(db_column='Nombre_prov', max_length=45)  # Field name made lowercase.
    correo_prov = models.CharField(db_column='Correo_prov', max_length=45)  # Field name made lowercase.
    cuit_prov = models.IntegerField(db_column='CUIT_prov')  # Field name made lowercase.
    telefono_prov = models.IntegerField(db_column='Telefono_prov')  # Field name made lowercase.
    descripcion_prov = models.CharField(db_column='Descripcion_prov', max_length=455)  # Field name made lowercase.
    estado_prov = models.IntegerField(db_column='Estado_prov', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'proveedoress'


class Provxprod(models.Model):
    id_provxprod = models.AutoField(db_column='Id_provXprod', primary_key=True)  # Field name made lowercase.
    id_prov_fk = models.ForeignKey(Proveedoress, models.DO_NOTHING, db_column='Id_prov_fk')  # Field name made lowercase.
    id_prod_fk = models.ForeignKey(Productos, models.DO_NOTHING, db_column='Id_prod_fk')  # Field name made lowercase.
    estado_provxprod = models.IntegerField(db_column='Estado_provXprod', blank=True, null=True)  # Field name made lowercase.
    nombre_prov = models.CharField(db_column='Nombre_prov', max_length=455)  # Field name made lowercase.
    nombre_prod = models.CharField(db_column='Nombre_prod', max_length=455)  # Field name made lowercase.
    fecha_entrega_provxprod = models.DateField(db_column='Fecha_entrega_provXprod')  # Field name made lowercase.
    descripcion_provxprod = models.CharField(db_column='Descripcion_provXprod', max_length=455)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'provxprod'


class Roles(models.Model):
    id_rol = models.AutoField(db_column='Id_rol', primary_key=True)  # Field name made lowercase.
    nombre_rol = models.CharField(db_column='Nombre_rol', max_length=95)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'roles'


class Servicios(models.Model):
    id_servicio = models.AutoField(db_column='Id_servicio', primary_key=True)  # Field name made lowercase.
    nombre_servicio = models.CharField(db_column='Nombre_servicio', max_length=45)  # Field name made lowercase.
    descripcion_servicio = models.CharField(db_column='Descripcion_servicio', max_length=455)  # Field name made lowercase.
    tipo_servicio = models.CharField(db_column='Tipo_servicio', max_length=45)  # Field name made lowercase.
    estado_servicio = models.IntegerField(db_column='Estado_servicio', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'servicios'


class ServiciosPrestados(models.Model):
    id_serv_prest = models.AutoField(primary_key=True)
    nombre_serv_prest = models.CharField(max_length=45)
    id_empleados_serp = models.ForeignKey(Empleados, models.DO_NOTHING, db_column='Id_empleados_serp')  # Field name made lowercase.
    id_servicios_serp = models.ForeignKey(Servicios, models.DO_NOTHING, db_column='Id_servicios_serp')  # Field name made lowercase.
    id_turno_serp = models.ForeignKey('Turnos', models.DO_NOTHING, db_column='Id_turno_serp')  # Field name made lowercase.
    apellido_serv_prest = models.CharField(db_column='Apellido_serv_prest', max_length=45)  # Field name made lowercase.
    dni_serv_prest = models.IntegerField(db_column='DNI_serv_prest')  # Field name made lowercase.
    fecha_naci_serv_prest = models.DateField(db_column='Fecha_naci_serv_prest')  # Field name made lowercase.
    estado_serv_prest = models.IntegerField(db_column='Estado_serv_prest', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'servicios_prestados'


class SolicitudOrdenCompras(models.Model):
    id_solicitud_orden_compra = models.AutoField(db_column='Id_solicitud_orden_compra', primary_key=True)  # Field name made lowercase.
    fecha_solicitud_orc = models.DateField(db_column='Fecha_solicitud_orc')  # Field name made lowercase.
    descripcion_orc = models.CharField(db_column='Descripcion_orc', max_length=455)  # Field name made lowercase.
    estado_orc = models.IntegerField(db_column='Estado_orc')  # Field name made lowercase.
    id_empleado_orc = models.ForeignKey(Empleados, models.DO_NOTHING, db_column='Id_empleado_orc', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'solicitud_orden_compras'


class Stocks(models.Model):
    id_stock = models.AutoField(db_column='Id_stock', primary_key=True)  # Field name made lowercase.
    cantidad_stock = models.IntegerField(db_column='Cantidad_stock')  # Field name made lowercase.
    fecha_egreso_stock = models.DateTimeField(db_column='Fecha_egreso_stock')  # Field name made lowercase.
    fecha_vencimiento_stock = models.DateTimeField(db_column='Fecha_vencimiento_stock')  # Field name made lowercase.
    id_prod_stock = models.ForeignKey(Productos, models.DO_NOTHING, db_column='Id_prod_stock')  # Field name made lowercase.
    estado_stock = models.IntegerField(db_column='Estado_stock')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'stocks'


class Turnos(models.Model):
    id_turno = models.AutoField(db_column='Id_turno', primary_key=True)  # Field name made lowercase.
    fecha_turno = models.DateField(db_column='Fecha_turno')  # Field name made lowercase.
    hora_turno = models.TimeField(db_column='Hora_turno')  # Field name made lowercase.
    motivo_cance_turno = models.CharField(db_column='Motivo_cance_turno', max_length=255, blank=True, null=True)  # Field name made lowercase.
    estado_turno = models.IntegerField(db_column='Estado_turno')  # Field name made lowercase.
    id_masc_turno = models.ForeignKey(Mascotas, models.DO_NOTHING, db_column='Id_masc_turno', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'turnos'
