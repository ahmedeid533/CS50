import os
import datetime

from cs50 import SQL
from flask import Flask, flash, redirect, render_template, request, session
from flask_session import Session
from tempfile import mkdtemp
from werkzeug.security import check_password_hash, generate_password_hash

from helpers import apology, login_required, lookup, usd

# Configure application
app = Flask(__name__)

# Custom filter
app.jinja_env.filters["usd"] = usd

# Configure session to use filesystem (instead of signed cookies)
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

# Configure CS50 Library to use SQLite database
db = SQL("sqlite:///finance.db")


@app.after_request
def after_request(response):
    """Ensure responses aren't cached"""
    response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    response.headers["Expires"] = 0
    response.headers["Pragma"] = "no-cache"
    return response


@app.route("/")
@login_required
def index():
    """Show portfolio of stocks"""
    shares = db.execute("SELECT * FROM shares WHERE user_id = ?", session["user_id"])
    cash = db.execute("SELECT cash FROM users WHERE id = ?", session["user_id"])
    total = cash[0]["cash"]
    i = 0
    for share in shares:
        total += share["price"]
        shares[i]["oneShare"] = share["price"] / share["amount"]
        i += 1
    return render_template(
        "index.html", shares=shares, cash=cash[0]["cash"], total=total
    )


@app.route("/buy", methods=["GET", "POST"])
@login_required
def buy():
    """Buy shares of stock"""
    if request.method == "POST":
        if not request.form.get("symbol"):
            return apology("must provide symbol", 400)
        try:
            if not request.form.get("shares") or int(request.form.get("shares")) < 0 or (float(request.form.get("shares")) != int(request.form.get("shares"))):
                return apology("must provide +ve integer number of shares", 400)
        except:
            return apology("must provide +ve integer number of shares", 400)

        shares = lookup(request.form.get("symbol"))
        user = db.execute("SELECT * FROM users WHERE id = ?", session["user_id"])
        if not shares:
            return apology("symbol not found", 400)
        elif user[0]["cash"] < (shares["price"] * int(request.form.get("shares"))):
            return apology("can't afford", 400)

        user[0]["cash"] -= shares["price"] * int(request.form.get("shares"))
        db.execute(
            "UPDATE users SET cash = ? WHERE id = ?",
            user[0]["cash"],
            session["user_id"],
        )
        user_shares = db.execute(
            "SELECT * FROM shares WHERE user_id = ? AND symbol = ?",
            session["user_id"],
            shares["symbol"],
        )
        if len(user_shares) == 1:
            user_shares[0]["price"] += shares["price"] * int(request.form.get("shares"))
            user_shares[0]["amount"] += int(request.form.get("shares"))
            db.execute(
                "UPDATE shares SET price = ?, amount = ? WHERE user_id = ? AND symbol = ?",
                user_shares[0]["price"],
                user_shares[0]["amount"],
                session["user_id"],
                shares["symbol"],
            )
        else:
            db.execute(
                "INSERT INTO shares (user_id, name, symbol, amount, price) VALUES(?, ?, ?, ?, ?)",
                session["user_id"],
                shares["name"],
                shares["symbol"],
                int(request.form.get("shares")),
                (shares["price"] * int(request.form.get("shares"))),
            )
        db.execute(
                "INSERT INTO history (user_id, symbol, price, amount, 'date') VALUES(?, ?, ?, ?, ?)",
                session["user_id"],
                shares["symbol"],
                shares["price"],
                int(request.form.get("shares")),
                datetime.datetime.now()
            )
        # Redirect user to home page
        return redirect("/")
    else:
        return render_template("buy.html")


@app.route("/history")
@login_required
def history():
    """Show history of transactions"""
    historys = db.execute("SELECT * FROM history WHERE user_id = ?", session["user_id"])
    return render_template(
        "history.html", historys = historys
    )


@app.route("/login", methods=["GET", "POST"])
def login():
    """Log user in"""

    # Forget any user_id
    session.clear()

    # User reached route via POST (as by submitting a form via POST)
    if request.method == "POST":
        # Ensure username was submitted
        if not request.form.get("username"):
            return apology("must provide username", 403)

        # Ensure password was submitted
        elif not request.form.get("password"):
            return apology("must provide password", 403)

        # Query database for username
        rows = db.execute(
            "SELECT * FROM users WHERE username = ?", request.form.get("username")
        )

        # Ensure username exists and password is correct
        if len(rows) != 1 or not check_password_hash(
            rows[0]["hash"], request.form.get("password")
        ):
            return apology("invalid username and/or password", 403)

        # Remember which user has logged in
        session["user_id"] = rows[0]["id"]

        # Redirect user to home page
        return redirect("/")

    # User reached route via GET (as by clicking a link or via redirect)
    else:
        return render_template("login.html")


@app.route("/logout")
def logout():
    """Log user out"""

    # Forget any user_id
    session.clear()

    # Redirect user to login form
    return redirect("/")


