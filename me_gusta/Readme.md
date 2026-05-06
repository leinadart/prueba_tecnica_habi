Servicio 2 Me gusta.

En el archivo entidadRelacion.pdf se expone gráficamente la relación entre la nueva tabla de like_history con las tablas property y auth_user.

En la solución que se se plantea, para dar like debemos tener información tanto de la propiedad y del usuario que está usando la plataforma.

Campos:

id: tipo entero incremental
user_id: clave foránea que apunta a la clave primaria del id de la tabla auth_user
property_id: clave foránea que apunta a la clave primaria del id de la tabla property
like: tipo boleano que indica si al usuario le gusta o no la propiedad
update_date: Fecha de actualización del me gusta
