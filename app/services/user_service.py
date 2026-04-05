users = [
    {
        "id": 0,
        "name": "Stefan",
        "lastname": "Ramac",
        "phone": "0638393112",
        "email": "stefanramac@gmail.com",
        "age": 27,
        "nickname": "ramke"
    }
]

def get_users():
    return users

def create_user(user):
    new_id = len(users)

    new_user = {
        "id": new_id,
        "name": user.name,
        "lastname": user.lastname,
        "phone": user.phone,
        "email": user.email,
        "age": user.age,
        "nickname": user.nickname
    }

    users.append(new_user)
    return {
        "message": "User created",
        "data": new_user
    }

def delete_user(user_id: int):
    for i, u in enumerate(users):
        if u["id"] == user_id:
            deleted = users.pop(i)
            return {
                "message": "User deleted",
                "data": deleted
            }

    return {"error": "User not found"}