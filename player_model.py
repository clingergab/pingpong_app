from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from settings import app

db = SQLAlchemy(app)

class Player(db.Model):
    __tablename__ = 'player'
    name = db.Column(db.String(128), primary_key=True, unique=True, nullable=False)
    wins = db.Column(db.Integer)
    cumulative = db.Column(db.Integer)


    def json(self):
        return {'name': self.name, 'wins': self.wins, 'cumulaive': self.cumulative}

    def add_player(_name):
        new_player = Player(name=_name, wins=0, cumulative=0)
        db.session.add(new_player)
        db.session.commit()

    def get_all_players():
        return [Player.json(player) for player in Player.query.all()]

    def get_player(_name):
        player = Player.query.filter_by(name=_name).first()
        return Player.json(player)

    def get_player_wins(_name):
        player = Player.query.filter_by(name=_name).first()
        return Player.wins

    def get_player_cumulative(_name):
        player = Player.query.filter_by(name=_name).first()
        return Player.cumulative

    def update_player_wins(_name, _wins):
        player = Player.query.filter_by(name=_name).first()
        player.wins = _wins
        db.session.commit()

    def update_player_cumulative(_name, _cumulative):
        player = Player.query.filter_by(name=_name).first()
        player.cumulative = _cumulative
        db.session.commit()