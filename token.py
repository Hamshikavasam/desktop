def token (seconds):
    s=Serializer(app.config['SECRET_KEY'],50)
    return s.dumps({'user':rollno}).decode('utf-8')
