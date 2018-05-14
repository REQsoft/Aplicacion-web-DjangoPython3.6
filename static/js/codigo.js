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

    $("#form_eliminar").submit(function(evt){
        evt.preventDefault();
        $.ajax({
            url:$("#url").val(),
            type: "GET",
            success: function (datos) {
                $("#modal_eliminiar").html(datos);
                $("#mostrarmodal").modal("show");
            }
        });
    });
});

function validar_eliminacion(url, nombre, motor, usuario){
    $("#spn_nombre").html(nombre);
    $("#spn_motor").html(motor);
    $("#spn_usuario").html(usuario);
    $("#form_confirmacion").attr('action',url);
    $("#mostrarmodal").modal("show");

}