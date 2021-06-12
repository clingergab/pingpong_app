from flask import Flask, render_template, jsonify, request, url_for, redirect
from player_model import *
from settings import *
import pdb

p1 = 0
p2 = 0

@app.route("/", methods=["GET", "POST"])
def welcome():
    global p1
    global p2
    p1 = 0
    p2 = 0
    if request.method == "POST":
        player1 = request.form["player1"]
        Player.add_player(player1)
        player2 = request.form["player2"]
        Player.add_player(player2)

        return redirect(url_for("game", player1=player1, player2=player2, p1=p1, p2=p2))
    else:
        return render_template("welcome.html")


@app.route("/players")
def get_players():
    return render_template("players.html", players=Player.get_all_players())


@app.route("/game/<player1>/<player2>", methods=['GET', 'POST'])
def game(player1, player2):
    global p1
    global p2
    if request.method == "POST":
        if "player1" in request.form.keys():
            
            player1 = request.form["player1"]
            p1 += 1
            
            if p1 > 10 and p1 - p2 > 1:
                Player.update_player_wins(player1, Player.get_player_wins(player1) + 1)
                Player.update_player_cumulative(player1, Player.get_player_cumulative(player1) + p1)
                return redirect(url_for("winner", winner=player1))
        elif request.form.keys():
            player2 = request.form["player2"]
            p2 += 1
            if p2 > 10 and p2 - p1 > 1:
                Player.update_player_wins(player2, Player.get_player_wins(player2) + 1)
                Player.update_player_cumulative(player2, Player.get_player_cumulative(player2) + p2)
                return redirect(url_for("winner", winner=player2))
        
    return render_template("game.html",player1=player1, player2=player2, p1=p1, p2=p2)

@app.route("/winner/<winner>")
def winner(winner):
    return render_template("winner.html", winner=winner)