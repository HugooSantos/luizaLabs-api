import os
from pathlib import Path
from fastapi import HTTPException
import asyncio

UPLOAD_DIR = Path("static/images/")

async def delete(filename: str) -> None:
    file_path = UPLOAD_DIR / filename
    
    if not await asyncio.to_thread(file_path.exists):
        raise HTTPException(status_code=404, detail="File not found.")
    
    try:
        await asyncio.to_thread(file_path.unlink)
    except Exception as e:
        import traceback
        traceback.print_exc()
        raise HTTPException(status_code=500, detail=f"Error deleting file: {str(e)}")