@app.route("/quote", methods=["GET", "POST"])
@login_required
def quote():
    """Get stock quote."""
    if request.method == "POST":
        if not request.form.get("symbol"):
            return apology("must provide quote", 400)
        shard = lookup(request.form.get("symbol"))
        if not shard:
            return apology("symbol not found", 400)
        else:
            return render_template(
                "quote.html",
                name=shard["name"],
                symbol=shard["symbol"],
                price=shard["price"],
            )
    else:
        return render_template("quote.html")


@app.route("/register", methods=["GET", "POST"])
def register():
    """Register user"""

    # Forget any user_id
    session.clear()

    # User reached route via POST (as by submitting a form via POST)
    if request.method == "POST":
        # Ensure username was submitted
        if not request.form.get("username"):
            return apology("must provide username", 400)

        # Ensure password was submitted
        elif not request.form.get("password"):
            return apology("must provide password", 400)

        elif not request.form.get("confirmation"):
            return apology("must provide password confirmation", 400)

        elif request.form.get("confirmation") != request.form.get("password"):
            return apology("two passwords not match", 400)

        # Query database for username
        rows = db.execute(
            "SELECT * FROM users WHERE username = ?", request.form.get("username")
        )

        # Ensure username exists and password is correct
        if len(rows) != 0:
            return apology("username is taken", 400)
        db.execute(
            "INSERT INTO users (username, hash) VALUES(?, ?)",
            request.form.get("username"),
            generate_password_hash(request.form.get("password")),
        )
        rows = db.execute(
            "SELECT * FROM users WHERE username = ?", request.form.get("username")
        )
        # Remember which user has logged in
        session["user_id"] = rows[0]["id"]

        # Redirect user to home page
        return redirect("/")
    # User reached route via GET (as by clicking a link or via redirect)
    else:
        return render_template("register.html")


@app.route("/sell", methods=["GET", "POST"])
@login_required
def sell():
    """Sell shares of stock"""
    if request.method == "POST":
        if not request.form.get("symbol"):
            return apology("must provide symbol", 400)

        # Ensure password was submitted
        elif not request.form.get("shares"):
            return apology("must provide number", 400)
        user_shares = db.execute(
            "SELECT * FROM shares WHERE user_id = ? AND symbol = ?",
            session["user_id"],
            request.form.get("symbol"),
        )
        if user_shares[0]["amount"] == int(request.form.get("shares")):
            db.execute(
                "DELETE FROM shares WHERE user_id = ? AND symbol = ?",
                session["user_id"],
                request.form.get("symbol"),
            )
            user = db.execute("SELECT cash FROM users WHERE id = ?", session["user_id"])
            shares = lookup(request.form.get("symbol"))
            user[0]["cash"] += shares["price"] * int(request.form.get("shares"))
            db.execute(
                "UPDATE users SET cash = ? WHERE id = ?",
                user[0]["cash"],
                session["user_id"],
            )
            db.execute(
                "INSERT INTO history (user_id, symbol, price, amount, date) VALUES(?, ?, ?, ?, ?)",
                session["user_id"],
                shares["symbol"],
                shares["price"],
                -int(request.form.get("shares")),
                datetime.datetime.now()
            )
            return redirect("/")
        elif user_shares[0]["amount"] > int(request.form.get("shares")):
            user = db.execute("SELECT cash FROM users WHERE id = ?", session["user_id"])
            shares = lookup(request.form.get("symbol"))
            user[0]["cash"] += shares["price"] * int(request.form.get("shares"))
            db.execute(
                "UPDATE users SET cash = ? WHERE id = ?",
                user[0]["cash"],
                session["user_id"],
            )
            db.execute(
                "UPDATE shares SET price = ?, amount = ? WHERE user_id = ? AND symbol = ?",
                (
                    user_shares[0]["price"]
                    - (shares["price"] * int(request.form.get("shares")))
                ),
                user_shares[0]["amount"] - int(request.form.get("shares")),
                session["user_id"],
                request.form.get("symbol")
            )
            db.execute(
                "INSERT INTO history (user_id, symbol, price, amount, date) VALUES(?, ?, ?, ?, ?)",
                session["user_id"],
                shares["symbol"],
                shares["price"],
                -int(request.form.get("shares")),
                datetime.datetime.now()
            )
            return redirect("/")
        else:
            return apology("you don't have enough shares", 400)
    else:
        symbols = db.execute(
            "SELECT symbol FROM shares WHERE user_id = ?", session["user_id"]
        )
        return render_template("sell.html", symbols = symbols)
@app.route("/password", methods=["GET", "POST"])
@login_required
def password():
    if request.method == "POST":
        if not request.form.get("password"):
            return apology("please enter the new password", 403)
        else:
          db.execute(
                "UPDATE users SET hash = ? WHERE id = ?",
                generate_password_hash(request.form.get("password")),
                session["user_id"],
            )
        return redirect("/")
    else:
        return render_template("password.html")