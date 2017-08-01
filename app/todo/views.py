from flask import render_template, request, redirect, flash, url_for

from ..models import Category, Todo, Priority
from . import todo
from .. import db


@todo.route('/')
def index():
    return render_template(
        'todo/todo_tabs.html',
        todos = Todo.query.filter_by(is_done=0).all(),
    )


@todo.route('/list_todo')
def list_todo():
    return render_template(
        'todo/list_todo.html',
        todos = Todo.query.filter_by(is_done=0).all(),
    )


@todo.route('/finish_todo')
def finish_todo():
    return render_template(
        'todo/list_todo.html',
        todos = Todo.query.filter_by(is_done=1).all(),
    )

@todo.route('/new_todo', methods=['GET', 'POST'])
def new_todo():
    if request.method == 'POST':
        category = Category.query.filter_by(
            id=request.form['category']).first()
        priority = Priority.query.filter_by(
            id=request.form['priority']).first()
        todo = Todo(category=category, priority=priority,
                    description=request.form['description'])
        db.session.add(todo)
        db.session.commit()
        flash("Add new todo successfully.")
        return redirect(url_for('todo.index'))
    else:
        return render_template(
            'todo/new_todo.html',
            page='new_todo',
            categories=Category.query.all(),
            priorities=Priority.query.all()
        )


@todo.route('/edit_todo/', methods=['GET','POST'])
def edit_todo():
    if request.method == 'GET':
        todo_id = request.args.get('todo_id')
        todo = Todo.query.filter_by(id=todo_id).first()
        return render_template(
            'todo/modal_edit_todo.html',
            todo=todo,
            categories=Category.query.all(),
            priorities=Priority.query.all(),
        )
    else:
        todo_id = request.form['todo_id']
        category_id = request.form['category']
        priority_id = request.form['priority']
        description = request.form['description']
        todo = Todo.query.filter_by(id=todo_id).first()
        todo.category_id = category_id
        todo.priority_id = priority_id
        todo.description = description
        db.session.commit()
        return redirect(url_for('todo.index'))


@todo.route('/delete_todo/<int:todo_id>', methods=['POST'])
def delete_todo(todo_id):
    if request.method == 'POST':
        todo = Todo.query.get(todo_id)
        db.session.delete(todo)
        db.session.commit()
        return redirect(url_for('todo.index'))


@todo.route('/mark_done/<int:todo_id>', methods=['POST'])
def mark_done(todo_id):
    if request.method == 'POST':
        todo = Todo.query.get(todo_id)
        todo.is_done = True
        db.session.commit()
        return redirect(url_for('todo.index'))

@todo.route('/list_category')
def list_category():
    return render_template(
        'todo/list_category.html',
        categories = Category.query.all(),
    )


@todo.route('/list_todo/<name>')
def list_todo_by_cateory(name):
    category = Category.query.filter_by(name=name).first()
    return render_template(
        'todo/list_todo.html',
        todos=Todo.query.filter_by(category=category).all(),
    )


@todo.route('/new_category', methods=['POST'])
def new_category():
    if request.method == 'POST':
        category = Category(name=request.form['category'])
        db.session.add(category)
        db.session.commit()
        return redirect(url_for('todo.list_category'))


@todo.route('/edit_category', methods=['GET', 'POST'])
def edit_category():
    if request.method == 'GET':
        category_id = request.args.get('category_id')
        category = Category.query.get(category_id)
        return render_template(
            'todo/modal_edit_category.html',
            category=category
        )
    else:
        category_id = request.form['category_id']
        category = Category.query.filter_by(id=category_id).first()
        category.name = request.form['category']
        db.session.commit()
        return redirect(url_for('todo.list_category'))


@todo.route('/delete_category/<int:category_id>')
def delete_category(category_id):
    category = Category.query.get(category_id)
    if not category.todos:
        db.session.delete(category)
        db.session.commit()
    else:
        flash('You have TODOs in that category. Remove them first.')
    return redirect(url_for('todo.list_category'))

