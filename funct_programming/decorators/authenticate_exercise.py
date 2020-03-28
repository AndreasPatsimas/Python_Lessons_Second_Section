# Create an @authenticated decorator that only allows the function to run is user1 has 'valid' set to True:
user1 = {
    'name': 'Sorna',
    'valid': True #changing this will either run or not run the message_friends function.
}

# def authenticated(fn):
#   def wrapper(user):
#       if user["valid"] == True:
#           fn(user)
#       else:
#           print(f"User {user['name']} is not authenticated")
#       pass
#   return wrapper

def authenticated(fn):
  def wrapper(*args, **kwargs):
    if args[0]['valid']:
        return fn(*args, **kwargs)
    else:
        print(f"User {args[0]['name']} is not authenticated")
  return wrapper



@authenticated
def message_friends(user):
    print('message has been sent')

message_friends(user1)