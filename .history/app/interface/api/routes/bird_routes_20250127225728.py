from fastapi import APIRouter, Depends
from app.interface.api.schemas.bird_schema import BirdCreate, BirdResponse
from app.use_cases.bird.create_bird_use_case import CreateBirdUseCase

router = APIRouter()

@router.post("/birds", response_model=BirdResponse)
async def create_bird(
    bird_data: BirdCreate,
    use_case: CreateBirdUseCase = Depends(get_bird_use_case)
):
    bird = await use_case.execute(
        name=bird_data.name,
        species=bird_data.species
    )
    return BirdResponse.from_entity(bird)