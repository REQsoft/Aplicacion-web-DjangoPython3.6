$(document).ready(function () {
    $("#listar_bd").click(function () {
        $.ajax({
            url: $("#url").val(),
            type: "POST",
            data: $("#form_conexion").serialize(),
            success: function (datos) {
                $("#selector_bd").html(datos);
            }
        });
    });

    $("#validar_conexion").click(function (evt) {
        evt.preventDefault();
        $.ajax({
            url: $("#url").val(),
            type: "POST",
            data: $("#form_conexion").serialize(),
            success: function (datos) {
                $("#div_validacion").html(datos);
                window.setTimeout(function () {
                    $(".alert").fadeTo(1500, 0).slideUp(500, function () {
                        $(this).remove();
                    });
                }, 1000);
            }
        });
    });

});

function generar_formulario_conexion(motor_db) {
    switch (motor_db) {
        case "mysql":
            $("#motor").val("mysql");
            $("#puerto").val(3306);
            break;

        case "postgresql":
            $("#motor").val("postgres");
            $("#puerto").val(5432);
            break;

        case "oracle":
            $("#motor").val("oracle");
            $("#puerto").val(1521);
            break;
    }
}

function validar_eliminacion(url, nombre, motor, usuario) {
    $("#spn_nombre").html(nombre);
    $("#spn_motor").html(motor);
    $("#spn_usuario").html(usuario);
    $("#form_confirmacion").attr('action', url);
    $("#mostrarmodal").modal("show");
}

function validar_eliminacion_servicio(url, nombre, rol, descripcion) {
    $("#spn_nombre").html(nombre);
    $("#spn_rol").html(rol);
    $("#spn_descripcion").html(descripcion);
    $("#form_confirmacion").attr('action', url);
    $("#mostrarmodal").modal("show");
}

function validar_eliminacion_directorio(url, dependencia, extension, linea_directa) {
    $("#spn_dependencia").html(dependencia);
    $("#spn_extension").html(extension);
    $("#spn_linea_directa").html(linea_directa);
    $("#form_confirmacion").attr('action', url);
    $("#mostrarmodal").modal("show");
}

function validar_eliminacion_articulo(url, descripcion, fecha) {
    $("#spn_descripcion").html(descripcion);
    $("#spn_fecha").html(fecha);
    $("#form_confirmacion").attr('action', url);
    $("#mostrarmodal").modal("show");
}

function validar_eliminacion_localizacion(url, descripcion, longitud, latitud) {
    $("#spn_descripcion").html(descripcion);
    $("#spn_longitud").html(longitud);
    $("#spn_latitud").html(latitud);
    $("#form_confirmacion").attr('action', url);
    $("#mostrarmodal").modal("show");
}

function validar_conexion() {
    $.ajax({
        url: $("#url").val(),
        type: "POST",
        data: $("#form_conexion").serialize(),
        success: function (datos) {
            $("#div_validacion").html(datos);
            window.setTimeout(function () {
                $(".alert").fadeTo(1500, 0).slideUp(500, function () {
                    $(this).remove();
                });
            }, 1000);
        }
    });
}

function mostrar_db(db) {
    $("#nombre_bd").val(db);
}