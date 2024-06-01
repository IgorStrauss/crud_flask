from datetime import datetime

from . import db


class User(db.Model):
    __tablename__ = "user"
    Id = db.Column(db.Integer, primary_key=True, autoincrement=True, unique=True)
    Firstname = db.Column(db.String(35), nullable=False)
    Lastname = db.Column(db.String(35), nullable=False)
    Email = db.Column(db.String(35), nullable=False, unique=True)
    Created_at = db.Column(
        db.DateTime, default=datetime.now, server_default=db.func.now()
    )
    Phone_user = db.relationship(
        "Phone", back_populates="User_phone", uselist=False, cascade="all, delete"
    )
    Is_active = db.Column(db.Boolean, default=True)
    Is_admin = db.Column(db.Boolean, default=False)

    def __init__(self, Firstname, Lastname, Email) -> None:
        super().__init__()
        self.Created_at = datetime.now()
        self.Firstname = Firstname
        self.Lastname = Lastname
        self.Email = Email
        self.is_active = True
        self.is_admin = False

    @property
    def format_date(self):
        return f"{self.created_at.day}/{self.created_at.month}/{self.created_at.year} as \
            {self.created_at.hour}:{self.created_at.minute}"

    def __str__(self):
        return str(self.Firstname)

    @property
    def First_Name(self):
        return f"{self.Firstname}".title()

    @property
    def Last_Name(self):
        return f"{self.Lastname}".title()

    @property
    def Username(self):
        return f"{self.Lastname} {self.Firstname}".upper()


class Phone(db.Model):
    __tablename__ = "phone"
    Id = db.Column(db.Integer, primary_key=True)
    Cellphone = db.Column(db.String(11), nullable=False, unique=True)
    User_id = db.Column(db.Integer, db.ForeignKey(User.Id))
    User_phone = db.relationship(
        "User",
        back_populates="Phone_user",
        uselist=False,
        cascade="all, delete",
        lazy="joined",
    )

    def __str__(self) -> str:
        return str(self.Cellphone)

    def __init__(self, Cellphone, User_id) -> None:
        self.Cellphone = Cellphone
        self.User_id = User_id

    @property
    def Format_Cellphone(self):
        return f"({self.Cellphone[:2]})\
 {self.Cellphone[2]} {self.Cellphone[3:7]}-{self.Cellphone[7:]}"
