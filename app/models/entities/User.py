from werkzeug.security import check_password_hash, generate_password_hash
from flask_login import UserMixin


class User(UserMixin):

    def __init__(self, id, username, password, fullname="") -> None:
        self.id = id
        self.username = username
        self.password = password
        self.fullname = fullname

    @classmethod
    def check_password(self, hashed_password, password):
        return check_password_hash(hashed_password, password)

#print(generate_password_hash("linerangers"))    
#print(generate_password_hash("bonin@321"))
#print(generate_password_hash("bonin@325"))
#print(generate_password_hash("bonin@329"))
#print(generate_password_hash("bonin@333"))
#print(generate_password_hash("bonin@337"))
#print(generate_password_hash("bonin@341"))
#print(generate_password_hash("bonin@345"))
#print(generate_password_hash("bonin@349"))
#print(generate_password_hash("bonin@353"))
#print(generate_password_hash("bonin@357"))
#print(generate_password_hash("bonin@361"))
#print(generate_password_hash("bonin@365"))
#print(generate_password_hash("bonin@369"))
#print(generate_password_hash("bonin@373"))
#print(generate_password_hash("bonin@377"))
#print(generate_password_hash("bonin@381"))
#print(generate_password_hash("bonin@385"))
#print(generate_password_hash("bonin@389"))
#print(generate_password_hash("bonin@393"))
#print(generate_password_hash("bonin@397"))
#print(generate_password_hash("bonin@401"))
#print(generate_password_hash("bonin@405"))
#print(generate_password_hash("bonin@409"))    
#print(generate_password_hash("bonin@413"))
#print(generate_password_hash("bonin@417"))