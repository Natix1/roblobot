import rblxopencloud as rbx

def findRoleID(group: rbx.Group, rank: int) -> int:
    targetID = None
    for role in group.list_roles():
        if role.rank == rank:
            targetID = role.id
    
    if targetID is not None:
        return targetID
    else:
        raise rbx.exceptions.NotFound
    
def setRank(group: rbx.Group, userID: int, rank: int) -> tuple[bool, str]:
    RoleID = findRoleID(group, rank)
    try:
        group.update_member(userID, RoleID)
        return True, ""
    except rbx.exceptions.NotFound:
        return False, "User not found in group"