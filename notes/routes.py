from flask import (
    redirect,
    render_template, 
    request,
    url_for,
)

from app import db # Объект для работы с базой данных
from notes import notes_blueprint
from notes.models import Note


@notes_blueprint.route("", methods=["GET", "POST"]) # Регистрируем роут в нашем модуле с указанными методами
def notes_list_create():
    notes = list(db.session.execute(db.select(Note).order_by(Note.id)).scalars())
    # Выполняем запрос в базу для получения списка всех заметок
    
    if request.method == "POST": # При создании новой заметки
        text = request.form["text"] # Забираем данные из формы в шаблоне
        title = request.form["title"]
        
        note = Note(
            text=text, 
            title=title,
        ) # Создаем новую заметку на основе данных из формы

        db.session.add(note)
        db.session.commit() # Сохраняем заметку в базу
        notes.append(note) # Добавляем заметку в список заметок, показываемых на странице

    return render_template(
        "notes_list.html", # Имя шаблона
        notes=notes, # Подставляем переменные в шаблон
        note_action="Create", # Имя аргумента в этой функции это переменная в шаблоне
        form_url=url_for("notes.notes_list_create"), # url_for - возвращает урл по соответствию названию функции
    )


@notes_blueprint.route("/<int:note_id>", methods=["GET", "POST"])
def note_detail_update(note_id: int): # Аргумент из роута выше
    note = db.get_or_404(Note, note_id) # Если заметки с объектом не найдется, браузер выкинет 404 ошибку

    if request.method == "POST": # Обновляем заметку
        note.text = request.form["text"] # Собираем данные из формы
        note.title = request.form["title"] # и устанавливаем атрибуты у заметки
        db.session.add(note)
        db.session.commit() # Делаем обновление в базе
    
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
    
