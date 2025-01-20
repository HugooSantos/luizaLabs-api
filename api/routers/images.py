import os
from fastapi import APIRouter,File, UploadFile, HTTPException
from pathlib import Path
import uuid
from api.schemas.images.delete_images import DeleteImage
from api.services import images_service


router = APIRouter()
 
UPLOAD_DIR = Path("static/images/")
UPLOAD_DIR.mkdir(parents=True, exist_ok=True)

@router.post("/", status_code=201)
async def upload_image(file: UploadFile = File(...)):
    if file.content_type not in ["image/jpeg", "image/png"]:
        raise HTTPException(status_code=400, detail="Invalid file type. Only JPEG or PNG allowed.")
    
    file_extension = file.filename.split(".")[-1]
    unique_filename = f"{uuid.uuid4()}.{file_extension}"
    
    file_path = UPLOAD_DIR / unique_filename
    
    with open(file_path, "wb") as buffer:
        buffer.write(await file.read())
    
    final_path = "images/" + unique_filename
    return {"filename": str(unique_filename), "message": "Upload successful", "file_path": final_path}


@router.delete("/", status_code=204)
async def delete_image(schema: DeleteImage):
    await images_service.delete(filename=schema.filename)
