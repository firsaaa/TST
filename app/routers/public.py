from fastapi import APIRouter

router = APIRouter()

@router.get("/", summary="Test public route")
async def get_testroute():
    """
    **Description**:  
    A simple test route for validating public access.
    """
    return {"message": "User tervalidasi"}

@router.get("/team_members", summary="Fetch all team members")
async def get_all_team_members() -> list:
    """
    **Description**:  
    Retrieves information about all team members.  
    **Response**:  
    - `list`: A list of team member details.
    """
    data_team = [{"name": "Firsa"}, {"name": "Alice"}]  
    return data_team
