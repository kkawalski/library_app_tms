from flask import (
    redirect,
    render_template, 
    request,
    url_for,
)

from app import db
from notes import notes_blueprint
from notes.models import Note


@notes_blueprint.route("", methods=["GET", "POST"])
def notes_list_create():
    notes = list(db.session.execute(db.select(Note).order_by(Note.id)).scalars())
    
    if request.method == "POST":
        text = request.form["text"]
        title = request.form["title"]
        
        note = Note(
            text=text, 
            title=title,
        )

        db.session.add(note)
        db.session.commit()
        notes.append(note)

    return render_template(
        "notes_list.html",
        notes=notes,
        note_action="Create",
        form_url=url_for("notes.notes_list_create"),
    )


@notes_blueprint.route("/<int:note_id>", methods=["GET", "POST"])
def note_detail_update(note_id: int):
    note = db.get_or_404(Note, note_id)

    if request.method == "POST":
        note.text = request.form["text"]
        note.title = request.form["title"]
        db.session.add(note)
        db.session.commit()
    
    return render_template(
        "note_detail.html",
        note=note,
        note_action="Update",
        form_url=url_for("notes.note_detail_update", note_id=note_id)
    )

# @notes_blueprint.get("")
# def notes_list():
#     notes = db.session.execute(db.select(Note)).scalars()
#     return render_template(
#         "notes_list.html",
#         notes=notes,
#     )

# @notes_blueprint.post("/create")
# def note_create():
#     text = request.form["text"]
#     title = request.form["title"]
    
#     note = Note(
#         text=text, 
#         title=title,
#     )

#     db.session.add(note)
#     db.session.commit()
#     return redirect(url_for("notes.notes_list"))
    
