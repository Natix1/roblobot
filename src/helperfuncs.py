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
    
def getRank(group: rbx.Group, userID: int) -> int:
    member = group.fetch_member(userID)
    rank = group.fetch_role(member.role_id).rank
    return rank

def isinGroup(group: rbx.Group, userID: int) -> bool:
    try:
        member = group.fetch_member(userID)
        if member:
            return True
        
        return False
    except rbx.exceptions.NotFound:
        return False