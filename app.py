
    user = User.query.filter_by(email=data["email"]).first()

    if not user or not check_password_hash(user.password, data["password"]):
        return {"error": "Invalid credentials"}, 401

    token = create_access_token(
        identity={"id": user.id, "role": user.role}
    )
    return {"access_token": token}

@app.route("/admin", methods=["GET"])
@jwt_required()
def admin_dashboard():
    user = get_jwt_identity()
    if user["role"] != "admin":
        return {"error": "Admins only"}, 403
    return {"message": "Welcome to Admin Dashboard"}

@app.route("/recruiter", methods=["GET"])
@jwt_required()
def recruiter_dashboard():
    user = get_jwt_identity()
    if user["role"] not in ["recruiter", "admin"]:
        return {"error": "Recruiters only"}, 403
    return {"message": "Welcome Recruiter"}

if __name__ == "__main__":
    app.run()
