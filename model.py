from peewee import IntegerField, SqliteDatabase, Model

db = SqliteDatabase("House.db")


class DataBase(Model):
    local = IntegerField()
    area = IntegerField()
    price=IntegerField()

    class Meta:
        database = db
        db_database = "house paramerts"


db.create_tables([DataBase])
