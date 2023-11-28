### Entidades

- Eventos.
- Usuarios:

  1. Productores
  2. Espectadores
  3. Admin

* Localizacion
* Suscripciones:
  - Gratis
  - Premium

### Relaciones

Productores -- crean -> Eventos
Espectadores -- buscan -> Eventos
Espectadores -- participan -> Eventos

Eventos:
creator_id: FK a productor
...

Asistentes:
event_id: FK a evento
user_id: FK a espectador

user:
user_id: pk
email
hashed_password
...
is_creator: bool
is_admin: bool

productor:
id: pk
billing_address
