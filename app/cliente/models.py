from app.db import db, ma


class Cliente(db.Model):
    cli_v_usuario = db.Column(db.String(50), primary_key=True)
    cli_v_contrasena = db.Column(db.String(50), nullable=False)
    cli_i_puntaje = db.Column(db.Integer, nullable=True)



class ClienteSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Cliente
        fields = ["cli_v_usuario", "cli_v_contrasena", "cli_i_puntaje"]


def get_clientes():
    clientes = Cliente.query.all()
    cliente_schema = ClienteSchema()
    clientes = [cliente_schema.dump(cliente) for cliente in clientes]
    return clientes

def obtener_cliente(usuario, contrasena):
    cliente = Cliente.query.filter_by(cli_v_usuario=usuario).first()
    if cliente != None:
        if cliente.cli_v_contrasena == contrasena:
            cliente_schema = ClienteSchema()
            return cliente_schema.dump(cliente)
    return None

def crear_cliente(usuario,contrasena):
    try:
        cliente = Cliente( cli_v_usuario=usuario,cli_v_contrasena= contrasena)
        db.session.add(cliente)
        db.session.commit()
        cliente_schema = ClienteSchema()
        return cliente_schema.dump(cliente)
    except:
        return None


def eliminar_cliente(usuario):
    cliente = Cliente.query.filter_by(cli_v_usuario=usuario).first()
    if cliente != None:
        Cliente.query.filter_by(cli_v_usuario=usuario).delete()
        db.session.commit()
        return True
    else:
        return False


def modificar_cliente(usuario, contrasena, puntaje):
    cliente = Cliente.query.filter_by(cli_v_usuario=usuario).first()
    if cliente != None:
        cliente.cli_v_contrasena = contrasena
        cliente.cli_i_puntaje = puntaje
        db.session.commit()
        cliente_schema = ClienteSchema()
        return cliente_schema.dump(cliente)
    return None
