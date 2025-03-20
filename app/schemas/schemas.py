from pydantic import BaseModel, ConfigDict, EmailStr, Field
from datetime import datetime

# 配置基类，启用 ORM 模式
class BaseSchema(BaseModel):
    model_config = ConfigDict(from_attributes=True)

# 用户相关模型
class UserCreate(BaseModel):
    username: str = Field(..., min_length=3, max_length=100)
    email: EmailStr | None = Field(None, max_length=255)
    full_name: str | None = Field(None, max_length=100)
    password: str = Field(..., min_length=3)
    
    
class UserInDB(BaseSchema):
    id: int
    username: str
    email: EmailStr | None = None
    full_name: str | None = None
    password_hash: str
    

class UserResponse(BaseSchema):
    id: int
    username: str
    email: str | None = None
    full_name: str | None = None
    created_at: datetime
    updated_at: datetime

    
class Token(BaseModel):
    access_token: str
    token_type: str = "bearer"
    

class LoginData(BaseModel):
    username: str
    password: str