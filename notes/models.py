from sqlalchemy.orm import Mapped, mapped_column

from app import db


class Note(db.Model):
    __tablename__ = "notes"

    id: Mapped[int] = mapped_column(primary_key=True)
    title: Mapped[str]
    text: Mapped[str]

    def __str__(self) -> str:
        return f"Note ({self.id}) {self.title}"
