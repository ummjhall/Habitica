from flask import Blueprint, request
from app.models import db, AvatarEquipment, Equipment
from flask_login import current_user, login_required

inventory_routes = Blueprint('inventory', __name__, url_prefix='/api/equipment')


@inventory_routes.route('/current/shop')
@login_required
def get_shop_equipment():
    """
    Get all Equipment available for purchase for the Current User
    """
    all_equipment = Equipment.query.all()

    shop_equipment = []
    for shop_item in all_equipment:
        item = shop_item.to_dict()

        item['imgae_url'] = shop_item.image.to_dict()['url']

        shop_equipment.append(item)

    return {'Equipment': shop_equipment}


@inventory_routes.route('/current')
@login_required
def get_user_equipment():
    """
    Get all of the Current User's Equipment
    """
    avatar = current_user.avatar
    if not avatar:
        return {'Equipment': []}

    owned_equipment = []
    for owned_item in avatar.equipment:
        item = owned_item.to_dict()

        item['user_id'] = current_user.id
        item['imgae_url'] = owned_item.image.to_dict()['url']
        item['nickname'] = AvatarEquipment.query.filter(
                AvatarEquipment.equipment_id == owned_item.id).first().equipment_nickname

        owned_equipment.append(item)

    return {'Equipment': owned_equipment}


@inventory_routes.route('/current/<equipment_id>', methods=['POST'])
@login_required
def collect_equipment(equipment_id):
    """
    Buy or collect a piece of Equipment for the Current User
    """

    # Couldn't find Equipment with the specified id
    found = Equipment.query.filter(Equipment.id == equipment_id).one_or_none()
    if not found:
        return {'message': "Equipment couldn't be found"}, 404

    # User already owns specified Equipment
    owned_equipment = current_user.avatar.equipment
    for item in owned_equipment:
        if item.to_dict()['id'] == int(equipment_id):
            return {'message': 'Equipment already owned'}, 400

    # SUCCESS
    new_equipment = AvatarEquipment(
        avatar_id=current_user.avatar.to_dict()['id'],
        equipment_id=equipment_id
    )
    db.session.add(new_equipment)
    db.session.commit()

    return new_equipment.to_dict(), 201


@inventory_routes.route('/current/<equipment_id>', methods=['PUT', 'PATCH'])
@login_required
def rename_equipment(equipment_id):
    """
    Renames the user's piece of Equipment specified by id and returns it.
    """

    nickname = request.json.get('nickname', None)

    # Body validation errors
    if not nickname:
        return {'nickname': 'Nickname is required'}, 400

    # Couldn't find Equipment with the specified id
    found = Equipment.query.filter(Equipment.id == equipment_id).one_or_none()
    if not found:
        return {'message': "Equipment couldn't be found"}, 404

    # User doesn't own specified Equipment
    owned = False
    owned_equipment = current_user.avatar.equipment
    for item in owned_equipment:
        if item.to_dict()['id'] == int(equipment_id):
            owned = True
    if not owned:
        return {'message': 'Equipment unowned'}, 400

    # SUCCESS
    equipment = AvatarEquipment.query.filter(AvatarEquipment.equipment_id == equipment_id).one()
    equipment.equipment_nickname = nickname
    db.session.add(equipment)
    db.session.commit()

    return equipment.to_dict()


@inventory_routes.route('/current/<equipment_id>', methods=['DELETE'])
@login_required
def delete_owned_equipment(equipment_id):
    """
    Deletes a piece of owned Equipment from the user's inventory.
    """

    # Couldn't find Equipment with the specified id
    found = Equipment.query.filter(Equipment.id == equipment_id).one_or_none()
    if not found:
        return {'message': "Equipment couldn't be found"}, 404

    # User doesn't own specified Equipment
    owned = False
    owned_equipment = current_user.avatar.equipment
    for item in owned_equipment:
        if item.to_dict()['id'] == int(equipment_id):
            owned = True
    if not owned:
        return {'message': 'Equipment unowned'}, 400

    # SUCCESS
    equipment = AvatarEquipment.query.filter(AvatarEquipment.equipment_id == equipment_id).one()
    db.session.delete(equipment)
    db.session.commit()

    return {'message': 'Successfully deleted'}
